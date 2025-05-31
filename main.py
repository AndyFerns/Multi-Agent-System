import argparse
from agents.classifier_agent import classify_and_route
from shared_memory.memory import init_db, print_memory_log  # Make sure print_memory_log exists

def main():
    parser = argparse.ArgumentParser(description="Multi-Agent AI System")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", help="Path to input file (PDF, JSON, or TXT)")
    group.add_argument("--print-memory", action="store_true", help="Print memory logs")

    args = parser.parse_args()

    db = init_db()

    if args.print_memory:
        print_memory_log(db)
    elif args.input:
        classify_and_route(args.input, db)

if __name__ == "__main__":
    main()
