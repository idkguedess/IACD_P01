# MÓDULO PARA EVALUAR LA

import string
import itertools

def create_truth_values():
    """
    Crea un diccionario con todas las letras del inglés en minúscula como claves
    y valores inicializados en None.
    """
    alphabet = string.ascii_lowercase  # Obtenemos el alfabeto en minúsculas
    truth_dic = {letter: None for letter in alphabet}  # Creamos un diccionario con las letras del alfabeto como
    # claves y valores inicializados en None
    return truth_dic  # Retornamos el diccionario creado


def generate_truth_combinations(variables):
    """
    Genera todas las combinaciones posibles de valores de verdad para las variables dadas.
    """
    truth_values = [True, False]  # Valores de verdad posibles
    return list(itertools.product(truth_values, repeat=len(variables)))


def evaluate_formula(formula, truth_dic):
    """
    Evalúa la fórmula utilizando los valores de verdad especificados en el diccionario truth_values.
    """
    stack = []  # Inicializamos una pila vacía
    i = 0
    while i < len(formula):
        char = formula[i]
        if char.isalpha():  # Si el carácter es una letra
            stack.append(truth_dic[char])  # Agregamos el valor de verdad correspondiente al carácter a la pila
        elif char in ['!', '|', '&', '>', '=']:  # Si el carácter es un operador lógico
            if char == '!':  # Si es el operador de negación
                if i + 1 < len(formula) and formula[i + 1].isalpha():
                    i += 1
                    next_char = formula[i]
                    stack.append(not truth_dic[next_char])  # Aplicamos la negación y agregamos el resultado a la pila
                else:
                    return "Error: Faltan operandos en la fórmula"
            else:  # Si es otro operador lógico
                if i + 1 < len(formula) and formula[i + 1].isalpha():
                    i += 1
                    next_char = formula[i]
                    if char == '|':
                        stack.append(stack.pop() or truth_dic[next_char])
                    elif char == '&':
                        stack.append(stack.pop() and truth_dic[next_char])
                    elif char == '>':
                        stack.append(not stack.pop() or truth_dic[next_char])
                    elif char == '=':
                        stack.append(stack.pop() == truth_dic[next_char])
                else:
                    return "Error: Faltan operandos en la fórmula"
        i += 1

        # Actualizar valores de verdad en el diccionario si es posible
        if char.isalpha() and truth_dic[char] is None:  # Si el carácter es una letra y su valor de verdad aún no
            # está definido
            truth_dic[char] = stack[-1]  # Actualizamos el valor de verdad en el diccionario con el último valor
            # agregado a la pila

    return stack[0]  # Retornamos el resultado final de la evaluación de la fórmula


def generate_truth_table(formula):
    """
    Genera una tabla de verdad para la fórmula dada.
    """
    # Obtener variables de la fórmula
    variables = set(char for char in formula if char.isalpha())

    # Generar combinaciones de valores de verdad para las variables
    truth_combinations = generate_truth_combinations(variables)

    # Evaluar la fórmula para cada combinación de valores de verdad
    results = []
    for truth_combination in truth_combinations:
        truth_dic = dict(zip(variables, truth_combination))
        result = evaluate_formula(formula, truth_dic)
        results.append((truth_combination, result))

    return results


def print_truth_table(formula):
    """
    Imprime la tabla de verdad para la fórmula dada con nombres de variables generados automáticamente.
    """
    # Obtener variables de la fórmula
    variables = [char for char in formula if char.isalpha()]
    num_variables = len(set(variables))

    # Generar nombres de variables
    variable_names = [i for i in variables]

    # Generar la tabla de verdad
    truth_table = generate_truth_table(formula)

    # Imprimir encabezado de la tabla
    header = " | ".join(variable_names + [formula])
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


# Ejemplo de uso con nombres de variables generados automáticamente:
formula = "p&q&a"  # Fórmula lógica
print_truth_table(formula)
