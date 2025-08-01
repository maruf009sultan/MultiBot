import os
import subprocess
import json
import time
import flask
import threading
import requests

app = flask.Flask(__name__)

@app.route('/')
def home():
    return """
<center>
    <img src="https://i.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.webp" style="border-radius: 12px;"/>
</center>
<style>
    body { background: antiquewhite; }
</style>
"""

def ping_server():
    while True:
        try:
            requests.get('http://0.0.0.0:10000')
        except:
            pass
        time.sleep(120)

def run_bots():
    with open("config.json", "r") as jsonfile:
        bots = json.load(jsonfile)

    bot_processes = []
    for bot_name, bot_config in bots.items():
        time.sleep(5)
        bot_dir = f"/app/{bot_name}"
        bot_file = os.path.join(bot_dir, bot_config['run'])

        # Set environment variables for this bot
        bot_env = os.environ.copy()
        for env_name, env_value in bot_config['env'].items():
            bot_env[env_name] = env_value

        print(f'Starting {bot_name} bot with {bot_file}')
        p = subprocess.Popen(['python3', bot_file], cwd=bot_dir, env=bot_env)
        bot_processes.append(p)

    for p in bot_processes:
        p.wait()

if __name__ == '__main__':
    # Start ping server in a separate thread
    threading.Thread(target=ping_server, daemon=True).start()
    # Start bots in a separate thread
    threading.Thread(target=run_bots, daemon=True).start()
    # Run Flask app
    app.run(host='0.0.0.0', port=10000)
