import streamlit as st
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Configuración de paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.common import generate_qr_code, create_download_link, apply_common_styles

# Configuración de correo
EMAIL_CONFIG = {
    'remitente': 'luz.ia@healthtracker.ai',
    'pass_remitente': 'zumt uxtw tmkm gdjk',
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'destinatarios': ['g.rojas@healthtracker.ai']
}

def enviar_correo(nombre, email, asunto, mensaje, origen_pagina="Gestión de Inasistencias IA CCPP"):
    """Función para enviar correos electrónicos usando SMTP"""
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
        sesion_smtp = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        sesion_smtp.starttls()
        sesion_smtp.login(EMAIL_CONFIG['remitente'], EMAIL_CONFIG['pass_remitente'])
        sesion_smtp.sendmail(EMAIL_CONFIG['remitente'], EMAIL_CONFIG['destinatarios'], msg.as_string())
        sesion_smtp.quit()

        return True, "Correo enviado exitosamente"
    except Exception as e:
        return False, f"Error al enviar correo: {str(e)}"


# Configuración de la página
st.set_page_config(
    page_title="Uso de Inteligencia Artificial para la gestión de inasistencias",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos
st.markdown(apply_common_styles(), unsafe_allow_html=True)

# Botón de regreso
if st.sidebar.button("🏠 Volver al Inicio", use_container_width=True):
    st.switch_page("Página principal.py")

# Header principal
st.markdown("""
<div class="main-header">
    <h1>🧠 Uso de Inteligencia Artificial para la gestión de inasistencias</h1>
    <h3>de pacientes paliativos: una experiencia innovadora</h3>
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
        En cuidados paliativos, cada visita no realizada puede comprometer la continuidad del cuidado del paciente.  
        La gestión de inasistencias es compleja debido a la diversidad de registros entre sistemas clínicos y agendas administrativas.  
        La aplicación de inteligencia artificial permite identificar al agente responsable, el motivo del incumplimiento y su evitabilidad, 
        optimizando la gestión clínica y la continuidad de los cuidados.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe, #00f2fe);
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
            <h3>📊 Datos Relevantes</h3>
            <h2>18%</h2>
            <p>Atenciones programadas inicialmente sin análisis sistemático</p>
            <h2>2022–2025</h2>
            <p>Período de registros analizados</p>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "🎯 Objetivo y Desarrollo":
    st.markdown("### 🎯 Objetivo y Desarrollo de la Experiencia")

    st.markdown("""
    #### 🎯 Objetivo
    Proporcionar **clasificación y análisis de inasistencias en cuidados paliativos** a partir de la implementación de **inteligencia artificial como herramienta de integración de datos**.

    #### 🧩 Desarrollo
    - Se identificó que el 18% de las atenciones programadas resultaban en inasistencias sin análisis sistemático, generando un cuello de botella operativo.
    - Se desarrolló un **modelo de clasificación** definido por *Healthtracker Analytics* y *Atención Domiciliaria* (prestador acreditado en Metodología Newpalex).
    - El modelo asocia un **agente responsable** y categoriza los motivos de ausencia según su **evitabilidad**.
    - Se entrenó una herramienta basada en modelos de lenguaje avanzados (Gemini 2.0 Flash – Google Cloud) con registros históricos desde 2022.
    - Los resultados fueron integrados en un **panel Looker Studio**, ofreciendo una panorámica histórica y la identificación de patrones evitables.
    """)

elif seccion == "📊 Resultados":
    st.markdown("### 📊 Resultados Principales")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        #### 📈 Principales hallazgos (2025)
        - **Errores de agendamiento:** 23,5%
        - **No realización de la atención:** 16,1%
        - **Fallecimiento:** 8,9%

        **Clasificación por evitabilidad:**
        - Evitables: errores de agendamiento y traslados.
        - Inevitables: hospitalización o fallecimiento del paciente.

        **Distribución 2025:**
        - 42,1% de inasistencias por condiciones del paciente.
        - Principales causas: hospitalización (19,9%) y traslado (23,6%).

        **Propuesta:**
        Asignar temporalmente un profesional en la zona para mantener la continuidad del cuidado.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #43cea2, #185a9d);
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>🎯 Resultados Clave</h3>
            <hr style="border-color:white;">
            <h4>🔍 42,1% por condiciones del paciente</h4>
            <h4>📊 Identificación de patrones evitables</h4>
            <h4>💡 Integración IA + Panel Looker</h4>
            <h4>🧩 Optimización operativa</h4>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "💡 Conclusiones":
    st.markdown("### 💡 Conclusiones")

    st.markdown("""
    - La integración de modelos de inteligencia artificial en la gestión de cuidados paliativos permite diferenciar factores inevitables de evitables.  
    - Esto optimiza los recursos, mejora la planificación y refuerza la continuidad del cuidado.  
    - La herramienta propone apoyar la **comunicación anticipada** con pacientes y redes asistenciales, potenciando la coordinación de traslados.  
    - La estrategia contribuye al fortalecimiento del modelo de atención y a la **transformación digital** de los cuidados paliativos.
    """)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #56ab2f, #a8e6cf);
                padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
        <h3>🏆 Conclusión General</h3>
        <p>Integrar IA en la gestión de inasistencias mejora la continuidad de los cuidados paliativos, 
        optimizando la respuesta ante eventos evitables e inevitables.</p>
    </div>
    """, unsafe_allow_html=True)

elif seccion == "📥 Descargas":
    st.markdown("### 📥 Descarga del Póster Completo")

    col1, col2 = st.columns([2, 1])
    with col1:
        file_path = os.path.join(parent_dir, "assets", "[CATALINA REYES] Gestión automática de visitas no realizadas a pacientes paliativos domiciliarios mediante Inteligencia Artificial.pptx.pdf")
        if os.path.exists(file_path):
            with open(file_path, "rb") as pdf_file:
                pdf_data = pdf_file.read()
            st.download_button(
                label="📄 Descargar Póster (PDF)",
                data=pdf_data,
                file_name="Gestion_inasistencias_IA.pdf",
                mime="application/pdf",
                use_container_width=True
            )
        else:
            st.warning("⚠️ El archivo PDF no está disponible en este momento.")
    with col2:
        st.markdown("#### 📱 Código QR")
        qr = generate_qr_code("https://healthtracker.ai/")
        st.image(qr, width=200)
        st.markdown("<p style='text-align:center;'>Escanea para más información</p>", unsafe_allow_html=True)

elif seccion == "📧 Contacto":
    st.markdown("### 📧 Contacto")

    st.markdown("""
    **Ing. Catalina Reyes Camaño**  
    Ingeniera Civil Biomédica – Universidad de Concepción  
    Ingeniera Trainee – Healthtracker Analytics  
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
                success, msg = enviar_correo(nombre, email, asunto, mensaje, "Gestión de Inasistencias IA CCPP")
            if success:
                st.success("✅ " + msg)
                st.info("📧 Tu mensaje ha sido enviado. Te contactaremos pronto.")
                st.balloons()
            else:
                st.error("❌ " + msg)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🧠 Uso de Inteligencia Artificial para la gestión de inasistencias |
    Health Tracker Analytics • Atención Domiciliaria • Chile</p>
</div>
""", unsafe_allow_html=True)
