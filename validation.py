#
# ESTE MÓDULO ES OPCIONAL, PARA VER SI ESTA BIEN FORMADA LA EXPRESIÓN: LO IMPORTANTE ES SU EVALUACIÓN
#
def is_valid_formula(formula):
    """
    Verifica si la fórmula es válida y bien formada.
    """
    stack = []
    for char in formula:
        if char.isalpha():
            stack.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            if '(' not in stack:
                return False  # Falta el paréntesis de apertura correspondiente
            else:
                # Verificar que haya al menos un operando entre los paréntesis
                while stack[-1] != '(':
                    if not stack or stack[-1] in ['!', '|', '&', '>', '=']:
                        return False  # Operadores consecutivos o falta de operando antes del operador
                    stack.pop()
                stack.pop()  # Eliminar el paréntesis de apertura
        elif char in ['!', '|', '&', '>', '=']:  # Operadores lógicos
            if not stack or (stack[-1] in ['!', '|', '&', '>', '='] or stack[-1] == '('):
                return False  # Operadores consecutivos o falta de operando antes del operador
            else:
                # Pop the operands and check if they are valid variables
                operand = stack.pop()
                if not operand.isalpha():
                    return False
                stack.append(char)
        else:
            return False  # Carácter inválido

    # Verificar si quedaron paréntesis de apertura sin cerrar
    if '(' in stack:
        return False  # Paréntesis de apertura sin cerrar

    # Verificar si la fórmula está bien formada
    if len(stack) != 1 or not stack[0].isalpha():
        return False  # La fórmula no está bien formada

    return True  # La fórmula es válida y bien formada
#Al finalizar la evaluación de la fórmula, si hay más de un elemento en la pila, significa que hay más de una
# expresión lógica o que no se ha completado correctamente la evaluación de la fórmula. Si no hay ningún elemento en
# la pila, indica que la fórmula está incompleta o que hay un paréntesis de apertura sin su correspondiente cierre.