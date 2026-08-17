import pandas as pd

sesiones = [
    {"dia": "Lunes", "ejercicios": "Piernas", "duracion_min": 60, "calorias": 450},
    {"dia": "Martes", "ejercicios": "Pecho", "duracion_min": 45, "calorias": 320},
    {"dia": "Viernes", "ejercicios": "Espalda", "duracion_min": 50, "calorias": 380},
    {"dia": "Sabado", "ejercicios": "Cardio", "duracion_min": 30, "calorias": 400 }
]

df = pd.DataFrame(sesiones)
df.to_csv("sesiones_gimnasio.csv", index=False)
df_desde_csv = pd.read_csv("sesiones_gimnasio.csv")

print(df_desde_csv)
print(df_desde_csv["calorias"].mean())

sesiones_largas = df[df["duracion_min"] >= 50]
piernas_o_espalda = df[df["ejercicios"] == "Piernas"]

print(df)
print()
print(df["calorias"])
print()
print(df["calorias"].mean())
print()
print(df["duracion_min"].sum())
print()
print(sesiones_largas)
print()
print(piernas_o_espalda)