from flask import Blueprint, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

# Usuarios hardcodeados, para simplificar (solo vos podés ser admin)
usuarios = {
    "admin": {
        "password": generate_password_hash("tusecretopersonal"),
        "rol": "admin"
    },
    "terapeuta": {
        "password": generate_password_hash("clave123"),
        "rol": "terapeuta"
    }
}

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = usuarios.get(data["username"])
    if user and check_password_hash(user["password"], data["password"]):
        session["usuario"] = data["username"]
        session["rol"] = user["rol"]
        return {"mensaje": "Login correcto"}
    return {"mensaje": "Credenciales inválidas"}, 401

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))
