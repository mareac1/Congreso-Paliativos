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

def enviar_correo(nombre, email, asunto, mensaje, origen_pagina="Agendamiento Automatizado IA CCPP"):
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

elif seccion == "🎯 Objetivo y Desarrollo":
    st.markdown("### 🎯 Objetivo y Desarrollo de la Experiencia")

    st.markdown("""
    #### 🎯 Objetivo
    Desarrollar e implementar un **sistema automatizado de agendamiento** que combine criterios clínicos y administrativos, 
    garantizando la compatibilidad entre **necesidades de los pacientes** y **cobertura del equipo profesional**, 
    optimizando tiempos y recursos en la gestión asistencial.

    #### 🧩 Desarrollo
    - Se diseñó una **estrategia de gestión clínica** que combina estabilidad del paciente, necesidades especializadas, 
      soporte familiar y grado de dependencia.  
    - Con base en estos perfiles se definieron **frecuencias de visita** que, junto con los criterios administrativos, 
      permiten mantener la compatibilidad entre **demanda y cobertura**.  
    - El sistema híbrido combina **visitas programadas y por demanda**, revisando activamente el cumplimiento y 
      **reprogramando** cuando es necesario.  
    - Implementación gradual desde **2022**, con progresiva automatización y consolidación de procesos.
    """)

elif seccion == "📊 Resultados":
    st.markdown("### 📊 Resultados Principales")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        #### 📈 Principales hallazgos
        - La automatización alcanzó un promedio del **70%** de las atenciones durante 2025.  
        - En **agosto 2025** el sistema logró **90% de automatización**.  
        - El tiempo promedio de gestión por atención se redujo de **90 segundos (manual)** 
          a **1 segundo (automático)**.  
        - Se fortaleció la coordinación con especialistas mediante un protocolo de revisión eficiente.  
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #11998e, #38ef7d);
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>🎯 Resultados Clave</h3>
            <hr style="border-color:white;">
            <h4>⚙️ 90% automatización alcanzada</h4>
            <h4>⏱️ Reducción de 90s → 1s por atención</h4>
            <h4>📅 Reprogramación inteligente</h4>
            <h4>👥 Coordinación clínica optimizada</h4>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "💡 Conclusiones":
    st.markdown("### 💡 Conclusiones")

    st.markdown("""
    - La implementación de un sistema de **agendamiento automatizado** permite equilibrar de forma eficiente las 
      **necesidades asistenciales** con la disponibilidad de recursos.  
    - Es altamente recomendable en contextos de **salud mixta**, como el chileno, por su capacidad de respuesta ágil.  
    - La capacitación de los equipos en **herramientas digitales y criterios estandarizados** es clave para sostener la calidad.  
    - La estrategia optimiza recursos y **potencia la equidad, calidad y humanización** de la atención paliativa.  
    """)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #56ab2f, #a8e6cf);
                padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
        <h3>🏆 Conclusión General</h3>
        <p>El agendamiento automatizado fortalece la eficiencia, equidad y calidad de la atención paliativa, 
        permitiendo un uso más humano y estratégico del tiempo de los profesionales.</p>
    </div>
    """, unsafe_allow_html=True)

elif seccion == "📥 Descargas":
    st.markdown("### 📥 Descarga y Vista Previa del Póster")

    file_path = os.path.join(parent_dir, "assets", "[THOMAS SCHADE] 1 - Congreso Cuidados Paliativos 2025 T21.pptx.pdf")
    if os.path.exists(file_path):
        with open(file_path, "rb") as pdf_file:
            pdf_data = pdf_file.read()
        st.download_button(
            label="📄 Descargar Póster (PDF)",
            data=pdf_data,
            file_name="Agendamiento_IA.pdf",
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
                success, msg = enviar_correo(nombre, email, asunto, mensaje, "Agendamiento Automatizado IA CCPP")
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
