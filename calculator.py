# calculator.py
import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Calculator")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")
    parser.add_argument("x", type=float, help="First number")
    parser.add_argument("y", type=float, help="Second number")
    args = parser.parse_args()

    if args.operation == "add":
        print(args.x + args.y)
    elif args.operation == "sub":
        print(args.x - args.y)
    elif args.operation == "mul":
        print(args.x * args.y)
    elif args.operation == "div":
        print(args.x / args.y if args.y != 0 else "Error: Division by zero")

if __name__ == "__main__":
    main()

