import subprocess
import os

def get_python_diff():
    base_sha = os.environ.get("GITHUB_EVENT_PULL_REQUEST_BASE_SHA")
    head_sha = os.environ.get("GITHUB_EVENT_PULL_REQUEST_HEAD_SHA")

    if not base_sha or not head_sha:
        print("Not a PR run or missing SHAs")
        return ""

    cmd = [
        "git",
        "diff",
        f"{base_sha}...{head_sha}",
        "--",
        "*.py"
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout.strip()
