from urllib.parse import urlparse
from azure.ai.inference import ChatCompletionsClient
from azure.identity import DefaultAzureCredential

# Project endpoint has the form:
#   https://<ai-services-name>.services.ai.azure.com/api/projects/<project-name>
# Inference endpoint strips the path and appends /models:
#   https://<ai-services-name>.services.ai.azure.com/models
endpoint = "<%= endpoint %>"
inference_endpoint = f"https://{urlparse(endpoint).netloc}/models"

chat = ChatCompletionsClient(
    endpoint=inference_endpoint,
    credential=DefaultAzureCredential(),
    credential_scopes=["https://ai.azure.com/.default"],
)

response = chat.complete(
    model="<%= chatDeploymentName %>",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "<%= userMessage %>"}
    ],
    stream=True,
)

for event in response:
    if event.choices:
        content = event.choices[0].delta.content
        if content:
            print(content, end="", flush=True)

print()
