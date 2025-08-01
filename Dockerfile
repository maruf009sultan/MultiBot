FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y git jq
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Clone repositories and install requirements
RUN bash run.sh

# Start the application
CMD python3 main.py
