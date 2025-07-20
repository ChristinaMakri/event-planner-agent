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
