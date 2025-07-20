import os
import gradio as gr
from tools import extract_vibe, generate_dalle_image, generate_pdf, predict_missing_needs
from prompts import system_prompt
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o"

def chat(history):
    messages = [{"role": "system", "content": system_prompt}] + history
    response = openai.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    
    assistant_reply = response.choices[0].message.content
    history.append({"role": "assistant", "content": assistant_reply})
    
    # Παίρνουμε το τελευταίο user μήνυμα για εργαλεία
    user_message = history[-2]["content"] if len(history) >= 2 else ""
    
    # 1. Δημιουργούμε prompt για DALL·E από την περιγραφή του χρήστη
    dalle_prompt = extract_vibe(user_message)
    
    # 2. Δημιουργούμε εικόνα και παίρνουμε URL
    image_url = generate_dalle_image(dalle_prompt)
    
    # 3. Προβλέπουμε πιθανές κρυφές ανάγκες
    missing_needs = predict_missing_needs(user_message)
    
    # 4. Δημιουργούμε απλό event plan για PDF (μπορείς να το βελτιώσεις)
    event_details = {
        "title": "Your Event Plan",
        "date": "To be decided",
        "location": "To be decided",
        "description": assistant_reply + "\n\nAdditional suggestions:\n" + missing_needs,
        "schedule": [
            "Welcome and introductions",
            "Main activities",
            "Networking time",
            "Closing remarks"
        ]
    }
    
    # 5. Δημιουργία PDF
    now_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    pdf_path = f"event_exports/pdfs/event_plan_{now_str}.pdf"
    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
    generate_pdf(event_details, pdf_path)
    
    # Επιστρέφουμε ιστορικό chat, εικόνα και path PDF για download
    return history, image_url, pdf_path

with gr.Blocks() as ui:
    chatbot = gr.Chatbot(height=400)
    image_output = gr.Image(height=300)
    pdf_download = gr.File(label="Download Event Plan PDF")
    
    with gr.Row():
        user_input = gr.Textbox(label="Describe your event:", placeholder="e.g. A rooftop party for 20 people at sunset")
    with gr.Row():
        clear_btn = gr.Button("Clear")
        submit_btn = gr.Button("Send")
    
    def user_submit(message, history):
        history = history or []
        history.append({"role": "user", "content": message})
        return "", history
    
    user_input.submit(user_submit, inputs=[user_input, chatbot], outputs=[user_input, chatbot]).then(
        chat, inputs=chatbot, outputs=[chatbot, image_output, pdf_download]
    )
    
    submit_btn.click(user_submit, inputs=[user_input, chatbot], outputs=[user_input, chatbot]).then(
        chat, inputs=chatbot, outputs=[chatbot, image_output, pdf_download]
    )
    
    clear_btn.click(lambda: ([], None, None), outputs=[chatbot, image_output, pdf_download])
    
ui.launch(inbrowser=True)
