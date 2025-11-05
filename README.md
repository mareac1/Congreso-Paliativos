# Aplicación Streamlit Multi-Página - Congresos Cuidados Paliativos

Esta aplicación combina dos interfaces de Streamlit en una sola aplicación multi-página, permitiendo acceso a través de diferentes rutas URL.

## Estructura del Proyecto

```
streamlit_app/
├── main.py                 # Página principal con navegación
├── requirements.txt        # Dependencias del proyecto
├── pages/                  # Páginas de la aplicación
│   ├── deteccion_temprana_ia.py    # Página sobre IA en CCPP
│   └── modelo_institucional.py     # Página sobre modelo formativo
├── utils/                  # Utilidades comunes
│   └── common.py          # Funciones compartidas
└── assets/                 # Recursos (PDFs, imágenes, etc.)
```

## Características Principales

### 🏠 Página Principal (`main.py`)
- Navegación central hacia las dos presentaciones
- Información general del proyecto
- Enlaces a las páginas específicas

### 🤖 Detección Temprana IA (`pages/deteccion_temprana_ia.py`)
- Investigación sobre IA generativa en cuidados paliativos
- Análisis de informes oncológicos con NLP
- Resultados del piloto con 4,099 informes

### 📚 Modelo Institucional (`pages/modelo_institucional.py`)
- Experiencia de formación continua en CCPP
- Tres ejes estratégicos del modelo formativo
- Resultados y proyecciones del programa

## URLs de Acceso

### Desarrollo Local
```
http://localhost:8501/                    # Página principal
http://localhost:8501/deteccion_temprana_ia    # IA en CCPP
http://localhost:8501/modelo_institucional     # Modelo formativo
```

### Producción (Streamlit Community Cloud)
```
https://tu-app.streamlit.app/                         # Página principal
https://tu-app.streamlit.app/deteccion_temprana_ia    # IA en CCPP
https://tu-app.streamlit.app/modelo_institucional     # Modelo formativo
```

## Instalación y Ejecución

### 1. Clonar y navegar al directorio
```bash
cd streamlit_app
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación
```bash
streamlit run main.py
```

## Deployment en Streamlit Community Cloud

### 1. Configuración en GitHub
- Subir el directorio `streamlit_app` a un repositorio de GitHub
- Asegurar que `main.py` esté en la raíz del directorio

### 2. Conectar con Streamlit Cloud
- Ir a [share.streamlit.io](https://share.streamlit.io)
- Conectar con GitHub y seleccionar el repositorio
- Configurar:
  - **Repository**: tu-usuario/tu-repositorio
  - **Branch**: main
  - **Main file path**: streamlit_app/main.py

### 3. Variables de Entorno (Opcional)
Si necesitas configurar variables de entorno, agregar en Streamlit Cloud:
```
STREAMLIT_SERVER_PORT=8501
```

## Deployment en Google Cloud Run

### 1. Crear Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 2. Construir y desplegar
```bash
# Construir imagen
docker build -t streamlit-congresos .

# Etiquetar para Google Cloud
docker tag streamlit-congresos gcr.io/[PROJECT-ID]/streamlit-congresos

# Subir a Container Registry
docker push gcr.io/[PROJECT-ID]/streamlit-congresos

# Desplegar en Cloud Run
gcloud run deploy streamlit-congresos \
  --image gcr.io/[PROJECT-ID]/streamlit-congresos \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## Características Técnicas

### Navegación Multi-Página
- Usa `st.switch_page()` para navegación entre páginas
- Sidebar con botón "Volver al Inicio" en cada página
- URLs limpias para acceso directo

### Funcionalidades Compartidas
- Generación de códigos QR
- Formularios de contacto
- Descarga de documentos
- Estilos CSS consistentes

### Responsivo y Accesible
- Diseño adaptable a móviles
- Navegación intuitiva
- Estilos CSS optimizados

## Archivos de Recursos

Para incluir PDFs u otros recursos:
1. Colocar archivos en la carpeta `assets/`
2. Usar la función `get_asset_path()` de `utils/common.py`
3. Actualizar las rutas en las páginas según sea necesario

## Contacto y Soporte

Para consultas sobre la aplicación:
- **Email**: fmartinez@atenciondomiciliaria.cl
- **Instituciones**: Atención Domiciliaria, Instituto del Cáncer RedSalud, Health Tracker Analytics

## Licencia

© 2024 Red Salud - Congresos de Cuidados Paliativos
