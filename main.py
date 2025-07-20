import os
import gradio as gr
from dotenv import load_dotenv
from prompts import system_prompt
from tools import chat, user_submit

load_dotenv()

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎉 Event Planner AI")
    gr.Markdown("Chat with an AI to plan your perfect event. Get ideas, image inspiration, and a downloadable PDF!")

    with gr.Row():
        chatbot = gr.Chatbot(label="💬 Event Chat", height=400)
        with gr.Column():
            image_output = gr.Image(label="🖼️ Generated Image", height=300)
            pdf_download = gr.File(label="📄 Download Event Plan PDF")

    user_input = gr.Textbox(label="✏️ Describe your event", placeholder="e.g. A birthday party in a botanical garden with live music.")
    with gr.Row():
        submit_btn = gr.Button("🚀 Submit")
        clear_btn = gr.Button("🔄 Clear")

    user_input.submit(user_submit, inputs=[user_input, chatbot], outputs=[user_input, chatbot]).then(
        chat, inputs=chatbot, outputs=[chatbot, image_output, pdf_download]
    )

    submit_btn.click(user_submit, inputs=[user_input, chatbot], outputs=[user_input, chatbot]).then(
        chat, inputs=chatbot, outputs=[chatbot, image_output, pdf_download]
    )

    clear_btn.click(lambda: ([], None, None), outputs=[chatbot, image_output, pdf_download])

demo.launch(inbrowser=True)
