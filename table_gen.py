# table_gen.py

# Importamos las funciones necesarias de otros módulos
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
    variables = [char for char in formula if char.isalpha()]  # Obtener variables de la fórmula

    if len(variables) == 1:  # Si la fórmula es una variable atómica (solo una variable)
        print('-' * (len(variables[0]) + 3))  # Imprimir una tabla de verdad simple con una columna para la variable y
        # una para el resultado
        print(variables[0])
        print('-' * (len(variables[0]) + 3))
        print(True)
        print(False)
        print('-' * (len(variables[0]) + 3))
    else:
        truth_table = generate_truth_table(formula)  # Generar la tabla de verdad completa

        # Imprimir encabezado de la tabla
        header = " # ".join(variables + [formula])  # Concatenar variables y fórmula con un separador #
        separator = "-" * len(header)  # Crear una línea divisoria del mismo tamaño que el encabezado
        print(separator)  # Imprimir línea divisoria superior
        print(header)  # Imprimir encabezado
        print(separator)  # Imprimir línea divisoria entre encabezado y datos

        # Imprimir filas de la tabla
        for truth_combination, result in truth_table:
            row_values = [str(value) for value in truth_combination] + [str(result)]  # Convertir valores a cadena
            row = " | ".join(row_values)  # Unir valores con un separador |
            print(row)  # Imprimir fila de la tabla

        print(separator)  # Imprimir línea divisoria inferior


def analyze_formula(formula):
    """
    Analiza la fórmula dada para determinar si es una tautología, contradicción o contingencia.
    """
    truth_table = generate_truth_table(formula)  # Obtener la tabla de verdad para la fórmula

    results = [result for _, result in truth_table]  # Obtener los resultados de la tabla de verdad

    # Verificar si todos los resultados son True (tautología), todos son False (contradicción) o hay una mezcla de
    # ambos (contingencia)
    if all(results):
        return "La fórmula es una tautología."
    elif not any(results):
        return "La fórmula es una contradicción."
    else:
        return "La fórmula es una contingencia."
