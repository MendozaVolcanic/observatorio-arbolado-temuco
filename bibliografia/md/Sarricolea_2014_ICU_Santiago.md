Revista de Geografía Norte Grande, 57: 123-141 (2014)
123
Artículos

El estudio de la Isla de Calor Urbana
de Superﬁ cie del Área Metropolitana
de Santiago de Chile con imágenes
Terra-MODIS y Análisis de
Componentes Principales1

Pablo Sarricolea Espinoza2 y Javier Martín-Vide3

RESUMEN

Con el objetivo de conocer los patrones e intensidades de la Isla de Calor Urbana
de  Superﬁ cie  (ICUs)  de  Santiago  se  han  calculado  las  temperaturas  de  emisión
para 53 imágenes Terra MODIS, se han trazado mapas de intensidad de la ICUS y
se ha aplicado Análisis de Componentes Principales. Los resultados muestran que
la  ICUs  tiende  a  localizar  el  máximo  en  las  comunas  centrales  y  de  Huechuraba
y  Quilicura,  con  intensidades  superiores  a  5°C.  El  ACP  revela  cuatro  patrones
típicos, que explican el 90,6% de las situaciones, a saber: ICUs consolidada, ICUs
del piedmont y cuña de altos ingresos, un tipo sin ICUs y otra más intensa al sur.
De las situaciones sin isla de calor, se ha sugerido la hipótesis de efecto sumidero,
asociado a brisa catabática, que barre la ICUs y la desplaza al poniente de la ciu-
dad.

Palabras clave: Isla de Calor Urbana de Superﬁ cie, efecto sumidero de calor, Terra
MODIS, Análisis de Componentes Principales.

ABSTRACT

In  order  to  understand  the  patterns  and  intensities  of  the  Surface  Urban  Heat  Is-
lands  (SUHIs)  of  Santiago  emission  temperatures  were  calculated  using  53 Terra
MODIS  satellite  images  and  then  factor  reduction  was  performed  using  Principal
Components  Analysis  (PCA).  In  addition,  intensity  maps  of  SUHIs  were  created.
Results  show  that  the  maximum  temperature  (with  intensities  measuring  above
5°C) within the SUHI tends to be located in the central municipalities of Santiago,
as  well  as  in  the  municipalities  of  Huechuraba  and  Quilicura.  Furthermore,  PCA
reveals  four  typical  patterns,  which  explain  90.6%  of  cases:  consolidated  SUHI,
piedmont SUHI and high income wedge, no SUHI and high intensity SUHI in the
south. It has been hypothesized that the lack of a SUHI to the drain effect, which
is linked to the katabatic breeze, causing the SUHI to move toward the west sector
of the city.

Key  words:  Principal  Component Analysis,  surface  urban  heat  island,  urban  heat
sink, Terra MODIS.

1  Artículo  recibido  el  3  de  agosto  de  2012,  aceptado
el 27 de junio de 2013 y corregido el 20 de octubre
de 2013.

2  Departamento  de  Geografía,  Universidad  de  Chile

(Chile). Email: psarricolea@uchilefau.cl

3  Grupo  de  Climatología,  Universidad  de  Barcelona

(España). Email: jmartinvide@ub.edu

124

R E V I S T A   D E   G E O G R A F Í A   N O R T E   G R A N D E

La  temperatura  superficial  es  de  vital
importancia  en  los  estudios  de  Climatología
urbana. Ella, al decir de Voogt y Oke (2003),
condiciona  y  modula  la  temperatura  del
aire  en  las  capas  más  bajas  de  la  atmósfera
urbana.  Además,  es  fundamental  para  esti-
mar  los  balances  energéticos,  determinar  las
condiciones  bioclimáticas  en  el  interior  de
los  edificios,  y,  también,  los  intercambios
térmicos  con  el  entorno,  que  afectan  al  con-
fort  de  los  habitantes  de  la  ciudad.  En  este
sentido, Stewart y Oke (2009) proponen áreas
homogéneas  desde  el  punto  de  vista  térmico
y  de  diseño  urbano,  las  cuales  son,  en  parte,
responsables de la distribución de las tempe-
raturas urbanas.

Para  obtener  la  temperatura  superﬁ cial  se
utilizan  esencialmente  sensores  remotos,  los
cuales  registran  los  valores  de  temperatura
de  emisión  de  las  cubiertas  de  suelo  a  vista
de ojo de pájaro (Oke y Voogt, 1997), permi-
tiendo así conocer su distribución espacial y,
en  las  áreas  urbanas,  estimar  la  isla  de  Calor
Urbana  de  Superﬁ cie  (ICUs,  homóloga  a  la
ICU  del  aire).  Cabe  recordar,  que  la  ICUs  ha
sido  estudiada  desde  el  advenimiento  de  la
teledetección, a mediados del siglo XX.

La  teledetección  ha  ampliado  las  oportu-
nidades en los estudios de Climatología urba-
na,  y  también  ha  signiﬁ cado  introducir  nue-
vos conceptos (Voogt & Oke, 2003). Existe un
gran  número  de  sensores  remotos  útiles  para
el estudio de la ICUs, tales como Landsat TM
y ETM+4, NOOA AVHRR, Terra ASTER y Terra
MODIS. Los sensores Terra han avanzado más
que  los  demás,  pues  han  suministrado  a  los
investigadores  las  librerías  de  emisividad  de
las diferentes cubiertas terrestres. Además, en
el  caso  de Terra  MODIS  se  poseen  subpro-
ductos  especíﬁ cos  corregidos  para  el  estudio
de  la  temperatura  de  superﬁ cie  y  su  frecuen-
cia de registro es diaria.

Las mediciones tradicionales de la isla de
calor  han  sido  mediante  pares  de  estaciones
meteorológicas  que  representan  las  áreas
urbana y rural (Kukla et al., 1986; Karl et al.,
1988),  o  bien,  mediante  el  método  de  los

4  El  radiómetro  térmico  de  Landsat  ETM+  funcionó

entre 1999 y septiembre de 2003.

transectos (Johnson, 1985; Torok et al., 2001,
Romero  et  al.,  2010a,  2010b).  No  obstante,
existe escasa información de la conﬁ guración
espacial  de  las  temperaturas  en  las  ciuda-
des,  lo  cual  implica  un  desafío  en  cuanto  a
poseer  una  mayor  cobertura  y  resolución  de
las  temperaturas  urbanas.  Es  por  ello  que  los
estudios  de  Climatología  urbana  a  alta  reso-
lución (espacial) son escasos, y referidos casi
en  exclusiva  a  las  temperaturas  superﬁ ciales,
es decir, a la ICUs (Streutker, 2003).

Las temperaturas de la superﬁ cie son más
fáciles  de  obtener,  principalmente  por  la
disponibilidad  de  productos  tales  como Terra
MODIS,  que  provee  la  temperatura  de  la  su-
perﬁ cie  de  la  tierra  (Land  Surface Temperatu-
re, LST). Es importante señalar que la relación
entre la temperatura del aire y de la superﬁ cie
no  está  completamente  consensuada,  y  hay
mucha  discusión  sobre  ello.  Así,  por  citar
casos extremos, están aquellos que señalan la
estrecha y positiva relación entre las tempera-
turas  del  aire  y  de  superﬁ cie  (Arnﬁ eld,  2003;
Weng,  2009;  Nichol,  1994),  y  otros  que  se
reﬁ eren a nulas relaciones entre ellas (Weller
y Thorne, 2001). A pesar de lo anteriormente
señalado, la Agencia de Protección Ambiental
de  Estados  Unidos  (EPA)  sugiere  que  en  el
caso de las temperaturas nocturnas existe una
relación  estrecha  entre  la  ICU  y  la  ICUs,  hi-
pótesis  que  se  asume.  Con  ello  por  ejemplo,
se elimina problemas encontrados por Rome-
ro et al. (2010a) referidos a sombras diurnas y
albedos de las estructuras urbanas.

