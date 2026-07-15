# Ciencia ciudadana de arbolado, verdor a nivel de calle y fuentes abiertas de Chile

**Proyecto:** Observatorio Ciudadano de Arbolado Urbano — Temuco (Daniela)
**Restricción dura:** solo herramientas y datos GRATIS / open / auto-hospedables.
**Fecha de compilación:** 2026-07-15
**Metodología:** Crossref (mailto=cvivallos@gmail.com), WebSearch/WebFetch, verificación de URLs vivas.

> Formato por hallazgo: **nombre** · tipo · qué hace · ¿gratis/open/auto-hospedable? + link · ¿aplica a Chile/Temuco? · cita/URL.

---

## 1. Plataformas de mapeo ciudadano de árboles

### OpenTreeMap (otm-core)
- **Tipo:** plataforma web colaborativa de inventario de arbolado urbano + cálculo de servicios ecosistémicos.
- **Qué hace:** mapa interactivo donde ciudadanos/organizaciones/municipios cargan árboles (especie, DAP, estado) y calcula beneficios (captura CO2, agua, sombra).
- **¿Open/auto-hospedable?** SÍ. Código abierto **GNU AGPL v3**. Repo: https://github.com/OpenTreeMap/otm-core (Django/Python + PostGIS). OJO: el servicio SaaS oficial (opentreemap.org) pasó a modelo de **suscripción paga**; solo la vía **auto-hospedada es gratis** pero requiere servidor propio (no corre en GitHub Pages, necesita backend PostGIS). Mantenimiento del repo algo estancado.
- **Chile/Temuco:** aplicable técnicamente; sin instancia chilena conocida. Curva de instalación alta.
- **URL:** https://github.com/OpenTreeMap/otm-core · https://opentreemap.github.io/

### iNaturalist / GBIF
- **Tipo:** plataforma global de biodiversidad por ciencia ciudadana (fotos georreferenciadas + ID de especie por comunidad/IA).
- **Qué hace:** registrar observaciones de árboles con foto y GPS; identificación colaborativa; datos exportables y volcados a GBIF.
- **¿Gratis?** SÍ, uso gratuito y datos abiertos (CC). No auto-hospedable (es servicio central), pero tiene **API abierta** para consumir observaciones en un mapa Leaflet propio.
- **Chile/Temuco:** SÍ, fuerte uso en Chile (iNaturalist Chile). Útil como capa de "árboles patrimoniales / especies", no como sistema de denuncias de tala.
- **URL:** https://www.inaturalist.org · API https://api.inaturalist.org

### Pl@ntNet
- **Tipo:** app de identificación de plantas por foto (IA).
- **Qué hace:** identifica especie desde una foto de hoja/flor/corteza; útil para que voluntarios sin formación botánica etiqueten especies.
- **¿Gratis?** SÍ, app gratuita + **API** (con cuota gratuita). No auto-hospedable, pero integrable.
- **Chile/Temuco:** funciona globalmente; sirve como complemento de identificación.
- **URL:** https://plantnet.org · https://my.plantnet.org (API)

### Treezilla (UK) / NYC Street Tree Map
- **Tipo:** ejemplos de referencia (no auto-hospedables directamente).
- **Treezilla:** "el mapa de árboles de Gran Bretaña", inventario ciudadano nacional (Open University). Referencia de modelo, no producto reutilizable. https://treezilla.org
- **NYC Street Tree Map:** visor del censo de arbolado de calle de NYC (datos abiertos + participación); el censo se hizo con voluntarios (TreesCount!). Buen modelo de UX. https://tree-map.nycgovparks.org
- **Chile/Temuco:** solo como inspiración de diseño y variables a capturar.

### OpenStreetMap (mapeo de árboles, `natural=tree`)
- **Tipo:** base cartográfica colaborativa mundial.
- **Qué hace:** permite mapear árboles individuales (`natural=tree`) y alineaciones (`natural=tree_row`) con atributos (especie, altura). Datos abiertos ODbL, interoperables.
- **¿Open/gratis?** SÍ, totalmente. Editable con iD/JOSM; consumible con Overpass API en un Leaflet propio.
- **Chile/Temuco:** SÍ. Existe guía LATAM de mapeo de árboles en OSM (wiki). Es la opción más "soberana" y sin backend propio: los datos viven en OSM.
- **URL:** https://wiki.openstreetmap.org/wiki/ES:Latam/Mapeo_de_%C3%A1rboles

