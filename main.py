from validation import is_valid_formula
from evaluation import print_truth_table


def main():
    formula = input("Ingrese la fórmula en lógica proposicional: ").replace(" ", "")
    print("Fórmula ingresada:", formula)  # Impresión de depuración

    # Generar y mostrar la tabla de verdad
    print("Tabla de Verdad:")
    print_truth_table(formula)


if __name__ == "__main__":
    main()
