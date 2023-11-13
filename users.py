from mysqlconnection import connectToMySQL
#Modelo de la clase (usuario)
class User: 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #Nombre completo del usuario
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    #conseguir todos los usuarios
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('db_users').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users
    
    #guardar usuario
    @classmethod
    def save (cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        result = connectToMySQL('db_users').query_db(query, data)
        return result
    
    #conseguir usuario
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('db_users').query_db(query, data)
        return cls(result[0])
    #Actualizar usuario

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('db_users').query_db(query, data)
    
    #Eliminar usuario
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('db_users').query_db(query, data)
