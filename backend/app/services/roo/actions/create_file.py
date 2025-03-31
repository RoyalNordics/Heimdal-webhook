from github import Github
import backend.app.core.config as config
OPENAI_API_KEY = config.OPENAI_API_KEY
GITHUB_PAT = config.GITHUB_PAT
GITHUB_REPO = config.GITHUB_REPO
GITHUB_BRANCH = config.GITHUB_BRANCH
import os
import json
import datetime

def create_file(filename, content):
    try:
        g = Github(config.GITHUB_PAT)
        repo = g.get_repo(config.GITHUB_REPO)
        branch = config.GITHUB_BRANCH
        
        # Check if file exists
        try:
            contents = repo.get_contents(filename, ref=branch)
            # File exists, update it
            repo.update_file(contents.path, "Updated file via webhook", content, contents.sha, branch=branch)
            # Commit and push changes
            os.system(f'git commit -m "Auto-update via Heimdal Assistant" && git push origin {branch}')
            # Log task in roo.runplan.json
            timestamp = datetime.datetime.utcnow().isoformat() + "Z"
            try:
                with open("ProjectAssistant/build/roo.runplan.json", "r+") as f:
                    data = json.load(f)
                    new_task = {
                        "task_id": "002",
                        "action": "create_file",
                        "filename": filename,
                        "status": "done",
                        "timestamp": timestamp
                    }
                    # If the file contains a single object, convert it to a list
                    if isinstance(data, dict):
                        data = [data]
                    data.append(new_task)
                    f.seek(0)
                    json.dump(data, f, indent=2)
                    f.truncate()
            except Exception as e:
                print(f"Error logging task in roo.runplan.json: {e}")
            return {"status": "success", "message": f"File {filename} updated successfully"}
        except:
            # File doesn't exist, create it
            repo.create_file(filename, content, "Created file via webhook", branch=branch)
            # Commit and push changes
            os.system(f'git commit -m "Auto-update via Heimdal Assistant" && git push origin {branch}')
            # Log task in roo.runplan.json
            timestamp = datetime.datetime.utcnow().isoformat() + "Z"
            try:
                with open("ProjectAssistant/build/roo.runplan.json", "r+") as f:
                    data = json.load(f)
                    new_task = {
                        "task_id": "002",
                        "action": "create_file",
                        "filename": filename,
                        "status": "done",
                        "timestamp": timestamp
                    }
                    # If the file contains a single object, convert it to a list
                    if isinstance(data, dict):
                        data = [data]
                    data.append(new_task)
                    f.seek(0)
                    json.dump(data, f, indent=2)
                    f.truncate()
            except Exception as e:
                print(f"Error logging task in roo.runplan.json: {e}")
            # Write confirmation to ai-communication.md
            try:
                with open("ProjectAssistant/communication/ai-communication.md", "a") as f:
                    f.write(f"\nFil {filename} oprettet/opdateret via webhook.")
            except Exception as e:
                print(f"Error writing to ai-communication.md: {e}")
            return {"status": "success", "message": f"File {filename} created successfully"}

    except Exception as e:
        return {"status": "error", "message": str(e)}