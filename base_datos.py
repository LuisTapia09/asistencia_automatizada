import os
import pandas as pd
from datetime import datetime

# Archivo CSV donde se guardarán los registros
ARCHIVO_CSV = "asistencia.csv"

def inicializar_csv():
    """Crea el archivo CSV con las columnas correspondientes si no existe."""
    if not os.path.exists(ARCHIVO_CSV):
        df = pd.DataFrame(columns=["Nombre", "Fecha", "Hora"])
        df.to_csv(ARCHIVO_CSV, index=False)
        print(f"📄 Archivo '{ARCHIVO_CSV}' creado exitosamente.")

def registrar_asistencia(nombre):
    """
    Registra a una persona con la fecha y hora actual en el archivo CSV.
    Retorna True si registró una nueva asistencia, o False si ya estaba registrada hoy.
    """
    inicializar_csv()

    ahora = datetime.now()
    fecha_actual = ahora.strftime("%Y-%m-%d")
    hora_actual = ahora.strftime("%H:%M:%S")

    # Leer las asistencias registradas hasta el momento
    df = pd.read_csv(ARCHIVO_CSV)

    # Verificar si la persona YA registró asistencia el día de hoy
    ya_registrado = not df[(df["Nombre"] == nombre) & (df["Fecha"] == fecha_actual)].empty

    if not ya_registrado:
        # Crear la nueva fila de asistencia
        nueva_asistencia = pd.DataFrame([{
            "Nombre": nombre,
            "Fecha": fecha_actual,
            "Hora": hora_actual
        }])

        # Concatenar la nueva fila y guardar en el CSV
        df = pd.concat([df, nueva_asistencia], ignore_index=False)
        df.to_csv(ARCHIVO_CSV, index=False)
        print(f"✅ Asistencia registrada: {nombre} a las {hora_actual}")
        return True
    else:
        # Ya está registrado, omitimos para evitar duplicados
        return False

def obtener_asistencias_hoy():
    """Devuelve un DataFrame de Pandas con las asistencias registradas el día de hoy."""
    inicializar_csv()
    df = pd.read_csv(ARCHIVO_CSV)
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    return df[df["Fecha"] == fecha_actual]

if __name__ == "__main__":
    # Prueba rápida del módulo de base de datos
    print("--- Probando sistema de registro CSV ---")
    registrar_asistencia("Sergio_Perez")
    
    # Intento de duplicado (debería indicarnos que ya fue registrado)
    registrar_asistencia("Sergio_Perez")
    
    print("\nRegistros de hoy:")
    print(obtener_asistencias_hoy())