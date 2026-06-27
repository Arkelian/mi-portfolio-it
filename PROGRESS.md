# 📊 Progress Tracker — Lekro IT Portfolio
> Fuente de verdad para Claude Cowork. Sincronizado con el plan real de Alex (mentor en Claude.ai).
> Última actualización: 2026-06-24

---

## 👤 Perfil

- **Nombre:** Lekro (Nazar) — GitHub: `Arkelian`
- **Objetivo:** Profesional IT remoto internacional — automatización IA, Python, agentes, ciberseguridad
- **Disponibilidad:** 1-2 horas semanales (sesiones densas, sin relleno)
- **Mercado objetivo:** Upwork + LinkedIn global + GitHub público
- **Entorno:** Windows / PowerShell — `python .\nombre.py`
- **Mentor:** Alex (Claude.ai — proyecto "Aprendizaje IT")

---

## 🗺️ Mapa de bloques

```
Bloque 0  → Entorno profesional        ✅ COMPLETADO (4 sesiones)
Bloque 1  → Python funcional           🔄 EN PROGRESO (Sesión 7 global / S3 Python)
Bloque 2  → Automatización con n8n     ⏳ Pendiente
Bloque 3  → IA aplicada y LLMs         ⏳ Pendiente
Bloque 4  → Análisis de datos          ⏳ Pendiente
Bloque 5  → Ciberseguridad ética       ⏳ Pendiente
Bloque 6  → Proyectos integradores     ⏳ Pendiente
```

---

## ✅ Bloque 0 — Entorno profesional (COMPLETADO)

| Sesión global | Contenido | Estado |
|---|---|---|
| S1 | Git: repositorio, commits, push | ✅ |
| S2 | Git: branches y merge | ✅ |
| S3 | Git: conflictos de merge | ✅ |
| S4 | VSCode: entorno profesional completo | ✅ |

**Temas dominados:** Git completo (branch, merge, conflictos, log), VSCode configurado con 12 extensiones (GitLens, Error Lens, Prettier, indent-rainbow, Python, Copilot Chat, Claude Code), settings.json personalizado.

---

## 🔄 Bloque 1 — Python funcional (EN PROGRESO)

### Sesiones completadas

| Sesión global | Sesión Python | Archivo | Conceptos | Estado |
|---|---|---|---|---|
| S5 | P1 | `perfil.py` | Variables, tipos, input(), f-strings, if/elif/else | ✅ |
| S6 | P2 | `perfiles_multiples.py` | Listas, while+break, diccionarios, enumerate(), list comprehension | ✅ |
| S7 | P3 | `perfiles_v2.py` | def, parámetros, return, docstrings, refactorización | 🔄 En progreso |

### Estado actual de `perfiles_v2.py`
- ✅ `calcular_nivel(meses)` — completa
- ✅ `pedir_perfil(nombre)` — completa (modificada para recibir nombre como parámetro)
- ✅ `imprimir_perfil(indice, perfil)` — completa
- ⏳ `imprimir_informe(perfiles)` — pendiente
- ⏳ Bloque `if __name__ == "__main__":` — pendiente

### Sesiones pendientes Bloque 1

| Sesión Python | Tema |
|---|---|
| P4 | Diccionarios a fondo — operaciones, iteración, anidamiento |
| P5 | Manejo de archivos — leer/escribir `.txt` y `.csv` |
| P6 | Manejo de errores — `try / except`, validación de inputs |
| P7 | Módulos y librerías estándar — `os`, `datetime`, `json` |
| P8 | Proyecto integrador Bloque 1 (enunciado al llegar) |

---

## ⚠️ Patrones de error conocidos (vigilar siempre)

1. **Typos en español** dentro de strings — "sequimos", "actulizar", "PROFECIONAL", "Sique" — revisar antes de commit
2. **Comillas curvas** de PowerShell al pegar comandos — siempre usar comillas rectas `"`
3. **Consolidar lectura de errores** de terminal antes de preguntar — en desarrollo

---

## 💪 Fortalezas identificadas por Alex

- Detecta errores conceptuales antes de ejecutar código
- Pregunta cuando no entiende en lugar de copiar ciegamente
- Constancia: retoma el plan tras días de pausa sin perder el hilo
- Criterio crítico: cuestiona explicaciones cuando algo no cuadra

---

## 📁 Estructura del repositorio

```
mi-portfolio-it/                    ← github.com/Arkelian/mi-portfolio-it
├── README.md
├── PROGRESS.md                     ← este archivo (Claude Cowork)
├── SESIONES.md                     ← log de sesiones
├── bloque1-python/
│   ├── perfil.py                   ✅ P1
│   ├── perfiles_multiples.py       ✅ P2
│   └── perfiles_v2.py              🔄 P3 (incompleto)
├── bloque2-n8n/                    ⏳
├── bloque3-llms/                   ⏳
├── bloque4-datos/                  ⏳
├── bloque5-ciberseguridad/         ⏳
└── bloque6-proyectos/              ⏳
```
