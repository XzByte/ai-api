from gradio import Interface
from chatbot import Chatbot

def main():
    chatbot = Chatbot()
    interface = Interface(fn=chatbot.get_response, inputs="text", outputs="text", title="AI Chatbot", description="Talk to the AI chatbot!")
    interface.launch()

if __name__ == "__main__":
    main()