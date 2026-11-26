#!/usr/bin/env python3
"""Aporte de un jugador a cada línea según puesto y orden.

Fuente de los porcentajes: data/contribuciones.csv (wiki de Hattrick, "Skill contribution",
edición del 7-dic-2019). Es una aproximación: no incluye forma, resistencia, experiencia,
lealtad, subniveles ni la penalización por varios jugadores en el centro.

Uso: python3 tools/aporte.py --pm 7 --df 6 --pa 3 --sc 2 --wg 3 [--gk 1] [--lado banda|centro]
"""
import argparse, csv, os

def main():
    ap = argparse.ArgumentParser()
    for k in ("pm", "df", "pa", "sc", "wg", "gk"):
        ap.add_argument("--" + k, type=float, default=0)
    ap.add_argument("--lado", choices=("banda", "centro"), default="banda",
                    help="posición lateral (banda) o central (centro) dentro de la línea")
    ap.add_argument("--puestos", default="IM,IMd,IMo,IMtw,W,Wtm,Wo,Wd,CDo,Fd")
    a = ap.parse_args()
    path = os.path.join(os.path.dirname(__file__), "..", "data", "contribuciones.csv")
    rows = {r["codigo"]: r for r in csv.DictReader(open(path))}
    f = lambda r, k: float(r[k]) / 100
    print(f"{'puesto':6} {'medio':>6} {'defC':>6} {'defL':>6} {'atqC':>6} {'atqL':>6}")
    for c in a.puestos.split(","):
        r = rows[c]
        dl = "DF_def_lateral_banda" if a.lado == "banda" else "DF_def_lateral_centro"
        pl = "PA_atq_lateral_banda" if a.lado == "banda" else "PA_atq_lateral_centro"
        medio = a.pm * f(r, "PM_medio")
        defc = a.df * f(r, "DF_def_central") + a.gk * f(r, "GK_def_central")
        defl = a.df * f(r, dl) + a.gk * f(r, "GK_def_lateral")
        atqc = a.pa * f(r, "PA_atq_central") + a.sc * f(r, "SC_atq_central")
        atql = a.wg * f(r, "WG_atq_lateral") + a.pa * f(r, pl) + a.sc * f(r, "SC_atq_lateral")
        print(f"{c:6} {medio:6.2f} {defc:6.2f} {defl:6.2f} {atqc:6.2f} {atql:6.2f}")

if __name__ == "__main__":
    main()
