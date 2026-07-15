# Brown, C.F.; Brumby, S.P.; Guzder-Williams, B.; et al. (2022)

**"Dynamic World, Near real-time global 10 m land use land cover mapping."** *Scientific Data* 9, 251. DOI: 10.1038/s41597-022-01307-4. Nature, open access (CC BY).

## Qué aporta al proyecto

Presenta "Dynamic World", un producto de clasificación de cobertura de suelo (land use/land cover) global, gratuito, actualizado casi en tiempo real, a 10 m de resolución, generado con deep learning sobre Sentinel-2 y disponible directamente como colección de imágenes en Google Earth Engine (`GOOGLE/DYNAMICWORLD/V1`). Incluye una clase explícita de "trees" (árboles/vegetación leñosa) con probabilidad por píxel, calculada para cada escena Sentinel-2 desde 2015 en adelante.

## Dato / cifra clave

- Resolución espacial 10 m, cadencia casi en tiempo real (una clasificación por cada escena Sentinel-2, ~cada 5 días con revisita combinada).
- 9 clases de cobertura, entre ellas "trees", con probabilidades continuas (no solo clase dura), lo que permite umbralizar según necesidad del análisis.
- Accesible sin costo ni registro adicional dentro de GEE, igual que Landsat/Sentinel-2 crudos.

## Cómo se usa en el observatorio — sugiere una adición a la capa 1

Es un insumo gratuito, en GEE, no contemplado en el plan original de 3 capas. La capa 1 (NDVI + LST) podría **sumar la banda "trees" de Dynamic World como capa de cruce/validación cruzada del NDVI** para distinguir cobertura arbórea de otra vegetación (pasto, cultivos), mejorando la correlación árbol↔calor sin costo ni esfuerzo adicional de descarga — es un `ee.ImageCollection` más a filtrar por fecha y clip por Temuco, igual que Landsat/Sentinel-2. No reemplaza el conteo manual de copas (capa 2, que necesita resolución mucho más fina para polígonos individuales), pero sí puede aportar una máscara de "área arbórea probable" a 10 m para toda la ciudad y toda la serie 2015–2025, complementando el NDVI que la capa 1 ya usa.
