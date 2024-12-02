def preprocess_text(text):
    # Function to preprocess user input text
    text = text.strip().lower()  # Remove leading/trailing whitespace and convert to lowercase
    return text

def format_response(response):
    # Function to format the chatbot's response
    return f"Chatbot: {response}"