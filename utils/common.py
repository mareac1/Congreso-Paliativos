import qrcode
import io
import base64
from PIL import Image
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def generate_qr_code(data):
    """Genera un código QR a partir de los datos proporcionados"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convertir a bytes para mostrar en Streamlit
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)
    return buf

def create_download_link(file_path, link_text):
    """Crea un enlace de descarga para archivos PDF"""
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        href = f'<a href="data:application/pdf;base64,{b64}" download="{os.path.basename(file_path)}" style="text-decoration: none; background-color: #4CAF50; color: white; padding: 10px 20px; border-radius: 5px; display: inline-block; margin: 10px 0;">{link_text}</a>'
        return href
    except FileNotFoundError:
        return f'<span style="color: red;">Archivo no encontrado: {file_path}</span>'

def send_email(name, email, interest, message):
    """Envía un email con la información del formulario de contacto"""
    try:
        # Configuración del servidor SMTP (ajustar según sea necesario)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = "tu_email@gmail.com"  # Cambiar por el email real
        sender_password = "tu_password"  # Usar variables de entorno en producción

        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = "contacto@redsalud.cl"  # Cambiar por el email de destino
        msg['Subject'] = f"Contacto desde Congresos CCPP - {interest}"

        body = f"""
        Nuevo mensaje desde la aplicación de Congresos de Cuidados Paliativos:

        Nombre: {name}
        Email: {email}
        Interés: {interest}

        Mensaje:
        {message}
        """

        msg.attach(MIMEText(body, 'plain'))

        # Enviar el email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, "contacto@redsalud.cl", text)
        server.quit()

        return True
    except Exception as e:
        print(f"Error al enviar email: {e}")
        return False

def get_asset_path(filename):
    """Obtiene la ruta completa de un archivo en la carpeta assets"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "..", "assets", filename)

def apply_common_styles():
    """Aplica estilos CSS comunes a todas las páginas"""
    return """
    <style>
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #4CAF50, #45a049);
            color: white;
            border-radius: 10px;
            margin-bottom: 2rem;
        }

        .info-card {
            background: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
            border-left: 5px solid #4CAF50;
        }

        .highlight-box {
            background: #f0f8f0;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #4CAF50;
            margin: 1rem 0;
        }

        .qr-container {
            text-align: center;
            padding: 1rem;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .back-button {
            position: fixed;
            top: 100px;
            left: 20px;
            z-index: 999;
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
        }

        .contact-form {
            background: #f9f9f9;
            padding: 2rem;
            border-radius: 10px;
            margin: 2rem 0;
        }

        .success-message {
            background: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 5px;
            border: 1px solid #c3e6cb;
            margin: 1rem 0;
        }

        .error-message {
            background: #f8d7da;
            color: #721c24;
            padding: 1rem;
            border-radius: 5px;
            border: 1px solid #f5c6cb;
            margin: 1rem 0;
        }
    </style>
    """
