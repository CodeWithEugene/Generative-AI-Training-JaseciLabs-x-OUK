import os
import google.generativeai as genai

def get_joke():
    try:
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content("Tell me a joke about a programmer.")
        return response.text
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    print(get_joke())
