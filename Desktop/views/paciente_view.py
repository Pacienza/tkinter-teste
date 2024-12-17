import tkinter as tk

class PacienteView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack()

        tk.Label(self.frame, text="Painel do Paciente").pack()
        tk.Button(self.frame, text="Sair", command=self.root.destroy).pack()