Múltiples  estudios  han  mencionado  ex-
plícitamente  el  potencial  y  la  utilidad  del
producto  MODIS  LST  en  la  investigación  de
la  ICUs  (Rajasekar  y  Weng,  2008;  Cheval  et
al.,  2009).  En  particular,  las  características
de realizar observaciones instantáneas, la co-
bertura  mundial  y  la  calidad  de  los  datos  de
MODIS (Jin y Shepherd, 2005).

Los  sensores Terra  y  Aqua  MODIS  están
operativos  desde  el  año  2000,  y  sus  datos
los  pueden  adquirir  gratuitamente  investi-
gadores  de  todo  el  mundo  para  sus  análisis.
Es  por  esta  razón  que  existe  una  creciente
utilización de ellos, que los valida como una
herramienta muy útil para la Climatología ur-
bana (Schwarz et al., 2011 y 2012, Clinton &
Gong, 2013, Hu y Brunsell, 2013).

E L  E S T U D I O  D E  L A  I S L A  D E  C A L O R  U R BA NA  D E  S U P E R F I C I E  D E L  Á R E A
METROPOLITANA  DE  SANTIAGO  DE  CHILE  CON  IMÁGENES  TERRA-MODIS  Y
ANÁLISIS DE COMPONENTES PRINCIPALES

125

No obstante, disponer de una mayor can-
tidad  de  datos  termométricos  implica  deﬁ nir
herramientas  que  permitan  sintetizar  la  infor-
mación. Y hay desde las más sencillas (mapas
promedios)  a  las  más  soﬁ sticadas,  como  el
Análisis  de  Componentes  Principales  (ACP).
Este  último  adquiere  una  gran  importancia,
y  tanto  en  Climatología  como  en  Geografía,
posee una amplia y reconocida trayectoria, a
diferentes escalas espaciales. Por ejemplo, en
estudios  de  Climatología  sinóptica  sus  apli-
caciones  se  centran  en  interpretar  patrones
espaciales  diarios  de  los  tipos  de  circulación
atmosférica,  facilita  realizar  catálogos  de
tipos  de  tiempo,  etc.  En  Climatología  urbana
ayuda  a  resumir  las  conﬁ guraciones  típicas  y
más representativas de la isla de calor, lo cual
da  carácter  climático  a  los  resultados,  pues
sintetiza información de resolución detallada.

Hasta  ahora,  el  conocimiento  de  la  con-
ﬁ guración  y  la  conformación  de  ICUs  en  el
Área Metropolitana de Santiago es un proble-
ma aún no resuelto. Por ejemplo, no se cono-
cen  los  patrones  espaciales  típicos  de  ICUs,
muy  importantes  para  proponer  medidas  de
mitigación, o las intensidades más habituales
de  ella.  Por  ello,  este  artículo  responde  a  di-
chas interrogantes.

Materiales y métodos

El  área  de  estudio  corresponde  al  área
metropolitana  de  Santiago.  Ella  es  la  capital
económica,  demográﬁ ca,  industrial,  comer-
cial  y  ﬁ nanciera  de  Chile,  además  de  ser  la
capital  de  la  Región  Metropolitana.  Posee
como región una superﬁ cie de 15.403,2 km²,
es  la  más  pequeña  de  todas  las  regiones  del
país,  pero  en  la  que  habitan  más  personas,
con  una  población  superior  a  los  7  millo-
nes  de  habitantes,  siendo  así  la  región  más
densamente  ocupada.  Su  clima  es  de  tipo
“mediterráneo  continental”,  el  cual  presenta
una  estación  seca  prolongada  e  inviernos
lluviosos.  Según  la  clasiﬁ cación  de  Köppen
presenta  un  clima  templado  de  verano  seco
(Csb).  Respecto  a  las  temperaturas  extremas
para  el  período  de  referencia  1981-2010,  el
mes de enero alcanza 30,1ºC como tempera-
tura  media  de  las  máximas,  mientras  que  ju-
lio registra una media de las mínimas de unos
3,9ºC, lo cual implica una oscilación térmica
de 26,2ºC. La temperatura media anual es de

14,7°C, enero es el mes más cálido, con una
temperatura  media  de  21,2°C,  y  el  mes  más
frío  corresponde  a  julio  con  8,2°C,  siendo  la
amplitud térmica media de unos 13ºC.

Al  tratarse  de  un  estudio  de  Climatología
urbana,  delimitaremos  el  área  adyacente  a  la
ciudad  de  Santiago  (que  puede  corresponder
a  un  área  de  inﬂ uencia  climática  de  la  ciu-
dad).  Esta  área  colindante  a  la  ciudad  está
compuesta  por  paisajes  agrarios,  naturales  y
seminaturales. Para demarcar el límite de esta
área  de  inﬂ uencia  o  similar  a  la  ciudad,  se
deﬁ nen los siguientes criterios:

1.    Que la altitud se encuentre entre los 400
y los 1.150 m.s.n.m. Esta condición deja
fuera  una  parte  del  núcleo  urbano  de
Peñaﬂ or  y  un  pequeño  sector  de  Lo  Bar-
nechea.

2.    Que  las  pendientes  sean  inferiores  a
16,7º  (30%),  lo  cual  permite  eliminar
áreas  que  no  están  urbanizadas  y  some-
tidas  a  una  insolación  diferente  al  área
metropolitana  de  Santiago.  Con  ello,  se
quedan  fuera  del  estudio  el  cordón  los
Ratones, cerro Chena, Aguirre, Colorado,
Renca, San Ignacio, La Región, San Cris-
tóbal,  Los  Cordones  y  Quilhuica,  entre
otras de menor tamaño.

Con ello se generó un área de estudio que
cubre 42 comunas y una superﬁ cie cercana a
las 190.000 hectáreas, de la cual casi un ter-
cio se encuentra urbanizada.

Se  utilizan  53  imágenes  Terra  MODIS
adquiridas  desde  el  servidor  de  imágenes
Global Visualization Viewer  del  Servicio  Geo-
lógico  de  los  Estados  Unidos  (United  States
Geological  Survey),  disponible  en  http://
glovis.usgs.gov/.  En  dicho  servidor,  se  dis-
pone  de  una  amplia  colección  de  productos
de  imágenes  de  satélite.  Para  efectos  de  este
artículo, se utilizó el producto MOD11A1, en
su versión 5.0.

El  producto  MOD11A1  corresponde
a  imágenes  de  temperatura  de  emisión  de
superficie,  en  este  caso  a  resolución  dia-
ria  y  a  una  hora  nocturna  (23:59  p.m.).  Un
importante  aspecto,  e  imprescindible,  fue
que  las  noches  fuesen  despejadas,  pues  no
existe  ningún  algoritmo  capaz  de  eliminar  la
nubosidad  y  rescatar  en  superﬁ cie  los  datos

126

R E V I S T A   D E   G E O G R A F Í A   N O R T E   G R A N D E

de  temperatura.  Las  imágenes  poseen  una
proyección  sinusoidal,  y  cubren  un  área  de
aproximadamente  1.100  x  1.100  kilómetros
(latitud  y  longitud). Además,  las  imágenes  ya
vienen corregidas, por lo tanto, este producto
está listo para su uso en aplicaciones cientíﬁ -
cas  y  publicaciones.  El  formato  de  los  datos
es HDF-EOS (Hierarchical Data Format - Earth
Observing  System  o  Formato  de  Datos  Jerár-
quicos  que  se  aplica  al  Sistema  de  Observa-
ción  de  la Tierra). Además,  dispone  de  varias
capas de información, entre las que encontra-
mos la temperatura de superﬁ cie nocturna. En
ella se indica la forma de almacenar los datos
(16  bit)  y  el  factor  de  conversión  a  Kelvin
(0,02);  por  lo  tanto,  para  cada  una  de  nues-
tras  imágenes  multiplicamos  los  valores  digi-
tales de cada píxel por 0,02 y posteriormente
restamos 273,15, quedando la temperatura en
grados Celsius.

