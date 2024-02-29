# Main.py

from table_gen import *
from validation import *


def main():
    formula = input("Ingrese la fórmula en lógica proposicional: ").replace(" ", "")
    print("Fórmula ingresada:", formula)  # Impresión de depuración

    if is_valid_formula(formula):
        print("La fórmula es válida.")
        print_truth_table(formula)
        print(analyze_formula(formula))
    else:
        print("La fórmula no es válida.")


if __name__ == "__main__":
    main()
