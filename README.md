# pred
🔮 Sports Match Prediction Agent
This project implements an AI agent powered by Google's Gemini ADK to predict the outcomes of various sports matches. It leverages a modular architecture with dedicated components for data collection, pattern detection, and sport-specific prediction models.

✨ Features
Multi-Sport Prediction: Predicts matches for Basketball, Football, Hockey, Volleyball, Cricket, and Tennis.

Agentic AI: Utilizes Google's Gemini Agent Development Kit (ADK) to create an intelligent agent that can understand natural language queries and use internal tools to provide predictions.

Modular Design: Separates concerns into distinct Python modules for easier maintenance and extension.

Head-to-Head Analysis (Placeholder): Includes logic for analyzing historical head-to-head match data to inform predictions (currently uses placeholder data).

Pattern Detection (Placeholder): Identifies potential patterns in match data to provide additional insights (currently uses placeholder data).

Containerized Deployment: Ready for deployment using Docker on platforms like Render or Railway.

📁 Project Structure
sports_predictor_agent/
├── adk_agent.py          # Defines the Gemini ADK agent and its tools. (Main entry for agent)
├── predictor.py          # Core logic to parse input and dispatch to sport-specific models.
├── h2h_collector.py      # Handles (placeholder) API calls for head-to-head match data and team/player search.
├── pattern_detector.py   # Contains logic for detecting patterns in match data.
├── basketball_model.py   # Prediction model for Basketball.
├── football_model.py     # Prediction model for Football.
├── hockey_model.py       # Prediction model for Hockey.
├── volleyball_model.py   # Prediction model for Volleyball.
├── cricket_model.py      # Prediction model for Cricket.
├── tennis_model.py       # Prediction model for Tennis.
├── requirements.txt      # Lists all Python dependencies.
└── Dockerfile            # Instructions for building the Docker image for deployment.

🚀 Prerequisites
Before you begin, ensure you have the following installed:

Python 3.9+

pip (Python package installer)

Git (for cloning the repository)

Docker (if you plan to build the Docker image locally or deploy to a container platform)

API Keys
This project requires the following API keys:

Google Gemini API Key: For the Gemini ADK agent to function. Obtain one from Google AI Studio.

API-Sports Key: For fetching sports data (currently uses placeholder data in h2h_collector.py, but a real implementation would use this key). Obtain one from API-Sports.

⚙️ Setup Instructions
Clone the repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

(Replace your-username/your-repo-name with your actual GitHub repository details.)

Create a Python virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set Environment Variables:
It is crucial to set your API keys as environment variables. Do NOT hardcode them in your code.

export GEMINI_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"
export API_SPORTS_KEY="YOUR_API_SPORTS_IO_KEY"

For persistent local development, you might use a .env file and a library like python-dotenv to load them (though this project doesn't explicitly include python-dotenv). For deployment, platforms handle these securely.

🏃 How to Run Locally (Gemini ADK Agent)
Once setup is complete, you can run the Gemini ADK agent's local web UI:

adk web adk_agent.py

This command will start a local web server (usually on http://127.0.0.1:8000). Open this URL in your browser to interact with your Sports Prediction Agent.

You can then type queries like:

Predict the basketball match: Los Angeles Lakers vs Boston Celtics

football: PSG vs Real Madrid

tennis: Rafael Nadal vs Novak Djokovic

hockey: New York Rangers vs Philadelphia Flyers

volleyball: Brazil vs USA

cricket: India vs Australia

The agent will use its internal predict_sports_match tool to process your request and return a prediction.

🐳 Docker Deployment
This project includes a Dockerfile to facilitate containerized deployment on platforms like Render or Railway.

Build the Docker image (optional, for local testing):

docker build -t sports-predictor-agent .

Run the Docker image locally (optional):

docker run -p 8000:8000 -e GEMINI_API_KEY="YOUR_KEY" -e API_SPORTS_KEY="YOUR_KEY" sports-predictor-agent

Then access http://localhost:8000 in your browser.

Deploy to Render/Railway:

Push your entire project (including Dockerfile and requirements.txt) to a GitHub repository.

Connect your GitHub repository to your chosen platform (Render or Railway).

Configure the GEMINI_API_KEY and API_SPORTS_KEY as environment variables within the platform's service settings.

The platform will automatically detect the Dockerfile and deploy your application.

⚠️ Disclaimer & Future Improvements
Placeholder Data: Currently, the h2h_collector.py and *_model.py files use placeholder data for head-to-head matches and team statistics. For real-world predictions, you would need to integrate with a live sports data API (using your API_SPORTS_KEY) to fetch actual, up-to-date information.

Pattern Detection: The pattern_detector.py also contains placeholder logic. Real pattern detection would require more sophisticated algorithms and a larger dataset.

Model Training: The current prediction models are simplified. A production-ready system would involve training robust machine learning models on extensive historical data.

This project serves as a strong foundation for building a more advanced sports prediction agent with Gemini ADK.