Cabe destacar que el producto MOD11A1
versión 5 posee correcciones topográﬁ cas, de
transparencia atmosférica, remoción de nubes
que  contaminan  el  cálculo  de  la  temperatura
y un error menor de 1 K en imágenes sin cu-
bierta nubosa (Wan, 2007).

Las  imágenes  fueron  recortadas  en  fun-
ción  del  límite  del  área  de  estudio,  quedan-
do  cada  una  con  1.800  píxeles.  Para  que
ellas  fueran  comparables,  se  estandarizaron
empleando  los  puntajes  Z.  Así,  se  obtuvo  el
valor  medio  de  cada  imagen  recortada  (μ)  y
su desviación estándar (σ), los cuales se apre-
cian  en  el  Cuadro  Nº  1.  Con  dichos  paráme-
tros de la distribución normal, se aplicó para
cada píxel (X) la siguiente operación:

Z=(X - μ)/σ

Cuadro Nº 1
Media y desviación estándar de las imágenes Terra MODIS analizadas

Media
(ºC)

Desv.
Est. (ºC)

Fecha

Día

Media
(ºC)

Desv.
Est. (ºC)

Fecha

4 de enero

8 de enero

9 de enero

Día

Lunes

Viernes

Sábado

14,87

15,66

15,77

1,24 8 de mayo

1,59 5 de junio

1,74 6 de junio

10 de enero

Domingo

17,34

1,74 25 de junio

11 de enero

Lunes

13,69

1,72 27 de junio

13 de enero

Miércoles

15,11

1,75 28 de junio

Sábado

Sábado

Domingo

Viernes

Domingo

Lunes

Martes

6,44

3,09

3,31

2,56

0,18

0,34

1,47

21 de enero

22 de enero

23 de enero

2 de febrero

9 de febrero

Jueves

Viernes

Sábado

Martes

Martes

21,36

18,59

18,58

16,76

18,12

1,81 29 de junio

1,85 18 de julio

Domingo

-1,34

1,37 20 de agosto

Viernes

1,79 25 de agosto

Miércoles

1,67 5 de septiembre

Domingo

10 de febrero

Miércoles

16,71

1,65 2 de octubre

Sábado

21 de febrero

Domingo

15,79

1,59 25 de noviembre

Jueves

12,66

24 de febrero

Miércoles

15,53

1,46 5 de diciembre

Domingo

13,97

9 de marzo

Martes

14,48

1,62 8 de diciembre

Miércoles

13,54

10 de marzo

Miércoles

15,50

1,89 9 de diciembre

15 de marzo

Lunes

15,45

1,47 13 de diciembre

Jueves

Lunes

12,15

10,05

6,40

4,91

5,78

6,63

1,10

1,47

1,72

0,92

0,90

1,09

1,15

0,93

1,64

1,24

1,14

1,56

1,25

1,33

1,34

1,37

1,53

E L  E S T U D I O  D E  L A  I S L A  D E  C A L O R  U R BA NA  D E  S U P E R F I C I E  D E L  Á R E A
METROPOLITANA  DE  SANTIAGO  DE  CHILE  CON  IMÁGENES  TERRA-MODIS  Y
ANÁLISIS DE COMPONENTES PRINCIPALES

127

Continuación Cuadro Nº 1

Fecha

16 de marzo

20 de marzo

Día

Martes

Sábado

Media
(ºC)

Desv.
Est. (ºC)

Fecha

14,34

15,16

1,87 14 de diciembre

1,55 16 de diciembre

Día

Martes

Jueves

Media
(ºC)

Desv.
Est. (ºC)

14,54

14,35

24 de marzo

Miércoles

13,91

1,89 19 de diciembre

Domingo

13,46

26 de marzo

3 de abril

4 de abril

5 de abril

Viernes

Sábado

15,70

12,02

1,74 20 de diciembre

1,76 21 de diciembre

Lunes

Martes

13,78

16,97

Domingo

12,57

1,94 22 de diciembre

Miércoles

15,76

Lunes

12,28

2,05 24 de diciembre

2,05 25 de diciembre

Viernes

Sábado

14,13

16,62

1,35

0,98

1,27

1,56

1,64

1,56

1,10

1,24

1,45

1,94 26 de diciembre

Domingo

15,96

1,46

14 de abril

Miércoles

15 de abril

22 de abril

Jueves

Jueves

8,73

9,08

5,51

Fuente: Elaboración propia.

De este modo, cabe destacar que dos ter-
cios  de  las  imágenes  son  de  día  laboral  (35
imágenes,  que  representan  el  66%  del  total),
tal como se aprecia en la Figura Nº 1, y que,
además, el reparto estacional de ellas indica,
24  imágenes  de  verano,  11  de  otoño,  8  de
invierno y 10 de primavera.

Para  simpliﬁ car  los  diversos  mapas  y  re-
gistros  de  temperatura  de  las  imágenes Terra
MODIS,  se  construyeron  tres  conjuntos  de
mapas y gráﬁ cos:

Mapas de las diferencias térmicas, restan-
do  en  cada  mapa  el  valor  de  un  píxel  consi-
derado  representativo  de  las  temperaturas  no
urbanas, que en este caso fue Pirque. En total
se  obtienen  5  mapas  (uno  anual  y  cuatro  de
las estaciones).

Mapas  promedios  de  las  temperaturas
estandarizadas,  tanto  anual  como  de  cada
estación,  obteniéndose  5  mapas,  los  cuales
están  mejorados  en  resolución  mediante  in-
terpolación geoestadística Kriging ordinario.

Figura Nº 1
Distribución porcentual, según el día de la semana y la estación del año de las imágenes
trabajadas.

Fuente: Elaboración propia.

128

R E V I S T A   D E   G E O G R A F Í A   N O R T E   G R A N D E

Cuatro  mapas  del  análisis  de  componen-

tes principales con rotación Varimax.

Resultados termométricos y
mapas de diferencias térmicas

De  manera  agregada  se  calculan  los  va-
lores  de  las  temperaturas  urbanas  y  rurales,

y  para  las  4  estaciones  del  año  (ver  Figura
Nº  2).  La  ciudad  de  Santiago  es  siempre  más
cálida que su entorno rural, con intensidades
promedio  de  la  ICUs  de  0,8ºC  en  invierno,
1,5ºC en primavera, 1,9ºC en verano y 2ºC en
otoño.

Figura Nº 2
Temperaturas promedio y diferencias térmicas entre áreas urbanas y rurales según estaciones
del año

Fuente: Elaboración propia.

También se ha calculado la ICUs conside-
rando como área rural los valores termométri-
cos  de  Pirque,  y  una  agregación  comunal  de
las temperaturas de superﬁ cie. Se ha obtenido
que  las  comunas  más  cálidas  (por  encima
de  3ºC)  corresponden  a  Providencia,  Ñuñoa,
Santiago,  Independencia,  Conchalí,  Huechu-

raba  y  Estación  Central.  Las  comunas  más
frescas  son  Pirque,  Lampa,  Peñaﬂ or,  Calera
de Tango y Paine, que son periféricas (Cuadro
Nº 2). A nivel estacional y anual la Tabla Nº 2
muestra la intensidad media de la ICUs según
comuna.

Cuadro Nº 2
Resumen estadístico de la ICUs promedio a nivel comunal, tanto anual como estacional

Comuna

Providencia

Ñuñoa

Santiago

Independencia

ICUs Verano

ICUs Otoño

ICUs Invierno

4,39

3,97

3,90

3,88

4,95

3,92

4,04

3,70

3,35

2,36

2,08

1,46

ICUs
Primavera

ICUs anual

4,14

3,59

3,53

3,41

