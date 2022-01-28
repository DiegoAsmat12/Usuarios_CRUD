from unittest import result
from flask import render_template, request, redirect
from usuarios_app import app
from usuarios_app.modelos.modelo_usuario import Usuario

@app.route("/users", methods=["GET"])
def renderUsers():
    usuarios = Usuario.obtenerUsuarios()
    return render_template('usuarios.html', usuarios = usuarios)

@app.route("/users/new", methods=["GET"])
def renderUserForm():
    return render_template('crea_usuarios.html')

@app.route("/users/new", methods=["POST"])
def postNewUser():
    nuevoUsuario ={
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.agregaUsuario(nuevoUsuario)
    return redirect("/users")

@app.route("/users/<int:id>", methods=["GET"])
def showUser(id):
    usuarioID ={
        "id":id
    }
    usuario = Usuario.obtenerUsuario(usuarioID)
    return render_template('muestra_usuario.html', usuario=usuario)


@app.route("/users/edit/<int:id>" , methods=["GET"])
def formEditUser(id):
    usuarioID = {
        "id":id
    }
    usuario= Usuario.obtenerUsuario(usuarioID)
    return render_template('editar_usuario.html', usuario=usuario)

@app.route("/users/edit/<int:id>", methods=["POST"])
def editUser(id):
    usuarioEditado = {
        "id":id,
        "nombre":request.form["nombre"],
        "apellido":request.form["apellido"],
        "email":request.form["email"],
    }
    resultado =Usuario.actualizaUsuario(usuarioEditado)
    return redirect(f"/users/{id}")

@app.route("/delete/<int:id>", methods=["POST"])
def deleteUser(id):
    usuarioID = {
        'id':id
    }
    resultado = Usuario.borraUsuario(usuarioID)
    return redirect("/users")
