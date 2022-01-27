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