4,21

3,46

3,39

3,11

E L  E S T U D I O  D E  L A  I S L A  D E  C A L O R  U R BA NA  D E  S U P E R F I C I E  D E L  Á R E A
METROPOLITANA  DE  SANTIAGO  DE  CHILE  CON  IMÁGENES  TERRA-MODIS  Y
ANÁLISIS DE COMPONENTES PRINCIPALES

129

Continuación Cuadro Nº 2

Comuna

ICUs Verano

ICUs Otoño

ICUs Invierno

ICUs
Primavera

ICUs anual

Conchalí

Huechuraba

Estación Central

Recoleta

Las Condes

San Miguel

Quinta Normal

Renca

Pedro Aguirre Cerda

Vitacura

Cerrillos

Macul

Lo Prado

La Reina

San Joaquín

La Cisterna

Lo Espejo

Peñalolén

Cerro Navia

La Florida

La Granja

Quilicura

El Bosque

San Ramón

Maipú

Lo Barnechea

Puente Alto

San Bernardo

Colina

Padre Hurtado

La Pintana

Pudahuel

Buin

Paine

Calera de Tango

Peñaﬂ or

Lampa

Pirque

3,77

3,43

3,68

3,66

3,14

3,54

3,59

3,39

3,53

2,84

3,49

3,37

3,40

2,87

3,32

3,12

3,14

2,71

3,04

2,77

2,82

2,68

2,67

2,72

2,13

1,67

1,91

1,59

1,73

1,04

1,56

1,60

0,94

0,61

0,30

0,14

0,30

0,00

3,43

3,43

3,29

3,51

3,66

3,32

3,25

3,03

3,12

3,33

2,93

3,02

2,85

3,19

3,04

2,98

2,83

3,01

2,39

2,72

2,61

2,09

2,53

2,54

1,84

2,48

2,07

1,55

1,46

1,15

1,30

0,74

0,81

0,72

0,56

-0,04

-0,05

0,00

1,59

2,18

1,60

1,54

2,21

1,48

1,33

1,66

1,57

2,32

1,44

1,33

1,05

1,84

1,05

1,22

0,99

1,26

0,68

1,10

0,72

0,88

0,75

0,55

0,99

1,14

0,84

0,91

0,79

1,44

0,28

-0,02

0,69

0,86

1,00

0,91

-0,10

0,00

3,46

3,19

3,44

3,18

2,80

3,07

3,23

3,28

3,11

2,53

3,09

2,98

3,14

2,42

2,85

2,81

2,71

2,14

2,92

2,22

2,32

2,77

2,39

2,21

2,35

1,19

1,49

1,90

1,76

1,82

1,46

1,73

1,40

1,03

1,03

0,81

0,56

0,00

3,06

3,06

3,00

2,97

2,95

2,85

2,85

2,84

2,83

2,76

2,74

2,68

2,61

2,58

2,57

2,53

2,42

2,28

2,26

2,20

2,12

2,11

2,08

2,01

1,83

1,62

1,58

1,49

1,44

1,36

1,15

1,01

0,96

0,81

0,72

0,45

0,18

0,00

Fuente: Elaboración propia.

Con el Cuadro Nº 2 se investigó sobre las
relaciones  entre  las  intensidades  de  la  ICUs

y  las  estaciones,  encontrándose  que  todas  se
relacionan  con  una  alta  signiﬁ cancia  estadís-

130

R E V I S T A   D E   G E O G R A F Í A   N O R T E   G R A N D E

tica (p-value menor a 0,05 o nivel de conﬁ an-
za  mayor  de  95%).  No  obstante,  el  invierno
posee  coeﬁ cientes  de  correlación  de  Pearson
(r)  entre  0,66  con  verano  y  0,79  con  otoño,
mientras  que  los  otros  están  correlacionados
con un «r» mayor a 0,91. Se ha cartograﬁ ado
la  ICUs  promedio  anual  y  de  estaciones  en
mapas  que  expresan  las  diferencias  térmicas
urbano-rural. Ello se realizó restando el valor
térmico  mínimo,  el  cual  está  localizado  en
Pirque (un mismo píxel para todos las imáge-
nes Terra  MODIS),  quedando  así  selecciona-
do como representante del área rural.

Las  Figuras  Nº  3  y  N°  4  indican  que  la
intensidad  de  la  isla  de  calor  urbana  de  su-
perﬁ cie (al considerar cero en el punto de Pir-
que)  es  de  mayor  magnitud  durante  el  otoño
(7,4ºC),  seguida  de  verano  (5,9ºC),  primavera
(5,4ºC)  e  invierno  (5,0ºC).  Los  mapas  indican
que  las  estaciones  de  mayor  intensidad  de  la

isla de calor son otoño y verano, con diferen-
cias térmicas superiores a los 4,6ºC respecto a
su periferia, e incluso llegando a los 7ºC en la
zona  oriente  de  mayor  densidad  construida;
mientras que en invierno y primavera la ICUs
es de menor tamaño, y circunscrita al oriente
de la capital y la zona industrial de Quilicura.

Las  laderas  del  sector  norte  del  área  de
estudio  parecen  desempeñar  un  importante
rol  en  las  temperaturas  nocturnas,  pues  se
muestran más cálidas que los fondos de valle,
y  con  temperaturas  similares  al  centro  de  la
ciudad.

Anualmente  (Figura  Nº  5),  los  patrones
conﬁ rman que la zona oriente de la ciudad y
las  laderas  del  sector  norte  acumulan  la  ma-
yor  temperatura,  con  lo  cual,  la  ICUs  anual
supera en Santiago los 5,5ºC.

Figura Nº 3
Mapas de la isla de calor urbana de Santiago de Chile (verano y otoño)

Fuente: Elaboración propia.

E L  E S T U D I O  D E  L A  I S L A  D E  C A L O R  U R BA NA  D E  S U P E R F I C I E  D E L  Á R E A
METROPOLITANA  DE  SANTIAGO  DE  CHILE  CON  IMÁGENES  TERRA-MODIS  Y
ANÁLISIS DE COMPONENTES PRINCIPALES

131

Figura Nº 4
Mapas de la isla de calor urbana de Santiago de Chile (invierno y primavera)

Fuente: Elaboración propia.

Figura Nº 5.
Mapas anuales de la isla de calor urbana de Santiago de Chile.

Fuente: Elaboración propia.

Síntesis del análisis de los
mapas estandarizados

Los mapas estandarizados de las tempera-
turas  de  superﬁ cie  fueron  promediados  para

cada  estación  del  año  (verano,  otoño,  invier-
no y primavera), además de uno anual. Todos
ellos  muestran  que  la  isla  de  calor  tiende  a
localizar  el  máximo  térmico  en  las  comunas
de Santiago, Providencia, Las Condes, Ñuñoa
y Vitacura,  conformando  un  núcleo  cálido

132

R E V I S T A   D E   G E O G R A F Í A   N O R T E   G R A N D E

asociado  a  la  mayor  densidad  construida.
Además,  las  comunas  de  Huechuraba  y  Qui-
licura  conforman  otro  núcleo  cálido,  el  que
está  asociado  a  viviendas  de  alto  nivel  de
ingresos  en  el  primer  caso  e  industrias  en  el
caso de Quilicura.

El  lector  advertirá  al  observar  las  ﬁ guras
promedio  estandarizadas  de  las  temperaturas
superﬁ ciales  nocturnas  que  la  periferia  de  la
ciudad  es  generalmente  fría,  lo  cual  resulta
del efecto isla de calor. No obstante, se debe
matizar tres singularidades interesantes:

