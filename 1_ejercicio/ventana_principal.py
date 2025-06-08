import tkinter as tk
from tkinter import messagebox
from notas import Notas  # Asegúrate de tener este archivo 'notas.py' con la clase Notas que mostraste

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Notas")
        self.root.geometry("280x330")
        self.root.resizable(False, False)

        # Lista para guardar los campos de entrada
        self.campos = []

        # Etiquetas y entradas creadas manualmente
        self.nota1 = tk.Label(root, text="Nota 1:")
        self.nota1.place(x=20, y=20)
        self.campo1 = tk.Entry(root)
        self.campo1.place(x=100, y=20, width=135)
        self.campos.append(self.campo1)

        self.nota2 = tk.Label(root, text="Nota 2:")
        self.nota2.place(x=20, y=50)
        self.campo2 = tk.Entry(root)
        self.campo2.place(x=100, y=50, width=135)
        self.campos.append(self.campo2)

        self.nota3 = tk.Label(root, text="Nota 3:")
        self.nota3.place(x=20, y=80)
        self.campo3 = tk.Entry(root)
        self.campo3.place(x=100, y=80, width=135)
        self.campos.append(self.campo3)

        self.nota4 = tk.Label(root, text="Nota 4:")
        self.nota4.place(x=20, y=110)
        self.campo4 = tk.Entry(root)
        self.campo4.place(x=100, y=110, width=135)
        self.campos.append(self.campo4)

        self.nota5 = tk.Label(root, text="Nota 5:")
        self.nota5.place(x=20, y=140)
        self.campo5 = tk.Entry(root)
        self.campo5.place(x=100, y=140, width=135)
        self.campos.append(self.campo5)

        # Botón Calcular
        self.boton_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.boton_calcular.place(x=40, y=180, width=80)

        # Botón Limpiar
        self.boton_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.boton_limpiar.place(x=140, y=180, width=80)

        # Etiquetas de resultados
        self.label_promedio = tk.Label(root, text="Promedio =")
        self.label_promedio.place(x=20, y=220)

        self.label_desviacion = tk.Label(root, text="Desviación estándar =")
        self.label_desviacion.place(x=20, y=250)

        self.label_mayor = tk.Label(root, text="Valor mayor =")
        self.label_mayor.place(x=20, y=280)

        self.label_menor = tk.Label(root, text="Valor menor =")
        self.label_menor.place(x=20, y=310)

    def calcular(self):
        try:
            notas = [float(c.get()) for c in self.campos]
        except ValueError:
            messagebox.showerror("Error", "Debes ingresar solo números.")
            return

        n = Notas(notas)
        self.label_promedio.config(text=f"Promedio = {n.calcular_promedio():.2f}")
        self.label_desviacion.config(text=f"Desviación estándar = {n.calcular_desviacion():.2f}")
        self.label_mayor.config(text=f"Valor mayor = {n.calcular_mayor():.1f}")
        self.label_menor.config(text=f"Valor menor = {n.calcular_menor():.1f}")

    def limpiar(self):
        for c in self.campos:
            c.delete(0, tk.END)
        self.label_promedio.config(text="Promedio =")
        self.label_desviacion.config(text="Desviación estándar =")
        self.label_mayor.config(text="Valor mayor =")
        self.label_menor.config(text="Valor menor =")