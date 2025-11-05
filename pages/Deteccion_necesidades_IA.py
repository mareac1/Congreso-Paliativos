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

def enviar_correo(nombre, email, asunto, mensaje, origen_pagina="Detección Temprana de Necesidades Paliativas IA CCPP"):
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
    page_title="IA para detección temprana de necesidades paliativas",
    page_icon="🩺",
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
    <h1>🩺 Inteligencia Artificial para detección temprana de necesidades paliativas</h1>
    <h3>basado en informe médico y validación profesional</h3>
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
        El acceso tardío a cuidados paliativos en pacientes oncológicos impacta negativamente su calidad de vida.  
        Detectar precozmente la necesidad de derivación es clave para mejorar la atención.  
        En Chile se estima una brecha del **58%** en cobertura de cuidados paliativos (67% en sistema público y 33% en privado).  
        Este proyecto aborda esa brecha mediante **una herramienta de IA generativa** capaz de detectar automáticamente 
        señales de derivación temprana a cuidados paliativos en informes oncológicos.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #36d1dc, #5b86e5);
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
            <h3>📊 Datos Clave</h3>
            <h2>4099</h2>
            <p>Informes clínicos analizados</p>
            <h2>821</h2>
            <p>Casos con necesidad potencial de cuidados paliativos</p>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "🎯 Objetivo y Desarrollo":
    st.markdown("### 🎯 Objetivo y Desarrollo de la Experiencia")

    st.markdown("""
    #### 🎯 Objetivo
    Desarrollar y pilotar una **herramienta de apoyo clínico** que identifique automáticamente, 
    a partir de informes de comité oncológico, la indicación o señales de riesgo que justifiquen 
    una derivación temprana a cuidados paliativos.

    #### 🧩 Desarrollo
    - Se analizaron informes clínicos de comités oncológicos, previamente anonimizados, mediante **modelos de lenguaje avanzado (Gemini 2.0 Flash)**.  
    - El sistema fue entrenado para detectar **12 criterios clínicos** definidos por expertos (síntomas severos, metástasis cerebrales, crisis existencial, cáncer avanzado, etc.).  
    - Los casos detectados son derivados a una **bandeja digital** donde el equipo de enfermería valida y coordina la derivación médica.  
    - Este flujo incorpora validación humana (*human-in-the-loop*) que garantiza control clínico, corrección de errores y retroalimentación continua al modelo.
    """)

elif seccion == "📊 Resultados":
    st.markdown("### 📊 Resultados Principales")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        #### 📈 Resultados Preliminares
        - **4.099 informes clínicos** procesados.  
        - **821 casos (20.0%)** con posible necesidad de cuidados paliativos.  
        - Promedio de **1.3 criterios detectados por caso**:
            - 472 casos (11.5%): 1 criterio  
            - 270 casos (6.5%): 2 criterios  
            - 60 casos (1.4%): 3–5 criterios  
        - Alta concordancia entre el modelo de IA y el juicio experto.  
        - Reducción del tiempo de revisión y generación de alertas útiles para gestión de pacientes.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #11998e, #38ef7d);
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>🎯 Resultados Clave</h3>
            <hr style="border-color:white;">
            <h4>🤖 12 criterios clínicos definidos</h4>
            <h4>📈 20% de pacientes con señales tempranas</h4>
            <h4>💬 Validación “human-in-the-loop”</h4>
            <h4>⏱️ Reducción de tiempo de revisión</h4>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "💡 Conclusiones":
    st.markdown("### 💡 Conclusiones")

    st.markdown("""
    - La combinación de **IA generativa y validación profesional** permite identificar precozmente 
      necesidades de cuidados paliativos.  
    - Este modelo contribuye a la **equidad en el acceso** y mejora la continuidad del cuidado clínico.  
    - Favorece la toma de decisiones informadas y la **optimización del flujo asistencial**.  
    - La estrategia es **escalable y transferible** a distintos niveles de atención.  
    """)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #56ab2f, #a8e6cf);
                padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
        <h3>🏆 Conclusión General</h3>
        <p>Integrar IA en la detección temprana de necesidades paliativas mejora la oportunidad de atención,
        reduce la carga administrativa y fortalece la toma de decisiones clínicas basadas en datos.</p>
    </div>
    """, unsafe_allow_html=True)

elif seccion == "📥 Descargas":
    st.markdown("### 📥 Descarga y Vista Previa del Póster")

    file_path = os.path.join(parent_dir, "assets", "[JAIME JIMENEZ] 1 - Congreso Cuidados Paliativos - T18.pptx.pdf")
    if os.path.exists(file_path):
        with open(file_path, "rb") as pdf_file:
            pdf_data = pdf_file.read()
        st.download_button(
            label="📄 Descargar Póster (PDF)",
            data=pdf_data,
            file_name="Deteccion_necesidades_IA.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        # Vista previa en proporción 3:4
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
    **M.Sc. Jaime Jiménez Ruiz**  
    Co-Founder & CTO – Healthtracker Analytics  
    Ingeniero Civil Biomédico, Mg. Ingeniería Eléctrica – Universidad de Concepción  
    Magíster en Inteligencia Artificial – Pontificia Universidad Católica de Chile  
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
                success, msg = enviar_correo(nombre, email, asunto, mensaje, "Detección Temprana de Necesidades Paliativas IA CCPP")
            if success:
                st.success("✅ " + msg)
                st.info("📧 Tu mensaje ha sido enviado. Te contactaremos pronto.")
                st.balloons()
            else:
                st.error("❌ " + msg)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🩺 Detección temprana de necesidades paliativas | Health Tracker Analytics • RedSalud • Atención Domiciliaria • Chile</p>
</div>
""", unsafe_allow_html=True)
