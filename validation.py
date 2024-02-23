#
# ESTE MÓDULO ES OPCIONAL, PARA VER SI ESTA BIEN FORMADA LA EXPRESIÓN: LO IMPORTANTE ES SU EVALUACIÓN
#
def is_valid_formula(formula):
    """
    Verifica si la fórmula es válida, bien formada.
    """
    stack = []
    for char in formula:
        if char.isalpha():
            if char.islower():
                stack.append(char)
            else:
                return False  # Carácter inválido
        elif char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) < 2:
                return False  # No hay suficientes operandos
            elif stack[-1] == '(':
                return False  # Paréntesis vacío
            elif stack[-2] != '(' and stack[-1] != ')':
                stack.pop()  # Elimina el paréntesis de cierre
                stack.pop()  # Elimina los operandos dentro del paréntesis
                stack.append('T')  # En lugar de mantener la subexpresión en la pila, que es una estructura temporal,
                # se reemplaza por el marcador 'T'. Esto indica que la subexpresión ha sido evaluada
                # correctamente y no es necesario seguir rastreándola en la pila
            else:
                return False  # Expresión inválida dentro del paréntesis
        elif char in ['!', '|', '&', '>', '=']:  # Operadores modificados
            if len(stack) < 2:
                return False  # No hay suficientes operandos
            elif stack[-1] in ['!', '|', '&', '>', '=']:
                return False  # Operadores consecutivos
            else:
                stack.pop()  # Elimina el segundo operando
                stack.pop()  # Elimina el primer operando
                stack.append('T')  # Reemplaza la subexpresión con 'T'
        else:
            return False  # Carácter inválido
    return len(stack) == 1 and stack[0].islower()
# Al finalizar la evaluación de la fórmula, si hay más de un elemento en la pila, significa que hay más de una
# expresión lógica o que no se ha completado correctamente la evaluación de la fórmula. Si no hay ningún elemento en
# la pila, indica que la fórmula está incompleta o que hay un paréntesis de apertura sin su correspondiente cierre.
