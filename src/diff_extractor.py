import subprocess
import os

def get_python_diff():
    base_sha = os.environ.get("BASE_SHA")
    head_sha = os.environ.get("HEAD_SHA")

    if not base_sha or not head_sha:
        print("Missing BASE_SHA or HEAD_SHA env variables.")
        return ""

    print(f"Base SHA: {base_sha}")
    print(f"Head SHA: {head_sha}")

    cmd = [
        "git",
        "diff",
        base_sha,
        head_sha,
        "--",
        "*.py",
    ]

    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error running git diff: {result.stderr}")
        return ""

    diff_content = result.stdout.strip()
    print(f"Diff content:\n{diff_content}")
    return diff_content