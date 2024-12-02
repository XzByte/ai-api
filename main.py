from chatbot import get_model_response
import gradio as gr

def main():
    interface = gr.Interface(fn=get_model_response, inputs="text", outputs="text", title="AI Chatbot", description="Talk to the AI chatbot!")
    interface.launch(server_name="0.0.0.0")

if __name__ == "__main__":
    main()