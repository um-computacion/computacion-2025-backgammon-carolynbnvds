import argparse
from core.dice import Dice

def main():
    parser = argparse.ArgumentParser(prog="backgammon", description="CLI Backgammon")
    parser.add_argument("--roll", action="store_true", help="Tirar dos dados")
    args = parser.parse_args()

    if args.roll:
        d = Dice()
        a, b = d.roll()
        print(f"Resultado: {a} y {b}")
    else:
        print("Backgammon CLI listo. Usa --roll para tirar los dados.")

if __name__ == "__main__":
    main()
