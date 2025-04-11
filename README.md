# assesment-for-PearlThoughts
Task: Implement an AI service that generates LinkedIn posts reflecting the client physician's perspective on healthcare AI topics

## Code Explanation Video
Watch this video for a detailed explanation of the code and how it works:

[![Code Explanation Video]](https://youtu.be/JK08FdWKbTU)


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

#### Running the Flask Application
To start the Flask API server:

```bash
python app.py
```

This will start the server on `http://127.0.0.1:5000/` by default. You can then send POST requests to the `/generate` endpoint as described below.

#### Using the API
The application provides a Flask API endpoint at `/generate` that accepts POST requests with the following JSON structure:

```json
{
    "article_summary": "Stanford researchers developed an AI tool that can detect early-stage lung cancer from CT scans with 94% accuracy.",
    "perspectives": [
        "AI is an enabler, not a replacement for physicians",
        "Patient outcomes must remain the primary focus",
        "Clinical validation is essential before deployment",
        "AI should reduce administrative burden",
        "Interdisciplinary collaboration is key to adoption"
    ]
}
```

The API will respond with a JSON object containing the generated LinkedIn post and a confidence score:

```json
{
    "confidence_score": 0.8,
    "linkedin_post": "🚀 Exciting advancements in healthcare AI! Recently, Stanford researchers have developed an impressive AI tool capable of detecting early-stage lung cancer from CT scans with an astonishing 94% accuracy.\n\nThis breakthrough represents a significant step forward in utilizing AI to enhance patient care. However, it's essential to remember that AI is an enabler, not a replacement for the invaluable expertise of physicians. The role of this AI tool is to support clinicians, offering them an additional layer of precision and efficiency when interpreting complex imaging data.\n\nPatient outcomes must always remain our top priority. Early detection of lung cancer can dramatically improve prognosis and treatment success rates. With AI's ability to analyze vast amounts of data swiftly, we can potentially save countless lives by catching diseases earlier and more accurately.\n\nYet, before we get ahead of ourselves, clinical validation is paramount. Rigorous testing and real-world trials are necessary to ensure this technology's reliability and safety. We must adopt a measured approach, integrating AI innovations in a manner that complements and enhances clinical workflows without compromising patient care.\n\nMoreover, AI tools like this one can significantly reduce the administrative burden on healthcare professionals, allowing them to dedicate more time to direct patient care and complex decision-making. Interdisciplinary collaboration will be key to the successful integration of AI in healthcare. Combining the strengths of data scientists, clinicians, and healthcare administrators will pave the way for a future where AI not only supports but elevates the practice of medicine.\n\nTogether, let's embrace a future where AI empowers better healthcare outcomes for all. 🌟\n\n#HealthcareAI #PatientCare #ClinicalExcellence #AIinMedicine #InterdisciplinaryCollaboration"
}
```

#### Using the Python Function
You can also use the function directly in your Python code:

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