---

## 2. Treepedia y verdor a nivel de calle (Green View Index)

### Treepedia (MIT Senseable City Lab)
- **Tipo:** metodología + librería para medir verdor de calle (Green View Index, GVI).
- **Qué hace:** muestrea puntos a lo largo de calles, baja panoramas de Google Street View, aplica segmentación para calcular % de dosel visible (GVI 0–100) y lo mapea.
- **¿Open?** SÍ, código Python abierto: https://github.com/mittrees/Treepedia_Public (fork Py3: https://github.com/y26805/Treepedia_Public).
- **LIMITACIÓN CLAVE:** depende de **Google Street View** → hoy el acceso masivo por API es **pago** (ver sección 4). El repo original está algo desactualizado.
- **Chile/Temuco:** metodológicamente aplicable, pero el cuello de botella es la imagen de calle (GSV pago / cobertura). Mejor usar alternativas con Mapillary (abajo).
- **URL:** https://senseable.mit.edu/treepedia

### AmericanRedCross / street-view-green-view  ⭐ (alternativa moderna con Mapillary)
- **Tipo:** pipeline Python de GVI usando imágenes **abiertas de Mapillary** en vez de GSV.
- **Qué hace:** `create_points.py` muestrea puntos cada ~20 m sobre calles; baja imágenes de Mapillary (token gratuito); segmenta y asigna GVI a cada punto.
- **¿Open/gratis?** SÍ. Repo abierto; solo requiere cuenta/token gratuito de Mapillary. Metodología basada en Li et al. (2015).
- **Chile/Temuco:** VIABLE si hay cobertura Mapillary; si no, se puede subir cobertura propia (ver sección 3). Esta es la ruta recomendada para "verdor de calle" sin costo.
- **URL:** https://github.com/AmericanRedCross/street-view-green-view

### ZenSVI (2024)
- **Tipo:** software open-source integral para Street View Imagery (adquisición + procesamiento + análisis) a escala.
- **Qué hace:** unifica descarga (Mapillary, etc.), segmentación semántica, cálculo de indicadores (GVI, sky view). Estado del arte para ciencia urbana con SVI.
- **¿Open?** SÍ. arXiv 2412.18641. https://arxiv.org/html/2412.18641v3
- **Chile/Temuco:** aplicable; más completo que Treepedia. Requiere Python + algo de cómputo.

### StreetView-NatureVisibility (Spatial Data Science & GEO-AI Lab)
- **Tipo:** framework reproducible de visibilidad de verdor con Mapillary, multi-ciudad.
- **¿Open?** SÍ. https://github.com/Spatial-Data-Science-and-GEO-AI-Lab/StreetView-NatureVisibility
- **Chile/Temuco:** aplicable como referencia/base de código escalable.
- **Paper asociado:** "Accessing eye-level greenness visibility from open-source street view images" (ScienceDirect S221067072400091X, 2024).

**Cita de método GVI:** Li, X. et al. (2015). *Who lives in greener neighborhoods? Assessment of residential greenness using GVI from GSV.* Urban Forestry & Urban Greening 14, 751–759.

---

## 3. Mapillary — imágenes de calle colaborativas y gratuitas

