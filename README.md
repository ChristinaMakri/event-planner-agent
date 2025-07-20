# event-planner-agent
An AI-powered multi-modal event planning assistant that generates creative images, suggests ideas, and creates PDF plans based on your event description.

## Features

- Chat with the assistant to describe your event.
- Generates creative banner images for your event using DALL·E.
- Suggests additional needs and considerations you might have missed.
- Creates a downloadable PDF event plan summarizing all details.

## Setup

1. Clone the repo:
```bash
git clone https://github.com/yourusername/event-planner-agent.git
cd event-planner-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY="your_api_key_here"  # Linux/macOS
setx OPENAI_API_KEY "your_api_key_here"    # Windows PowerShell
```

4. Run the app:
```bash
python main.py
Open the Gradio interface that opens in your browser and start chatting!
```

## Usage
Simply describe your event in the chat box, and the assistant will respond with ideas, generate an event banner image, suggest additional needs, and create a downloadable PDF plan.


## 📸 Screenshots
Below are snapshots showcasing the usage and features of the Event Planner AI application:

**Application Start**
The initial interface when launching the Gradio UI.
<img width="1536" height="712" alt="Screenshot (136)" src="https://github.com/user-attachments/assets/e18089bb-e205-462a-9820-db6888ba4f50" />

**Event Description Input**  
The user types a description of their event, e.g. “A sunset wedding for 100 people on a beach.”
<img width="1447" height="200" alt="Screenshot (131)" src="https://github.com/user-attachments/assets/0fdcfd93-b22e-45c4-bdf2-f69467a0695f" />

**DALL·E Generated Image**  
A visual representation of the event created automatically from the user’s description.
<img width="1485" height="327" alt="Screenshot (134)" src="https://github.com/user-attachments/assets/742bc9ee-b012-454d-96b5-7c6581f5bbae" />

**Generated Event Plan PDF**  
Automatic export of the event plan including title, schedule, and additional suggestions.
<img width="1475" height="127" alt="Screenshot (133)" src="https://github.com/user-attachments/assets/5174c3ed-dc73-45ef-b6dd-6c7c1c006460" />
[Download the Event Plan PDF](assets/event_plan.pdf)