Por  un  lado,  el  río  Maipo  en  el  límite  de
las  comunas  de  Buin  y  San  Bernardo  es,  du-
rante todo el año, más cálido que su entorno
(Figuras  Nº  6  a  8),  siendo  incluso  el  fenóme-
no  más  acusado  en  invierno.  Esto  se  explica
por las propiedades térmicas del agua, la cual
posee una alta capacidad de almacenar calor
y  una  elevada  inercia  térmica.  Este  fenóme-
no  también  es  apreciable,  aunque  en  menor
proporción,  en  el  río  Mapocho,  cerca  de  la
comuna de Padre Hurtado.

La zona norte del área estudiada, es decir,
Lampa  y  Colina,  presentan  en  sus  terrenos

más  elevados  (sin  superar  los  1.150  m.s.n.m
ﬁ jados), tanto en las faldas de la cordillera de
la  Costa  como  en  los  cordones  de  Chicureo,
una  superficie  recalentada,  lo  cual  puede
deberse  a  ﬂ ujos  nocturnos  de  montaña-valle
de carácter catabático. Esto genera una franja
que a las 0:00 a.m. es más cálida que los fon-
dos de valle, los cuales se presentan tan fríos
como muestran los registros de Pirque y Buin
(incluso  en  Puente  Alto  es  notorio).  Lo  ante-
riormente señalado es más intenso en otoño e
invierno (Figuras Nº 6 a 8).

Una  evidente  vaguada  térmica  que  ingre-
sa  a  la  ciudad  desde  la  comuna  de  La  Pin-
tana,  la  cual  posee  población  de  bajo  nivel
socioeconómico, alcanzando incluso parte de
las comunas de La Florida y La Granja en in-
vierno (Figuras Nº 6 a N° 8). Además, la cuña
es  poco  perceptible  en  primavera,  debido  a
las aguas frías de fusión del Maipo.

Salvando  estas  tres  peculiaridades,  los  re-
sultados indican una clara isla de calor urba-
na de superﬁ cie, con dos núcleos principales
de  mayor  nivel  térmico.  Asimismo,  ella  se
maniﬁ esta durante todo el año.

Figura Nº 6
Mapas promedio estandarizados de las temperaturas de verano y otoño

Fuente: Elaboración propia.

E L  E S T U D I O  D E  L A  I S L A  D E  C A L O R  U R BA NA  D E  S U P E R F I C I E  D E L  Á R E A
METROPOLITANA  DE  SANTIAGO  DE  CHILE  CON  IMÁGENES  TERRA-MODIS  Y
ANÁLISIS DE COMPONENTES PRINCIPALES

133

Figura Nº 7
Mapas promedio estandarizados de las temperaturas de invierno y primavera

Fuente: Elaboración propia.

Figura Nº 8
Mapa promedio estandarizado de las temperaturas anuales

Fuente: Elaboración propia.

Síntesis del Análisis de
Componentes Principales de
los mapas estandarizados

Con  el  propósito  de  conocer  los  patrones
típicos  que  adquiere  la  isla  de  calor  se  optó,

además de construir los mapas de promedios,
por realizar un análisis de componentes prin-
cipales.  Esta  técnica  permite  resumir  las  53
imágenes  en  nuevos  factores  complejos  que
explican  gran  parte  de  la  varianza,  y  posibi-
lita interpretar los patrones espaciales asocia-
dos a ellos.

134

R E V I S T A   D E   G E O G R A F Í A   N O R T E   G R A N D E

En  primer  lugar,  se  generó  la  matriz  de
correlación  de  las  imágenes,  y  con  ello  se
consiguió  detectar  días  con  baja,  moderada,
acusada y muy acusada correlación. Los días
comprendidos  entre  el  5  de  junio  y  el  2  de
octubre (a excepción del 25 de agosto) no se
relacionan  con  el  resto  de  los  días  del  año;
al  igual  que  las  imágenes  del  21  de  enero  y
el  13  de  diciembre. Todas  ellas  poseen  una
conﬁ guración  de  los  máximos  de  tempera-
tura  localizados  al  sur  y  poniente  del  área
Metropolitana  de  Santiago  de  Chile,  desde
Buin hasta Pudahuel. El resto de los días está
altamente correlacionado, y muestra patrones
más  concéntricos  a  las  comunas  de  Santiago
y Providencia.

Luego  de  obtener  las  correlaciones  entre
las  imágenes  se  ha  estimado  la  comunalidad
(h2) por el cuadrado del coeﬁ ciente de corre-
lación  múltiple  entre  x  y  las  demás  variable.
Ellas  explican  el  peso  de  cada  uno  de  los
días  en  la  varianza  explicada.  En  general  los
valores  son  mayores  a  0,8.  No  obstante,  hay
tres días que no superan dicho valor, los cua-
les  corresponden  a  situaciones  de  invierno
(25  y  27  de  junio  y  18  de  julio).  En  dichos

casos,  la  configuración  sinóptica  de  la  to-
pografía  de  500  hPa  muestra  un  bajo  índice
de  circulación  zonal  del  oeste,  con  vaguada
polar y una depresión aislada en niveles altos
(DANA),  desplazando  la  isla  de  calor  más  al
norte de la ciudad. Las mayores comunalida-
des  (iguales  o  superiores  a  0,97)  correspon-
den  a  6  casos,  centrados  entre  verano  y  oto-
ño,  siendo  los  de  los  días  22  de  enero,  21  y
24 de febrero, 10 y 16 de marzo y 4 de abril.

Comprobadas  las  comunalidades  se  esta-
blece el número de componentes principales.
El  Cuadro  Nº  3  resume  para  las  10  primeras
componentes  la  distribución  de  la  varian-
za  total  explicada  mediante  ACP.  En  ella  se
aprecia  que  luego  de  rotar  la  matriz  con  el
método Varimax (Kaiser, 1958) y aplicando la
regla  de  Kaiser  (1960),  es  decir,  conservando
aquellos  factores  cuyos  valores  propios  o
eigenvalues  sean  mayores  a  1,  y  el  criterio
del «scree graph» (Cattell, 1966), basta con 4
factores para explicar el 90,7% de la varianza
total. Así,  el  componente  1  rotado  explica  el
44,5%  de  la  varianza  total,  el  componente
2, un 22,2%, el 3, un 20,2% y, ﬁ nalmente, el
componente 4, un 3,6%.

Cuadro Nº 3
Varianza explicada del ACP, rotadas con el método varimax.

Comp.

Autovalores iniciales

Sumas de las saturaciones al
cuadrado de la extracción

Suma de las saturaciones al
cuadrado de la rotación

Total

% de la
varianza

%
acumulado

Total

% de la
varianza

%
acumulado

Total

% de la
varianza

%
acumulado

1

2

3

4

5

6

7

8

9

10

40,573

76,552

76,552 40,573

76,552

76,552 23,619

44,563

3,606

2,842

1,025

0,671

0,452

0,379

0,295

0,268

0,235

6,804

5,362

1,935

1,265

0,854

0,716

0,556

0,506

0,444

83,356

3,606

88,719

2,842

90,653

1,025

6,804

5,362

1,935

83,356 11,798

22,261

88,719 10,721

20,229

90,653

1,908

3,600

91,919

92,772

93,488

94,045

94,550

94,994

44,563

66,824

87,053

90,653

Fuente: Elaboración propia.

La matriz de carga factorial, indica el gra-
do de correspondencia entre las variables (es
decir cada uno de los 53 días) y los factores,

los  cuales  ya  se  presentan  rotados.  Como  se
sabe  en  ACP,  lo  ideal  es  que  cada  variable
posea  un  peso  alto  en  un  factor  y  bajo  en

E L  E S T U D I O  D E  L A  I S L A  D E  C A L O R  U R BA NA  D E  S U P E R F I C I E  D E L  Á R E A
METROPOLITANA  DE  SANTIAGO  DE  CHILE  CON  IMÁGENES  TERRA-MODIS  Y
ANÁLISIS DE COMPONENTES PRINCIPALES

135

