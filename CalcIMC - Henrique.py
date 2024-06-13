import tkinter

import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de IMC")
        
        self.label_altura = tk.Label(self.root, text="Altura (m):")
        self.label_altura.grid(row=0, column=0, padx=10, pady=5)
        self.entry_altura = tk.Entry(self.root)
        self.entry_altura.grid(row=0, column=1, padx=10, pady=5)

        self.label_peso = tk.Label(self.root, text="Peso (kg):")
        self.label_peso.grid(row=1, column=0, padx=10, pady=5)
        self.entry_peso = tk.Entry(self.root)
        self.entry_peso.grid(row=1, column=1, padx=10, pady=5)

        self.button_calcular = tk.Button(self.root, text="Calcular IMC", command=self.calculate_bmi)
        self.button_calcular.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        self.label_resultado = tk.Label(self.root, text="")
        self.label_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def calculate_bmi(self):
        try:
            altura = float(self.entry_altura.get())
            peso = float(self.entry_peso.get())
            if altura <= 0 or peso <= 0:
                messagebox.showerror("Erro", "Altura e peso devem ser valores positivos.")
            else:
                imc = peso / (altura ** 2)
                self.label_resultado.config(text=f"Seu IMC é {imc:.2f}")
                self.show_bmi_category(imc)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para altura e peso.")

    def show_bmi_category(self, imc):
        if imc < 18.5:
            category = "Abaixo do peso"
        elif imc < 24.9:
            category = "Peso normal"
        elif imc < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        messagebox.showinfo("Categoria de IMC", f"Você está na categoria: {category}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    calculator = BMICalculator()
    calculator.run()