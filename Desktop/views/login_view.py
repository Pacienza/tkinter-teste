import tkinter as tk
from controllers.auth_controller import authenticate_user
from views.admin_view import AdminView
from views.terapeuta_view import TerapeutaView
from views.paciente_view import PacienteView

# Tela de login
class LoginView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack()

        # Widgets
        tk.Label(self.frame, text="Login").grid(row=0, column=0)
        self.login_entry = tk.Entry(self.frame)
        self.login_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Senha").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.frame, text="Entrar", command=self.login).grid(row=2, columnspan=2)

    def login(self):
        username = self.login_entry.get()
        password = self.password_entry.get()
        role = authenticate_user(username, password)

        if role == "admin":
            self.frame.destroy()
            AdminView(self.root)
        elif role == "terapeuta":
            self.frame.destroy()
            TerapeutaView(self.root)
        elif role == "paciente":
            self.frame.destroy()
            PacienteView(self.root)
        else:
            tk.Label(self.frame, text="Login inválido").grid(row=3, columnspan=2)
