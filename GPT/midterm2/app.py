from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)

data = "data.jsonl"

file = client.files.create(
    file=open(data, "rb"),
    purpose="fine-tune"
)
print(file.id)