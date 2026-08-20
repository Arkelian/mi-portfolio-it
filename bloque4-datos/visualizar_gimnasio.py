import pandas as pd
import matplotlib.pyplot as plt

sesiones = [
    {"dia": "Lunes", "ejercicios": "Piernas", "duracion_min": 60, "calorias": 450},
    {"dia": "Martes", "ejercicios": "Pecho", "duracion_min": 45, "calorias": 320},
    {"dia": "Miércoles", "ejercicios": "Piernas", "duracion_min": 55, "calorias": 470},
    {"dia": "Viernes", "ejercicios": "Espalda", "duracion_min": 50, "calorias": 380},
    {"dia": "Sábado", "ejercicios": "Cardio", "duracion_min": 30, "calorias": 400}
]

df = pd.DataFrame(sesiones)

media_calorias = df.groupby("ejercicios")["calorias"].mean()

media_calorias.plot(kind="bar")

plt.title("Media de calorias por ejercicio")
plt.show()
