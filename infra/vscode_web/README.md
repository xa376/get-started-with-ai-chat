# VS Code for the Web - Get Started with AI Chat

We've generated a simple development environment for you to deploy the **Get Started with AI Chat** template.

This template deploys a web-based chat application powered by Microsoft Foundry. It supports direct AI model interaction and optional [Retrieval-Augmented Generation (RAG)](https://learn.microsoft.com/azure/ai-studio/concepts/retrieval-augmented-generation) using Azure AI Search for knowledge retrieval from uploaded files.

The Azure AI Foundry extension provides tools to help you build, test, and deploy AI models and AI Applications directly from VS Code. Click on the Azure AI Foundry Icon on the left to see more.

Follow the instructions below to get started!

You should see a terminal opened with the template code already cloned.

## Deploy the template

You can provision and deploy this template using:

```bash
azd up
```

Follow the prompts to select your Azure subscription and region. The deployment creates a Microsoft Foundry project, Foundry Tools (including a gpt-4o-mini model), and an Azure Container App to host the chat UI.

After deployment completes, the terminal will display the URL for your chat application.

If you need to delete the deployment and stop incurring any charges, run:

```bash
azd down
```

## Optional: Enable RAG with Azure AI Search

To enable knowledge retrieval from uploaded files, set the following variables in your `.env` before deploying:

```
AZURE_AI_EMBED_DEPLOYMENT_NAME="text-embedding-3-small"
AZURE_AI_EMBED_DIMENSIONS=100
AZURE_AI_SEARCH_ENDPOINT="https://<your-search-service>.search.windows.net"
AZURE_AI_SEARCH_INDEX_NAME="<your-index-name>"
```

See the [RAG documentation](https://github.com/Azure-Samples/get-started-with-ai-chat/blob/main/docs/RAG.md) for details.

## Continuing on your local desktop

You can keep working locally on VS Code Desktop by clicking "Continue On Desktop..." at the bottom left of this screen. Be sure to take the .env file with you using these steps:

- Right-click the .env file
- Select "Download"
- Move the file from your Downloads folder to the local git repo directory
- For Windows, you will need to rename the file back to .env using right-click "Rename..."

## More examples

- [Azure AI Inference client library for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-inference/README.md) — Chat completions, embeddings, and more
- [Azure AI Projects client library for Python](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/ai/azure-ai-projects/README.md) — Project management and AI service integration

## Troubleshooting

- If you are instantiating your client via endpoint on an Azure AI Foundry project, ensure the endpoint is set in the `.env` as `https://{your-foundry-resource-name}.services.ai.azure.com/api/projects/{your-foundry-project-name}`
- The default chat model is `gpt-4o-mini`. To use a different model, update `AZURE_AI_CHAT_DEPLOYMENT_NAME` in your `.env` file and ensure the model is deployed in your Foundry project.
- For tracing and monitoring, set `ENABLE_AZURE_MONITOR_TRACING="true"` in your `.env` and ensure Application Insights is enabled in your Foundry project.
