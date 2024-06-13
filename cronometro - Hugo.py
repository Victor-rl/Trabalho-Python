import tkinter as tk

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro Digital")
        self.root.geometry("500x300")
        self.root.configure(bg="#282C34")

        self.tempo = 0
        self.executando = False

        self.label_tempo = tk.Label(root, text="00:00:00", font=("Courier", 48, 'bold'), bg="#282C34", fg="#61AFEF")
        self.label_tempo.pack(pady=20)

        frame_botoes = tk.Frame(root, bg="#282C34")
        frame_botoes.pack()

        self.botao_iniciar = tk.Button(frame_botoes, text="Iniciar", font=("Courier", 14, 'bold'), bg="#98C379", fg="#282C34", command=self.iniciar)
        self.botao_iniciar.grid(row=0, column=0, padx=10, pady=10)

        self.botao_parar = tk.Button(frame_botoes, text="Parar", font=("Courier", 14, 'bold'), bg="#E06C75", fg="#282C34", command=self.parar)
        self.botao_parar.grid(row=0, column=1, padx=10, pady=10)

        self.botao_pausar = tk.Button(frame_botoes, text="Pausar", font=("Courier", 14, 'bold'), bg="#E5C07B", fg="#282C34", command=self.pausar)
        self.botao_pausar.grid(row=0, column=2, padx=10, pady=10)

        self.botao_reiniciar = tk.Button(frame_botoes, text="Reiniciar", font=("Courier", 14, 'bold'), bg="#61AFEF", fg="#282C34", command=self.reiniciar)
        self.botao_reiniciar.grid(row=0, column=3, padx=10, pady=10)

    def atualizar_tempo(self):
        if self.executando:
            self.tempo += 1
            minutos, segundos = divmod(self.tempo, 60)
            horas, minutos = divmod(minutos, 60)
            self.label_tempo.config(text=f"{horas:02}:{minutos:02}:{segundos:02}")
            self.root.after(1000, self.atualizar_tempo)

    def iniciar(self):
        if not self.executando:
            self.executando = True
            self.atualizar_tempo()

    def parar(self):
        self.executando = False

    def pausar(self):
        self.executando = False

    def reiniciar(self):
        self.executando = False
        self.tempo = 0
        self.label_tempo.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()
