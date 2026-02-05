import argparse
from diff_extractor import get_python_diff
from llm_client import generate_tests
from test_writer import write_tests

def load_prompt(diff):
    with open("prompts/python_tests.txt") as f:
        return f.read().replace("{{DIFF}}", diff)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode")
    parser.add_argument("--provider")
    parser.add_argument("--model")
    args = parser.parse_args()

    if args.mode != "local" or args.provider != "ollama":
        print("Only local Ollama mode supported in prototype")
        return

    diff = get_python_diff()

    if not diff:
        print("No Python changes detected")
        return

    prompt = load_prompt(diff)
    tests = generate_tests(prompt, args.model)

    write_tests(tests)

    print("✅ Tests generated successfully")

if __name__ == "__main__":
    main()
