import subprocess

def get_python_diff():
    result = subprocess.run(
        ["git", "diff", "origin/main...HEAD", "--", "*.py"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()
