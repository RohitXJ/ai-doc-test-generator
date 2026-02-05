import subprocess
import os

def get_python_diff():
    base_ref = os.environ.get("GITHUB_BASE_REF")
    head_ref = os.environ.get("GITHUB_HEAD_REF")

    if not base_ref or not head_ref:
        print("Missing GITHUB_BASE_REF or GITHUB_HEAD_REF env variables.")
        return ""

    print(f"Base ref: {base_ref}")
    print(f"Head ref: {head_ref}")

    # Fetch the base and head refs
    subprocess.run(["git", "fetch", "origin", base_ref, "--depth=1"])
    subprocess.run(["git", "fetch", "origin", head_ref, "--depth=1"])

    # Get the SHAs of the fetched refs
    base_sha = subprocess.run(["git", "rev-parse", f"origin/{base_ref}"], capture_output=True, text=True).stdout.strip()
    head_sha = subprocess.run(["git", "rev-parse", f"origin/{head_ref}"], capture_output=True, text=True).stdout.strip()
    
    if not base_sha or not head_sha:
        print("Could not determine base or head SHA.")
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

    return result.stdout.strip()
