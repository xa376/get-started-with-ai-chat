from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

project = AIProjectClient(
    endpoint="<%= endpoint %>",
    credential=DefaultAzureCredential())

client = project.get_openai_client(api_version="2024-12-01-preview")

response = client.chat.completions.create(
    model="<%= chatDeploymentName %>",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "<%= userMessage %>"}
    ],
    stream=True,
)

for chunk in response:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print()
