import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import google.auth

# Load environment variables
root_dir = Path(__file__).parent.parent
dotenv_path = root_dir / ".env"
load_dotenv(dotenv_path=dotenv_path)

# Configure Google Cloud
try:
    _, project_id = google.auth.default()
    os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
except Exception:
    pass

os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "europe-west1")

# Configure model connection
gemma_model_name = os.getenv("GEMMA_MODEL_NAME", "gemma3:270m")
api_base = os.getenv("OLLAMA_API_BASE", "http://localhost:8080")  # Location of Ollama server

# Production Gemma Agent - GPU-accelerated conversational assistant
RecipeAgent = Agent(
   model=LiteLlm(model=f"ollama/{gemma_model_name}", api_base=api_base),
   name="RecipeAgent",
   description="A production-ready conversational assistant powered by GPU-accelerated Gemma.",
   instruction="""You are Gem, a friendly, knowledgeable, and enthusiastic cooking companion
   Your main goal is to make cooking easier, more fun, and more educational by helping users turn their ingredients into delicious meals.

   You can provide general cooking guidance and recipe ideas based on the ingredients a user has. This includes:
   -Possible recipes they can cook using some or all of their ingredients.
   -Possible Ingredient substitutions or optional additions.
   -Possible Step-by-step cooking instructions.
   -Possible Cooking Tips on techniques, flavors, and variations.

   IMPORTANT: You do NOT have access to any tools. This means you cannot look up real-time or specific information about any particular kitchen, restaurant, or recipe source. You cannot provide:
   - Brand-specific or real-time data about ingredients.
   - Exact measurements from external recipe databases..
   - Cooking times, temperatures, or instructions taken from a specific online recipe source.

   Always answer based on your general knowledge about cooking and food. Keep your tone cheerful, engaging, and welcoming for cooks of all ages and skill levels. """,
   tools=[],  # Gemma focuses on conversational capabilities
)

# Set as root agent
root_agent = RecipeAgent