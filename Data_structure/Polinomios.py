"""
Suma y resta de polinomios
"""

# Ingreso de datos

n1 = int(input("Ingrese el grado del polinomio 1: "))
p1 = [0] * (n1 + 1) # Se crea un arreglo de tamaño n + 1

# Se agregan los coeficientes
for i in range(n1, -1 ,-1):
    p1[i] = int(input(f"Ingrese el coeficiente del polinomio: x^{i}: "))

n2 = int(input("Ingrese el grado del polinomio 2: "))
p2 = [0] * (n2 + 1) # Se crea un arreglo de tamaño n + 1

# Se agregan los coeficientes
for i in range(n2, -1 ,-1):
    p2[i] = int(input(f"Ingrese el coeficiente del polinomio: x^{i}: "))

#########################################################################################

def SumPol(pol1, grade1, pol2, grade2):
    if grade1 < grade2:
        grademax = grade2
        pol1.extend([0] * (grade2 - grade1))  # Agregar ceros a pol1
    else:
        grademax = grade1
        pol2.extend([0] * (grade1 - grade2))  # Agregar ceros a pol2

    # Crear un polinomio resultado con ceros
    p3 = [0] * (grademax + 1)

    # Sumar los coeficientes de ambos polinomios
    for i in range(grademax + 1):
        p3[i] = pol1[i] + pol2[i]

    return p3

def MultiplyPol(pol1, grade1, pol2, grade2):
    # Grado del polinomio resultante
    grade_result = grade1 + grade2

    # Inicializar el polinomio resultante con ceros
    result = [0] * (grade_result + 1)

    # Multiplicar los polinomios
    for i in range(grade1 + 1):  # Recorrer cada término de pol1
        for j in range(grade2 + 1):  # Recorrer cada término de pol2
            # Multiplicar los coeficientes y sumar en la posición correcta
            result[i + j] += pol1[i] * pol2[j]

    return result


# Se llaman a las funciones y se almacenan en variables
sum = SumPol(p1, n1, p2, n2)
mul = MultiplyPol(p1, n1, p2, n2)


# def Derivate(pol, grade):
#     df = [0] * grade
#     for i in range(grade, -1, -1):
#         if i == 0: break
#         df[i - 1] = i * pol[i]

#     print(df)
    
def print_pol(pol):
    expresion = []
    for i in range(len(pol) - 1, -1, -1):
        coef = pol[i]
        if coef == 0:
            continue

        if i == 0:
            term = f"{coef}"
        elif i == 1:
            term = f"{coef}x"
        else:
            term = f"{coef}x^{i}"

        expresion.append(term)

    print(" + ".join(expresion))
    



# Se llama a la funcion que imprime los polinomios
print_pol(sum)
print_pol(mul)