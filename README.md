# 🚀 MultiBots: The Ultimate Multi-Telegram Bot Hosting Platform

---

> **Host, scale, and manage ALL your Python Telegram bots in ONE blazing-fast, resource-efficient Docker container.**  
> Perfect for indie developers, small teams, hobbyists, and students.  
> **Save money. Save RAM. Save time. Get started in minutes.**

---

![MultiBots Hero Banner](https://i.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.webp)

---

## 🏆 WHY MULTIBOTS?

- **All-in-One:** Host UNLIMITED Python Telegram bots together—no more separate servers or costly cloud bills!
- **Plug & Play:** Just list your bots in `config.json`, build, and you're LIVE.
- **Super Scalable:** Add/remove bots with ONE config file edit. Instantly scale as your project grows!
- **Private/Public Repo Support:** Seamlessly clone bots from both public and private GitHub repositories.
- **Fully Dockerized:** One command, one container, all your bots.
- **Ultra Lightweight:** Designed to run 5+ bots with as little as 500MB RAM!
- **Isolated Environments:** Each bot gets its own directory and environment variables—no messy cross-talk.
- **Free Hosting Ready:** Optimized for platforms like Render, Scalingo, Heroku, and more.
- **SEO-Optimized:** Find this project with keywords: `Telegram bot hosting`, `multi-bot Docker`, `Python bot framework`, `free Telegram bot hosting`.

---

## 🌍 WHO IS IT FOR?

- **Indie Hackers & Makers:** Launch, test, and run multiple side projects with ease.
- **Open Source Developers:** Maintain all your bots in one place, share with the world.
- **Small Teams/Startups:** Drastically cut infrastructure costs.
- **Students & Learners:** The IDEAL playground for mastering Python, Docker, and bot development.
- **Community Managers:** Deploy multiple community bots from a SINGLE dashboard.

---

## 💡 FEATURES AT A GLANCE

- 🚦 **Multi-Bot, Multi-Repo:** One container, many bots, any repo.
- 🔒 **Secure Private Repo Cloning:** Easy GitHub token integration.
- 💬 **Custom ENV for Each Bot:** No accidental token leaks or conflicts.
- 🛡️ **Web Keep-Alive:** Built-in Flask server keeps your bots running on free hosts.
- 🛠️ **Minimal Setup:** Get started in under 10 minutes!
- 🏗️ **Docker First:** Build once, run anywhere.
- 🔍 **Easy Debugging:** Standard Docker logging, clean structure.
- 💸 **Budget Friendly:** Zero-cost hosting for small teams and indie devs.
- 🧑‍💻 **Developer-Focused:** Clean Python code, fully open source, MIT licensed.

---

# 🚀 GETTING STARTED (5 mins!)

## 1️⃣ Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed (locally or on your cloud host)
- [GitHub Account](https://github.com/)
- **Basic Python knowledge**
- A Docker-compatible hosting platform (Render, Scalingo, Heroku, etc.)

---

## 2️⃣ Installation

### Clone this Repo:
```bash
git clone https://github.com/<your-username>/MultiBot.git
cd MultiBot
```

### Configure Your Bots:
Edit `config.json` to define as many bots as you want!
```json
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
```
- **Private bots?** Insert your GitHub token into the repo URL.
- **Each repo must have a `requirements.txt`.**
- Get your bot tokens from [BotFather](https://core.telegram.org/bots#botfather).

---

### Make the Script Executable:
```bash
chmod +x run.sh
```

### Build and Run Docker:
```bash
docker build -t multibots .
docker run -p 10000:10000 multibots
```
- Web server runs on **port 10000**.
- All bots start automatically!

---

### Deploy to the Cloud:
- Push your MultiBot repo to GitHub.
- Deploy to any Docker-compatible host (Render, Scalingo, Heroku, etc.).
- Set exposed port to **10000** on your dashboard.
- Watch your logs for startup messages.

---

# 💻 HOW TO USE

- **Check your bots:** Visit `http://<your-host>:10000` (fun GIF = it's working!).
- **Add or remove bots:** Edit `config.json`, rebuild the Docker image.
- **Private repos:** Use your GitHub token in the URL.
- **Logs:** Use `docker logs` or your platform's dashboard for debugging.
- **Change environment variables:** Just update the `env` section per bot in `config.json`.

---

# 🏗️ HOW IT WORKS (Under the Hood)

### Main Components

- **`main.py`:**  
  - Runs a Flask server for keep-alive and status page.
  - Reads `config.json`, spawns each bot as a separate subprocess with its own env.
  - Pings itself to prevent idling on free hosts.

- **`run.sh`:**  
  - Clones each bot repo.
  - Installs Python dependencies from `requirements.txt`.

- **`Dockerfile`:**
  - Installs system dependencies (`git`, `jq`), Python, Flask, Requests.
  - Runs `run.sh` during build.
  - Starts `main.py` at runtime.

### Execution Flow

1. **Build Stage:**
   - System and Python deps installed.
   - Bot repos cloned, their dependencies installed.

2. **Run Stage:**
   - Flask server starts (port 10000).
   - Thread pings server every 120 secs (keeps it alive).
   - Reads `config.json`, spawns each bot with its own env.

3. **Bot Lifecycle:**
   - Each bot runs in its own directory.
   - Each gets its own environment (no secret leaks).
   - All logs available via Docker or your host's dashboard.

---

# ⚠️ LIMITATIONS

- **Python Telegram bots ONLY** (no native Dockerfile-per-bot support).
- **Recommended:** Max 5 bots per 500MB RAM for best stability.
- **Must expose port 10000** on your host.
- **No built-in auto-redeploy** on `config.json` change (rebuild Docker image if you update bots).

---

# 🎯 SEO & DISCOVERABILITY

**Keywords:**  
`Telegram bot hosting`, `multi-bot Docker Python`, `free Telegram bot hosting`, `Python Telegram bot framework`, `host multiple Telegram bots`, `dockerized bot deployment`, `GitHub Telegram bot integration`.

---

# 🤝 CONTRIBUTING

We love contributors!  
1. Fork this repo.
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature`
5. Open a Pull Request.

See our Code of Conduct and report issues via GitHub Issues.

---

# 🆘 SUPPORT

- **Bugs or Requests?** [GitHub Issues](https://github.com/<your-username>/MultiBot/issues)
- **Community:** Join discussions on X (Twitter) or Telegram developer groups.
- **Collab?** DM via GitHub!

---

## ⚡ MultiBots: Simplify, scale, and supercharge your Telegram bot empire—TODAY!

---