### Mapillary
- **Tipo:** plataforma colaborativa de imágenes de calle (fotos con GPS subidas por cualquiera desde el celular).
- **Qué hace:** cualquiera captura imágenes de calle con la app y las sube; quedan bajo licencia abierta (CC-BY-SA); disponibles vía API/visor. +3.000 M de imágenes globales.
- **¿Gratis/open?** SÍ. App gratuita; **API gratuita** con token; imágenes con licencia abierta. Segmentación semántica (incluye vegetación) provista por Mapillary.
- **Chile/Temuco — cobertura:** VARIABLE. No se pudo confirmar densidad en Temuco desde búsqueda; hay que verificar en el visor https://www.mapillary.com/app/ (zoom a Temuco). **Ventaja decisiva:** si falta cobertura, Daniela y voluntarios pueden **generar la suya** recorriendo Av. Caupolicán, Av. Alemania, Av. Pablo Neruda, etc. con el celular, creando un registro "antes/después" propio y abierto.
- **Modelos de detección de árboles:** sí, Mapillary entrega segmentación semántica (clase vegetación) y los pipelines de sección 2 (Red Cross, ZenSVI) detectan verdor sobre sus imágenes.
- **URL:** https://www.mapillary.com · https://www.mapillary.com/developer

---

## 4. Google Street View histórico — gratis vs pago

- **Ver "time travel" (histórico) gratis:** SÍ, manualmente en el visor de Google Maps/Google Earth (icono reloj) se pueden ver panoramas de años pasados donde existan. Útil para comparar **una avenida antes/después a mano** (ej. Caupolicán 2010 vs 2024), tomar capturas y documentar. Sin costo, pero **manual, no automatizable** y sujeto a Términos de Google (cuidado con re-publicar capturas).
- **Acceso por API:** **Street View Static API es PAGO** (pay-as-you-go, ~USD 0,0056–0,007 por panorama) con crédito/cuota gratuita mensual limitada (miles de eventos, según SKU). No hay API pública para descargar el **histórico** de forma masiva y gratuita; el histórico está pensado para el visor de Google Earth, no para pipelines.
- **Street View Publish API:** gratis, pero es para **subir** tus propias fotos 360, no para bajar las de Google.
- **Conclusión:** para automatizar verdor/detección, GSV no es la vía gratuita → usar **Mapillary**. GSV histórico sirve solo como verificación visual puntual manual del "antes/después".
- **URLs:** https://developers.google.com/maps/documentation/streetview/usage-and-billing · https://developers.google.com/maps/documentation/earth/historical-street-view

---

## 5. Fuentes abiertas de Chile

### IDE Chile (Infraestructura de Datos Geoespaciales) — ide.cl  ✅ verificada
- **Qué es:** red de instituciones públicas que publica información geoespacial oficial. Centro de descarga con capas (shapefile) y **fotografías aéreas de alta resolución (formato ECW)** para descarga directa gratuita.
- **Fotografía aérea:** desde dic. hay ortofotos de alta resolución de comunas del norte/centro descargables gratis; útil para comparar dosel en el tiempo donde haya cobertura de Temuco/Araucanía (verificar disponibilidad por comuna).
- **¿Gratis?** SÍ. Centro de descarga: https://www.ide.cl/descarga/capas.html
- **URL:** https://www.ide.cl · noticia ortofotos: https://www.ide.cl/index.php/noticias/item/982

