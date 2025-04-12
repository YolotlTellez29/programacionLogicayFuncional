# Importamos el módulo tkinter para crear interfaces gráficas de usuario (GUI).
# `tk` es el módulo principal de tkinter, y `messagebox` es un submódulo que permite mostrar cuadros de diálogo.
import tkinter as tk
from tkinter import messagebox

# Definimos la función `calculate`, que realiza operaciones matemáticas (suma o multiplicación) entre dos números.
def calculate(operation):
    """
    Realiza una operación matemática (suma o multiplicación) entre dos números ingresados por el usuario.
    
    Parámetros:
    - operation (str): Puede ser "sum" para sumar o "multiply" para multiplicar.

    Comportamiento:
    - Obtiene los valores de los campos de entrada `entry1` y `entry2`.
    - Convierte los valores a tipo float.
    - Realiza la operación especificada.
    - Muestra el resultado en un cuadro de diálogo.
    - Si ocurre un error (por ejemplo, si los valores no son numéricos), muestra un mensaje de error.
    """
    try:
        # Obtenemos los valores de los campos de entrada y los convertimos a float.
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        # Realizamos la operación según el parámetro `operation`.
        if operation == "sum":
            result = num1 + num2
        elif operation == "multiply":
            result = num1 * num2
        
        # Mostramos el resultado en un cuadro de diálogo informativo.
        messagebox.showinfo("Resultado", f"El resultado es: {result}")
    except ValueError:
        # Si ocurre un error de conversión (por ejemplo, si el usuario ingresa texto en lugar de números),
        # mostramos un cuadro de diálogo de error.
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Creamos la ventana principal de la aplicación.
root = tk.Tk()
root.title("Calculadora")  # Establecemos el título de la ventana.

# Creamos etiquetas y campos de entrada para que el usuario ingrese los números.
tk.Label(root, text="Valor 1:").grid(row=0, column=0, padx=10, pady=10)  # Etiqueta para el primer número.
entry1 = tk.Entry(root)  # Campo de entrada para el primer número.
entry1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Valor 2:").grid(row=1, column=0, padx=10, pady=10)  # Etiqueta para el segundo número.
entry2 = tk.Entry(root)  # Campo de entrada para el segundo número.
entry2.grid(row=1, column=1, padx=10, pady=10)

# Creamos botones para realizar las operaciones de suma y multiplicación.
btn_sum = tk.Button(root, text="Sumar", command=lambda: calculate("sum"))
btn_sum.grid(row=2, column=0, padx=10, pady=10)  # Botón para sumar.

btn_multiply = tk.Button(root, text="Multiplicar", command=lambda: calculate("multiply"))
btn_multiply.grid(row=2, column=1, padx=10, pady=10)  # Botón para multiplicar.

# Iniciamos el bucle principal de la interfaz gráfica.
# Esto mantiene la ventana abierta.
root.mainloop()