# assesment-for-PearlThoughts
Task: Implement an AI service that generates LinkedIn posts reflecting the client physician's perspective on healthcare AI topics

## Setup Instructions

### 1. Environment Setup
1. Create a virtual environment:
```bash
python -m venv .venv
```

2. Activate the virtual environment:
- Windows:
```bash
.venv\Scripts\activate
```
- Linux/Mac:
```bash
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 2. Environment Variables
Create a `.env` file in the root directory with the following variables:
```
AZURE_OPENAI_API_KEY=your_api_key_here
AZURE_OPENAI_ENDPOINT=your_endpoint_here
AZURE_OPENAI_DEPLOYMENT_EMBEDDING=your_embedding_deployment_name
AZURE_OPENAI_DEPLOYMENT_CHAT=your_chat_deployment_name
AZURE_OPENAI_API_VERSION_CHAT=your_api_version
```

Replace the placeholder values with your actual Azure OpenAI credentials.

### 3. Running the Code
The main functionality is in `generator.py`. You can use it to generate LinkedIn posts by providing an article summary and perspectives.

Example usage:
```python
from generator import generate_physician_linkedin_post

article_summary = "Your article summary here"
perspectives = [
    "Perspective 1",
    "Perspective 2",
    "Perspective 3"
]

result = generate_physician_linkedin_post(article_summary, perspectives)
print(result["linkedin_post"])
print(f"Confidence Score: {result['confidence_score']}")
```

## Notes
- Make sure you have valid Azure OpenAI credentials
- The code uses Azure OpenAI's embedding and chat models
- The generated posts are optimized for LinkedIn's format and length
- A confidence score is provided to indicate how well the post aligns with the given perspectives
