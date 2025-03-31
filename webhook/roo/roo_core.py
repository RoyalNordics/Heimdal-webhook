from webhook import config
from webhook.roo.actions import create_file

from webhook.roo.actions import openai_prompt

from webhook.roo.actions import write_to_assistant

def handle_action(action, filename, content, assistant_id=None):
    if action == "create_file":
        return create_file.create_file(filename, content)
    elif action == "openai_prompt":
        return openai_prompt.openai_prompt(content)
    elif action == "write_to_assistant":
        return write_to_assistant.write_to_assistant(assistant_id, content)
    else:
        return {"status": "error", "message": "Unknown action"}