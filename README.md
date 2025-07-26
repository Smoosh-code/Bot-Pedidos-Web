# 🛒 Bot de Pedidos Web (con confirmación y email)

Este es un formulario web hecho en Flask para que clientes realicen pedidos fácilmente desde el celular o la PC. Ideal para freelancers, pequeños comercios o servicios personalizados.

## ✅ ¿Qué hace?

- Muestra un formulario para capturar: nombre, apellido, email, teléfono, producto y comentario.
- El cliente puede confirmar los datos antes de enviarlos.
- Guarda los datos en base de datos SQLite.
- Envía un email automático de confirmación al cliente.

## 💌 Requisitos de configuración

Crea un archivo `.env` con tu correo y contraseña de aplicación de Gmail:

```env
EMAIL_USER=tu_email@gmail.com
EMAIL_PASS=tu_contraseña_de_aplicación


🚀 Cómo correr el proyecto

pip install -r requirements.txt
python app.py


🧠 Autor
Gustavo Günther – LinkedIn
Este bot está pensado para ser simple, funcional y fácil de personalizar.