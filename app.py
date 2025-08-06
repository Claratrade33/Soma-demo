from flask import Flask, render_template

# Criação do app Flask
app = Flask(__name__)
app.secret_key = 'super-secret-key-demo'

# Importa e registra blueprints
from registro.rotas import registro_bp
from usuarios.rotas import usuarios_bp
from operacoes.manual.rotas import manual_ops_bp
from operacoes.automatico.rotas import auto_ops_bp

app.register_blueprint(registro_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(manual_ops_bp)
app.register_blueprint(auto_ops_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
