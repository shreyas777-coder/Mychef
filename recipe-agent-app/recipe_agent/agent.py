import os
from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
import google.auth

# 1. Configure the LLM
MODEL_NAME = "gemini-2.5-flash"

# 1. Configure the LLM
# The ADK will automatically look for the GEMINI_API_KEY environment variable.
MODEL_NAME = "gemini-2.5-flash"  # A fast, capable model for this task

# 2. Define the Agent
RecipeAgent = Agent(
    model=MODEL_NAME,
    name="RecipeAssistant",
    description="An AI agent that generates detailed recipes from ingredients or dish names.",
    instruction=(
        """
        You are a world-class culinary expert AI. Your task is to act as a recipe generator.
        
        RULES:
        1. If the user provides a list of ingredients, suggest a matching dish and provide a detailed, step-by-step recipe.
        2. If the user asks for a specific dish, provide the complete, step-by-step recipe for that dish.
        3. The recipe must include: The dish name, a brief description, a list of ingredients with measurements, and numbered cooking instructions.
        4. Always be encouraging and friendly.
        """
    ),
    tools=[],  # No external tools are strictly necessary for simple generation
)

# 3. Set the root agent
# This agent will be the entry point for all interactions.
root_agent = RecipeAgent

if __name__ == "__main__":
    # Example local interaction (requires setting GEMINI_API_KEY)
    print("Recipe Agent Ready. Ask for a recipe!")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                break
            
            # The agent's core interaction method
            response = root_agent.send_message(user_input)
            print(f"Agent: {response.text}")
            
        except Exception as e:
            print(f"An error occurred: {e}")