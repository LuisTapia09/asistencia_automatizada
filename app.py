import base64
import os
from pathlib import Path
from flask import Flask, render_template, jsonify, request
from deepface import DeepFace
from base_datos import registrar_asistencia, obtener_asistencias_hoy

app = Flask(__name__)

DATASET = Path("dataset")
TEMP_IMG_PATH = "temp_frame.jpg"

@app.route("/")
def index():
    """Renderiza la página principal con la interfaz web."""
    return render_template("index.html")

@app.route("/api/asistencias", methods=["GET"])
def get_asistencias():
    """Devuelve la lista de asistencias registradas el día de hoy en formato JSON."""
    df = obtener_asistencias_hoy()
    datos = df.to_dict(orient="records")
    return jsonify(datos)

@app.route("/procesar_frame", methods=["POST"])
def procesar_frame():
    """Recibe un fotograma en Base64 desde el navegador y realiza el reconocimiento facial."""
    try:
        data = request.get_json()
        image_data = data.get("image")

        if not image_data:
            return jsonify({"status": "error", "message": "No se recibió imagen"}), 400

        # Separar el encabezado de Base64 ("data:image/jpeg;base64,...") y decodificar los datos
        header, encoded = image_data.split(",", 1)
        binary_data = base64.b64decode(encoded)

        # Guardar la imagen temporalmente para enviarla a DeepFace
        with open(TEMP_IMG_PATH, "wb") as f:
            f.write(binary_data)

        # Evaluar el fotograma guardado contra el dataset
        resultados = DeepFace.find(
            img_path=TEMP_IMG_PATH,
            db_path=str(DATASET),
            model_name="Facenet512",
            detector_backend="ssd",
            distance_metric="cosine",
            enforce_detection=True
        )

        if len(resultados) > 0 and not resultados[0].empty:
            coincidencia = resultados[0].iloc[0]
            identidad = coincidencia["identity"]
            distancia = float(coincidencia["distance"])
            
            nombre = os.path.basename(os.path.dirname(identidad))
            se_registro = registrar_asistencia(nombre)

            return jsonify({
                "status": "success",
                "nombre": nombre,
                "distancia": round(distancia, 4),
                "se_registro": se_registro
            })
        else:
            return jsonify({"status": "no_match", "nombre": "Desconocido"})

    except Exception as e:
        # Excepción capturada si no se detecta ningún rostro en el fotograma
        return jsonify({"status": "no_face", "message": "No se detectó rostro"})

    finally:
        # Eliminar el archivo temporal para mantener el proyecto limpio
        if os.path.exists(TEMP_IMG_PATH):
            os.remove(TEMP_IMG_PATH)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)