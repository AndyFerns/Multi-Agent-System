import argparse
from agents.classifier_agent import classify_and_route
from shared_memory.memory import init_db

def main():
    parser = argparse.ArgumentParser(description="Multi-Agent AI System")
    parser.add_argument("--input", required=True, help="Path to input file (PDF, JSON, or TXT)")
    args = parser.parse_args()

    db = init_db()
    classify_and_route(args.input, db)

if __name__ == "__main__":
    main()
