import tkinter as tk
from views.login_view import LoginView

# Classe principal que inicializa o programa
class PortalApp:
    def __init__(self, root):
        root.title("Portal Desktop")
        root.geometry("400x300")
        LoginView(root)  # Abre a tela de login inicialmente

if __name__ == "__main__":
    root = tk.Tk()
    app = PortalApp(root)
    root.mainloop()
