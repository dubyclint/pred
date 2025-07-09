# adk_agent.py
import os
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool
from predictor import predict_sports_match # Import your main prediction function

# It's crucial to set your API keys as environment variables.
# Do NOT hardcode them directly in the script for production.
# For local testing, you would run:
# export GEMINI_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY_HERE"
# export API_SPORTS_KEY="YOUR_API_SPORTS_KEY_HERE"

def create_sports_prediction_agent() -> LlmAgent:
    """
    Creates a Gemini ADK agent for sports predictions.
    """
    return LlmAgent(
        name="SportsPredictorAgent",
        model="gemini-1.5-pro",  # Using a powerful Gemini model
        instruction=(
            "You are an expert sports prediction agent. "
            "Your main goal is to predict the outcomes of sports matches given the sport and two team names. "
            "Always use the 'predict_sports_match' tool to get predictions. "
            "Provide the prediction result clearly, including the winner, win percentage, score range, and any pattern summaries. "
            "If a team is not found or the sport is not supported, report the error from the tool."
        ),
        tools=[
            FunctionTool(
                func=predict_sports_match,
                name="predict_sports_match",
                description="Predicts the outcome of a sports match given the sport and two team names. "
                            "Input format for the tool is a string like: 'sport: teamA vs teamB'. "
                            "Example usage: 'basketball: Lakers vs Celtics' or 'football: PSG vs Real Madrid'. "
                            "The tool will return a dictionary with prediction details or an error."
            ),
        ],
    )

# This makes the agent discoverable by `adk web` or `adk run`
root_agent = create_sports_prediction_agent()

if __name__ == "__main__":
    print("Agent definition file loaded. Use 'adk web adk_agent.py' or 'adk run adk_agent.py' to interact.")
