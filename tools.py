import os
import openai
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") or "your-key-here"

def extract_vibe(user_input):
    return f"Atmospheric scene: {user_input}, cinematic lighting, colorful, stylized illustration"

def generate_dalle_image(prompt):
    try:
        response = openai.images.generate(
            prompt=prompt,
            model="dall-e-3",
            n=1,
            size="1024x1024"
        )
        return response.data[0].url
    except Exception as e:
        print("Image generation failed:", e)
        return None

def predict_missing_needs(user_input):
    prompt = f"""The user said: "{user_input}". What are 3 things people often forget for events like this? Bullet points."""
    try:
        res = openai.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return res.choices[0].message.content.strip()
    except:
        return "No suggestions available."

def generate_pdf(event_data, filename):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, y, event_data["title"])
    y -= 30

    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Date: {event_data['date']}")
    y -= 20
    c.drawString(50, y, f"Location: {event_data['location']}")
    y -= 40

    for line in event_data["description"].split('\n'):
        c.drawString(50, y, line)
        y -= 18

    y -= 20
    c.setFont("Helvetica-Bold", 13)
    c.drawString(50, y, "Schedule:")
    y -= 20

    c.setFont("Helvetica", 12)
    for item in event_data["schedule"]:
        c.drawString(60, y, f"- {item}")
        y -= 16

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    c.save()

def chat(history):
    from prompts import system_prompt

    messages = [{"role": "system", "content": system_prompt}] + [
        {"role": role.lower(), "content": content} for role, content in history
    ]

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    assistant_reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_reply})

    user_msg = messages[-2]["content"]
    image_url = generate_dalle_image(extract_vibe(user_msg))
    suggestions = predict_missing_needs(user_msg)

    event_data = {
        "title": "Your Event Plan",
        "date": "To be decided",
        "location": "To be decided",
        "description": assistant_reply + "\n\n📝 Additional suggestions:\n" + suggestions,
        "schedule": ["Welcome", "Main activities", "Breaks", "Closing"]
    }

    filename = f"event_exports/pdfs/event_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    generate_pdf(event_data, filename)

    updated = [(m["role"].capitalize(), m["content"]) for m in messages if m["role"] in ["user", "assistant"]]
    return updated, image_url, filename

def user_submit(message, history):
    history = history or []
    history.append(("User", message))
    return "", history
