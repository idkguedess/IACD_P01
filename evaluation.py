# evaluation.py

import itertools


def generate_truth_combinations(variables):
    """
    Genera todas las combinaciones posibles de valores de verdad para las variables dadas.
    """
    truth_values = [True, False]  # Valores de verdad posibles
    return list(itertools.product(truth_values, repeat=len(variables)))


def evaluate_formula(formula, variables, truth_combinations):
    """
    Evalúa la fórmula utilizando las combinaciones de valores de verdad especificadas.
    """
    results = []

    # Definimos la precedencia de los operadores lógicos
    precedence = {'!': 3, '&': 1, '|': 1, '>': 0, '=': 0}

    for truth_combination in truth_combinations:
        truth_dic = dict(zip(variables, truth_combination))
        stack = []  # Inicializamos una pila vacía
        output = []  # Inicializamos una lista de salida

        for char in formula:
            if char.isalpha():  # Si el carácter es una letra
                if char in truth_dic:
                    output.append(truth_dic[
                                      char])  # Agregamos el valor de verdad correspondiente al carácter a la lista
                    # de salida
                else:
                    output.append(
                        not truth_dic.get('!' + char, True))  # Si la variable negada no está definida, asumimos True
            elif char == '!':  # Si el carácter es una negación
                stack.append(char)  # Agregamos la negación a la pila
            elif char in ['&', '|', '>', '=']:  # Si el carácter es un operador lógico
                while stack and precedence.get(stack[-1], 0) >= precedence[char]:
                    output.append(
                        stack.pop())  # Desapilamos los operadores con mayor o igual precedencia que el operador actual
                stack.append(char)  # Agregamos el operador actual a la pila
            elif char == '(':  # Si el carácter es un paréntesis de apertura
                stack.append(char)  # Agregamos el paréntesis a la pila
            elif char == ')':  # Si el carácter es un paréntesis de cip&!qerre
                while stack and stack[-1] != '(':
                    output.append(
                        stack.pop())  # Desapilamos los operadores hasta encontrar el paréntesis de apertura
                    # correspondiente
                stack.pop()  # Quitamos el paréntesis de apertura de la pila

        while stack:
            output.append(stack.pop())  # Desapilamos los operadores restantes

        # Ahora evaluamos la expresión en notación polaca inversa (RPN)
        eval_stack = []
        for token in output:
            if token in [True, False]:  # Si el token es un valor de verdad
                eval_stack.append(token)  # Apilamos el valor de verdad
            elif token == '!':  # Si el token es una negación
                operand = eval_stack.pop()  # Desapilamos el operando
                eval_stack.append(not operand)  # Aplicamos la negación y apilamos el resultado
            elif token in ['&', '|', '>', '=']:  # Si el token es un operador lógico
                operand2 = eval_stack.pop()  # Desapilamos el segundo operando
                operand1 = eval_stack.pop()  # Desapilamos el primer operando
                if token == '&':
                    eval_stack.append(operand1 and operand2)  # Aplicamos la conjunción y apilamos el resultado
                elif token == '|':
                    eval_stack.append(operand1 or operand2)  # Aplicamos la disyunción y apilamos el resultado
                elif token == '>':
                    eval_stack.append(not operand1 or operand2)  # Aplicamos la implicación y apilamos el resultado
                elif token == '=':
                    eval_stack.append(operand1 == operand2)  # Aplicamos la doble implicación y apilamos el resultado

        results.append(eval_stack[0])  # Agregamos el resultado de la evaluación a la lista de resultados

    return results
