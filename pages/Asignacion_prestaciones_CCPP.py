import streamlit as st
import sys
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import base64

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

def enviar_correo(nombre, email, asunto, mensaje, origen_pagina="Asignación Automática de Prestaciones IA CCPP"):
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
    page_title="Asignación automática de prestaciones en pacientes paliativos",
    page_icon="🧩",
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
    <h1>🧩 Identificación y asignación automática de prestaciones paquetizadas</h1>
    <h3>en pacientes paliativos domiciliarios</h3>
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
        La asignación de paquetes de prestaciones en cuidados paliativos domiciliarios suele requerir **revisión manual** de informes clínicos, generando demoras y variabilidad en los criterios.  
        Se implementó un **sistema con inteligencia artificial** capaz de analizar los registros médicos y asignar automáticamente el nivel de complejidad del paciente, mejorando la **eficiencia** y **estandarización** del proceso.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #7b4397, #dc2430);
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
            <h3>📊 Datos Clave</h3>
            <h2>93.8%</h2>
            <p>Validación clínica del sistema</p>
            <h2>59%</h2>
            <p>Concordancia automática con profesionales</p>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "🎯 Objetivo y Desarrollo":
    st.markdown("### 🎯 Objetivo y Desarrollo de la Experiencia")

    st.markdown("""
    #### 🎯 Objetivo
    Desarrollar e implementar un **sistema automatizado con inteligencia artificial** capaz de analizar informes médicos domiciliarios y asignar automáticamente el **paquete de prestaciones** según la complejidad del paciente, optimizando la gestión clínica y administrativa en cuidados paliativos domiciliarios.

    #### 🧩 Desarrollo
    1. **Extracción de datos:** identificación de variables clínicas clave, como estado funcional (ECOG), nivel de dolor (EVA), frecuencia de visitas y procedimientos requeridos.  
    2. **Procesamiento con IA:** los datos son comparados con criterios institucionales definidos para proponer automáticamente el paquete correspondiente.  
    3. **Integración administrativa:** los resultados son enviados a una bandeja de revisión, donde el equipo clínico valida, ajusta o aprueba la clasificación.  
    4. **Validación humana:** retroalimentación del equipo clínico para ajustar precisión y confiabilidad del modelo.
    """)

elif seccion == "📊 Resultados":
    st.markdown("### 📊 Resultados Principales")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        #### 📈 Resultados Destacados
        - Validación clínica del sistema en **93.8%** de los casos.  
        - Concordancia automática de **59%** entre IA y clasificación profesional.  
        - Reducción significativa de **tiempos de revisión y asignación**.  
        - Estandarización del proceso administrativo y clínico.  
        - Mejora en la **trazabilidad** de los casos revisados y en la **consistencia** de criterios.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #42275a, #734b6d);
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>🎯 Resultados Clave</h3>
            <hr style="border-color:white;">
            <h4>✅ 93.8% validación clínica</h4>
            <h4>🤝 59% concordancia automática</h4>
            <h4>🕒 Reducción de tiempos de revisión</h4>
            <h4>📋 Proceso estandarizado</h4>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "💡 Conclusiones":
    st.markdown("### 💡 Conclusiones")

    st.markdown("""
    La incorporación de inteligencia artificial en la **asignación de paquetes de prestaciones** en cuidados paliativos domiciliarios:
    - **Reduce tiempos administrativos.**  
    - **Estandariza criterios clínicos.**  
    - **Mejora la coherencia** en la clasificación de pacientes.  
    - **Complementa la valoración profesional**, fortaleciendo la gestión integral del cuidado.

    El modelo se presenta como una herramienta **eficiente, escalable y replicable**, aplicable a otros contextos clínicos.
    """)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #56ab2f, #a8e6cf);
                padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
        <h3>🏆 Conclusión General</h3>
        <p>La automatización mediante IA mejora la eficiencia y estandarización en la gestión clínica, integrándose como soporte estratégico a la toma de decisiones en cuidados paliativos.</p>
    </div>
    """, unsafe_allow_html=True)

elif seccion == "📥 Descargas":
    st.markdown("### 📥 Descarga del Póster Completo")

    col1, col2 = st.columns([2, 1])
    with col1:
        file_path = os.path.join(parent_dir, "assets", "[GONZALO ROJAS] 2 - Congreso Cuidados Paliativos 2025 T17.pptx.pdf")
        if os.path.exists(file_path):
            with open(file_path, "rb") as pdf_file:
                pdf_data = pdf_file.read()
            st.download_button(
                label="📄 Descargar Póster (PDF)",
                data=pdf_data,
                file_name="Asignacion_prestaciones_CCPP.pdf",
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
    # Vista previa del PDF
    # Mostrar vista previa del PDF en proporción 3:4 (vertical)
    if os.path.exists(file_path):
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
            <p style="color:#666; font-size:0.9rem; margin-top:0.5rem;">Vista previa del póster (3401×4534 px)</p>
        </div>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.warning("⚠️ No se encontró el archivo PDF para previsualizar.")
elif seccion == "📧 Contacto":
    st.markdown("### 📧 Contacto")

    st.markdown("""
    **M.Sc. (C) Gonzalo Rojas Bernard**  
    Hyperautomation Engineer – Healthtracker Analytics  
    Ingeniero Civil Biomédico, MSc (C) Ciencias de Datos para la Innovación – Universidad de Concepción  
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
                success, msg = enviar_correo(nombre, email, asunto, mensaje, "Asignación Automática de Prestaciones IA CCPP")
            if success:
                st.success("✅ " + msg)
                st.info("📧 Tu mensaje ha sido enviado. Te contactaremos pronto.")
                st.balloons()
            else:
                st.error("❌ " + msg)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🧩 Asignación automática de prestaciones en cuidados paliativos |
    Health Tracker Analytics • Atención Domiciliaria • Chile</p>
</div>
""", unsafe_allow_html=True)
