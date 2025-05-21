from google import genai

client = genai.Client(api_key="YourAPIKey")

QUESTION = input("Enter a question, and gemini Ai will answer it: ")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=f"my question is {QUESTION}",
)
print(response.text)
