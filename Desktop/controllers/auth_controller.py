from models.database import USERS

# Função para autenticar usuário
def authenticate_user(username, password):
    user = USERS.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None
