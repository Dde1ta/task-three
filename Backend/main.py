import socket
import urllib.request
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins (good for local dev, change for production)
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/maker")
def maker():
    return {"name": "D_delta", "place": "India"}


@app.get("/who")
def whoami():
    container_id = socket.gethostname()
    ec2_instance_id = "Not running on EC2 or IMDS disabled"
    instance_tags = {}

    try:
        # Step 1: Request a session token (required for IMDSv2)
        token_req = urllib.request.Request(
            "http://169.254.169.254/latest/api/token",
            headers={"X-aws-ec2-metadata-token-ttl-seconds": "21600"},
            method="PUT"
        )
        with urllib.request.urlopen(token_req, timeout=1) as response:
            token = response.read().decode()

        # Step 2: Use the token to fetch the instance-id
        id_req = urllib.request.Request(
            "http://169.254.169.254/latest/meta-data/instance-id",
            headers={"X-aws-ec2-metadata-token": token}
        )
        with urllib.request.urlopen(id_req, timeout=1) as response:
            ec2_instance_id = response.read().decode()

        # Step 3: Fetch the Instance Tags
        tags_req = urllib.request.Request(
            "http://169.254.169.254/latest/meta-data/tags/instance",
            headers={"X-aws-ec2-metadata-token": token}
        )
        with urllib.request.urlopen(tags_req, timeout=1) as response:
            # This returns a newline-separated list of tag keys
            tag_keys = response.read().decode().split('\n')

        # Step 4: Loop through the keys to get their values
        for key in tag_keys:
            if key:  # ensure the key isn't empty
                val_req = urllib.request.Request(
                    f"http://169.254.169.254/latest/meta-data/tags/instance/{key}",
                    headers={"X-aws-ec2-metadata-token": token}
                )
                with urllib.request.urlopen(val_req, timeout=1) as val_res:
                    instance_tags[key] = val_res.read().decode()

    except Exception as e:
        # Fails gracefully if not on EC2 or if tags are not enabled in the Launch Template
        instance_tags = {"error": "Could not fetch tags. Ensure 'Allow tags in metadata' is enabled."}

    return {
        "container_id": container_id,
        "ec2_instance_id": ec2_instance_id,
        "tags": instance_tags
    }
