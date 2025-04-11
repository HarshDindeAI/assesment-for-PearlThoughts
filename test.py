from generator import generate_physician_linkedin_post
summary = "Stanford researchers developed an AI tool that can detect early-stage lung cancer from CT scans with 94% accuracy."
perspectives = [
    "AI is an enabler, not a replacement for physicians",
    "Patient outcomes must remain the primary focus",
    "Clinical validation is essential before deployment",
    "AI should reduce administrative burden",
    "Interdisciplinary collaboration is key to adoption"
]

result = generate_physician_linkedin_post(summary, perspectives)
print(result["linkedin_post"])
print("Confidence:", result["confidence_score"])



