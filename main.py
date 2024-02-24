# Main.py

from validation import is_valid_formula
from evaluation import print_truth_table

def main():
    formula = input("Ingrese la fórmula en lógica proposicional: ").replace(" ", "")
    print("Fórmula ingresada:", formula)  # Impresión de depuración

    # Verificar si la fórmula es válida
    if not is_valid_formula(formula):
        print("La fórmula ingresada no es válida.")
        return

    # Generar y mostrar la tabla de verdad
    print("Tabla de Verdad:")
    print_truth_table(formula)

if __name__ == "__main__":
    main()
