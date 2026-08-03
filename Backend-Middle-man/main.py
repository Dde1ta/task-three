import httpx
import os
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins (good for local dev, change for production)
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)


# The destination server where requests will be forwarded
TARGET_URL = os.getenv("BACKEND-URL", None)


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"])
async def forward_request(path: str, request: Request):

    if TARGET_URL is None:
        return JSONResponse(content={"error": "url not set"}, status_code=500)

    # 1. Extract request details
    url = f"{TARGET_URL}/{path}"
    headers = dict(request.headers)

    # Remove the original host header to let the target server handle it correctly
    headers.pop("host", None)

    # 2. Forward the request asynchronously using httpx
    async with httpx.AsyncClient() as client:
        target_response = await client.request(
            method=request.method,
            url=url,
            headers=headers,
            params=dict(request.query_params),
            content=await request.body()
        )

    # 3. Return the response back to the client
    return Response(
        content=target_response.content, # This is raw bytes, which Response expects
        status_code=target_response.status_code,
        headers=dict(target_response.headers)
    )
