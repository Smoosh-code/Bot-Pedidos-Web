from flask import Flask, render_template, request
import sqlite3
import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Crear la app de Flask
app = Flask(__name__)

# Ruta principal: muestra el formulario
@app.route('/')
def index():
    return render_template('pedido_form.html')

# Ruta intermedia: muestra los datos para confirmar
@app.route('/confirmar_pedido', methods=['POST'])
def confirmar_pedido():
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "telefono": request.form['telefono'],
        "producto": request.form['producto'],
        "comentario": request.form['comentario']
    }
    return render_template("confirmar.html", **datos, datos=datos)

# Ruta final: guarda el pedido y envía el correo
@app.route('/enviar_pedido', methods=['POST'])
def enviar_pedido():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    email = request.form['email']
    telefono = request.form['telefono']
    producto = request.form['producto']
    comentario = request.form['comentario']

    # Guardar los datos en la base SQLite
    conn = sqlite3.connect('database/pedidos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            email TEXT,
            telefono TEXT,
            producto TEXT,
            comentario TEXT
        )
    ''')
    cursor.execute('INSERT INTO pedidos (nombre, apellido, email, telefono, producto, comentario) VALUES (?, ?, ?, ?, ?, ?)',
                   (nombre, apellido, email, telefono, producto, comentario))
    conn.commit()
    conn.close()

    # Enviar email de confirmación
    enviar_correo_confirmacion(email, nombre, producto)

    return render_template('gracias.html', nombre=nombre, apellido=apellido)

# Función para enviar un correo usando SMTP
def enviar_correo_confirmacion(destinatario, nombre, producto):
    remitente = os.getenv("EMAIL_USER")
    contraseña = os.getenv("EMAIL_PASS")

    mensaje = EmailMessage()
    mensaje['Subject'] = 'Confirmación de tu pedido'
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje.set_content(f"Hola {nombre}, gracias por tu pedido de '{producto}'. En breve nos contactaremos con vos.")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(remitente, contraseña)
            smtp.send_message(mensaje)
    except Exception as e:
        print("Error al enviar correo:", e)

# Ejecutar la app
if __name__ == '__main__':
    app.run(debug=True)
