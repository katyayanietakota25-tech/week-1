
from google import genai
from getpass import getpass

try:
    api_key = getpass("Enter your Gemini API key: ")

    if not api_key:
        raise ValueError("Gemini API key is missing.")

    client = genai.Client(api_key=api_key)

    prompt = "What is prompt engineering? Answer in one sentence."

    print("Environment ready. Sending prompt...")
    print("\nPrompt:")
    print(prompt)

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    print("\nResponse:")
    print(response.text)

    second_prompt = "Explain AI in one sentence."

    response2 = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=second_prompt
    )

    print("\nSecond Response:")
    print(response2.text)

    print("\nConnectivity test completed successfully.")

except ValueError as e:
    print("Input Error:", e)

except Exception as e:
    print("API/Network Error:", e)
