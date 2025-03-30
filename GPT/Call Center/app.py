import openai
import config
import time
import json

client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

# Upload files
qa_analysis_file = client.files.create(
  file=open("Quality Assurance Analysis.pdf", "rb"),
  purpose='assistants'
)

qa_guidance_file = client.files.create(
  file=open("Quality_Assurance_Guidance.pdf", "rb"),
  purpose='assistants'
)

core_values_file = client.files.create(
  file=open("Core_Values.txt", "rb"),
  purpose='assistants'
)

# Create an assistant
call_center_assistant = client.beta.assistants.create(
  name="Call Center Assistant",
  instructions=open("instructions.txt", "r").read(),  # Read file content as string
  model="gpt-4-turbo-preview",
  tools=[{"type": "file_search"}],
  tool_resources={
    "code_interpreter": {
      "file_ids": [qa_analysis_file.id, qa_guidance_file.id, core_values_file.id]
    }
  }
)

# Create a thread
thread = client.beta.threads.create()

# Read JSON file content
with open("output.json", "r") as json_file:
    json_content = json.load(json_file)

# Send a message
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=json.dumps(json_content)
)

# Run the assistant
run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=call_center_assistant.id
)

# Function to wait for completion
def waiting_assistant_in_progress(thread_id, run_id, max_loops=20):
    for _ in range(max_loops):
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )
        if run.status != "in_progress":
            break
        time.sleep(1)
    return run

run = waiting_assistant_in_progress(thread.id, run.id)

# Retrieve messages
messages = client.beta.threads.messages.list(thread_id=thread.id)
print(messages.data[0].content[0].text.value)
