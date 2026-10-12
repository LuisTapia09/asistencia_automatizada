# 📸 Sistema de Asistencia Automatizada con Reconocimiento Facial

Este proyecto implementa un sistema automatizado de control de asistencia en tiempo real utilizando Visión por Computadora e Inteligencia Artificial. Identifica a las personas mediante su rostro a través de una cámara web, registra su hora de entrada y evita registros duplicados en un historial estructurado en CSV.

---

## 🚀 Características Principales

* **Detección y Reconocimiento Facial:** Motor basado en `DeepFace` y `OpenCV`.
* **Registro de Asistencia:** Almacenamiento continuo en archivos `.csv` mediante `Pandas`.
* **Interfaz Web:** Panel interactivo en vivo construido con `Flask`.
* **Prevención de Duplicados:** Lógica de control para no registrar múltiples veces a la misma persona el mismo día.

---

## 🛠️ Requisitos Previos e Instalación

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd TU_REPOSITORIO
```

### 2. Crear y activar el entorno virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## 📁 Estructura del Dataset

Para agregar nuevos alumnos o empleados al sistema, coloca sus fotografías dentro de la carpeta `dataset/` siguiendo este formato:

```text
dataset/
├── Nombre_Apellido1/
│   ├── foto_1.jpg
│   └── foto_2.jpg
└── Sergio_Perez/
    ├── foto_1.jpg
    └── foto_2.jpg
```

---

## 💻 Ejecución del Proyecto

1. **Poblado inicial del dataset (Opcional):**
   ```bash
   python3 preparar_dataset.py
   ```

2. **Iniciar el servidor del sistema de asistencia:**
   ```bash
   python3 app.py
   ```

3. Abre tu navegador web y entra a: `http://127.0.0.1:5000`

---

## 🔒 Nota de Privacidad y Ética Biométrica

Este proyecto ha sido desarrollado estrictamente con **fines académicos e ilustrativos**. Las fotografías almacenadas en la carpeta de pruebas pertenecen a figuras públicas o bancos de imágenes con licencia libre, utilizadas bajo el consentimiento explícito de las partes para pruebas de concepto en visión artificial.