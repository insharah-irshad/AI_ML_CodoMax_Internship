import os
from google import genai


# Get API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY is not set.")
    print("Please set your Gemini API key before running the program.")
    exit()


# Create Gemini client
client = genai.Client(api_key=api_key)


def summarize_text(text, summary_type):
    """Generate a summary using Gemini."""

    if summary_type == "1":
        instruction = "Summarize the text in 2-3 concise sentences."

    elif summary_type == "2":
        instruction = "Summarize the text in one clear paragraph while keeping the important details."

    else:
        instruction = "Provide a detailed summary covering all important points from the text."


    prompt = f"""
You are a helpful AI text summarization assistant.

{instruction}

Do not add information that is not present in the original text.

Text:
{text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text


# Main program
print("=" * 45)
print("          AI TEXT SUMMARIZER")
print("=" * 45)

print("\nChoose summary length:")
print("1. Short")
print("2. Medium")
print("3. Detailed")

summary_type = input("\nEnter your choice (1/2/3): ").strip()

if summary_type not in ["1", "2", "3"]:
    print("\nInvalid choice. Please select 1, 2, or 3.")
    exit()


print("\nEnter the text you want to summarize.")
print("Type 'END' on a new line when finished.\n")

lines = []

while True:
    line = input()

    if line.strip().upper() == "END":
        break

    lines.append(line)

text = "\n".join(lines)


if not text.strip():
    print("\nError: No text was entered.")

else:
    try:
        summary = summarize_text(text, summary_type)

        print("\n" + "=" * 45)
        print("                  SUMMARY")
        print("=" * 45)
        print(summary)

    except Exception as error:
        print("\nAn error occurred:")
        print(error)