# Use a lightweight Python 3.9 image as the base
# Python 3.9 is chosen for broad compatibility, but you can adjust if needed.
FROM python:3.9-slim-buster

# Set the working directory inside the container
# All subsequent commands will be executed relative to this directory.
WORKDIR /app

# Copy the requirements.txt file into the container
# This step is done separately to leverage Docker's build cache.
# If only requirements.txt changes, Docker won't re-run the pip install step.
COPY requirements.txt .

# Install the Python dependencies
# --no-cache-dir: Prevents pip from storing cached downloads, reducing image size.
# -r requirements.txt: Installs all packages listed in requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
# The '.' copies everything from the current host directory (where Dockerfile is)
# to the /app directory inside the container.
COPY . .

# Expose port 8000
# The `adk web` command, which we'll use to run the agent's UI, defaults to port 8000.
# This tells Docker that the container listens on this port at runtime.
EXPOSE 8000

# Define the command to run when the container starts
# `adk web adk_agent.py`: Starts the ADK web UI for your agent defined in adk_agent.py.
# `--host 0.0.0.0`: This is crucial for containerized applications. It tells the server
#                   to bind to all available network interfaces, allowing the deployment
#                   platform's proxy to forward requests to your application.
# `--port 8000`: Explicitly sets the port, matching the EXPOSE instruction.
CMD ["adk", "web", "adk_agent.py", "--host", "0.0.0.0", "--port", "8000"]
