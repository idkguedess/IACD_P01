# table_gen.py

from evaluation import evaluate_formula
from evaluation import generate_truth_combinations


def generate_truth_table(formula):
    """
    Genera una tabla de verdad para la fórmula dada.
    """
    # Obtener variables de la fórmula
    variables = [char for char in formula if char.isalpha()]

    # Generar combinaciones de valores de verdad para las variables
    truth_combinations = generate_truth_combinations(variables)

    # Evaluar la fórmula utilizando las combinaciones de valores de verdad generadas
    results = evaluate_formula(formula, variables, truth_combinations)

    # Regresar los resultados junto con las combinaciones de valores de verdad
    return list(zip(truth_combinations, results))


def print_truth_table(formula):
    """
    Imprime la tabla de verdad para la fórmula dada con nombres de variables generados automáticamente.
    """
    # Obtener variables de la fórmula
    variables = [char for char in formula if char.isalpha()]

    # Generar la tabla de verdad
    truth_table = generate_truth_table(formula)

    # Imprimir encabezado de la tabla
    header = " | ".join(variables + [formula])
    separator = "-" * len(header)
    print(separator)
    print(header)
    print(separator)

    # Imprimir filas de la tabla
    for truth_combination, result in truth_table:
        row_values = [str(value) for value in truth_combination] + [str(result)]
        row = " | ".join(row_values)
        print(row)

    print(separator)
