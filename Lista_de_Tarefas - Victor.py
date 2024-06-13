import tkinter as tk
from tkinter import ttk
import json

class ToDoListApp(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.title("Lista de Tarefas")
        self.geometry("400x400")
        
        # Criar um campo de entrada (CdE) para adicionar as tarefas
        self.tarefa_entrada = ttk.Entry(self, font=("TKDefaltFont", 16), width=30)
        self.tarefa_entrada.pack(pady=10)
        
        # Botar um placeholder no CdE
        self.tarefa_entrada.insert(0, "Entre com seu ToDo aqui...")
        
        # Vincular evento para limpar o placeholder quando o CdE for clicado
        self.tarefa_entrada.bind("<FocusIn>", self.limpar_placeholder)
        # Vincular evento para restaurar o placeholder quando o CdE perder foco
        self.tarefa_entrada.bind("<FocusOut>", self.restaurar_placeholder)
        
        # Cria um botão para adicionar tarefas
        ttk.Button(self, text="Adicionar Tarefa", command=self.add_tarefa).pack(pady=5)
        
        # Cria uma listbox para mostrar as tarefas adicionadas
        self.lista_tarefas = tk.Listbox(self, font=("TKDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.lista_tarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Cria botões para marcar se a tarefa está pronta ou para deleta-las
        ttk.Button(self, text="Concluir", style="sucess.TButton", command=self.concluida_tarefa).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Remover", style="danger.TButton", command=self.remover_tarefa).pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Carrega a lista do Tarefas.json 
        self.carregar_tarefas()
        

    def add_tarefa(self):
        tarefa = self.tarefa_entrada.get()
        if tarefa != "Entre com seu ToDo aqui...":
            self.lista_tarefas.insert(tk.END, tarefa)
            self.lista_tarefas.itemconfig(tk.END, fg="orange")
            self.tarefa_entrada.delete(0, tk.END)
            self.salvar_tarefas()
    
    def concluida_tarefa(self):
        index_tarefa = self.lista_tarefas.curselection()
        if index_tarefa:
            self.lista_tarefas.itemconfig(index_tarefa, fg="green")
            self.salvar_tarefas()
         
    def remover_tarefa(self):
        index_tarefa = self.lista_tarefas.curselection()
        if index_tarefa:
            self.lista_tarefas.delete(index_tarefa)
            self.salvar_tarefas()
           
    def limpar_placeholder(self, event):
        if self.tarefa_entrada.get() == "Entre com seu ToDo aqui...":
            self.tarefa_entrada.delete(0, tk.END)
            self.tarefa_entrada.configure(style="TEntry")
        
    def restaurar_placeholder(self, event):
        if self.tarefa_entrada.get() == "":
            self.tarefa_entrada.insert(0, "Entre com seu ToDo aqui...")
            self.tarefa_entrada.configure(style="Custom.TEntry")
    
    # Carrega a lista do Tarefas.json 
    
    def carregar_tarefas(self):
        try:
            with open("Tarefas.json", "r") as f:
                data = json.load(f)
                for tarefas in data:
                    self.lista_tarefas.insert(tk.END, tarefas["texto"])
                    self.lista_tarefas.itemconfig(tk.END, fg=tarefas["cor"])
        except FileNotFoundError:
            pass

    # Salva a lista no Tarefas.json
            
    def salvar_tarefas(self):
        data = []
        for i in range(self.lista_tarefas.size()):
            texto = self.lista_tarefas.get(i)
            cor = self.lista_tarefas.itemcget(i, "fg")
            data.append({"texto": texto, "cor": cor})
        with open("Tarefas.json", "w") as f:
            json.dump(data, f)
    

if __name__ == "__main__":
    app = ToDoListApp()
    app.mainloop()