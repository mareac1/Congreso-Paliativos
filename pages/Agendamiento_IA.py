import streamlit as st
import sys
import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Configuración de paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.common import generate_qr_code, apply_common_styles
# Configuración de correo
EMAIL_CONFIG = {
    'remitente': 'luz.ia@healthtracker.ai',
    'pass_remitente': 'zumt uxtw tmkm gdjk',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'destinatarios': ['g.rojas@healthtracker.ai', 'm.reyes@healthtracker.ai', 'f.moreno@healthtracker.ai', 'j.jimenez@healthtracker.ai', 't.schade@healthtracker.ai', 's.villagra@healthtracker.ai', 'c.reyes@healthtracker.ai']
}
def enviar_correo(nombre, email, asunto, mensaje, institucion, cargo, origen_pagina="Pacientes Críticos RFM CCPP"):
    """Envía correos electrónicos usando SMTP."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['remitente']
        msg['To'] = ', '.join(EMAIL_CONFIG['destinatarios'])
        msg['Subject'] = f"[{origen_pagina}] {asunto}"

        body = f"""
        Nuevo mensaje desde la página de {origen_pagina}:

        NOMBRE: {nombre}
        EMAIL: {email}
        ASUNTO: {asunto}

        MENSAJE:
        {mensaje}

        INSTITUCIÓN:
        {institucion}

        CARGO:
        {cargo}

        ---
        Enviado desde: {origen_pagina}
        Fecha: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        """

        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        smtp = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        smtp.starttls()
        smtp.login(EMAIL_CONFIG['remitente'], EMAIL_CONFIG['pass_remitente'])
        smtp.sendmail(EMAIL_CONFIG['remitente'], EMAIL_CONFIG['destinatarios'], msg.as_string())
        smtp.quit()

        return True, "Correo enviado exitosamente"
    except Exception as e:
        return False, f"Error al enviar correo: {str(e)}"
def correo_simple(asunto, cuerpo_html, destinatarios):
    remitente = 'luz.ia@healthtracker.ai'
    pass_remitente = 'zumt uxtw tmkm gdjk'
    
    sesion_smtp = smtplib.SMTP(host='smtp.gmail.com', port=587)
    sesion_smtp.ehlo()
    sesion_smtp.starttls()
    sesion_smtp.login(remitente, pass_remitente)


    mensaje = MIMEMultipart('mixed')
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto

    cuerpo_completo = f"""
    <html>
    <body>
        {cuerpo_html}
        <br><br>
    </body>
    </html>
    """

    mensaje.attach(MIMEText(cuerpo_completo, 'html'))

    # Enviar correo
    sesion_smtp.sendmail(remitente, destinatarios, mensaje.as_string())
    print('📨 Correo enviado')
    sesion_smtp.quit()
# Configuración de la página
st.set_page_config(
    page_title="Agendamiento automatizado de visitas para cuidados paliativos",
    page_icon="📅",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar estilos comunes
st.markdown(apply_common_styles(), unsafe_allow_html=True)

# Botón de regreso
if st.sidebar.button("🏠 Volver al Inicio", use_container_width=True):
    st.switch_page("Página principal.py")

# Header principal
st.markdown("""
<div class="main-header">
    <h1>📅 Agendamiento automatizado de visitas de profesionales</h1>
    <h3>para cuidados paliativos domiciliarios</h3>
</div>
""", unsafe_allow_html=True)

# Navegación lateral
st.sidebar.title("🧭 Navegación")
seccion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "📋 Resumen de la Investigación"
    ]
)

# --- SECCIONES ---

if seccion == "📋 Resumen de la Investigación":
    st.markdown("### 📋 Resumen de la Investigación")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        #### 🔍 Introducción
        En el contexto actual de los cuidados paliativos, la creciente complejidad clínica y social de los pacientes 
        exige una planificación asistencial más precisa y personalizada.  
        Se implementó un **sistema de agendamiento automatizado** que integra criterios clínicos y administrativos, 
        optimizando los recursos y respondiendo con agilidad a los cambios en la condición del paciente.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #36d1dc, #5b86e5);
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
            <h3>📊 Datos Clave</h3>
            <h2>90%</h2>
            <p>Automatización alcanzada en agosto 2025</p>
            <h2>70%</h2>
            <p>Promedio anual de atenciones automáticas</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### 📧 Contacto")

    st.markdown("""
    **M.Sc. Thomas Schade Villagrán**  
    DPO – Healthtracker Analytics  
    Diplomado en Seguridad de Datos Personales – Pontificia Universidad Católica de Chile  
    Magíster en Ciencia de Datos – Universidad de Concepción  
    Ingeniero Civil Biomédico – Universidad de Concepción  
    [https://healthtracker.ai/](https://healthtracker.ai/)
    """)

    st.markdown("---")
    st.markdown("### 📝 Formulario de Contacto")

    with st.form("contact_form"):
        nombre = st.text_input("👤 Nombre completo *")
        institucion = st.text_input("🏢 Institución / Empresa *")
        cargo = st.text_input("💼 Cargo / Profesión *")
        email = st.text_input("📧 Email *")
        asunto = st.selectbox(
            "📋 Motivo de contacto *",
            [
                "Consulta general sobre la investigación",
                "Colaboración o replicación de modelo",
                "Implementación institucional",
                "Solicitud de información técnica",
                "Otro"
            ]
        )
        mensaje = st.text_area("💬 Mensaje *", height=150)
        
        aceptar = st.checkbox(
            "✅ Acepto que el equipo de Healthtracker Analytics se comunique conmigo por correo electrónico"
        )

        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("📤 Enviar Mensaje", use_container_width=True)
        with col2:
            if st.form_submit_button("🔄 Limpiar", use_container_width=True):
                st.rerun()

    if submitted:
        if not nombre or not email or not asunto or not mensaje:
            st.error("❌ Todos los campos son obligatorios.")
        elif not aceptar:
            st.warning("⚠️ Debes aceptar el envío de correos para poder continuar.")
        else:
            with st.spinner("📤 Enviando mensaje..."):
                success, msg = enviar_correo(nombre, email, asunto, mensaje, institucion, cargo, "Agendamiento IA CCPP")
                
                # Enviar correo simple con saludo de luz.ia y el enlace
                cuerpo_html = f"""
                <p>Hola,</p>
                <p>Espero que te encuentres bien. Te comparto el enlace de referencia:</p>
                <br>
                <p><a href="https://drive.google.com/file/d/17qfudi4GpbRsX2gh_b6UeA7c37pfhHYc/view?usp=drive_link">Ver documento en Drive</a></p>
                <br>
                <p>Saludos,<br>Luz.IA</p>
                """
                correo_simple(
                    asunto="Enlace de referencia - Agendamiento IA CCPP",
                    cuerpo_html=cuerpo_html,
                    destinatarios=[email]
                )
                
            if success:
                st.success("✅ " + msg)
                st.info("📧 Tu mensaje ha sido enviado. Te contactaremos pronto.")
                st.balloons()
            else:
                st.error("❌ " + msg)


    
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>📅 Agendamiento automatizado de visitas para cuidados paliativos |
    Health Tracker Analytics • Atención Domiciliaria • Chile</p>
</div>
""", unsafe_allow_html=True)
