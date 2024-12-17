import tkinter as tk
from controllers.data_controller import list_users, add_user
from tkinter import messagebox

class AdminView:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(root)
        self.frame.pack()

        tk.Label(self.frame, text="Painel do Administrador").pack()

        # Botão para listar usuários
        tk.Button(self.frame, text="Listar Usuários", command=self.show_users).pack()

        # Botão para adicionar um usuário
        tk.Button(self.frame, text="Adicionar Usuário", command=self.add_user).pack()

        tk.Button(self.frame, text="Sair", command=self.root.destroy).pack()

    def show_users(self):
        users = list_users()
        user_list = "\n".join([f"{u['username']} - {u['role']}" for u in users])
        messagebox.showinfo("Usuários", user_list)

    def add_user(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Adicionar Usuário")

        tk.Label(add_window, text="Username:").grid(row=0, column=0)
        username_entry = tk.Entry(add_window)
        username_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Password:").grid(row=1, column=0)
        password_entry = tk.Entry(add_window, show="*")
        password_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Role (admin/terapeuta/paciente):").grid(row=2, column=0)
        role_entry = tk.Entry(add_window)
        role_entry.grid(row=2, column=1)

        def save_user():
            username = username_entry.get()
            password = password_entry.get()
            role = role_entry.get()
            if add_user(username, password, role):
                tk.messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
                add_window.destroy()
            else:
                tk.messagebox.showerror("Erro", "Usuário já existe!")

        tk.Button(add_window, text="Salvar", command=save_user).grid(row=3, columnspan=2)
