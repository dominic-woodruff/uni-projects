from openai import OpenAI
import config
import subprocess

client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are Gene Siskel and Roger Ebert and you review movies."},
        {
            "role": "user",
            "content": "Can you give 10 different reviews of the movie 'The Wind Rises'",
        },
        {
            "role": "assistant",
            "content": "Yes, here are 10 reviews by us, Siskel and Ebert,",
        },
    ]
)

output = response.choices[0].message.content
# print(output)
subprocess.run(['python', 'app_json.py', output])