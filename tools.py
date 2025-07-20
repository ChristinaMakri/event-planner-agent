import openai
import os
from fpdf import FPDF

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_vibe(event_description: str) -> str:
    """
    Given the user event description, generate a creative prompt for DALL·E.
    """
    prompt = f"""
    Create an artistic image prompt based on the following event description:
    {event_description}

    Make it descriptive and capture the atmosphere and style fitting the theme.
    """

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    vibe_prompt = response.choices[0].message.content.strip()
    return vibe_prompt


def generate_dalle_image(prompt: str) -> str:
    """
    Generate an image using OpenAI's DALL·E API.
    Returns the URL of the generated image.
    """
    response = openai.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response.data[0].url
    return image_url


def predict_missing_needs(event_text: str) -> str:
    """
    Given event details, predict any missing needs or recommendations.
    """
    prompt = f"""
    Given the following event description, suggest any missing needs or important considerations that the organizer might have overlooked:
    {event_text}
    """

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    suggestions = response.choices[0].message.content.strip()
    return suggestions


def generate_pdf(event_details: dict, output_path: str):
    """
    Generate a PDF summary of the event.
    
    Args:
        event_details (dict): {
            'title': str,
            'date': str,
            'location': str,
            'description': str,
            'schedule': list of str (each step/activity)
        }
        output_path (str): path to save the PDF file
    """
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, event_details.get('title', 'Event Plan'), ln=True, align='C')

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Date: {event_details.get('date', 'N/A')}", ln=True)
    pdf.cell(0, 10, f"Location: {event_details.get('location', 'N/A')}", ln=True)
    pdf.ln(5)

    description = event_details.get('description', '')
    pdf.multi_cell(0, 10, description)
    pdf.ln(10)

    schedule = event_details.get('schedule', [])
    if schedule:
        pdf.set_font("Arial", 'B', 14)
        pdf.cell(0, 10, "Schedule:", ln=True)
        pdf.set_font("Arial", size=12)
        for item in schedule:
            pdf.cell(0, 10, f"- {item}", ln=True)

    pdf.output(output_path)
