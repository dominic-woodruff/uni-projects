from openai import OpenAI
import config
import sys

client = OpenAI(api_key=config.OPENAI_API_KEY)


# User Query command line 
response = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type": "json_object"},
    messages=[{"role": "system",
               "content": "Convert the user's query in a JSON object"},
              {"role": "user",
               "content": sys.argv[1]}])

# Extract the response
print(response.choices[0].message.content)
