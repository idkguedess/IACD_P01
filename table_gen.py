# table_gen.py

from evaluation import evaluate_formula
from evaluation import generate_truth_combinations


def generate_truth_table(formula):
    """
    Genera una tabla de verdad para la fórmula dada.
    """
    # Obtener variables únicas de la fórmula
    unique_variables = list(set(char for char in formula if char.isalpha()))

    # Generar combinaciones de valores de verdad para las variables únicas
    truth_combinations = generate_truth_combinations(unique_variables)

    # Evaluar la fórmula utilizando las combinaciones de valores de verdad generadas
    results = evaluate_formula(formula, unique_variables, truth_combinations)

    # Regresar los resultados junto con las combinaciones de valores de verdad
    return list(zip(truth_combinations, results))


def print_truth_table(formula):
    """
    Imprime la tabla de verdad para la fórmula dada con nombres de variables generados automáticamente.
    """
    # Obtener variables únicas de la fórmula
    unique_variables = list(set(char for char in formula if char.isalpha()))

    if len(unique_variables) == 1:  # Si la fórmula tiene una única variable
        header = f"{unique_variables[0]} # {formula}"  # Encabezado con el nombre de la variable y la fórmula
        separator = "-" * len(header)  # Línea separadora
        print(separator)
        print(header)
        print(separator)
        # Imprimir los valores de verdad para la variable única
        print(f"True | {evaluate_formula(formula, unique_variables, [(True,)])[0]}")
        print(f"False | {evaluate_formula(formula, unique_variables, [(False,)])[0]}")
        print(separator)
    else:
        # Generar la tabla de verdad
        truth_table = generate_truth_table(formula)

        # Imprimir encabezado de la tabla
        header = " # ".join(unique_variables + [formula])
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


def analyze_formula(formula):
    # Obtener la tabla de verdad
    truth_table = generate_truth_table(formula)

    # Obtener los resultados de la tabla de verdad
    results = [result for _, result in truth_table]

    # Verificar si es una tautología, contradicción o contingencia
    if all(results):
        return "La fórmula es una tautología."
    elif not any(results):
        return "La fórmula es una contradicción."
    else:
        return "La fórmula es una contingencia."
