from models.database import USERS

# Função para listar todos os usuários no sistema
def list_users():
    return [{"username": user, "role": data["role"]} for user, data in USERS.items()]

# Função para adicionar um novo usuário
def add_user(username, password, role):
    if username not in USERS:
        USERS[username] = {"password": password, "role": role}
        return True
    return False

# Função para verificar se um usuário existe
def user_exists(username):
    return username in USERS
