import pandas as pd

sesiones = [
    {"dia": "Lunes", "ejercicios": "Piernas", "duracion_min": 60, "calorias": 450},
    {"dia": "Martes", "ejercicios": "Pecho", "duracion_min": 45, "calorias": None},
    {"dia": "Miércoles", "ejercicios": None, "duracion_min": 40, "calorias": 300},
    {"dia": "Viernes", "ejercicios": "Espalda", "duracion_min": 50, "calorias": 380},
    {"dia": "Sábado", "ejercicios": "Cardio", "duracion_min": 30, "calorias": 400}
]

df = pd.DataFrame(sesiones)

print(df.isnull())

df_sin_huecos = df.dropna()
print(df_sin_huecos)

df_relleno = df.copy()
df_relleno["calorias"] = df_relleno["calorias"].fillna(df_relleno["calorias"].mean())
df_relleno["ejercicios"] = df_relleno["ejercicios"].fillna("Desconocido")
print(df_relleno)