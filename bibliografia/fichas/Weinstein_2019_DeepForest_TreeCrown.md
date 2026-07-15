# Weinstein, B.G.; Marconi, S.; Bohlman, S.; Zare, A.; White, E. (2019)

**"Individual Tree-Crown Detection in RGB Imagery Using Semi-Supervised Deep Learning Neural Networks."** *Remote Sensing* 11(11), 1309. DOI: 10.3390/rs11111309. MDPI, open access (CC BY). (Este trabajo dio origen a la librería DeepForest.)

## Qué aporta al proyecto

Es el paper fundacional de DeepForest, la herramienta más citada para detección automática de copas de árboles individuales con deep learning. Describe el enfoque semi-supervisado: un detector no supervisado (basado en LIDAR) genera datos de entrenamiento "ruidosos" a gran escala, que luego se refinan con un número pequeño de anotaciones manuales de alta calidad (2848 árboles) para afinar el modelo.

## Dato / cifra clave

- La imagen de entrada usada es RGB de **0.1 m (10 cm) de resolución espacial**, mosaicos de 1 km × 1 km del programa NEON (EE.UU.), con datos LIDAR coincidentes para generar el entrenamiento inicial no supervisado.
- Incluso con este enfoque semi-supervisado que reduce la necesidad de anotación manual masiva, el modelo requiere: (a) imagen RGB submétrica, y (b) LIDAR o anotaciones manuales de calidad para calibrar y validar.

## Cómo se usa en el observatorio — confirma la decisión ya tomada, no la cambia

Este paper **confirma, no cambia**, la decisión del plan de hacer conteo manual (no IA) en la capa 2. La condición de entrada de DeepForest —RGB a 10 cm de resolución, idealmente con LIDAR de apoyo— es exactamente lo que el proyecto ya diagnosticó como no disponible gratis para Temuco (sur de Chile no tiene ortofoto fina gratuita). Aplicar DeepForest sobre imágenes gratuitas más gruesas (Google Earth Pro, Sentinel-2) daría resultados no confiables, porque el modelo fue entrenado y validado específicamente a esa resolución submétrica. Conclusión: mantener el conteo manual de copas en los corredores piloto (Av. Olimpia, Caupolicán) es la decisión correcta dado el estado actual de datos gratuitos; DeepForest queda como opción futura solo si se consigue imagen de dron o satélite submétrico gratuito o de bajo costo para Temuco.
