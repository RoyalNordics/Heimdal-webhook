import openai
import backend.app.core.config as config
OPENAI_API_KEY = config.OPENAI_API_KEY

def openai_prompt(prompt):
    try:
        openai.api_key = config.OPENAI_API_KEY
        response = openai.Completion.create(
            engine="text-davinci-003",  # Or any other suitable engine
            prompt=prompt,
            max_tokens=150
        )
        return {"status": "success", "message": response.choices[0].text.strip()}
    except Exception as e:
        return {"status": "error", "message": str(e)}