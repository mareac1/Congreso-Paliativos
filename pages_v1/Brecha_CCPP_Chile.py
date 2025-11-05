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

def enviar_correo(nombre, email, asunto, mensaje, origen_pagina="Brecha Cuidados Paliativos Chile"):
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
    page_title="Brecha de Cuidados Paliativos en Chile",
    page_icon="📊",
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
    <h1>📊 Estudio sobre la brecha en Cuidados Paliativos en Chile</h1>
    <h3>e identificación de Mayor Demanda</h3>
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
        Chile enfrenta un doble desafío en salud pública:  
        una **transición epidemiológica avanzada** con envejecimiento poblacional acelerado 
        y aumento de **enfermedades crónicas no transmisibles (ECNT)**, junto con la implementación 
        de la **Ley N° 21.375 de Cuidados Paliativos Universales**.  
        
        Este estudio aborda la magnitud y distribución territorial de la **brecha en la provisión de cuidados paliativos**, 
        identificando regiones y comunas con **mayor demanda no cubierta**.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #43cea2, #185a9d);
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
            <h3>📈 Datos Clave</h3>
            <h2>1997–2025</h2>
            <p>Período analizado en bases de defunciones</p>
            <h2>20</h2>
            <p>Condiciones de salud incluidas en el modelo</p>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "🎯 Objetivo y Desarrollo":
    st.markdown("### 🎯 Objetivo y Desarrollo de la Experiencia")

    st.markdown("""
    #### 🎯 Objetivo
    Determinar la magnitud de la **brecha en la provisión de cuidados paliativos** en Chile, 
    identificando y visibilizando las desigualdades territoriales (comunas y regiones) con mayor demanda mediante 
    el análisis estadístico de **datos de defunciones** y variables sociodemográficas.

    #### 🧩 Desarrollo
    - **Etapa 1:** Recopilación y preprocesamiento de datos de defunciones (MINSAL), demografía (CENSO 2017 – INE) y CASEN 2022.  
    - **Etapa 2:** Diseño del índice compuesto “Necesidad Cuidados”, integrando prevalencia de 20 condiciones, tasas de mortalidad y factores de vulnerabilidad.  
    - **Etapa 3:** Implementación de **K-means** para segmentar comunas según perfiles de necesidad y desarrollo de un **dashboard interactivo en Python** para apoyo a la decisión.
    """)

elif seccion == "📊 Resultados":
    st.markdown("### 📊 Resultados Principales")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        #### 📈 Principales Hallazgos
        - Se observó **correlación positiva** entre población mayor (EDAD_CANT) y necesidad de CCPP.  
        - El análisis de **agrupamiento K-means (K=4)** identificó cuatro grupos de comunas según su nivel de necesidad.  
        - El **“Clúster 3”** (Alta Necesidad y Alta Edad) representa el grupo de **máxima prioridad** para la política pública.  
        - Este grupo concentra comunas con **“triple vulnerabilidad”**: alta carga epidemiológica, pobreza y barreras de acceso.  
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #11998e, #38ef7d);
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>🎯 Resultados Clave</h3>
            <hr style="border-color:white;">
            <h4>🧬 K=4 grupos de comunas</h4>
            <h4>📊 Alta necesidad en comunas vulnerables</h4>
            <h4>📍 Clúster 3: prioridad nacional</h4>
            <h4>🧩 Dashboard Python interactivo</h4>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "💡 Conclusiones":
    st.markdown("### 💡 Conclusiones")

    st.markdown("""
    - La brecha en cuidados paliativos en Chile **no es uniforme**; se concentra en comunas con mayor vulnerabilidad social.  
    - La **edad avanzada y la pobreza** emergen como determinantes clave de necesidad de cuidados.  
    - El enfoque territorial propuesto permite priorizar recursos y orientar políticas públicas hacia zonas de alta necesidad.  
    - La integración de **análisis geoespacial y machine learning** favorece la toma de decisiones basadas en evidencia.  
    """)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #56ab2f, #a8e6cf);
                padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
        <h3>🏆 Conclusión General</h3>
        <p>El análisis territorial y predictivo de la brecha en cuidados paliativos contribuye 
        a la equidad sanitaria, priorizando la atención en las comunas con mayor vulnerabilidad y menor cobertura.</p>
    </div>
    """, unsafe_allow_html=True)

elif seccion == "📥 Descargas":
    st.markdown("### 📥 Descarga y Vista Previa del Póster")

    file_path = os.path.join(parent_dir, "assets", "[JOAN RETAMALES] Plantilla Póster - Congreso Cuidados Paliativos 2025.pptx.pdf")
    if os.path.exists(file_path):
        with open(file_path, "rb") as pdf_file:
            pdf_data = pdf_file.read()
        st.download_button(
            label="📄 Descargar Póster (PDF)",
            data=pdf_data,
            file_name="Brecha_CCPP_Chile.pdf",
            mime="application/pdf",
            use_container_width=True
        )

        # Vista previa en proporción 3:4 (vertical)
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
    **Ing. Joan Retamales Moya**  
    Ingeniero Civil en Ciencia de Datos – Universidad Tecnológica Metropolitana  
    Colaborador en Healthtracker Analytics y Atención Domiciliaria  
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
                success, msg = enviar_correo(nombre, email, asunto, mensaje, "Brecha Cuidados Paliativos Chile")
            if success:
                st.success("✅ " + msg)
                st.info("📧 Tu mensaje ha sido enviado. Te contactaremos pronto.")
                st.balloons()
            else:
                st.error("❌ " + msg)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>📊 Estudio sobre la brecha en Cuidados Paliativos en Chile |
    Health Tracker Analytics • Atención Domiciliaria • Chile</p>
</div>
""", unsafe_allow_html=True)
