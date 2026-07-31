import React, { useState } from 'react';

// Reusable component to handle individual API calls
const EndpointSection = ({ title, description, endpoint, baseUrl }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const callApi = async () => {
    setLoading(true);
    setError(null);
    setData(null);

    try {
      const response = await fetch(`${baseUrl}${endpoint}`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const result = await response.json();
      setData(result);
    } catch (err) {
      setError(`Error connecting to API: ${err.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ marginBottom: '2rem', paddingBottom: '2rem', borderBottom: '1px solid #eaeaea' }}>
      <h2>{title}</h2>
      <p>{description}</p>

      <button
        onClick={callApi}
        disabled={loading}
        style={{
          padding: '0.5rem 1rem',
          cursor: loading ? 'not-allowed' : 'pointer',
          backgroundColor: '#efefef',
          border: '1px solid #ccc',
          borderRadius: '4px'
        }}
      >
        {loading ? 'Calling API...' : `Call API`}
      </button>

      {/* Error Message */}
      {error && (
        <div style={{ color: '#900', marginTop: '1rem', padding: '1rem', backgroundColor: '#fee', borderRadius: '4px' }}>
          {error}
        </div>
      )}

      {/* Success Message & JSON Data */}
      {data && (
        <div style={{ marginTop: '1rem' }}>
          <div style={{ color: '#090', marginBottom: '0.5rem', fontWeight: 'bold' }}>Success!</div>
          <pre style={{ backgroundColor: '#f4f4f4', padding: '1rem', borderRadius: '4px', overflowX: 'auto' }}>
            {JSON.stringify(data, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

export default function App() {
  // Base URL setup
  // Note: If using Create React App, use process.env.REACT_APP_BACKEND_URL
  // If using Vite, use import.meta.env.VITE_BACKEND_URL
  const BASE_URL = import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

  return (
    <div style={{ fontFamily: 'sans-serif', maxWidth: '800px', margin: '0 auto', padding: '2rem' }}>
      <h1>FastAPI API Client</h1>
      <p>A simple UI to test our backend endpoints.</p>

      <hr style={{ margin: '2rem 0', border: 'none', borderTop: '2px solid #eaeaea' }} />

      <EndpointSection
        title="1. Root Endpoint (/)"
        description="Fetches the welcome message."
        endpoint="/"
        baseUrl={BASE_URL}
      />

      <EndpointSection
        title="2. Maker Endpoint (/maker)"
        description="Fetches information about the creator."
        endpoint="/maker"
        baseUrl={BASE_URL}
      />

      <EndpointSection
        title="3. WhoAmI Endpoint (/who)"
        description="Fetches container and instance metadata."
        endpoint="/who"
        baseUrl={BASE_URL}
      />
    </div>
  );
}