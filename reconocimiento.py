import os
from pathlib import Path
from deepface import DeepFace

DATASET = Path("dataset")

def reconocer_persona(ruta_imagen):
    """
    Busca a quién pertenece una imagen dentro del dataset usando Facenet512 y SSD.
    """
    resultados = DeepFace.find(
        img_path=ruta_imagen,
        db_path=str(DATASET),
        model_name="Facenet512",
        detector_backend="ssd",
        distance_metric="cosine",
        enforce_detection=True
    )
    return resultados

if __name__ == "__main__":
    # Limpiamos caché binaria obsoleta
    os.system("rm -f dataset/*.pkl")

    imagenes_prueba = [
        "dataset/florence_pugh/foto2.jpg",
        "dataset/sergio_perez/foto2.jpg",
        "dataset/brad_pitt/foto2.jpg"
    ]

    for imagen in imagenes_prueba:
        print("\n==============================")
        print("Probando archivo de entrada:", imagen)
        print("==============================")

        try:
            resultados = reconocer_persona(imagen)

            if len(resultados) > 0 and not resultados[0].empty:
                coincidencia = resultados[0].iloc[0]
                identidad = coincidencia["identity"]
                distancia = coincidencia["distance"]
                
                # Extraer nombre del sujeto
                nombre_persona = os.path.basename(os.path.dirname(identidad))

                print(f"✅ Persona reconocida: {nombre_persona}")
                print(f"   └── Foto matched en dataset: {os.path.basename(identidad)}")
                print(f"   └── Distancia calculada:    {distancia:.4f}")
            else:
                print("❌ No se encontró ninguna coincidencia por debajo del umbral estricto.")

        except Exception as e:
            print("⚠️ Error en la evaluación:", e)