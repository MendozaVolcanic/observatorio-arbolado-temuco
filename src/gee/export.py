"""Exportar imágenes GEE a PNG estáticos (thumbnails) para el dashboard.

Los tiles en vivo de GEE llevan tokens que expiran, así que NO sirven para una
página pública. En cambio los thumbnails PNG son estáticos: cualquiera los ve sin
login ni cuota. Esta es la base de la Capa 3 (observatorio en GitHub Pages).
"""
import os
import urllib.request
import ee
from src.gee._init import init_ee


def thumb_png(image: "ee.Image", region: "ee.Geometry", vis: dict, out_path: str,
              dimensions: int = 900) -> str:
    """Renderiza una ee.Image visualizada a un PNG local vía getThumbURL."""
    init_ee()
    params = dict(vis)
    params.update({"region": region, "dimensions": dimensions, "format": "png"})
    url = image.getThumbURL(params)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    urllib.request.urlretrieve(url, out_path)
    return out_path


def con_borde(vis_image: "ee.Image", aoi: "ee.Geometry", color: str = "black",
              width: int = 2) -> "ee.Image":
    """Superpone el contorno de un AOI sobre una imagen ya visualizada (RGB)."""
    outline = ee.Image().byte().paint(
        ee.FeatureCollection([ee.Feature(aoi)]), 1, width
    )
    return vis_image.blend(outline.visualize(palette=[color]))
