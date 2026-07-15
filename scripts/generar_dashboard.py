"""Genera los mapas del panel principal (docs/img/) y calcula las cifras titulares.

Serie 2005-2024, NDVI armonizado (Roy 2016). PNGs estáticos con contorno comunal.

Uso: python scripts/generar_dashboard.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import ee
from src.gee._init import init_ee
from src.gee.aoi_temuco import get_aoi_temuco, TEMUCO_BBOX
from src.gee.ndvi_series import ndvi_anual_landsat
from src.gee.lst_series import lst_anual
from src.gee.change_correlacion import correlacion_ndvi_lst
from src.gee.dynamicworld import mascara_arboles
from src.gee.export import thumb_png, con_borde

init_ee()
aoi = get_aoi_temuco()
urbano = ee.Geometry.Rectangle(TEMUCO_BBOX)

PAL_NDVI = ["#c8b18f", "#f7f7c8", "#a6d96a", "#1a9641", "#006837"]
PAL_DELTA = ["#8c1515", "#d73027", "#ffffbf", "#1a9850", "#006837"]
PAL_LST = ["#2166ac", "#67a9cf", "#fddbc7", "#ef8a62", "#b2182b"]
BASE, ACT = 2005, 2024

ndvi_base = ndvi_anual_landsat(BASE)
ndvi_act = ndvi_anual_landsat(ACT)
delta = ndvi_act.subtract(ndvi_base).rename("dNDVI")
lst_act = lst_anual(ACT)

thumb_png(con_borde(ndvi_act.visualize(min=0, max=0.85, palette=PAL_NDVI), aoi),
          urbano, {}, f"docs/img/ndvi_{ACT}_urbano.png")
thumb_png(con_borde(ndvi_base.visualize(min=0, max=0.85, palette=PAL_NDVI), aoi),
          urbano, {}, f"docs/img/ndvi_{BASE}_urbano.png")
thumb_png(con_borde(delta.visualize(min=-0.3, max=0.3, palette=PAL_DELTA), aoi),
          urbano, {}, "docs/img/delta_ndvi_urbano.png")
thumb_png(con_borde(lst_act.visualize(min=18, max=42, palette=PAL_LST), aoi),
          urbano, {}, "docs/img/lst_2024_urbano.png")
thumb_png(con_borde(ndvi_act.visualize(min=0, max=0.85, palette=PAL_NDVI), aoi),
          aoi, {}, "docs/img/ndvi_2024_comuna.png")

# --- Cifras titulares ---
arb = mascara_arboles(2016)
perd = delta.lt(-0.15)
frac_urb = perd.reduceRegion(ee.Reducer.mean(), urbano, 30, maxPixels=int(1e9)).getInfo()["dNDVI"]
frac_arb = perd.updateMask(arb).reduceRegion(ee.Reducer.mean(), urbano, 30, maxPixels=int(1e9)).getInfo()["dNDVI"]
corr = correlacion_ndvi_lst(ACT, urbano)["correlation"]
tg = lst_act.updateMask(ndvi_act.lt(0.3)).reduceRegion(ee.Reducer.mean(), urbano, 30, maxPixels=int(1e9)).getInfo()["LST"]
tv = lst_act.updateMask(ndvi_act.gt(0.6)).reduceRegion(ee.Reducer.mean(), urbano, 30, maxPixels=int(1e9)).getInfo()["LST"]

print(f"Pérdida de verde {BASE}->{ACT} (área urbana): {frac_urb*100:.1f}%")
print(f"Pérdida de verde en zonas ARBÓREAS: {frac_arb*100:.1f}%")
print(f"Correlación NDVI-LST: {corr:.2f}")
print(f"LST zonas sin árboles {tg:.1f}°C vs con árboles {tv:.1f}°C = +{tg-tv:.1f}°C")
print("Mapas del panel en docs/img/")
