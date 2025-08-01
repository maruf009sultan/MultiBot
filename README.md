MultiBots: Run Multiple Telegram Bots in One Instance

MultiBots is a lightweight, open-source solution for hosting multiple Telegram bots in a single Dockerized Python environment. Say goodbye to managing separate hosting instances for each bot—MultiBots streamlines deployment, reduces resource usage, and supports public and private GitHub repositories. Perfect for developers, hobbyists, and small teams looking to host Python-based Telegram bots efficiently.

Features

Multi-Bot Hosting: Run multiple Telegram bots in one instance, saving resources and simplifying management.
GitHub Integration: Clone public or private bot repositories directly from GitHub.
Custom Environments: Set unique environment variables for each bot.
Flexible Execution: Specify the main script for each bot to start execution.
Web Keep-Alive: Built-in Flask web server prevents hosting services from idling.
Dockerized: Easy deployment with Docker, compatible with platforms like Render, Scalingo, or Heroku.
Lightweight: Optimized for low-memory environments (500MB recommended for up to 5 bots).


Why Choose MultiBots?

Cost-Effective: Host multiple bots for free on platforms with Docker support.
Scalable: Easily add more bots by updating a single configuration file.
Secure: Supports private repositories with GitHub tokens for secure access.
Developer-Friendly: Minimal setup with clear documentation for Python developers.
SEO-Optimized: Keywords like "Telegram bot hosting," "multi-bot Docker," and "Python bot framework" ensure discoverability.


Getting Started
Prerequisites

Docker: Installed on your local machine or hosting service.
GitHub Account: For accessing bot repositories (public or private).
Python Knowledge: Basic understanding of Python and environment variables.
Hosting Platform: A service supporting Docker (e.g., Render, Scalingo, or Heroku).

Installation

Fork or Clone the Repository
git clone https://github.com/<your-username>/MultiBots.git
cd MultiBots


Configure config.json
Edit config.json to define your bots. Each bot needs a source (GitHub repository URL), env (environment variables), and run (main script to execute). Example:
{
    "EbookBot": {
        "source": "https://github.com/<username>/Ebooks-Bot.git",
        "env": {
            "TOKEN": "your-telegram-bot-token",
            "ID": "123",
            "HASH": "abc123"
        },
        "run": "main.py"
    },
    "PrivateBot": {
        "source": "https://<username>:<github-token>@github.com/<username>/private-bot.git",
        "env": {
            "TOKEN": "another-telegram-bot-token"
        },
        "run": "bot.py"
    }
}


Replace <username> and <github-token> for private repositories.
Obtain Telegram bot tokens from BotFather.
Ensure each bot repository has a requirements.txt for dependencies.


Make run.sh Executable
chmod +x run.sh


Build and Run the Docker Container
docker build -t multibots .
docker run -p 10000:10000 multibots

The Flask web server runs on port 10000, and bots start automatically.

Deploy to a Hosting Platform

Push your repository to GitHub.
Connect it to a Docker-compatible hosting service (e.g., Render).
Set the port to 10000 in the hosting service’s configuration.
Monitor logs to ensure bots are running.




Usage

Access the web server at http://<your-host>:10000 to verify the app is running (displays a GIF).
Bots run in their respective directories with isolated environments.
Add or remove bots by updating config.json and rebuilding the Docker image.
For private repositories, use a GitHub personal access token in the source URL.


Technical Details
Project Structure

main.py: Core Python script handling:
Flask web server for keep-alive and basic UI.
Bot execution with custom environments.
Periodic pinging to prevent idling.


run.sh: Shell script to clone bot repositories and install their dependencies.
config.json: Configuration file for bot definitions (source, env, run script).
Dockerfile: Sets up a Python 3.9 environment, installs dependencies, and runs the app.

Dependencies

Python 3.9: Base environment in the Docker image.
Flask (2.0.1): Lightweight web server for hosting and keep-alive.
Requests: For internal pinging to keep the server active.
Git and jq: Installed in the Docker image for repository cloning and JSON parsing.

How It Works

Docker Build:

Installs system dependencies (git, jq) and Python packages (flask, requests).
Runs run.sh to clone bot repositories and install their requirements.txt.


Runtime:

main.py starts a Flask server on port 10000.
A thread pings the server every 120 seconds to prevent idling.
Another thread reads config.json, sets environment variables, and spawns bot processes.
Each bot runs in its own directory with isolated environment variables.


Bot Execution:

Bots are cloned from GitHub (public or private).
Their dependencies are installed via pip.
The specified run script is executed with python3.



Limitations

Supports Python-based Telegram bots only (no native Docker bot support).
Recommended max of 5 bots for 500MB memory to avoid resource exhaustion.
Hosting service must support Docker and expose port 10000.


Marketing & SEO
Target Audience

Indie Developers: Building Telegram bots for personal or community use.
Small Teams: Needing a cost-effective way to host multiple bots.
Hobbyists: Experimenting with Telegram bot development.
Students: Learning Python, Docker, or bot development.

SEO Keywords

Telegram bot hosting
Multi-bot Docker Python
Free Telegram bot hosting
Python Telegram bot framework
Host multiple Telegram bots
Dockerized bot deployment
GitHub Telegram bot integration




Contributing
We welcome contributions! To contribute:

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

Please follow the Code of Conduct and report issues via GitHub Issues.



Support

Issues: Report bugs or request features on GitHub Issues.
Community: Join discussions on X or Telegram developer groups.
Contact: Reach out via GitHub for collaboration or inquiries.


MultiBots: Simplify your Telegram bot hosting today! 🚀
