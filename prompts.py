# prompts.py

system_prompt = """
You are a smart assistant that helps organize events (parties, trips, presentations).
Ask the user for necessary details (date, location, number of attendees).
Create a schedule, suggest ideas, and generate creative images based on the theme.
Also, suggest any needs the user might not have considered.
Be friendly, creative, and clear.
"""

dalle_prompt_template = """
Create an artistic image prompt based on the following event description:
{event_description}

Make it descriptive, capturing the atmosphere and style fitting the theme.
"""

pdf_prompt_template = """
Help organize the event information we have planned into a clear and concise PDF program:
{event_details}
"""
