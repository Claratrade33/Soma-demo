from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import json
import os

usuarios_bp = Blueprint('usuarios', __name__)

USERS_FILE = os.path.join(os.path.dirname(__file__), 'users.json')

@usuarios_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'r') as f:
                users = json.load(f)
            for user in users:
                if user['username'] == username and user['password'] == password:
                    session['user'] = user
                    return redirect(url_for('manual_ops.painel'))
        flash('Credenciais inválidas. Registre-se ou tente novamente.', 'danger')
    return render_template('login.html')

@usuarios_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logout efetuado.', 'info')
    return redirect(url_for('usuarios.login'))
