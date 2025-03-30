from flask import Flask, request, render_template
from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)
from typing import List

app = Flask(__name__)

def assist_transcriber(url: str):
    from openai import OpenAI
    from youtube_transcript_api import YouTubeTranscriptApi

    import config
    import json

    client = OpenAI(api_key=config.OPENAI_API_KEY)

    # Download the transcript from the YouTube video
    transcript_list = YouTubeTranscriptApi.list_transcripts(url)
    transcript = transcript_list.find_generated_transcript(['en']).fetch()

    # Extract and concatenate all text elements
    concatenated_text = " ".join(item['text'] for item in transcript)

    #  Call the openai ChatCompletion endpoint, with the ChatGPT model
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Summarize the following transcript."},
            {"role": "assistant", "content": "Yes."},
            {"role": "user", "content": concatenated_text}])

    return (response.choices[0].message.content)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    url = request.form["url"]
    ai_response = assist_transcriber(url)
    return render_template("index.html",summary=ai_response)

if __name__ == "__main__":
    app.run()