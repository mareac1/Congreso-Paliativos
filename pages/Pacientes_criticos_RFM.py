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

def enviar_correo(nombre, email, asunto, mensaje, origen_pagina="Pacientes Críticos RFM CCPP"):
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
    page_title="Identificación de pacientes críticos en Cuidados Paliativos",
    page_icon="📉",
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
    <h1>📉 Identificación de pacientes críticos en Cuidados Paliativos</h1>
    <h3>basado en su Recencia, Frecuencia y Monto de consumo</h3>
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
        El modelo **RFM (Recencia, Frecuencia y Monto de consumo)** permite segmentar pacientes según:
        - **Recencia:** tiempo desde la última atención registrada.  
        - **Frecuencia:** número de atenciones en un período definido.  
        - **Monto:** nivel de recursos clínicos y logísticos utilizados.  
        
        Adaptado al ámbito de la salud, este enfoque facilita **identificar pacientes críticos**, 
        priorizar intervenciones y optimizar la planificación del cuidado, fortaleciendo la continuidad 
        y eficiencia del servicio asistencial.
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #36d1dc, #5b86e5);
                    padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
            <h3>📊 Datos Clave</h3>
            <h2>4 grupos</h2>
            <p>Clasificación RFM de pacientes</p>
            <h2>2 clústeres críticos</h2>
            <p>Grupos 1 y 2: mayor riesgo</p>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "🎯 Objetivo y Desarrollo":
    st.markdown("### 🎯 Objetivo y Desarrollo de la Experiencia")

    st.markdown("""
    #### 🎯 Objetivo
    Aplicar el modelo **RFM (Recencia, Frecuencia y Monto de consumo)** al contexto de cuidados paliativos domiciliarios, 
    para **identificar pacientes críticos**, priorizar su seguimiento clínico y optimizar la asignación de recursos asistenciales.

    #### 🧩 Desarrollo
    1. **Selección de variables:** se definieron tres indicadores principales (Recencia, Frecuencia y Monto).  
    2. **Procesamiento de datos:** se estandarizaron registros y se aplicó un algoritmo no supervisado de segmentación, adaptado al contexto clínico.  
    3. **Identificación de grupos:** el modelo clasificó pacientes en **4 grupos** según riesgo, adherencia y consumo de recursos.  
    4. **Visualización:** integración en un panel interactivo en **Looker Studio**, mostrando distribución, evolución y vista individual por paciente.
    """)

elif seccion == "📊 Resultados":
    st.markdown("### 📊 Resultados Principales")

    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        #### 📈 Grupos identificados
        - **Grupo 1:** bajo contacto y escasa frecuencia de atenciones → alto riesgo de abandono.  
        - **Grupo 2:** alta frecuencia e inestabilidad → requiere monitoreo intensivo.  
        - **Grupo 3:** seguimiento adecuado y adherencia estable.  
        - **Grupo 4:** adherencia óptima, buena estabilidad clínica y bajo uso de recursos.  

        Esta clasificación permite priorizar el seguimiento de pacientes más vulnerables (clústeres 1 y 2) 
        y reconocer buenas prácticas en los grupos de mejor desempeño (3 y 4).  
        """)
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #11998e, #38ef7d);
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <h3>🎯 Resultados Clave</h3>
            <hr style="border-color:white;">
            <h4>🧠 Clasificación RFM aplicada al ámbito clínico</h4>
            <h4>🔍 Identificación de pacientes críticos</h4>
            <h4>📊 Integración en panel Looker Studio</h4>
            <h4>🤝 Mejora en priorización y eficiencia</h4>
        </div>
        """, unsafe_allow_html=True)

elif seccion == "💡 Conclusiones":
    st.markdown("### 💡 Conclusiones")

    st.markdown("""
    - La aplicación del modelo **RFM** en cuidados paliativos domiciliarios permite segmentar y priorizar pacientes según su comportamiento clínico y uso de recursos.  
    - Promueve una **gestión proactiva y basada en datos**, mejorando la continuidad y calidad del cuidado.  
    - Permite **reconocer patrones de riesgo**, fortalecer la toma de decisiones y destacar buenas prácticas.  
    - Favorece la integración entre equipos clínicos y analíticos mediante herramientas digitales.  
    """)

    st.markdown("""
    <div style="background: linear-gradient(135deg, #56ab2f, #a8e6cf);
                padding: 1.5rem; border-radius: 15px; color: white; text-align: center;">
        <h3>🏆 Conclusión General</h3>
        <p>El modelo RFM fortalece la gestión clínica en cuidados paliativos, integrando analítica avanzada 
        y segmentación automatizada para mejorar la continuidad y eficiencia del cuidado.</p>
    </div>
    """, unsafe_allow_html=True)

elif seccion == "📥 Descargas":
    st.markdown("### 📥 Descarga y Vista Previa del Póster")

    file_path = os.path.join(parent_dir, "assets", "[GONZALO ROJAS] 3 - Congreso Cuidados Paliativos 2025 T24.pptx.pdf")
    if os.path.exists(file_path):
        with open(file_path, "rb") as pdf_file:
            pdf_data = pdf_file.read()
        st.download_button(
            label="📄 Descargar Póster (PDF)",
            data=pdf_data,
            file_name="Pacientes_Criticos_RFM.pdf",
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
                success, msg = enviar_correo(nombre, email, asunto, mensaje, "Pacientes Críticos RFM CCPP")
            if success:
                st.success("✅ " + msg)
                st.info("📧 Tu mensaje ha sido enviado. Te contactaremos pronto.")
                st.balloons()
            else:
                st.error("❌ " + msg)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>📉 Identificación de pacientes críticos en cuidados paliativos |
    Health Tracker Analytics • Atención Domiciliaria • Chile</p>
</div>
""", unsafe_allow_html=True)
