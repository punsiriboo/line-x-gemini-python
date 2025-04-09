from google import genai
from google.genai import types
import os
from PIL import Image as PILImage
import io
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])


def generate_text(text):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[text],
        config=types.GenerateContentConfig(
            max_output_tokens=200,
        ),
    )
    print(f"Gemini response: {response.text}")
    return response.text


def image_description(image_content):
    pil_image = PILImage.open(io.BytesIO(image_content))

    prompt = "What is shown in this image in Thai?"
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=[
            prompt,
            pil_image,
        ],
        config=types.GenerateContentConfig(
            max_output_tokens=200,
        ),
    )
    print(f"Gemini response: {response.text}")
    return response.text


def document_description(file_content):
    prompt = "Summarize this document in Thai"
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[
            types.Part.from_bytes(
                data=file_content,
                mime_type="application/pdf",
            ),
            prompt,
        ],
        config=types.GenerateContentConfig(
            max_output_tokens=200,
        ),
    )
    print(f"Gemini response: {response.text}")
    return response.text
