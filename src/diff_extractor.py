import subprocess
import os

def get_python_diff():
    base = os.environ.get("GITHUB_BASE_REF")

    if not base:
        # fallback for non-PR runs
        cmd = ["git", "diff", "HEAD~1", "--", "*.py"]
    else:
        # PR run (this is your case)
        cmd = ["git", "diff", f"origin/{base}...HEAD", "--", "*.py"]

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True
    )

    return result.stdout.strip()
