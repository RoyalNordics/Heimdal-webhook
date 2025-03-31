import openai
import config
OPENAI_API_KEY = config.OPENAI_API_KEY

def write_to_assistant(assistant_id, content):
    try:
        openai.api_key = OPENAI_API_KEY
        # Create a message to send to the assistant
        message = openai.beta.threads.messages.create(
            thread_id=assistant_id,
            role="user",
            content=content
        )

        return {"status": "success", "message": "Message sent to assistant successfully!"}
    except Exception as e:
        return {"status": "error", "message": str(e)}