los  demás,  facilitando  la  interpretación  (y
parsimonia)  de  los  factores.  Podemos  decir
que  la  mayoría  de  los  días  son  asignados  al
componente rotado 1 (RPC1), y que ninguno
carga  al  RPC4.  Esto  implica  que  este  último
factor  es  meramente  complementario,  lo
cual  se  verá  mejor  explicado  en  los  mapas
de  componentes  rotados.  Para  construir
cada factor lo que se hace matemáticamente
es  una  suma  de  cada  día  multiplicada  por
el  valor  de  cada  carga  factorial.  Siendo  el
primer  factor  rotado  «0,830*04  de  enero
+  0,778*08  de  enero+  0,662*09  de  ene-
ro+….….+  0,861*26  de  diciembre»  para
cada uno de los 1.800 píxeles.

Los  mapas  de  componentes  principales
rotados  (ver  Figuras  Nº  9  y  N°  10)  muestran
los  patrones  espaciales  que  ﬁ nalmente  serán
interpretados.  Es  conveniente  recordar  que
ellos  explican  el  90,65%  de  la  varianza  to-
tal.  Cada  uno  de  ellos  será  interpretado  en
concomitancia  con  las  distribuciones  de  las
puntuaciones  de  cada  factor  (previamente
rotado)  en  el  espacio,  lo  cual  no  necesaria-
mente implica que valores altos se relacionen
con  mayor  temperatura.  Las  conﬁ guraciones
de  los  factores  rotados  se  nominan  de  la  si-
guiente manera:

-  RPC1  (ver  Figura  Nº  9).  Isla  de  calor  ur-
bana  asociada  a  la  cuña  de  las  activida-
des  industriales.  Gran  parte  de  la  ciudad
muestra valores altos de esta componente,
pero,  sin  duda,  es  mayor  en  las  comunas
más  ligadas  a  actividades  industriales,  lo-
calizadas de modo contiguo a la Paname-
ricana, al norte de la comuna de Santiago,
generando  una  dorsal  que  alcanza  gran
parte de la comuna de Colina.

-  RPC2  (ver  Figura  Nº  9).  Isla  de  calor  del
piedmont y cuña de población de altos in-
gresos económicos. El piedmont de la ciu-
dad  (entre  Pirque  y  Colina  al  norte),  ade-
más de las laderas de los cerros aislados y
la cordillera de la Costa, muestran valores
altos  del  factor,  al  igual  que  las  comunas
donde  se  localizan  las  actividades  de  ser-
vicios, oﬁ cinas y la población de mayores
ingresos  económicos  (Providencia,  Las
Condes, Vitacura).  La  mayor  presencia  de
esta conﬁ guración es en el invierno, justa-
mente cuando las brisas montaña valle se
hacen más importantes.

-  RPC3  (ver  Figura  Nº10).  Situaciones  sin
isla  de  calor  urbana.  Este  factor  indica
que  sus  valores  máximos  y  los  de  las
temperaturas  en  el  interior  de  la  ciudad
son  notoriamente  menores  a  los  del  sec-

Figura Nº 9
Mapas de los factores 1 y 2 derivados del análisis de componentes principales

Fuente: Elaboración propia.

136

R E V I S T A   D E   G E O G R A F Í A   N O R T E   G R A N D E

tor  periférico  del  sur  y  poniente,  lo  que,
pese  a  ocurrir  en  pocos  días  distribuidos
en todas las estaciones del año, no posee
una  variable  que  permita  explicarlos  (se
ha revisado causas asociadas a los vientos
regionales,  circulación  sinóptica,  tempe-
ratura, humedad, nubosidad y nieblas).

-  RPC4  (ver  Figura  Nº  10).  Situación  com-
plementaria a los componentes principales
rotados  RPC1  y  RPC2,  es  decir,  bajo  pre-
sencia  de  isla  de  calor  urbana  de  superﬁ -
cie. Destaca el sur con una dorsal térmica
y  zonas  más  cálidas  que  la  zona  oriente
de  la  ciudad,  mientras  que  las  comunas
del norte se muestran mucho más frías.

Figura Nº 10
Mapas de los factores 3 y 4 derivados del análisis de componentes principales

Fuente: Elaboración propia.

Islas de Calor Urbana
de Superﬁ cie del Área
Metropolitana de Santiago

Una  de  las  hipótesis  de  la  investigación
señala  que  “el  uso  de  la  teledetección  a  una
resolución  espacial  moderada  es  un  procedi-
miento  adecuado  para  el  análisis  y  la  carac-
terización  espacial  y  temporal  de  la  ICUs”,
lo  que  ciertamente  se  ha  comprobado.  Esto
es  así  porque  la  teledetección  permite  un
adecuado  número  de  observaciones  en  una
ciudad  del  tamaño  del  Área  Metropolitana
de  Santiago  de  Chile.  Efectivamente,  son
1.800  observaciones  puntuales,  algo  que  sin
duda  es  una  cobertura  densa,  e  imposible
de  conseguir  a  costos  razonables  a  través  de
otros métodos, como transectos en automóvil
o  una  red  de  estaciones  ﬁ jas.  No  obstante,

no  es  una  escala  adecuada  para  observar  los
cañones urbanos. Es decir, su resolución de 1
km permite cartograﬁ ar patrones de la isla de
calor, tal y como se consigue con menor pre-
cisión con transectos o datos de observatorios
meteorológicos,  pero  no  así  los  microclimas
urbanos, que sí se consigue con imágenes Te-
rra ASTER. A continuación, en la Figura Nº 11
se muestra un ejemplo con estas imágenes en
Santiago para una madrugada de 2006 (Sarri-
colea,  2010).  Es  posible  apreciar  en  la  ﬁ gura
que las calles se muestran más cálidas, y que
existe consistencia con los resultados de Terra
MODIS.

La  ciudad  presenta  la  ICUs  en  las  áreas
más  densamente  construidas,  y  también  en
aquellas dedicadas a actividades industriales.
Además, en la Figura Nº 12, de resolución 90
m,  prácticamente  todos  los  cañones  urbanos

E L  E S T U D I O  D E  L A  I S L A  D E  C A L O R  U R BA NA  D E  S U P E R F I C I E  D E L  Á R E A
METROPOLITANA  DE  SANTIAGO  DE  CHILE  CON  IMÁGENES  TERRA-MODIS  Y
ANÁLISIS DE COMPONENTES PRINCIPALES

137

de la ciudad son más cálidos que su entorno,
tal como dice Eliasson (1994). Las áreas rura-
les se presentan más frías que la ciudad, con
algunas excepciones, y los cursos de agua en
la  fecha  de  la  observación  también  son  más
cálidos.

No  obstante,  hay  asuntos  referidos  a  la
distribución  de  las  temperaturas  que  aún  no
se  han  explicado  de  manera  óptima.  Uno  de
ellos  tiene  relación  con  patrones  no  espera-
dos,  y  que,  además,  poseen  una  persistencia
notable  tanto  en  espacio  como  el  tiempo.
Nos  referimos  al  efecto  que  las  laderas  del
norte  ejercen  sobre  las  temperaturas  de  emi-
sión superﬁ cial, alcanzando valores próximos
al centro urbano.

Figura Nº 11
Temperatura de emisión superﬁ cial a las 0:00
a. m. del día 28/04/2006, usando sensor
Terra ASTER.

Fuente: Sarricolea (2010)

Más  aún,  las  áreas  del  poniente  en  algu-
nas noches también se presentan más cálidas
que  la  ciudad,  tal  como  conﬁ rma  el  ACP  en
su  factor  rotado  RPC3.  Una  posible  hipótesis
que aquí proponemos es la retroalimentación
del  calor  por  efecto  sumidero  y  la  suma  de

