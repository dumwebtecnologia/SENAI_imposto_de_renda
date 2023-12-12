import tkinter as tk
from tkinter import messagebox


def calcular_imposto():
    try:
        renda = float(entrada_renda.get())
        despesas = float(entrada_despesas.get())

        # Lógica de cálculo de imposto (ajuste conforme necessário)
        imposto = max(0, renda - despesas) * 0.2

        messagebox.showinfo("Resultado", f"O imposto de renda devido é: R$ {imposto:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")


# Criar a interface gráfica
root = tk.Tk()
root.title("Simulador de Imposto de Renda")

# Widgets
label_renda = tk.Label(root, text="Renda Anual:")
label_renda.pack()

entrada_renda = tk.Entry(root)
entrada_renda.pack()

label_despesas = tk.Label(root, text="Despesas Dedutíveis:")
label_despesas.pack()

entrada_despesas = tk.Entry(root)
entrada_despesas.pack()

botao_calcular = tk.Button(root, text="Calcular Imposto", command=calcular_imposto)
botao_calcular.pack()

# Iniciar a interface gráfica
root.mainloop()