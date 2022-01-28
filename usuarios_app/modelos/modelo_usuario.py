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
    
    @classmethod
    def obtenerUsuario(cls,usuario:dict):
        query=  '''
                    SELECT *
                    FROM usuarios
                    WHERE id= %(id)s;
                '''
        resultado = connectToMySQL("esquema_usuario").query_db(query,usuario)
        print(resultado)
        if(resultado!= False):
            usuario = Usuario(resultado[0]["id"], resultado[0]["nombre"], 
                            resultado[0]["apellido"], resultado[0]["email"], 
                            resultado[0]["created_at"], resultado[0]["updated_at"])
            return usuario
        return resultado

    @classmethod
    def actualizaUsuario(cls,usuario:dict):
        query = '''
                    UPDATE usuarios
                    SET nombre=%(nombre)s, apellido=%(apellido)s,
                    email=%(email)s, updated_at=NOW()
                    WHERE id = %(id)s
                '''
        resultado = connectToMySQL("esquema_usuario").query_db(query,usuario)
        return resultado

    @classmethod
    def borraUsuario(cls, usuario:dict):
        query = '''
                    DELETE
                    FROM usuarios 
                    WHERE id = %(id)s
                '''
        resultado = connectToMySQL("esquema_usuario").query_db(query,usuario)
        print(resultado)
        return resultado