las  brisas  campo-ciudad  y  la  catabática.  Esto
se  puede  apreciar  esquemáticamente  en  la
Figura  Nº  12,  la  cual  muestra  que  la  brisa
de  la  cordillera  de  los  Andes  barre  la  ICU,
y  es  relocalizada  al  poniente  de  la  ciudad.
El  efecto  sumidero  de  calor  o  «urban  heat
sink»  (Carnahan  y  Larson,  1990)  es  similar  a
lo encontrado en la mañana para Santiago de
Chile  por  Peña  (2008),  pero  en  nuestro  caso
es  constatado  en  la  noche,  y  asumiendo  la
convección de calor en el centro y su redistri-
bución a la periferia poniente, lo que en días
de  contaminación  por  material  particulado
(PM10) tendría efectos nocivos sobre la salud
de esta población.

Para  conocer  de  mejor  manera  la  conﬁ -
guración  de  la  isla  de  calor  es  fundamental
contar con un buen modelo de los vientos, lo
cual  ya  ha  sido  enunciado  por  Cuadrat  et  al.
(2003  y  2005).  Por  ello,  se  propone  generar
en  el  futuro  un  modelo  mesoescalar  de  vien-
tos,  similar  al  existente  para  Chile-Central,
pero  con  la  novedad  de  incorporar  la  para-
metrización  del  efecto  urbano,  tal  como  lo
expone  Martilli  (2010)  en  el  caso  de  Madrid.
Por lo tanto, se espera desarrollar para Santia-
go un modelo que permita mejorar el conoci-
miento  del  comportamiento  del  viento  a  las
0:00  a.  m.,  pues  el  nivel  de  detalle  actual  es
el que se muestra en la Figura Nº 13.

Respecto  a  la  estacionalidad  de  la  isla  de
calor, se han encontrado resultados inversos a
los  de  la  ciudad  de  Seúl  (Kim  y  Baik,  2002),
es  decir,  en  promedio  la  máxima  intensidad
de la ICUs en Santiago es más alta en verano
y otoño, siendo relativamente débil en prima-
vera  e  invierno.  Esto  puede  deberse  a  que  el
calor  antropogénico  a  la  latitud  de  Santiago
(33º  30’  S)  no  suele  superar  el  aporte  ener-
gético  de  la  radiación  solar,  a  excepción  del
sector  oriente,  donde  debe  ser  importante  el
uso  de  sistemas  de  calefacción  y  aire  acon-
dicionado  por  los  hogares  y  las  abundantes
oﬁ cinas y actividades comerciales.

En  la  Figura  Nº  14  llama  la  atención  que
el  método  de  clasiﬁ cación  automática  de  si-
tuaciones  sinópticas  de  Jenkinson  y  Collison
(J&C)  arroje  5  días  de  tipo  ciclónico,  para  el
conjunto  de  días  analizado,  de  los  cuales  4
son de ICUs muy fuerte (Sarricolea et al., 2014).
Revisando  los  tipos  de  tiempo  ciclónicos  y

138

R E V I S T A   D E   G E O G R A F Í A   N O R T E   G R A N D E

Figura Nº 12
Esquema hipotético de días de débil o nula ICU en la ciudad y sector poniente más cálido.

Fuente: Elaboración propia.

Figura Nº 13
Dirección y velocidad del viento del 11 de abril de 2012 a las 0:00 a.m. Dominio de mayor detalle
para Chile Central.

Fuente: Dirección Meteorológica de Chile. Disponible en inter-
net: http://www.meteochile.cl/modeloMM5dominio3_c.html.

sus  híbridos  nos  encontramos  con  días  de
temperaturas superiores a 26ºC, lo cual impli-
ca  que  son  bajas  térmicas. A  su  vez,  los  días

de  ICUs  moderada  se  corresponden  con  días
con  altas  térmicas  (situaciones  anticiclónicas
de invierno).

E L  E S T U D I O  D E  L A  I S L A  D E  C A L O R  U R BA NA  D E  S U P E R F I C I E  D E L  Á R E A
METROPOLITANA  DE  SANTIAGO  DE  CHILE  CON  IMÁGENES  TERRA-MODIS  Y
ANÁLISIS DE COMPONENTES PRINCIPALES

139

Figura Nº 14
Número de días analizados con Terra MODIS según tipo de tiempo de J&C y categorías de ICUs.

Fuente: Elaboración propia.

Conclusiones

Los  sensores  de  moderada  resolución  en
ciudades como Santiago son muy adecuados,
más  aún  al  ser  procesadas  sus  imágenes  me-
diante  Sistemas  de  Información  Geográﬁ ca,
lo  que  mejora  bastante  su  calidad  gráfica
para el estudio de la ICUs.

En  especial,  las  imágenes  Terra  MODIS
vienen listas para ser procesadas, son de reso-
lución  diaria  y  gratuitas.  Por  lo  tanto,  permi-
ten  caracterizar  espacial  y  temporalmente  la
isla  de  calor.  El  único  inconveniente  que  po-
seen es el hecho de no registrar la temperatu-
ra  superﬁ cial  en  días  nublados.  No  obstante,
como la ICUs es un fenómeno estructural del
clima  urbano,  una  muestra  de  días  despeja-
dos es suﬁ ciente para caracterizarla.

La  isla  de  calor  urbana  de  superﬁ cie  y  el
máximo  térmico  de  la  ciudad  de  Santiago  se
localizan, efectivamente, en la zona más den-
samente  construida.  Sin  embargo,  también
coincide con la zona industrial de Quilicura.
Es  decir,  la  hipótesis  se  confirma,  pero  se
debe precisar que tanto las zonas más densa-
mente  construidas,  como  las  industriales,  de
Santiago poseen una marcada ICUs.

La  intensidad  de  la  isla  de  calor  urbana
de  superﬁ cie  es  de  mayor  magnitud  durante
el  otoño  (7,4ºC),  seguida  de  verano  (5,9ºC),
primavera (5,4ºC) e invierno (5,0ºC), y con un
máximo  en  los  barrios  donde  se  localiza  la

población  de  mayores  ingresos  económicos.
Pero  las  áreas  verdes  mitigan  su  intensidad,
incluso  el  albedo  de  dicha  zona,  que  es  más
bajo  en  comparación  con  el  resto  de  la  ciu-
dad.

El  análisis  de  componentes  principales
revela  cuatro  patrones  típicos  de  ICUs,  que
explican el 90,6% de las situaciones, a saber:
ICUs  consolidada  (44,5%),  ICUs  del  pied-
mont  y  cuña  de  altos  ingresos  (22,3%),  un
tipo  sin  isla  de  calor  urbana  (20,2%)  e  ICUs
más intensa al sur (3,6%).

De  las  situaciones  sin  isla  de  calor,  se  ha
sugerido  la  hipótesis  de  efecto  sumidero  de
calor  o  «urban  heat  sink»,  asociado  a  fuerte
brisa  de  la  cordillera  de  los  Andes,  que  ba-
rre  la  ICUs  y  la  desplaza  al  poniente  de  la
ciudad, lo que en días de contaminación por
material  particulado  (PM10)  tendría  efectos
nocivos sobre la salud de la población de esa
parte de la ciudad.

Referencias bibliográﬁ cas

ARNFIELD,  J. Two  Decades  of  Urban  Cli-
mate  Research:  A  Review  of Turbulence,  Ex-
changes  of  Energy  and Water,  and  the  Urban
Heat  Island.  International  Journal  of  Climato-
logy, 2003, Vol. 1, N° 23, p. 1-26.

CARNAHAN, W. & LARSON, R. An analy-
sis  of  an  urban  heat  sink.  Remote  Sensing  of
Environment, 1990, Vol. 33, p. 65-71.

140

R E V I S T A   D E   G E O G R A F Í A   N O R T E   G R A N D E

CATTELL,  R. The  screen  test  for  the  num-
ber  of  factors.  Multivariate  Behavioral  Re-
search, 1966, Vol. 1, p. 245-276.

KIM, Y.  &  BAIK,  J.  Maximum  Urban  Heat
Island  Intensity  in  Seoul.  Journal  of  Applied
Meteorology, 2002, N° 41, p. 651-659.

