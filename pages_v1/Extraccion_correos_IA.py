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
    'destinatarios': ['g.rojas@healthtracker.ai']
}

def enviar_correo(nombre, email, asunto, mensaje, origen_pagina="Extracción de Correos IA CCPP"):
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

# Configuración de la página
st.set_page_config(
    page_title="Extracción de información clínica desde correos electrónicos con IA",
    page_icon="📬",
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
    <h1>📬 Extracción de información clínica desde correos electrónicos</h1>
    <h3>en cuidados paliativos mediante Inteligencia Artificial</h3>
</div>
""", unsafe_allow_html=True)

# Navegación lateral
st.sidebar.title("🧭 Navegación")
seccion = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "📋 Resumen de la Investigación",
        "🎯 Objetivo y Desarrollo",
        "📊 Resultados",
        "💡 Conclusiones",
        "📥 Descargas",
        "📧 Contacto"
    ]
)

# --- SECCIONES ---

if seccion == "📋 Resumen de la Investigación":
    st.markdown("### 📋 Resumen de la Investigación")

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        #### 🔍 Introducción
        En la atención domiciliaria de cuidados paliativos, los equipos clínicos enfrentan una alta carga administrativa por la **lectura y clasificación manual de correos electrónicos**.  
        La variabilidad y el volumen dificultan una gestión oportuna.  
        Mediante **Inteligencia Artificial (IA)**, los sistemas pueden aprender de los datos y ejecutar tareas de forma autónoma, reduciendo la carga operativa y mejorando la continuidad asistencial.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #36d1dc, #5b86e5);
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
            <h3>📊 Datos Clave</h3>
            <h2>150</h2>
            <p>Correos procesados mensualmente</p>
            <h2>3</h2>
            <p>Proyectos en operación o piloto</p>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "🎯 Objetivo y Desarrollo":
    st.markdown("### 🎯 Objetivo y Desarrollo de la Experiencia")

    st.markdown("""
    #### 🎯 Objetivo
    Desarrollar e implementar un **sistema automatizado** que, mediante bots y modelos de IA, 
    sea capaz de **leer, anonimizar y clasificar texto libre** proveniente de correos clínicos, 
    reduciendo la carga manual y garantizando la **protección de datos personales**.

    #### 🧩 Desarrollo
    - Se diseñaron flujos automáticos para la clasificación de correos de respuesta.  
    - El sistema comienza con la **anonimización** de datos personales.  
    - Los correos se clasifican mediante IA en **válidos e irrelevantes**.  
    - Los válidos son procesados con **Gemini 2.0 (Google Cloud)**, que interpreta y estructura la información de los adjuntos.  
    - Los registros válidos se consolidan para trazabilidad y análisis continuo.  
    """)

elif seccion == "📊 Resultados":
    st.markdown("### 📊 Resultados Principales")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        #### 📈 Impacto del sistema
        - Detección automatizada con **alta concordancia** respecto al juicio experto.  
        - Reducción significativa en el **tiempo de revisión manual**.  
        - Mejora de la **trazabilidad** y calidad del registro clínico.  
        - **150 correos mensuales** procesados en promedio.  
        - Dos proyectos en producción y uno en fase piloto desde octubre 2025.  
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #11998e, #38ef7d);
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>🎯 Resultados Clave</h3>
            <hr style="border-color:white;">
            <h4>🤖 Clasificación automática de correos</h4>
            <h4>📂 Estructuración de información clínica</h4>
            <h4>⏱️ Ahorro de tiempo para el equipo</h4>
            <h4>🔒 Anonimización y trazabilidad</h4>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "💡 Conclusiones":
    st.markdown("### 💡 Conclusiones")

    st.markdown("""
    - La automatización de la lectura y clasificación de correos mediante IA **mejora la eficiencia operativa**.  
    - **Reduce la carga administrativa** del equipo de coordinación.  
    - Garantiza la **confidencialidad y estructuración de datos** clínicos.  
    - Contribuye a la **continuidad asistencial** en cuidados paliativos domiciliarios.  
    """)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #56ab2f, #a8e6cf);
                padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
        <h3>🏆 Conclusión General</h3>
        <p>La automatización de correos clínicos con IA permite optimizar los procesos administrativos, 
        fortalecer la trazabilidad y asegurar la continuidad de los cuidados paliativos.</p>
    </div>
    """, unsafe_allow_html=True)

elif seccion == "📥 Descargas":
    st.markdown("### 📥 Descarga y Vista Previa del Póster")

    file_path = os.path.join(parent_dir, "assets", "[MATIAS REYES] Extracción de información clínica desde correos electrónicos en cuidados paliativos mediante inteligencia artificial.pptx.pdf")
    if os.path.exists(file_path):
        with open(file_path, "rb") as pdf_file:
            pdf_data = pdf_file.read()
        st.download_button(
            label="📄 Descargar Póster (PDF)",
            data=pdf_data,
            file_name="Extraccion_correos_IA.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        # Vista previa 3:4 (vertical)
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f"""
        <div style="text-align:center; margin-top:1rem;">
            <iframe 
                src="data:application/pdf;base64,{base64_pdf}" 
                width="100%" 
                height="1200px" 
                style="border:none; border-radius:12px; box-shadow:0 0 10px rgba(0,0,0,0.1);"
            ></iframe>
            <p style="color:#666; font-size:0.9rem; margin-top:0.5rem;">Vista previa del póster (proporción 3:4)</p>
        </div>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.warning("⚠️ El archivo PDF no está disponible en este momento.")

elif seccion == "📧 Contacto":
    st.markdown("### 📧 Contacto")

    st.markdown("""
    **Ing. Matías Reyes Acuña**  
    Ingeniero Civil Biomédico – Universidad de Concepción  
    Ingeniero Trainee – Healthtracker Analytics  
    [https://healthtracker.ai/](https://healthtracker.ai/)
    """)

    st.markdown("---")
    st.markdown("### 📝 Formulario de Contacto")

    with st.form("contact_form"):
        nombre = st.text_input("👤 Nombre completo *")
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
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("📤 Enviar Mensaje", use_container_width=True)
        with col2:
            if st.form_submit_button("🔄 Limpiar", use_container_width=True):
                st.rerun()

    if submitted:
        if not nombre or not email or not asunto or not mensaje:
            st.error("❌ Todos los campos son obligatorios.")
        else:
            with st.spinner("📤 Enviando mensaje..."):
                success, msg = enviar_correo(nombre, email, asunto, mensaje, "Extracción de Correos IA CCPP")
            if success:
                st.success("✅ " + msg)
                st.info("📧 Tu mensaje ha sido enviado. Te contactaremos pronto.")
                st.balloons()
            else:
                st.error("❌ " + msg)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>📬 Extracción de información clínica desde correos electrónicos |
    Health Tracker Analytics • Atención Domiciliaria • Chile</p>
</div>
""", unsafe_allow_html=True)