### SAF — Servicio Aerofotogramétrico (FACh)  ✅ verificada
- **Qué es:** servicio estatal de aerofotogrametría y percepción remota. Posee el **archivo histórico de fotografía aérea de Chile** (vuelos de décadas atrás) — clave para el "antes" (2005, 2010…) que pide Daniela.
- **¿Gratis?** PARCIAL. El sitio existe (https://www.saf.cl) pero muchas imágenes históricas de alta resolución se solicitan/compran; parte del material se libera vía IDE Chile. **Verificar caso a caso** cotizando vuelos históricos sobre Temuco. NO asumir gratuidad total.
- **URL:** https://www.saf.cl

### IDE Temuco (Municipalidad de Temuco / SECPLA)  ✅ verificada (hub vivo)
- **Qué es:** portal ArcGIS Hub municipal con capas descargables en **CSV, KML, Zip, GeoJSON, GeoTIFF, PNG** + servicios **WMS/WFS/GeoServices**.
- **¿Catastro de arbolado?** NO confirmado como capa pública dedicada en el catálogo (el catálogo es JS-renderizado; hay que abrirlo y buscar "arbolado/áreas verdes"). La Muni **creó una Unidad de Parques y Arbolado Urbano**, así que puede existir o estar en desarrollo. **Acción recomendada:** contactar SECPLA / pedir la capa por transparencia.
- **URL:** https://ide-munitemuco.hub.arcgis.com · catálogo: https://ide-munitemuco.hub.arcgis.com/pages/catalogoidetemuco

### Observatorio Urbano MINVU / IDE MINVU  ✅
- **Qué es:** geoportal del MINVU con datos de expansión urbana, límites, permisos y planificación. Útil para cruzar **pérdida de árboles vs expansión inmobiliaria**.
- **¿Gratis?** SÍ. https://ide.minvu.cl
- **Chile/Temuco:** SÍ (cobertura nacional).

### INE — Geodatos abiertos  ✅
- **Qué es:** portal de mapas y geodatos del Instituto Nacional de Estadísticas (manzanas censales, población). Útil para densificación/contexto socioeconómico.
- **URL:** https://www.ine.gob.cl/herramientas/portal-de-mapas/geodatos-abiertos

### CONAF — Sistema de Información Territorial (SIT) + denuncia forestal
- **Qué es:** SIT con catastro de uso de suelo y bosque nativo (escala regional, no árbol-a-árbol urbano). Además canal oficial de **denuncia de tala ilegal** (para bosque nativo → CONAF/SAG).
- **URLs:** https://sit.conaf.cl · denuncia: https://www.conaf.cl/tramites/denuncia-posible-infraccion-a-la-normativa-forestal-denuncia-tala-ilegal/
- **SMA (Superintendencia de Medio Ambiente):** portal ciudadano de denuncias ambientales: https://portal.sma.gob.cl
- **Nota:** el arbolado urbano en bandejón/vereda suele ser competencia **municipal** (ordenanzas), no CONAF. Temuco tiene Ordenanza 2021 relacionada (transparencia.temuco.cl).

### Documento parlamentario clave
- **"Deforestación del arbolado urbano en la ciudad de Temuco"** — documento del Senado de Chile. Evidencia oficial del problema exacto que Daniela quiere monitorear; útil como respaldo/justificación del observatorio.
- **URL:** https://microservicio-documentos.senado.cl/v1/archivos/b5e5779e-adf1-4411-95be-f1992b39366c?includeContent=true

---

## 6. Casos / proyectos similares en Chile y LATAM

- **Providencia (Santiago) — Censo del arbolado (2021):** censo de +60.000 árboles (42.000 en calles, 18.000 en parques), hecho con egresados PUC en 150 días; identificó 3.500 ejemplares enfermos. Modelo municipal, no ciudadano-abierto, pero referencia local fuerte. https://providencia.cl/.../por-que-estamos-censando-todos-los-arboles-de-la-comuna
- **La Reina — "Más que un Árbol" / Catastro de Árboles:** catastro 2021–22 de 35.995 árboles, 254 especies. Municipal, sin plataforma abierta de ciencia ciudadana. https://masqueunarbol.cl/programa/catastro-de-arboles/
- **Buenos Aires (Arg) — Censo y Mapa de Arbolado / Arbopedia:** censo público abierto desde 2014, con mapa. Modelo LATAM de datos abiertos de arbolado. https://buenosaires.gob.ar/.../censo-y-mapa-de-arbolado
- **Corrientes (Arg) — dataset abierto de arbolado urbano.** https://datos.ciudaddecorrientes.gov.ar/dataset/arbolado-urbano
- **Bogotá (Col) — Censo del Arbolado Urbano (datos abiertos).** https://datosabiertos.bogota.gov.co/dataset/censo-arbolado-urbano
- **Montevideo/Uruguay — catálogo de datos abiertos con capa arbolado.** https://catalogodatos.gub.uy
- **Arbolado ZMG (Guadalajara, Méx):** visor ciudadano de arbolado (maptitud). http://arboladozmg.maptitud.xyz/mapa/
- **"En Defensa del Árbol Urbano en Chile"** — comunidad activa (Facebook) de denuncias ciudadanas de tala; potencial aliada/fuente de reportes. https://www.facebook.com/groups/838603902837674/
- **Guía CONAF "Árboles urbanos de Chile":** recurso de reconocimiento de especies para etiquetar el catastro. https://www.conaf.cl/cms/editorweb/institucional/Arboles_urbanos_de_Chile-2da_edicion.pdf

**Referencia académica (Crossref):** *Integrating Urban Tree Carbon Sequestration into Metropolitan Ecosystem Services... A Citizen Science-Based Methodology* (Urban Science, 2025, DOI 10.3390/urbansci9110463) — metodología reciente de ciencia ciudadana de arbolado + servicios ecosistémicos.

---

## 7. Stack técnico gratis recomendado para el Observatorio

Objetivo: sitio en **GitHub Pages** (gratis, sin backend propio) + captación de fotos/denuncias georreferenciadas + mapa.

### Front / mapa (GitHub Pages compatible)
- **Leaflet** (open, MIT) + tiles gratuitos de **OpenStreetMap** → mapa base. Corre 100% estático en GitHub Pages. https://leafletjs.com
- **uMap** (open, AGPL) → crear mapas colaborativos con capas y markers **sin programar**; se puede embeber en el sitio. Instancia pública gratuita o auto-hospedable. Alternativa libre a Google My Maps. https://umap.openstreetmap.fr

### Captación de reportes (fotos + GPS + podas/talas)
- **KoBoToolbox** ⭐ (open AGPL, gratis, servidor público o auto-hospedable): formularios avanzados, **captura offline**, geolocalización, **adjuntar fotos**, API para exportar. Ideal para "denuncia de poda/tala con foto y ubicación". Los datos salen por API y se pintan en el Leaflet del sitio. https://www.kobotoolbox.org
- **Alternativa simple:** Google Forms con campo de ubicación + subida de foto (gratis, cero fricción) → export a CSV/Sheets → mapa. Menos "soberano" que KoBo pero más fácil para voluntarios.
- **Ushahidi** (open, plataforma de crowdmapping de crisis/denuncias): más pesada, requiere hosting; útil si el observatorio escala a muchos reportes moderados. https://www.ushahidi.com

### Verdor de calle / análisis (opcional, avanzado)
- **Mapillary** (captura propia de imágenes de calle) + **AmericanRedCross/street-view-green-view** o **ZenSVI** para GVI. Todo gratis/open. Requiere Python.

### Antes/después e imagen histórica
- Ortofotos **IDE Chile** (ECW, gratis) + **SAF** (histórico, verificar costo) para dosel aéreo por año.
- **GSV histórico manual** (visor) para chequeo puntual de avenidas.
- Comparación de dosel: QGIS (open) para digitalizar copas sobre ortofotos de distintos años.

### Arquitectura mínima sugerida (todo gratis)
```
GitHub Pages (sitio estático, HTML + Leaflet)
   ├── Mapa base OSM + capa de árboles (GeoJSON local o iNaturalist/OSM API)
   ├── Reportes ciudadanos ← KoBoToolbox (form con foto+GPS) → export GeoJSON/CSV
   ├── Capa "antes/después" ← ortofotos IDE Chile / capturas GSV histórico
   └── (avanzado) capa GVI ← Mapillary + street-view-green-view
```

---

## Resumen de verificación de URLs (vivas al 2026-07-15)
- ✅ IDE Chile (ide.cl), centro de descarga y noticia de ortofotos.
- ✅ IDE Temuco hub ArcGIS (catálogo activo; capa de arbolado NO confirmada como pública).
- ✅ IDE MINVU (ide.minvu.cl), INE geodatos, CONAF SIT/denuncias, SMA denuncias.
- ✅ Repos GitHub: otm-core, Treepedia_Public, street-view-green-view, StreetView-NatureVisibility.
- ✅ KoBoToolbox, uMap, Leaflet, Mapillary, iNaturalist, OSM wiki LATAM.
- ⚠️ SAF (saf.cl) existe pero gratuidad del histórico NO confirmada — cotizar.
- ⚠️ Catastro de arbolado abierto de Temuco: NO confirmado; pedir a SECPLA.
