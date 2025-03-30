import openai
import config
import requests
import json
from pywinauto import Application
import logging
from concurrent.futures import ThreadPoolExecutor
import webbrowser
import os

openai.api_key = config.OPENAI_API_KEY

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def toJson(text_data):
    with open('text.json', 'w') as file:
        json.dump({"text": text_data}, file)

def save_to_html(text_data, output_file):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Translator</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                height: 100vh;
                display: flex;
                flex-direction: column;
            }}
            .container {{
                background-color: #fff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                width: 100%;
                height: 100%;
                box-sizing: border-box;
                overflow: auto;
            }}
            h1 {{
                text-align: center;
                color: #007bff;
                font-size: 2em;
                margin: 10px 0;
            }}
            pre {{
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 5px;
                font-size: 1.1em;
                line-height: 1.5;
                overflow: auto;
                height: calc(100% - 60px); /* Adjust for header and padding */
                margin: 0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Translator</h1>
            <pre>{text_data}</pre>
        </div>
    </body>
    </html>
    """


    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_template)

def download_webpage_html(url, output_file):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(response.text)
    except requests.RequestException as e:
        logging.error(f"Error downloading the webpage: {e}")
        return None
    return output_file

def get_open_webpage_url():
    try:
        app = Application(backend='uia').connect(title_re=".*Mozilla Firefox")
        main_firefox_winspec = app.window(title_re=".*Mozilla Firefox")
        url_bar = main_firefox_winspec.child_window(title_re=".*or enter address", control_type="Edit", found_index=0)
        if url_bar.exists(timeout=10):
            return url_bar.get_value()
        logging.warning("URL bar not found.")
    except TimeoutError as e:
        logging.error(f"TimeoutError: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    return None

def chunk_text(text, max_token_size=3000):
    words = text.split()
    chunks = []
    chunk = []
    for word in words:
        chunk.append(word)
        if len(" ".join(chunk)) > max_token_size:
            chunks.append(" ".join(chunk))
            chunk = []
    if chunk:
        chunks.append(" ".join(chunk))
    return chunks

def translate_chunk(chunk):
    try:
        translation = openai.ChatCompletion.create(
            model='gpt-4o',
            messages=[
                {"role": "system", "content": "You are a translator."},
                {"role": "assistant", "content": """Translate the following text into English, this is content of a website so 
                 ignore any html elements that are not visable to a reader and anything that may be a part of a toolbar, a sidebar, link, etc: """},
                {"role": "user", "content": chunk}
            ],
            max_tokens=4096,
            temperature=0.7
        )
        return translation['choices'][0]['message']['content'].strip()
    except Exception as e:
        logging.error(f"Error during translation: {e}")
        return ""

# Main logic
if __name__ == "__main__":

    url = get_open_webpage_url()
    if not url:
        logging.error("No open webpage found. Exiting.")
        exit()

    output_file = 'downloaded_page.html'
    if not download_webpage_html(url, output_file):
        logging.error("Failed to download webpage. Exiting.")
        exit()

    with open(output_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    chunks = chunk_text(html_content)
    
    with ThreadPoolExecutor() as executor:
        translated_chunks = list(executor.map(translate_chunk, chunks))

    translated_text = "\n".join(translated_chunks)

    print(translated_text)

    # Save the translated text
    toJson(translated_text)
    logging.info("Translation completed and saved to 'text.json'.")

    # Save the translated text to an HTML file
    html_output_file = 'translated_page.html'
    save_to_html(translated_text, html_output_file)
    logging.info(f"Translated text saved to '{html_output_file}', opening in browser.")

    # Open the translated output in the web browser
    webbrowser.open('file://' + os.path.realpath(html_output_file))