CHEVAL,  S.  &  DUMISTRECU, A. The  July
urban  heat  island  of  Bucharest  as  derived
from MODIS images. Theoretical and Applied
Climatology, 2009, Vol. 96, p. 145–153.

CLINTON, N. & GONG, P. MODIS detec-
ted surface urban heat islands and sinks: Glo-
bal locations and controls. Remote Sensing of
Environment, 2013, Vol. 134, p. 294–304.

CUADRAT,  J.;  SAZ,  M.  & VICENTE-SE-
RRANO,  S.  Surface  wind  direction  inﬂ uence
on  spatial  patterns  of  urban  heat  island  in
Zaragoza  (Spain).  Geophysical  Research Abs-
tracts, 2007, Vol. 5, s/p.

CUADRAT,  J.; VICENTE-SERRANO,  S.  &
SAZ, M. Los efectos de la urbanización en el
clima  de  Zaragoza  (España):  La  Isla  de  Calor
y  sus  factores  condicionantes.  Boletín  de  la
A.G.E., 2005, Nº 40, p. 311-327.

ELIASSON,  I.  Urban-suburban-rural  air
temperature  differences  related  to  street  geo-
metry.  Physical  Geography,  1994, Vol.  15,  p.
1-22.

JIN,  M.  &  SHEPHERD,  J.  Inclusion  of  ur-
ban  landscape  in  a  climate  model.  How  can
satellite  data  help?  Bulletin  of  the  American
Meteorological  Society,  2005, Vol.  86,  N°  5,
p. 681–689.

JOHNSON,  D.  Urban  modification  of
diurnal  temperature  cycles  in  Birmingham,
U.K.  International  Journal  of  Climatology,
1985, Vol. 5, p. 221–225.

KAISER,  H.  The  Varimax  criterion  for
analytic rotation in factor analysis. Psychome-
trika, 1958, Vol. 23, p. 187-200.

KAISER,  H. The  application  of  electronic
computers to factor analysis. Educational and
Psychological  Measurement,  1960,  N°  20,  p.
141-151.

KARL, T.; DIAZ, H. & KUKLA, G. Urbani-
zation:  Its  Detection  and  Effect  in  the  United
States  Climate  Record.  Journal  of  Climate,
1998, Vol. 1, p. 1099-1123.

KUKLA,  G.;  GAVIN,  J.  &  KARL, T.  Urban
Warming. Journal of Climate and Applied Me-
teorology, 1986, N° 25, p. 1265-1270.

MARTILLI,  A.  Modelización  del  clima  ur-

bano a mesoecala. Madrid: AEC, 2010.

NICHOL,  J.  A  GIS-based  approach  to
microclimate  monitoring  in  Singapure’s  high-
rise  housing  estates.  Photogrammetric  Engi-
neering and Remote Sensing, 1994, N° 60, p.
1225-1232.

OKE,  T.  &  VOOGT,  J.  Complete  urban
surface  temperatures.  Journal  of  Applied  Me-
teorology, 1997, Vol. 9, N° 36, p. 1117-1132.

PEÑA, M. Relationships between remotely
sensed surface parameters associated with the
urban  heat  sink  formation  in  Santiago,  Chi-
le.  International  Journal  of  Remote  Sensing,
2008, Vol. 29, N° 15, p. 4385-4404.

RAJASEKAR,  U.  & WENG,  Q.  Urban  heat
island  monitoring  and  analysis  using  a  non-
parametric  model:  A  case  study  of  Indiana-
polis. Journal of Photogrammetry and Remote
Sensing, 2008, N° 64, p. 86–96.

ROMERO,  H.;  IRARRÁZAVAL,  F.;  OPAZO,
D.; SALGADO, M. & SMITH, P. Climas urbanos
y  contaminación  atmosférica  en  Santiago  de
Chile. EURE, 2010a, Vol. 36, N° 109, p. 35-62.

ROMERO,  H.;  SALGADO,  M.  &  SMITH,
P.  Cambios  climáticos  y  climas  urbanos:  Re-
laciones  entre  zonas  termales  y  condiciones
socioeconómicas de la población de Santiago
de Chile. Revista INVI, 2010b, Vol. 25, N° 70,
p. 151-179.

SARRICOLEA,  P.  Climatología  urbana
mediante  el  uso  de  la  teledetección:  aporta-
ciones  a  la  planiﬁ cación  territorial  y  gestión
ambiental del área metropolitana de Santiago.
Barcelona:  Universitat  de  Barcelona,  Depar-
tamento  de  Geografía  Física  y  A.G.R.  Barce-
lona, 2010.

SARRICOLEA,  P.;  MESEGUER-RUIZ,  O.  y
MARTÍN-VIDE,  F. Variabilidad  y  tendencias

E L  E S T U D I O  D E  L A  I S L A  D E  C A L O R  U R BA NA  D E  S U P E R F I C I E  D E L  Á R E A
METROPOLITANA  DE  SANTIAGO  DE  CHILE  CON  IMÁGENES  TERRA-MODIS  Y
ANÁLISIS DE COMPONENTES PRINCIPALES

141

climáticas  en  Chile  central  en  el  período
1950-2010 mediante la determinación de los
tipos  sinópticos  de  Jenkinson  y  Collison.  Bo-
letín de la A.G.E., 2014, Nº 64, p. 227-247.

TOROK, S.; MORRIS, C.; SKINNER, C.; &
PLUMMER,  N.  Urban  heat  island  features  of
southeast Australian towns. Australian Meteo-
rological Magazine, 2001, N° 50, p. 1–13.

SCHWARZ,  N.;  LAUTENBACH,  S.  &  SEP-
PELT,  R.  Exploring  indicators  for  quantifying
surface  urban  heat  islands  of  European  cities
with  MODIS  land  surface  temperatures.  Re-
mote Sensing of Environment, 2011, Vol. 115,
N° 12, p. 3175–3186.

SCHWARZ,  N.;  SCHLINK,  U.;  FRANCK,
U.  &  GROßMANN,  K.  Relationship  of  land
surface  and  air  temperatures  and  its  implica-
tions  for  quantifying  urban  heat  island  indi-
cators—An  application  for  the  city  of  Leipzig
(Germany).  Ecological  Indicators,  2012,  N°
18, p. 693–704.

STEWART,  I.  &  OKE, T.  Classifying  urban
climate  ﬁ eld  sites  by  “local  climate  zones”:
The case of Nagano, Japan. In: Seventh Inter-
national  Conference  on  Urban  Climate,  June
29 – July 3 of 2009, Yokohama.

STREUTKER, D. Satellite-measured growth
of  the  urban  heat  island  of  Houston, Texas.
Remote  Sensing  of  Environment,  2003, Vol.
85, p. 282–289.

VOOGT,  J.  &  OKE,  T.  Thermal  Remote
Sensing  of  Urban  Climates.  Remote  Sensing
of Environment, 2003, N° 86, p. 370-384.

WAN,  Z.  Collection-5.  MODIS  Land
Surface Temperature  Products  Users’  Guide.
Santa  Bárbara:  ICESS,  2007.  Disponible  en
internet:  http://www.icess.ucsb.edu/modis/Ls-
tUsrGuide/MODIS_LST_products_Users_gui-
de_C5.pdf

WELLER,  J.  & THORNES,  J.  An  investiga-
tion  of  winter  nocturnal  air  and  road  surface
temperature  variation  in  the  West  Midlands,
UK  under  different  synoptic  conditions.
Meteorological  Applications,  2001,  N°  8,  p.
461–474.

WENG,  Q. Thermal  infrared  remote  sen-
sing  for  urban  climate  and  environmental
studies:  Methods,  applications,  and  trends.
Journal  of  Photogrammetry  and  Remote  Sen-
sing, 2009, N° 64, p. 335–344.

