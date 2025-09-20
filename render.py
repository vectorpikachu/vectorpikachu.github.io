import subprocess
import os
import datetime

def render_site():
    """Render the Quarto website."""
    try:
        subprocess.run(["quarto", "render"], check=True)
        print("Website rendered successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while rendering the website: {e}")
    
def git_add_commit_push(commit_message):
    """Add, commit, and push changes to the Git repository."""
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes pushed to the repository successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pushing changes: {e}")

if __name__ == "__main__":
    render_site()
    git_add_commit_push(f"Update website content - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")