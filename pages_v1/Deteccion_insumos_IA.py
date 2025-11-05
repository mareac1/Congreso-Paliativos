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

def enviar_correo(nombre, email, asunto, mensaje, origen_pagina="Detección Temprana de Insumos IA CCPP"):
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
    page_title="Sistema automatizado con IA para detección temprana de necesidad de insumos",
    page_icon="📦",
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
    <h1>📦 Sistema automatizado con Inteligencia Artificial</h1>
    <h3>para detección temprana de necesidad de insumos en Cuidados Paliativos domiciliarios</h3>
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
        La atención domiciliaria en cuidados paliativos enfrenta el desafío de responder de manera oportuna a las necesidades cambiantes de los pacientes.  
        Una de las principales dificultades radica en la **identificación temprana de necesidad de insumos clínicos**, como material de curación, hidratación o administración subcutánea.  
        Su disponibilidad incide directamente en la **calidad de vida** y en la **continuidad del cuidado**.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #36d1dc, #5b86e5);
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
            <h3>📊 Datos Clave</h3>
            <h2>48%</h2>
            <p>Registros con necesidad potencial de insumos</p>
            <h2>4%</h2>
            <p>Casos validados y despachados efectivamente</p>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "🎯 Objetivo y Desarrollo":
    st.markdown("### 🎯 Objetivo y Desarrollo de la Experiencia")

    st.markdown("""
    #### 🎯 Objetivo
    Desarrollar e implementar un **sistema automatizado basado en inteligencia artificial** que permita detectar de manera temprana la necesidad de insumos clínicos en pacientes en cuidados paliativos domiciliarios, mediante el análisis estructurado de **registros de enfermería**, con el fin de **anticipar requerimientos**, **optimizar procesos de despacho** y **mejorar la continuidad del cuidado**.

    #### 🧩 Desarrollo
    1. **Extracción de datos:** identificación y estructuración de campos relevantes en los informes clínicos (síntomas, procedimientos, observaciones).
    2. **Procesamiento con IA:** análisis de textos con modelos de lenguaje natural (NLP) para detectar patrones de necesidad de insumos (apósitos, hidratación, material subcutáneo, etc.).
    3. **Envío a bandeja administrativa:** registros con alta probabilidad de requerir insumos son derivados automáticamente al equipo encargado para revisión y despacho.
    4. **Retroalimentación:** evaluación clínica de las detecciones y ajustes continuos para mejorar precisión.
    """)

elif seccion == "📊 Resultados":
    st.markdown("### 📊 Resultados Principales")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        #### 📈 Resultados Destacados
        - El sistema identificó necesidad potencial de insumos en el **48%** de los registros analizados.
        - El **4%** de los casos detectados fueron validados y despachados efectivamente.
        - Se observó un **alto número de falsos positivos**, lo cual permitió **priorizar revisión** de registros críticos.
        - La integración con la bandeja administrativa **redujo los tiempos de respuesta** y **mejoró la trazabilidad**.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #11998e, #38ef7d);
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>🎯 Resultados Clave</h3>
            <hr style="border-color:white;">
            <h4>🧠 48% con necesidad potencial</h4>
            <h4>✅ 4% validados y despachados</h4>
            <h4>📉 Reducción de tiempos de respuesta</h4>
            <h4>📦 Mejora en trazabilidad y eficiencia</h4>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "💡 Conclusiones":
    st.markdown("### 💡 Conclusiones")

    st.markdown("""
    La implementación del sistema automatizado con inteligencia artificial demostró que el análisis estructurado de los registros de enfermería permite **detectar tempranamente necesidades de insumos clínicos**.  
    Esto se traduce en:
    - **Optimización de la gestión de recursos.**
    - **Reducción de tiempos de despacho.**
    - **Fortalecimiento de la continuidad del cuidado.**
    - **Consolidación de la trazabilidad operativa.**
    """)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #56ab2f, #a8e6cf);
                padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
        <h3>🏆 Conclusión General</h3>
        <p>El uso de IA en la gestión de insumos clínicos representa un avance concreto hacia la automatización y sostenibilidad de los cuidados paliativos domiciliarios.</p>
    </div>
    """, unsafe_allow_html=True)

elif seccion == "📥 Descargas":
    st.markdown("### 📥 Descarga del Póster Completo")

    col1, col2 = st.columns([2, 1])
    with col1:
        file_path = os.path.join(parent_dir, "assets", "[GONZALO ROJAS] 1 - Congreso Cuidados Paliativos 2025 T19.pptx.pdf")
        if os.path.exists(file_path):
            with open(file_path, "rb") as pdf_file:
                pdf_data = pdf_file.read()
            st.download_button(
                label="📄 Descargar Póster (PDF)",
                data=pdf_data,
                file_name="Deteccion_temprana_insumos_IA.pdf",
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
                success, msg = enviar_correo(nombre, email, asunto, mensaje, "Detección Temprana de Insumos IA CCPP")
            if success:
                st.success("✅ " + msg)
                st.info("📧 Tu mensaje ha sido enviado. Te contactaremos pronto.")
                st.balloons()
            else:
                st.error("❌ " + msg)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>📦 Sistema automatizado con IA para detección de insumos |
    Health Tracker Analytics • Atención Domiciliaria • Chile</p>
</div>
""", unsafe_allow_html=True)
