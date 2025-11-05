
import streamlit as st
import os

# Configuración de la página principal
st.set_page_config(
    page_title="Congresos Cuidados Paliativos",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar la navegación
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #3a6ccaff, #3a6ccaff);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }

    .navigation-card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
        border-left: 5px solid #3a3cb0;
    }

    .nav-button {
        display: inline-block;
        padding: 12px 24px;
        background-color: #4CAF50;
        color: white;
        text-decoration: none;
        border-radius: 6px;
        font-weight: bold;
        margin: 10px 5px;
        transition: background-color 0.3s;
    }

    .nav-button:hover {
        background-color: #3a3cb0;
        color: white;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown("""
<div class="main-header">
    <h1>🏥 Congresos de Cuidados Paliativos</h1>
    <h3>Presentaciones Académicas</h3>
</div>
""", unsafe_allow_html=True)

# Función para obtener la URL base
def get_base_url():
    """Obtiene la URL base dependiendo del entorno"""
    if 'STREAMLIT_SERVER_PORT' in os.environ:
        # En producción (Streamlit Cloud)
        return ""
    else:
        # En desarrollo local
        return "http://localhost:8501"

# Navegación principal
st.markdown("## 📋 Selecciona una presentación:")

# Primera fila
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="navigation-card">
        <h3>🧠 IA para la gestión de inasistencias</h3>
        <p>Uso de inteligencia artificial para anticipar y gestionar inasistencias de pacientes
        paliativos, optimizando los recursos clínicos.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🤖 Ver Gestión de Inasistencias", key="inasistencias_button", use_container_width=True):
        st.switch_page("pages/Gestion_inasistencias_IA.py")

with col2:
    st.markdown("""
    <div class="navigation-card">
        <h3>📦 Detección temprana de necesidad de insumos</h3>
        <p>Sistema automatizado con IA para identificar la necesidad de insumos clínicos
        en cuidados paliativos domiciliarios.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📦 Ver Sistema de Insumos", key="insumos_button", use_container_width=True):
        st.switch_page("pages/Deteccion_insumos_IA.py")

with col3:
    st.markdown("""
    <div class="navigation-card">
        <h3>🧩 Asignación automática de prestaciones</h3>
        <p>Algoritmo de IA que identifica y asigna automáticamente prestaciones paquetizadas
        en pacientes paliativos domiciliarios.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🧾 Ver Asignación Automática", key="prestaciones_button", use_container_width=True):
        st.switch_page("pages/Asignacion_prestaciones_CCPP.py")


# Segunda fila
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="navigation-card">
        <h3>📉 Identificación de pacientes críticos (RFM)</h3>
        <p>Modelo predictivo basado en Recencia, Frecuencia y Monto de consumo
        para priorizar pacientes críticos en cuidados paliativos.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📊 Ver Modelo RFM", key="rfm_button", use_container_width=True):
        st.switch_page("pages/Pacientes_criticos_RFM.py")

with col5:
    st.markdown("""
    <div class="navigation-card">
        <h3>🩺 IA para detección temprana de necesidades paliativas</h3>
        <p>Uso combinado de informes médicos y validación profesional
        para mejorar la detección temprana de necesidades paliativas.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🩺 Ver Detección por Informe", key="necesidades_button", use_container_width=True):
        st.switch_page("pages/Deteccion_necesidades_IA.py")

with col6:
    st.markdown("""
    <div class="navigation-card">
        <h3>📊 Estudio de brecha en Cuidados Paliativos</h3>
        <p>Análisis nacional de brechas en cobertura y demanda de cuidados paliativos
        en Chile, con enfoque en proyección de necesidades.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📊 Ver Brecha CCPP", key="brecha_button", use_container_width=True):
        st.switch_page("pages/Brecha_CCPP_Chile.py")


# Tercera fila
col7, col8, col9 = st.columns(3)

with col7:
    st.markdown("""
    <div class="navigation-card">
        <h3>📬 Extracción de información clínica desde correos</h3>
        <p>Automatización mediante IA para extraer información clínica estructurada
        desde correos electrónicos en cuidados paliativos.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📬 Ver Extracción desde Correos", key="correos_button", use_container_width=True):
        st.switch_page("pages/Extraccion_correos_IA.py")

with col8:
    st.markdown("""
    <div class="navigation-card">
        <h3>📅 Agendamiento automatizado de visitas</h3>
        <p>Sistema automatizado para la asignación inteligente de visitas domiciliarias
        de profesionales en cuidados paliativos.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📅 Ver Agendamiento Automático", key="agenda_button", use_container_width=True):
        st.switch_page("pages/Agendamiento_IA.py")

with col9:
    st.markdown("""
    <div class="navigation-card">
        <h3>⚖️ Ley N° 21.719 y protección de datos</h3>
        <p>Aplicación práctica de la Ley de Protección de Datos Personales
        en registros de Cuidados Paliativos.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("⚖️ Ver Aplicación de la Ley", key="ley_button", use_container_width=True):
        st.switch_page("pages/Ley_Proteccion_Datos_CCPP.py")


# Información adicional
# st.markdown("---")
# st.markdown("""
# ### ℹ️ Información Adicional

# Esta aplicación presenta tres investigaciones desarrolladas por Red Salud en el ámbito de los cuidados paliativos:

# 1. **Detección Temprana mediante IA**: Utiliza tecnologías de inteligencia artificial para mejorar la identificación temprana de pacientes que requieren cuidados paliativos.

# 2. **Modelo Institucional de Formación**: Presenta la experiencia y metodología desarrollada para la formación continua del personal sanitario en cuidados paliativos.

# 3. **Estrategia de Mitigación del Burnout**: Implementación de un plan sistemático para la detección precoz y mitigación del síndrome de burnout en equipos de cuidados paliativos domiciliarios.

# Todas las presentaciones incluyen material descargable y códigos QR para facilitar el acceso a los recursos.
# """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>Congresos de Cuidados Paliativos</p>
    <p>Desarrollado para facilitar el acceso a presentaciones académicas</p>
</div>
""", unsafe_allow_html=True)

