from usuarios_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Usuario:
    def __init__(self,id,nombre,apellido,email,created_at,updated_at):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.created_at=created_at
        self.updated_at=updated_at

    @classmethod
    def agregaUsuario(cls,nuevoUsuario:dict):
        query = '''
                    INSERT INTO usuarios(nombre,apellido, email, created_at, updated_at)
                    VALUES ( %(nombre)s, %(apellido)s, %(email)s, NOW(), NOW());
                '''
        resultado = connectToMySQL("esquema_usuario").query_db(query,nuevoUsuario)
        return resultado

    @classmethod
    def obtenerUsuarios(cls):
        query = '''
                    SELECT *
                    FROM usuarios;
                '''
        resultado = connectToMySQL("esquema_usuario").query_db(query)
        listaUsuarios:list[Usuario] = []
        for usuario in resultado:
            listaUsuarios.append(Usuario(usuario["id"], 
                usuario["nombre"], usuario["apellido"], 
                usuario["email"],usuario["created_at"],usuario["updated_at"]))

        return listaUsuarios