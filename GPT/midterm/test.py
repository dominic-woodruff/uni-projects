from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What are the differences between these files?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://live.staticflickr.com/65535/53917125800_a8a617e93f_m.jpg",
          },
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://live.staticflickr.com/65535/53916680331_723921f01e_m.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])