import os
import uvicorn
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app

# Get the directory where main.py is located, which is also the agent's root directory
AGENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Arguments for the ADK FastAPI integration
# 'agents_dir' tells ADK where to find the agent.py file
# 'web=True' enables the built-in ADK web UI for easy testing
app_args = {"agents_dir": AGENT_DIR, "web": True}

# Create the FastAPI app with ADK integration
app: FastAPI = get_fast_api_app(**app_args)

# Simple health check endpoint for Cloud Run
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "adk-recipe-agent"}

# Main execution block for local testing
if __name__ == "__main__":
    # Cloud Run exports the port number to the PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")