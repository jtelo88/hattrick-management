#!/usr/bin/env python3
"""Calculadora de velocidad de entrenamiento (fórmula de Schum, la que usa Hattrick Organizer).

T = f(nivel) * K(entrenador) * K(asistentes) * K(intensidad) * K(resistencia) * K(tipo) * K(edad) * K(minutos)

Fuente: Hattrick Organizer, core/training/WeeklyTrainingType.java (commit 8abe284, 2026-11-19).
Validada contra el ejemplo del manual oficial (Staff > Assistant Coach) y contra la
"Training estimation" del juego para Satoshian FC (27-nov-2026).

Ejemplos:
  python3 tools/entrenamiento.py --nivel 7 --edad 17
  python3 tools/entrenamiento.py --nivel 6 --edad 17 --puesto medio --dias 29 --hasta 8
"""
import argparse, math

TIPO = {"jugadas": (3.36, 1/8), "defensa": (2.88, 1/6), "anotacion": (3.24, 1/6),
        "extremo": (4.80, 1/8), "pases": (3.60, 1/6), "porteria": (5.10, 0), "balon_parado": (14.70, 0)}
# Nivel de entrenador del juego (1-5) -> coeficiente
ENTRENADOR = {1: 0.7343, 2: 0.8324, 3: 0.92, 4: 1.0, 5: 1.0375}
PUESTO = {"completo": 1.0, "medio": 0.5}

def f_nivel(n):
    return 16.289 * math.exp(-0.1396 * n) if n < 9 else 54.676 / n - 1.438

def subida_semanal(nivel, edad=17, entrenador=3, asistentes=6, intensidad=100, resistencia=10,
                   tipo="jugadas", puesto="completo", minutos=90):
    k_tipo, k_fondo = TIPO[tipo]
    k_puesto = k_fondo if puesto == "fondo" else PUESTO[puesto]
    return (f_nivel(nivel) * ENTRENADOR[entrenador] * (1 + 0.035 * asistentes) * intensidad / 100
            * (1 - resistencia / 100) * k_tipo * 54 / (edad + 37) * k_puesto * min(minutos, 90) / 90) / 100

def simular(nivel, edad, dias, hasta, sub=0.0, **kw):
    """Semanas hasta alcanzar 'hasta', partiendo de nivel+sub. Devuelve lista (semana, nivel, edad)."""
    x, sem, out = nivel + sub, 0, []
    while x < hasta and sem < 80:
        x += subida_semanal(int(x), edad, **kw)
        sem += 1; dias += 7
        if dias >= 112: dias -= 112; edad += 1
        if int(x) > nivel:
            nivel = int(x); out.append((sem, nivel, f"{edad}a{dias}d"))
    return out

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--nivel", type=int, required=True); p.add_argument("--sub", type=float, default=0.0)
    p.add_argument("--edad", type=int, default=17); p.add_argument("--dias", type=int, default=0)
    p.add_argument("--hasta", type=int); p.add_argument("--entrenador", type=int, default=3)
    p.add_argument("--asistentes", type=int, default=6); p.add_argument("--intensidad", type=int, default=100)
    p.add_argument("--resistencia", type=int, default=10); p.add_argument("--tipo", default="jugadas")
    p.add_argument("--puesto", default="completo", choices=["completo", "medio", "fondo"])
    a = p.parse_args()
    kw = dict(entrenador=a.entrenador, asistentes=a.asistentes, intensidad=a.intensidad,
              resistencia=a.resistencia, tipo=a.tipo, puesto=a.puesto)
    s = subida_semanal(a.nivel, a.edad, **kw)
    print(f"Subida semanal: {s*100:.1f}% de nivel -> {1/s:.1f} semanas por nivel ({a.puesto})")
    for sem, niv, ed in simular(a.nivel, a.edad, a.dias, a.hasta or a.nivel + 1, a.sub, **kw):
        print(f"  semana {sem}: llega a {niv} con {ed}")
