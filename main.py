# Main.py

from table_gen import *


def main():
    formula = input("Ingrese la fórmula en lógica proposicional: ").replace(" ", "")
    print("Fórmula ingresada:", formula)  # Impresión de depuración

    print_truth_table(formula)
    print(analyze_formula(formula))

if __name__ == "__main__":
    main()
