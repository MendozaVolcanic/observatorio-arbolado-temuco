Article
Heat on the Move: Contrasting Mobile and Fixed Insights into
Temuco’s Urban Heat Islands

Aner Martinez-Soto 1,*
and Matthew Shupler 3

, Michelle Vera-Fonseca 1, Pablo Valenzuela-Toledo 2, Aliwen Melillan-Raguileo 2

1 Department of Civil Engineering, Faculty of Engineering and Science, Universidad de La Frontera,

Temuco 4811230, Chile; m.vera06@ufromail.cl

2 Department of Computer Science, Faculty of Engineering and Science, Universidad de La Frontera,

Temuco 4811230, Chile; pablo.valenzuela@ufrontera.cl (P.V.-T.); aliwen.melillan@ufrontera.cl (A.M.-R.)

3 Department of Epidemiology, Harvard T.H. Chan School of Public Health, Boston, MA 02115, USA
* Correspondence: aner.martinez@ufrontera.cl; Tel.: +56-4525-96816

Abstract: This study evaluates the combined use of mobile transects and fixed stations to
analyze atmospheric urban heat islands (UHIs’a) in Temuco, Chile. Data were collected
using 23 fixed stations and 3 mobile transects traversing predefined city routes, captur-
ing temperature records at one-minute intervals. Results revealed moderate correlations
between methodologies (coefficients: 0.55–0.62) and average temperature differences of
0.72 ◦C to 1.6 ◦C, confirming their compatibility for integrated use. UHI intensities ranged
from weak (0.5 ◦C) to extremely strong (13 ◦C), with the highest urban temperature (33.1 ◦C)
observed in Zone Z-3, contrasting with 25.4 ◦C at the rural Maquehue station. Simulations
and isothermal maps identified four UHI zones, highlighting the influence of impervious
surfaces, traffic density, and limited vegetation on temperature distribution. Fluctuation
plots revealed rapid cooling in vegetated areas and high heat retention in dense urban
zones. These findings validate the methodologies for spatial and temporal UHI analysis
and provide actionable insights for urban planning. Targeted interventions, such as increas-
ing vegetation in high-risk zones, are recommended to mitigate extreme heat and enhance
thermal comfort in urban areas.

Academic Editor: Michele Penza

Keywords: urban heat islands; mobile transects; fixed stations

Received: 23 December 2024

Revised: 17 January 2025

Accepted: 13 February 2025

Published: 18 February 2025

Citation: Martinez-Soto, A.;

Vera-Fonseca, M.; Valenzuela-Toledo,

P.; Melillan-Raguileo, A.; Shupler, M.

Heat on the Move: Contrasting Mobile

and Fixed Insights into Temuco’s

Urban Heat Islands. Sensors 2025, 25,

1251. https://doi.org/10.3390/

s25041251

Copyright: © 2025 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license

(https://creativecommons.org/

licenses/by/4.0/).

1. Introduction

The expansion of urban centers and their growth into peripheral areas have signifi-
cantly altered local weather patterns, primarily through changes in land cover and urban
infrastructure [1]. This transformation has led to the replacement of natural surfaces, which
dissipate radiative energy, with urban materials that absorb and retain heat, resulting in
elevated temperatures in urban areas. This phenomenon, known as the urban heat island
(UHI), is defined as the temperature difference between urban zones and their surrounding
rural areas at a given time [2–4].

The UHI effect significantly increases energy demand for cooling in urban areas. For
instance, in Tampico, Mexico, UHI effects have been shown to raise nighttime temperatures
by up to 2.5 ◦C, reducing nighttime cooling and increasing indoor discomfort levels [5]. On
a larger scale, energy consumption can rise by 10–25% during summer months due to the
UHI effect, which also leads to higher emissions of greenhouse gases like carbon dioxide
and nitrogen oxide, intensifying smog formation and contributing to global warming [6,7].
Such emissions are estimated to account for over 70% of urban air pollution during peak

Sensors 2025, 25, 1251

https://doi.org/10.3390/s25041251

Sensors 2025, 25, 1251

2 of 18

UHI events, particularly in regions with dense populations and limited vegetation [8]. Pro-
jections from the Intergovernmental Panel on Climate Change (IPCC) indicate that global
temperatures may rise by 1.4 ◦C to 5.8 ◦C by 2100, compared to 1990 levels [9,10]. Extreme
cases, such as Kuwait City, highlight the severity of these issues, with annual temperature
increases of 0.3 ◦C to 0.8 ◦C and frequent occurrences of temperatures exceeding 50 ◦C [11].
Heatwaves, intensified by global warming, further amplify the UHI effect, impacting
human health and comfort. For example, the 2003 European heatwave caused an esti-
mated 70,000 deaths, while similar events in Russia (2010) and India (2015) led to over
20,500 fatalities, with UHI effects compounding the risks [4,12]. UHI intensities have
been observed year-round, during both day and night. In Ias, i, Romania, nighttime UHI
intensities range from 3.0 ◦C to 4.0 ◦C, while Mexico City experiences daytime intensities of
3.0 ◦C to 5.0 ◦C during the rainy season [13,14]. In Phoenix, Arizona, UHI intensities range
from 0.8 ◦C to 5.4 ◦C depending on seasonal conditions [15,16]. These findings emphasize
the global prevalence of UHIs, regardless of geographic location.

Several methodologies have been developed to quantify UHI intensity, including mo-
bile transects, fixed weather stations, and satellite imagery. Mobile transects, used for over
40 years, provide spatially detailed data but are limited to capturing static moments. For
instance, Martínez (2014) measured UHI intensities of up to 4.5 ◦C in Alicante, Spain, but
the method failed to depict diurnal variability [17]. Fixed weather stations offer continuous
data, as demonstrated in Athens, Greece, where UHI intensities reached 5 ◦C during the
summer [14,17]. However, such networks are costly to maintain and often insufficient
for spatial coverage [18]. Satellite imaging provides extensive spatial coverage, as seen
in Johannesburg, where UHI intensities of 2.0–3.5 ◦C were observed. Yet, this method
primarily measures surface temperatures and may not correlate with air temperatures,
leading to potential errors of up to 1.68 ◦C, as seen in Apatity, Russia [19,20]. Emerging
techniques and frameworks have furthered UHI analysis. Local Climate Zones (LCZs),
a classification system for urban areas based on land use and morphology, improve UHI
mapping by considering factors such as building density, vegetation, and surface type [16].
In Xi’an, China, LCZ-based studies revealed that UHI intensities in compact high-rise zones
exceeded those in open low-rise zones by up to 5.6 ◦C, with shielding effects from tall build-
ings also altering pedestrian-level temperatures [21]. Similarly, integrating crowdsourced
data, such as temperature sensors embedded in personal vehicles, enables high-resolution
UHI mapping, revealing localized cooling effects from parks and green spaces. For instance,
in Rennes and Dijon, France, green areas reduced temperatures by up to 3.5 ◦C [22]. Despite
these advancements, the simultaneous validation and comparison of methodologies remain
underexplored. For example, in Utrecht, combining fixed station and mobile transect
data reduced measurement discrepancies by over 15%, demonstrating the potential for
integrated approaches [23]. However, such efforts are rare in under-represented regions
like Chile, where most UHI studies focus on central areas, using either mobile transects
or satellite data [1,24,25]. Southern cities, such as Temuco, remain largely unexamined
despite their unique climatic and urban characteristics, including high annual precipitation
exceeding 1200 mm and heterogeneous land cover [26,27].

This study aims to measure and analyze UHI intensity in Temuco, Chile, through
the combined application of fixed station and mobile transect methods. By validating
the integration of these approaches and georeferencing UHI zones, this research provides
a robust framework for understanding UHI dynamics in diverse climatic regions and
supports urban planning strategies to mitigate its impacts on quality of life.

Sensors 2025, 25, 1251

3 of 18

2. Methodology
2.1. Study Area: Temuco

Temuco, located at latitude 38◦44′00′′ S and longitude 72◦35′00′′ W, spans an area of
464 km2. The city is geographically defined by the Ñielol and Conunhueno hills, with
altitudes of 335 m and 360 m above sea level, respectively. The Cautín River traverses
the city, flowing northeast to southwest and contributing to the region’s microclimatic
conditions [28]. These geographic features contribute to the region’s distinct microclimatic
conditions, including localized variations in temperature and humidity. Temuco has experi-
enced steady population growth over recent decades. Between 2002 and 2015, its population
increased from 227,086 to 275,617 inhabitants [29,30]. This urban expansion has led to the
construction of extensive residential neighborhoods, replacing vegetation with impervious
surfaces such as concrete and asphalt. These materials have higher heat retention capacities,
which significantly contribute to the urban heat island (UHI) phenomenon, resulting in
increased urban temperatures [31]. Studies in similar urbanizing regions suggest that such
land cover changes can amplify daytime temperatures by 2–3 ◦C while reducing nighttime
cooling [32]. Temuco’s climate is classified as Csb under the Köppen climate classification,
characterized by cold winters and dry summers, with mean annual temperatures exceeding
10 ◦C. Typical maximum and minimum temperatures range from 23 ◦C to 1 ◦C, respec-
tively [33]. However, recent trends indicate a departure from historical climatic norms.
Temperature data from the Maquehue weather station (38◦44′00′′ S, 72◦35′00′′ W) reveal
that 6.65% of days between 2000 and 2019 recorded maximum temperatures above 30 ◦C,
compared to only 3.2% of days during the 1980–2000 period. This doubling of extreme
heat events underscores a clear warming trend. A record high of 40.2 ◦C was observed
on 15 February 2019, at 3:00 PM, highlighting the intensifying thermal extremes. Seasonal
analysis shows February accounts for approximately 50% of the highest temperatures,
followed by January (43.75%) and March (6.25%).

The region’s warming trend aligns with broader climatic shifts observed across south-
ern Chile. Studies suggest that regional warming, exacerbated by global climate change, is
particularly pronounced in urbanized areas like Temuco, where vegetation loss and high
urban density intensify heat retention [34]. Moreover, UHIs in Mediterranean climates,
such as Temuco, are particularly severe during summer, with differences of up to 9 ◦C
between urban and rural areas observed in similar Chilean cities [35]. Temuco’s rapid
population growth, urban expansion, and distinct climatic and geographic features make it
a relevant study area for examining UHI effects. This study aims to quantify UHI intensity
in the city by integrating fixed weather station data with mobile transects, providing a
comprehensive understanding of the phenomenon and its implications for urban planning
and public health.

2.2. Procedure to Contrast Heat Island Location Methodologies

Urban heat islands (UHIs) are classified into two distinct types: surface urban heat
islands (UHIs’s) and atmospheric urban heat islands (UHIs’a) [36]. Surface UHIs refer to
the thermal differences between artificial and natural surfaces, while atmospheric UHIs
refer to the air temperature differences observed between various urban zones [36]. Each
type of UHI requires specific methodologies to determine its intensity. Satellite image
analysis is typically employed to assess UHIs’s, as it captures surface temperatures over
large spatial areas. In contrast, UHIs’a, which focus on air temperatures, are evaluated
using methods such as mobile transects or fixed weather stations [37]. In this study, the
focus was on UHIs’a, as they provide a direct understanding of temperature impacts
on human comfort and energy use. Data for UHI’a analysis were collected using two
complementary methodologies: mobile transects and fixed stations. Both approaches

Sensors 2025, 25, 1251

4 of 18

rely on air temperature measurements but differ in their spatial and temporal resolutions.
Mobile transects, conducted with high-resolution sensors mounted on moving vehicles,
offer detailed spatial data across urban and rural zones. Fixed stations provide continuous
temporal data at specific locations, allowing long-term trends to be observed.

These complementary datasets enable a robust comparison of UHI’a intensity and
distribution. The datasets generated by the two methodologies were contrasted using three
key statistical measures: Pearson’s correlation coefficient, average temperature difference,
and standard deviation. Pearson’s correlation coefficient was used to assess the degree of
similarity between the two datasets, providing a quantitative measure of methodological
consistency (see Table 1 for interpretation). Correlation values ranging from 0.75 to 1.0 indicate
strong alignment, reflecting a high degree of methodological reliability [32]. In addition
to correlation, average temperature differences and standard deviations were calculated
to evaluate methodological precision and variability. The choice of Pearson’s correlation
coefficient is supported by studies demonstrating its effectiveness in comparing urban and
(2023) highlighted its utility in
rural temperature profiles. For example, Moreno et al.
understanding urban–rural thermal contrasts and vegetation’s mitigating effects [32]. Similarly,
Verichev et al. (2023) emphasized that statistical metrics like standard deviation are critical
for interpreting variations in cooling degree days (CDDs) across urban landscapes, further
validating its inclusion in this study [38].

Table 1. Coefficient classification of Pearson’s correlation values according to Zühlke [39].

Correlation

Pearson’s Correlation Coefficient (r)

Interpretation

Perfect
Very strong
Medium
Weak
None
Very weak

r = 1
0.75 ≤ r ≤ 1
0.50 ≤ r ≤ 0.75
0.00 ≤ r ≤ 0.50
0.00
−1 ≤ r ≤ 0.00

Perfect similarity, identical profiles
Very similar, significant similarity
Moderate similarity
Little similarity
No correlation
Very large differences, opposite curves

Furthermore, methodological comparisons in similar studies have demonstrated the
unique strengths and limitations of mobile transects and fixed stations. Mobile transects
are particularly valuable for mapping spatial gradients of UHI intensity, capturing urban-
to-rural transitions that are often missed by fixed stations [34]. On the other hand, fixed
stations provide continuous, high-frequency data, making them ideal for temporal analysis
of diurnal and seasonal UHI patterns. By integrating these methods, this study achieves a
more comprehensive analysis of UHI’a intensity in Temuco.

2.2.1. Mobile Transect Method

The mobile transect method involves collecting air temperature data by traversing
predefined routes through the city, capturing localized temperature variations in urban
and surrounding areas [40]. In this study, three mobile transects were conducted simultane-
ously using three vehicles equipped with HOBO Pendant MX2201 and MX2202 sensors
(HOBO®, Bourne, MA, USA). These sensors are responsive to thermal variations, with a
measurement range of −20 ◦C to 70 ◦C and an accuracy of ±0.5 ◦C. Their specifications
ensure precise temperature data collection, necessary for analyzing the urban heat island
(UHI) phenomenon.

Before data collection, the three sensors were calibrated to ensure consistent measure-
ments. Calibration involved recording air temperatures under conditions with direct solar
radiation and minimal shading to test sensor accuracy. The calibration process verified that
the maximum variation among sensors was ±0.15 ◦C, ensuring reliability during the study.

Sensors 2025, 25, 1251

5 of 18

The sensors were mounted on the passenger-side windows of the vehicles to avoid interfer-
ence from engine heat and urban obstructions. The vehicles traveled at an average speed
of 30 km/h, which allowed for the collection of detailed temperature gradients while main-
taining consistency across all routes. Each data point was georeferenced using GPS, and the
data were downloaded via Bluetooth using the HOBOmobile platform, available on Android,
iOS, and Windows. Measurements were conducted between 20:00 and 20:30 to minimize the
influence of direct solar radiation. At this time, urban infrastructure begins releasing heat
absorbed during the day, offering a representation of UHI effects. This timing aligns with
standard practices for UHI analysis and ensures comparability with previous studies.

The design of the transect routes was informed by previous UHI analyses conducted in
Temuco on 27 November 2017 and 19 January 2018, when the highest annual temperatures
of 28.5 ◦C and 31.4 ◦C were recorded, respectively. The data from these dates identified four
key UHI zones in the city: Z-1, Z-2, Z-3, and Z-4 (Figure 1). These zones were characterized
by distinct environmental and urban features. Z-1 (Coord.: −38.709179, −72.554418) and
Z-3 (Coord.: −38.742428, −72.643479) showed limited vegetation within urbanized areas
compared to surrounding green spaces, leading to significant heat retention during the
day. Conversely, Z-2 (Coord.: −38.753900, −72.624335) and Z-4 (Coord.: −38.726355,
−72.619119) experienced heavy traffic congestion, contributing to high anthropogenic
heat emissions.

Figure 1. Location of the UHI in Temuco on 27 November 2017 at 9:00 p.m. (left) and 19 January 2018 at
8:00 p.m. (right) to determine the circuit to carry out the measurements with mobile transects.

Based on these findings, three simultaneous routes were defined to maximize spatial
coverage and accurately represent the UHI phenomenon in Temuco (Figure 2). Transect
1 (red) covered a total distance of 10.50 km, traversing the city from north to south along
Avenida Caupolicán and passing through Z-1 and Z-2. Transect 2 (magenta) spanned
10.35 km from the western sector of the city to the northeast, covering Z-3 and Z-4. Transect
3 (green) extended 10.73 km, initially crossing the city from north to south before following
the Cautín River in an east–west direction through Z-2. The overlapping endpoints of
Transects 2 and 3 were designed to analyze temperature reduction rates across the period
of measurement.

To confirm that the chosen routes represented the thermal profile of the UHI, a prior
simulation of the UHI phenomenon was performed using isothermal maps derived from
fixed station data (discussed in Section 2.3). This simulation supported the selection of
routes and ensured that the mobile transects captured the spatial distribution of temperature
variations across the city.

Sensors 2025, 25, x FOR PEER REVIEW 5 of 19   avoid interference from engine heat and urban obstructions. The vehicles traveled at an average speed of 30 km/h, which allowed for the collection of detailed temperature gra-dients while maintaining consistency across all routes. Each data point was georeferenced using GPS, and the data were downloaded via Bluetooth using the HOBOmobile plat-form, available on Android, iOS, and Windows. Measurements were conducted between 20:00 and 20:30 to minimize the influence of direct solar radiation. At this time, urban infrastructure begins releasing heat absorbed during the day, offering a representation of UHI effects. This timing aligns with standard practices for UHI analysis and ensures com-parability with previous studies. The design of the transect routes was informed by previous UHI analyses conducted in Temuco on 27 November 2017 and 19 January 2018, when the highest annual tempera-tures of 28.5 °C and 31.4 °C were recorded, respectively. The data from these dates iden-tified four key UHI zones in the city: Z-1, Z-2, Z-3, and Z-4 (Figure 1). These zones were characterized by distinct environmental and urban features. Z-1 (Coord.: −38.709179, −72.554418) and Z-3 (Coord.: −38.742428, −72.643479) showed limited vegetation within urbanized areas compared to surrounding green spaces, leading to significant heat reten-tion during the day. Conversely, Z-2 (Coord.: −38.753900, −72.624335) and Z-4 (Coord.: −38.726355, −72.619119) experienced heavy traffic congestion, contributing to high anthro-pogenic heat emissions.  Figure 1. Location of the UHI in Temuco on 27 November 2017 at 9:00 p.m. (left) and 19 January 2018 at 8:00 p.m. (right) to determine the circuit to carry out the measurements with mobile tran-sects. Based on these findings, three simultaneous routes were defined to maximize spatial coverage and accurately represent the UHI phenomenon in Temuco (Figure 2). Transect 1 (red) covered a total distance of 10.50 km, traversing the city from north to south along Avenida Caupolicán and passing through Z-1 and Z-2. Transect 2 (magenta) spanned 10.35 km from the western sector of the city to the northeast, covering Z-3 and Z-4. Tran-sect 3 (green) extended 10.73 km, initially crossing the city from north to south before following the Cautín River in an east–west direction through Z-2. The overlapping end-points of Transects 2 and 3 were designed to analyze temperature reduction rates across the period of measurement. To confirm that the chosen routes represented the thermal profile of the UHI, a prior simulation of the UHI phenomenon was performed using isothermal maps derived from fixed station data (discussed in Section 2.3). This simulation supported the selection of routes and ensured that the mobile transects captured the spatial distribution of temper-ature variations across the city. Sensors 2025, 25, 1251

6 of 18

Figure 2. Route to capture data with the mobile transect method (red for transect 1, magenta for
transect 2, and green lines for transect 3) and fixed stations distributed in different points of the city
(black points).

2.2.2. Fixed Station Method

For the fixed station method, this study utilized temperature data collected by the
National Monitoring Network (ReNaM). This network consists of 23 intelligent sensors (Ne-
tatmo), represented as black dots in Figure 2. These sensors are installed in private homes
distributed across various zones in Temuco, providing spatial coverage for monitoring
urban heat island (UHI) intensity.

The Netatmo weather stations comprise two devices (interior and exterior) made
of UV-resistant aluminum. The exterior sensors operate within a measurement range of
−40 ◦C to 65 ◦C with an accuracy of ±0.3 ◦C. To ensure data reliability, the outdoor sensors
are protected from direct solar radiation and precipitation, minimizing potential sources of
error. Temperature data are captured at 30-min intervals, following a predefined schedule
(e.g., 8:00, 8:30, 9:00) to standardize the time of measurements and reduce temporal vari-
ability. These sensors were calibrated and validated by the Ministry of Housing and Urban
Development (MINVU) in conjunction with the Chile Foundation, ensuring alignment with
national standards.

To ensure consistency between datasets collected via the fixed stations and the mobile
transects, the temperature data from the HOBO and Netatmo sensors were compared
prior to analysis. This comparison showed an average variation of 0.48 ◦C between the
two devices, indicating that the potential influence of differing sensors on temperature
measurements was minimal.

2.3. Methodologies for UHI Simulation and Location in Temuco

This study utilized a structured methodological framework to simulate and locate urban
heat islands (UHIs) in Temuco. The framework consists of three main stages: analysis and data
preprocessing, data formatting and sampling, and image generation using processed data.

Sensors 2025, 25, x FOR PEER REVIEW 6 of 19    Figure 2. Route to capture data with the mobile transect method (red for transect 1, magenta for transect 2, and green lines for transect 3) and fixed stations distributed in different points of the city (black points). 2.2.2. Fixed Station Method For the fixed station method, this study utilized temperature data collected by the National Monitoring Network (ReNaM). This network consists of 23 intelligent sensors (Netatmo), represented as black dots in Figure 2. These sensors are installed in private homes distributed across various zones in Temuco, providing spatial coverage for moni-toring urban heat island (UHI) intensity. The Netatmo weather stations comprise two devices (interior and exterior) made of UV-resistant aluminum. The exterior sensors operate within a measurement range of −40 °C to 65 °C with an accuracy of ±0.3 °C. To ensure data reliability, the outdoor sensors are protected from direct solar radiation and precipitation, minimizing potential sources of error. Temperature data are captured at 30-minute intervals, following a predefined schedule (e.g., 8:00, 8:30, 9:00) to standardize the time of measurements and reduce tem-poral variability. These sensors were calibrated and validated by the Ministry of Housing and Urban Development (MINVU) in conjunction with the Chile Foundation, ensuring alignment with national standards. To ensure consistency between datasets collected via the fixed stations and the mo-bile transects, the temperature data from the HOBO and Netatmo sensors were compared prior to analysis. This comparison showed an average variation of 0.48 °C between the two devices, indicating that the potential influence of differing sensors on temperature measurements was minimal. 2.3. Methodologies for UHI Simulation and Location in Temuco This study utilized a structured methodological framework to simulate and locate urban heat islands (UHIs) in Temuco. The framework consists of three main stages: anal-ysis and data preprocessing, data formatting and sampling, and image generation using processed data. These steps were implemented to ensure an accurate representation of the UHI phenomenon and to enable visualization through heat island maps and fluctuation plots [41]. The first stage involved analyzing temperature data collected on 4 December 2019, when the Maquehue station recorded a maximum temperature of 25.4 °C, one of the Sensors 2025, 25, 1251

7 of 18

These steps were implemented to ensure an accurate representation of the UHI phenomenon
and to enable visualization through heat island maps and fluctuation plots [41].

The first stage involved analyzing temperature data collected on 4 December 2019,
when the Maquehue station recorded a maximum temperature of 25.4 ◦C, one of the highest
temperatures observed that month. Data preprocessing included correcting records with
erroneous numerical formats, filtering out dates without associated data, and generating a
standardized CSV file containing the parameters Date–Time, Station Identifier, Temperature
(◦C), Latitude, and Longitude (Table 2). This processed file served as the input for the
image generation process.

Table 2. CSV file format with parameters Date-Time, ID, Temperature, Coordinates (Latitude,
Longitude) processed from ReNaM data.

Date–Time

2017-01-10 00:00:00
2017-01-10 00:00:00
2018-12-11 23:30:00

ID

245
246
294

T [◦C]

9.0
9.4
15.2

Latitude

−38.721
−38.707
−38.740

Longitude

−72.600
−72.665
−72.648

Two types of visualizations were created to analyze UHI characteristics: heat island
maps and fluctuation plots. The heat island maps depict the UHI phenomenon at specific
times by plotting isotherms based on recorded temperature data. These isotherms were con-
structed using Delaunay’s triangulation, which connects data points into non-overlapping
triangles and ensures a structured spatial interpolation of temperature distributions [42].
Each isotherm was represented in a distinct color, with red indicating high temperatures
and blue representing cooler zones [42]. Fluctuation plots, on the other hand, illustrate
24-h temperature variations recorded at the stations with the highest and lowest tempera-
tures during the study period. Data from the official Maquehue weather station were also
included to provide an external reference point outside the urban area.

The intensity of UHIs was calculated for each time period using the following equation:

UH I Intensity = TU,max − TR,min

where

•
•

TU,max: Maximum urban temperature recorded within the city.
TR,min: Minimum temperature recorded in the surrounding rural areas, serving as a
reference for non-urban conditions

UHI intensities were classified according to Table 3, which categorizes the effects into
five levels: weak, moderate, strong, very strong, and extremely strong. This classification
provides a standardized interpretation of temperature differentials observed during the
study. To reconcile the differing temporal resolutions of fixed station and mobile transect
data, the fixed station data (recorded at 30-min intervals) were interpolated to match the
one-minute frequency of the mobile transects. Linear interpolation was used to estimate
intermediate temperature values, ensuring consistency and comparability across datasets.

Sensors 2025, 25, 1251

8 of 18

Table 3. Classification and temperature ranges associated with UHI intensity based on [43].

Classification

Intensity

Interpretation

Weak

UHI ≤ 2 ◦C

Moderate

2 ◦C < UHI ≤ 4 ◦C

Strong

4 ◦C < UHI ≤ 6 ◦C

Very strong

6 ◦C < UHI ≤ 8 ◦C

Extremely strong

8 ◦C < UHI

There is no major difference between the
temperature in the city and
adjacent sectors
There is a slight difference between the
temperature in the city and adjacent
sectors not perceptible by people
The difference in temperature between
the city and adjacent sectors is
moderately perceptible by people
There is a big difference in temperature
between the city and adjacent sectors
very perceptible by people
The difference in temperature between
the city and adjacent sectors is extreme
and dangerous for people

The methodology integrates robust data preprocessing, standardized classification
frameworks, and advanced spatial analysis techniques to visualize UHI phenomena. To
ensure consistency and comparability between the fixed station and mobile transect method-
ologies, all temperature measurements were conducted at a standardized height of 1.5 m
above the ground. This height was chosen to align with common practices in UHI studies
and minimize variability introduced by differing sensor elevations [44–47]. Maintaining
the same height for both methodologies reduces the potential influence of ground-level
heat, which can significantly elevate temperatures closer to the surface [48]. This approach
ensures that the recorded temperatures reflect ambient air conditions rather than localized
ground heat, thereby enhancing the reliability of the data for UHI analysis. By standardiz-
ing sensor height, the study provides a robust basis for comparing spatial and temporal
variations in temperature between methodologies. Despite these strengths, potential chal-
lenges such as sensor placement biases and interpolation uncertainties were mitigated
through sensor calibration, validation, and data cross-referencing to enhance reliability
and accuracy.

3. Results
3.1. Temperature Patterns and Spatial Variability Across Transects

Figures 3–5 illustrate a comparison of the temperature records obtained using the mo-
bile transect and fixed station methodologies. These records were compared to determine
how close the values are that these methodologies provide and to be able to validate their
use separately or combined.

Transect 1 covered the route represented in red in Figure 2 of 10.5 km, where temper-
ature data were captured every one minute. The route took thirty minutes, where thirty
points were captured along the route. Figure 3 provides the graphical representation of
the temperatures recorded by the transect contrasted with the temperatures obtained by
isothermal maps given by the fixed station methodology. It is observed that both method-
ologies yield similar temperature records. From record N◦ 1 to record N◦ 12, there is an
increase in temperature, after which there is a decrease until record N◦ 15. The similarity
between the records obtained with the two methodologies is confirmed with the correlation
coefficient of 0.55.

Sensors 2025, 25, 1251

9 of 18

Figure 3. Comparison of temperatures recorded in Transect 1 and UHI simulations based on fixed
stations for the time period corresponding to 20:00 h and 21:00 h.

Figure 4. Comparison of temperatures recorded in Transect 2 and UHI simulations based on fixed
stations for the time period corresponding to 20:00 h and 21:00 h.

The greatest maximum temperature difference between the two methodologies at the
same point reached 1.76 ◦C, located at the moment at which the city is entered, where
the change in temperature is considerable. However, the average temperature difference
captured by the two methodologies along the entire route was 0.72 ◦C, which implies that
the classification of the UHI phenomenon is not altered by the points that have the greatest
temperature difference. The standard deviation between the two temperature datasets is
0.5. This value is very close to the accuracy of the sensor, which implies that the dispersion
of the data is not significant.

Sensors 2025, 25, x FOR PEER REVIEW 9 of 19    Figure 3. Comparison of temperatures recorded in Transect 1 and UHI simulations based on fixed stations for the time period corresponding to 20:00 h and 21:00 h.  Figure 4. Comparison of temperatures recorded in Transect 2 and UHI simulations based on fixed stations for the time period corresponding to 20:00 h and 21:00 h. Sensors 2025, 25, x FOR PEER REVIEW 9 of 19    Figure 3. Comparison of temperatures recorded in Transect 1 and UHI simulations based on fixed stations for the time period corresponding to 20:00 h and 21:00 h.  Figure 4. Comparison of temperatures recorded in Transect 2 and UHI simulations based on fixed stations for the time period corresponding to 20:00 h and 21:00 h. Sensors 2025, 25, 1251

10 of 18

Figure 5. Comparison of temperatures recorded in Transect 3 and UHI simulations based on fixed
stations for the time period corresponding to 20:00 h and 21:00 h.

Transect 2 performed the route represented by magenta in Figure 2, which took
26–36 min. The circuit covered 10.35 km, where 36 temperature records were captured. It
might be considered that, unlike Transect 1, the route ran through sectors with high traffic
congestion, which acquired a larger amount of temperature data in a shorter distance.
In Figure 4, it is possible to visualize with the fixed station methodology that there are
four zones in the city with high temperatures. These zones are not clearly reflected in the
mobile transect methodology. However, it is noted that the intensity of both temperature
records decreases until record N◦ 29, when they begin to increase their intensity again. The
similarity between the values is confirmed with the correlation coefficient of 0.61, a value
classified as mean correlation.

The greatest maximum temperature difference captured by both methodologies at
the same point was 2.91 ◦C, whereas the average temperature difference captured by both
methodologies at the same point was 1.6 ◦C, a lower value than the ranges for which the
UHI is defined, which does not alter its classification. The standard deviation that yields
this temperature dataset is 0.65. This value indicates that despite analyzing the intensity of
the phenomenon with the most distant record, its classification did not change.

Transect 3 performed the route represented in green in Figure 2 of 10.73 km, where
data were captured for 30 min, creating a record of 30 points. Although the distance was
greater than the other transects, the sector encompassed has few traffic lights, which makes
the traffic steady and flow better. Figure 5 shows that the similarity in the two records is
greater than Transects 1 and 2. With both methodologies it is observed that the journey goes
between zones in the city that have a lower temperature to zones with a higher temperature.
Figure 5 shows that both temperature intensities of the zones covered begin to decrease
until record N◦ 8, the point where the temperatures in the zones begin to increase. This
similarity that the records have in the increase and decrease in their intensity in similar
ranges is confirmed by the correlation coefficient of 0.62. This value is classified as mean
correlation.

The greatest maximum temperature difference captured was 2.7 ◦C, whereas the
average temperature difference captured by both methodologies at the same point was
1.2 ◦C, a lower value than the ranges for which the UHI intensity is defined that does not
alter its classification. The standard deviation obtained from this temperature dataset is
0.91, a range in which the data tend to disperse.

Sensors 2025, 25, x FOR PEER REVIEW 10 of 19    Figure 5. Comparison of temperatures recorded in Transect 3 and UHI simulations based on fixed stations for the time period corresponding to 20:00 h and 21:00 h. Transect 2 performed the route represented by magenta in Figure 2, which took 26–36 min. The circuit covered 10.35 km, where 36 temperature records were captured. It might be considered that, unlike Transect 1, the route ran through sectors with high traffic congestion, which acquired a larger amount of temperature data in a shorter distance. In Figure 4, it is possible to visualize with the fixed station methodology that there are four zones in the city with high temperatures. These zones are not clearly reflected in the mo-bile transect methodology. However, it is noted that the intensity of both temperature records decreases until record N° 29, when they begin to increase their intensity again. The similarity between the values is confirmed with the correlation coefficient of 0.61, a value classified as mean correlation. The greatest maximum temperature difference captured by both methodologies at the same point was 2.91 °C, whereas the average temperature difference captured by both methodologies at the same point was 1.6 °C, a lower value than the ranges for which the UHI is defined, which does not alter its classification. The standard deviation that yields this temperature dataset is 0.65. This value indicates that despite analyzing the intensity of the phenomenon with the most distant record, its classification did not change. Transect 3 performed the route represented in green in Figure 2 of 10.73 km, where data were captured for 30 min, creating a record of 30 points. Although the distance was greater than the other transects, the sector encompassed has few traffic lights, which makes the traffic steady and flow better. Figure 5 shows that the similarity in the two rec-ords is greater than Transects 1 and 2. With both methodologies it is observed that the journey goes between zones in the city that have a lower temperature to zones with a higher temperature. Figure 5 shows that both temperature intensities of the zones covered begin to decrease until record N° 8, the point where the temperatures in the zones begin to increase. This similarity that the records have in the increase and decrease in their in-tensity in similar ranges is confirmed by the correlation coefficient of 0.62. This value is classified as mean correlation. The greatest maximum temperature difference captured was 2.7 °C, whereas the av-erage temperature difference captured by both methodologies at the same point was 1.2 °C, a lower value than the ranges for which the UHI intensity is defined that does not alter its classification. The standard deviation obtained from this temperature dataset is 0.91, a range in which the data tend to disperse. Sensors 2025, 25, 1251

11 of 18

3.2. Location of Heat Islands in Temuco

Figure 6 shows the isothermal map (left) and fluctuation plot (right) generated at the time
and in the sector where the city reaches its maximum temperature. The maximum tempera-
ture reached in Temuco is visualized on the isothermal map in Zone 3 (Coord.: −38.740785,
−72.645474) at 14:00 h with 33.1 ◦C. The minimum temperature reached in the city at the same
time was located in Zone 2 (Coord.: −38.745916, −72.633190), with 29.7 ◦C. The intensity of
the UHI phenomenon was 3.4 ◦C, classified as a moderate UHI. However, when calculating
the intensity of the phenomenon on the basis of the temperature of the Maquehue station at
14:00 h (20.1 ◦C), 13 ◦C of difference is obtained between the urban and rural sectors, which
classifies the UHI as extremely strong. The fluctuation plot (Figure 6, right) also shows that
the maximum temperature in the city (Stn. 288) increases and decreases in short periods of
time. This may be due to the fact that in the zone where the temperature peak is reached, there
is abundant vegetation and most of the infrastructures are isolated houses, which allow for
rapid air circulation and therefore reduce the temperature in the sector. Additionally, this area,
located in the suburban outskirts of the city, has historically maintained a high percentage
of green spaces and vegetation due to its prior classification as a rural zone. Recent urban
development has introduced residential buildings, yet the general layout continues to support
efficient air flow due to its flat terrain and dispersed infrastructure. These characteristics
collectively contribute to the localized reduction in temperature, emphasizing the role of
vegetation and urban design in mitigating UHI effects in this region.

Figure 6. Simulation of the UHI phenomenon in Temuco using fixed station methodology (left) and
fluctuation plot (right) on 4 December 2019, between sectors that have the maximum and minimum
temperatures at 14:00 h.

In Figure 6, it is observed that in addition to the zone with the maximum temperature
(Z-3), there are two sectors that tend to have a higher temperature than the rest of the city
(Z-1 and Z-4).

Figure 7 (left) shows the 24-h temperature fluctuation at station 247 in Zone
4 (Coord.:−38.733095, −72.6031539), where a temperature of 30.2 ◦C was recorded at
14:00 h. When calculating the temperature difference in the sector compared to the temper-
ature at the Maquehue station at the same time, a UHI intensity of 10.1 ◦C was obtained, a
value classified as an extremely strong UHI. However, when calculating the temperature
difference that exists between city sectors, an intensity of 0.5 ◦C was obtained, classifying it
as a weak UHI. Figure 7 (right) represents the temperatures at station 256 in Zone 1 (Coord.:
−38.697133, −72.535842), which reached a temperature of 31.8 ◦C at 14:00 h. When deter-
mining the intensity of the UHI phenomenon, there was a difference of 11.7 ◦C, classifying
it as an extremely strong UHI. By linking the minimum temperature found in the city to the
temperature in the sector at the same time, a temperature difference of 2.1 ◦C was obtained,
classifying it as a moderate UHI. When comparing any point of the city with an external
point, intensities over 10 ◦C were reached. This would mean that the UHI phenomenon
would influence the microclimate in every sector in the city.

Sensors 2025, 25, x FOR PEER REVIEW 11 of 19   3.2. Location of Heat Islands in Temuco Figure 6 shows the isothermal map (left) and fluctuation plot (right) generated at the time and in the sector where the city reaches its maximum temperature. The maximum temperature reached in Temuco is visualized on the isothermal map in Zone 3 (Coord.: −38.740785, −72.645474) at 14:00 h with 33.1 °C. The minimum temperature reached in the city at the same time was located in Zone 2 (Coord.: −38.745916, −72.633190), with 29.7 °C. The intensity of the UHI phenomenon was 3.4 °C, classified as a moderate UHI. However, when calculating the intensity of the phenomenon on the basis of the temperature of the Maquehue station at 14:00 h (20.1 °C), 13 °C of difference is obtained between the urban and rural sectors, which classifies the UHI as extremely strong. The fluctuation plot (Fig-ure 6, right) also shows that the maximum temperature in the city (Stn. 288) increases and decreases in short periods of time. This may be due to the fact that in the zone where the temperature peak is reached, there is abundant vegetation and most of the infrastructures are isolated houses, which allow for rapid air circulation and therefore reduce the temper-ature in the sector. Additionally, this area, located in the suburban outskirts of the city, has historically maintained a high percentage of green spaces and vegetation due to its prior classification as a rural zone. Recent urban development has introduced residential buildings, yet the general layout continues to support efficient air flow due to its flat ter-rain and dispersed infrastructure. These characteristics collectively contribute to the local-ized reduction in temperature, emphasizing the role of vegetation and urban design in mitigating UHI effects in this region.  Figure 6. Simulation of the UHI phenomenon in Temuco using fixed station methodology (left) and fluctuation plot (right) on 4 December 2019, between sectors that have the maximum and minimum temperatures at 14:00 h. In Figure 6, it is observed that in addition to the zone with the maximum temperature (Z-3), there are two sectors that tend to have a higher temperature than the rest of the city (Z-1 and Z-4). Figure 7 (left) shows the 24-hour temperature fluctuation at station 247 in Zone 4 (Coord.:−38.733095, −72.6031539), where a temperature of 30.2 °C was recorded at 14:00 h. When calculating the temperature difference in the sector compared to the temperature at the Maquehue station at the same time, a UHI intensity of 10.1 °C was obtained, a value classified as an extremely strong UHI. However, when calculating the temperature differ-ence that exists between city sectors, an intensity of 0.5 °C was obtained, classifying it as a weak UHI. Figure 7 (right) represents the temperatures at station 256 in Zone 1 (Coord.: −38.697133, −72.535842), which reached a temperature of 31.8 °C at 14:00 h. When deter-mining the intensity of the UHI phenomenon, there was a difference of 11.7 °C, classifying it as an extremely strong UHI. By linking the minimum temperature found in the city to the temperature in the sector at the same time, a temperature difference of 2.1 °C was obtained, classifying it as a moderate UHI. When comparing any point of the city with an Sensors 2025, 25, 1251

12 of 18

Figure 7. Fluctuation plot with stations in the city that record high temperatures compared to their
adjacent sectors. Station 247 left plot. Zone 4 −38.733095, −72.6031539. Station 256 right plot. Zone 1
−38.697133, −72.535842.

4. Discussion

The 3D representation of temperature variations across mobile transects in Temuco
(Figure 8) highlights significant spatial heterogeneity, particularly at the intersections of
transects. These variations underscore the localized thermal dynamics shaped by urban
morphology and anthropogenic factors. For example, at the downtown intersection of Mobile
Transects 1 and 2, temperatures differ by approximately 5 ◦C, with Transect 1 recording
near 25 ◦C and Transect 2 around 20 ◦C. Similarly, in Zone 2 (Z-2), Transect 1 registers
temperatures near 23 ◦C, contrasting with Transect 3 at approximately 18 ◦C. These findings
corroborate research demonstrating significant microclimatic variability even within short
distances, influenced by urban structures and heat retention properties [49,50].

Figure 8. Three-dimensional representation of temperature variations across mobile transects in Temuco.

Such variations are consistent with studies emphasizing the critical role of land use
and cover changes in shaping urban microclimates [51,52]. Urban centers, dominated
by impervious surfaces and high-density constructions, intensify the urban heat island
(UHI) effect through reduced evapotranspiration and increased thermal inertia [53,54].
Conversely, areas with greater vegetation cover demonstrate cooler temperatures, under-
scoring the role of green spaces in mitigating UHI effects [51,55]. The observed variations
at transect intersections further reflect the methodological challenges inherent in mobile
monitoring campaigns, as highlighted in other studies. For instance, differences in tim-
ing, measurement resolution, and urban characteristics can contribute to discrepancies in
recorded temperatures [50,56]. This underscores the importance of integrating mobile and
fixed monitoring systems to enhance spatial and temporal data resolution [52,54].

Sensors 2025, 25, x FOR PEER REVIEW 12 of 19   external point, intensities over 10 °C were reached. This would mean that the UHI phe-nomenon would influence the microclimate in every sector in the city.  Figure 7. Fluctuation plot with stations in the city that record high temperatures compared to their adjacent sectors. Station 247 left plot. Zone 4 −38.733095, −72.6031539. Station 256 right plot. Zone 1 −38.697133, −72.535842. 4. Discussion The 3D representation of temperature variations across mobile transects in Temuco (Figure 8) highlights significant spatial heterogeneity, particularly at the intersections of transects. These variations underscore the localized thermal dynamics shaped by urban morphology and anthropogenic factors. For example, at the downtown intersection of Mobile Transects 1 and 2, temperatures differ by approximately 5 °C, with Transect 1 re-cording near 25 °C and Transect 2 around 20 °C. Similarly, in Zone 2 (Z-2), Transect 1 registers temperatures near 23 °C, contrasting with Transect 3 at approximately 18 °C. These findings corroborate research demonstrating significant microclimatic variability even within short distances, influenced by urban structures and heat retention properties [49,50].  Figure 8. Three-dimensional representation of temperature variations across mobile transects in Temuco. Such variations are consistent with studies emphasizing the critical role of land use and cover changes in shaping urban microclimates [51,52]. Urban centers, dominated by impervious surfaces and high-density constructions, intensify the urban heat island (UHI) effect through reduced evapotranspiration and increased thermal inertia [53,54]. Con-versely, areas with greater vegetation cover demonstrate cooler temperatures, underscor-ing the role of green spaces in mitigating UHI effects [51,55]. The observed variations at transect intersections further reflect the methodological challenges inherent in mobile Sensors 2025, 25, x FOR PEER REVIEW 12 of 19   external point, intensities over 10 °C were reached. This would mean that the UHI phe-nomenon would influence the microclimate in every sector in the city.  Figure 7. Fluctuation plot with stations in the city that record high temperatures compared to their adjacent sectors. Station 247 left plot. Zone 4 −38.733095, −72.6031539. Station 256 right plot. Zone 1 −38.697133, −72.535842. 4. Discussion The 3D representation of temperature variations across mobile transects in Temuco (Figure 8) highlights significant spatial heterogeneity, particularly at the intersections of transects. These variations underscore the localized thermal dynamics shaped by urban morphology and anthropogenic factors. For example, at the downtown intersection of Mobile Transects 1 and 2, temperatures differ by approximately 5 °C, with Transect 1 re-cording near 25 °C and Transect 2 around 20 °C. Similarly, in Zone 2 (Z-2), Transect 1 registers temperatures near 23 °C, contrasting with Transect 3 at approximately 18 °C. These findings corroborate research demonstrating significant microclimatic variability even within short distances, influenced by urban structures and heat retention properties [49,50].  Figure 8. Three-dimensional representation of temperature variations across mobile transects in Temuco. Such variations are consistent with studies emphasizing the critical role of land use and cover changes in shaping urban microclimates [51,52]. Urban centers, dominated by impervious surfaces and high-density constructions, intensify the urban heat island (UHI) effect through reduced evapotranspiration and increased thermal inertia [53,54]. Con-versely, areas with greater vegetation cover demonstrate cooler temperatures, underscor-ing the role of green spaces in mitigating UHI effects [51,55]. The observed variations at transect intersections further reflect the methodological challenges inherent in mobile Sensors 2025, 25, 1251

13 of 18

From an urban planning perspective, these findings underline the need for targeted
interventions. Strategies such as increasing vegetation cover, optimizing urban design, and
enhancing surface albedo are pivotal for improving thermal comfort [53,55]. For instance,
compact high-rise zones have been shown to exhibit the highest temperature disparities due
to reduced vegetation and extensive impervious surfaces [21]. Similarly, in Temuco, high-
density zones have been identified as hotspots with maximum UHI intensities reaching
up to 13 ◦C. The integration of green infrastructure, particularly in high-risk zones like
Z-1 and Z-3, could mitigate extreme heat events, aligning with global best practices while
addressing local climatic challenges.

The integration of diverse methodological approaches has significantly advanced UHI
research. Mobile transects provide granular spatial data, complementing fixed station
records and remote sensing observations. Studies utilizing low-cost sensors on mobile
vehicles have demonstrated the feasibility of mapping urban temperature gradients while
maintaining cost efficiency [52].

Further, the differences between transects illustrate the complexity of UHI phenomena,
which are influenced not only by surface materials and vegetation but also by meteoro-
logical conditions and human activity patterns. Studies have noted that such variability
complicates the development of universal mitigation strategies and highlights the necessity
for localized approaches tailored to specific urban contexts [49,50,52,57]. Incorporating
Local Climate Zone (LCZ) classifications has further standardized UHI comparisons across
urban morphologies, revealing the influence of building density and vegetation on cooling
demands [38]. These approaches are reflected in Temuco, where thoughtfully designed
transect routes have enhanced the understanding of localized UHI dynamics.

Mitigation strategies such as urban greening have demonstrated measurable impacts
on UHI reduction. Research indicates that increasing vegetation cover can decrease summer
daytime UHI intensities by up to 1.5 K, contributing to both thermal regulation and urban
sustainability [58,59].
In Temuco, integrating these measures could improve thermal
comfort in vulnerable zones while promoting sustainable urban development. However,
localized adaptations are necessary, as the cooling potential of vegetation varies with
species and urban context.

The use of thresholds derived from existing studies, such as those presented in Table 3,
provides a general framework for classifying UHI intensity. However, these thresholds are
not tailored to the specific climatic and urban conditions of the study area. For instance,
the thresholds in this study are adapted from reference [43], which focuses on Spain and
its surrounding regions. While they provide a useful benchmark, applying them to a
city like Temuco, with distinct geographical and climatic characteristics, may introduce
inaccuracies. Temuco’s high annual precipitation, heterogeneous urban layout, and mix
of dense and vegetated zones suggest the need for locally derived thresholds to enhance
classification accuracy. Future research should prioritize the development of region-specific
thresholds to better reflect local temperature patterns and urban dynamics, particularly in
under-represented areas like southern Chile. This limitation has been acknowledged and
highlights the importance of continuous methodological refinement in UHI studies.

The selection of the 20:00–21:00 timeframe for temperature measurements aligns with
established best practices for UHI analysis, as this period minimizes the influence of solar
radiation and allows for stabilized temperature conditions [60–62]. This timeframe is
particularly critical in ensuring reliable comparisons between urban and rural zones, as it
mitigates variability caused by daytime solar heating or nighttime cooling dynamics [63,64].
While the observed consistency between methodologies during this timeframe supports
the validity of the approach, measurements at other times of the day may introduce greater
variability, potentially affecting the comparability and classification of UHI intensities [65].

Sensors 2025, 25, 1251

14 of 18

This limitation highlights the importance of selecting appropriate measurement windows
tailored to specific study objectives and regional climatic conditions. Future studies could
explore how diurnal variability influences UHI patterns to provide a more comprehensive
understanding of temporal dynamics.

Anthropogenic waste heat plays a significant role in shaping UHI dynamics, partic-
ularly in urban areas with high traffic density and industrial activity [66]. Fixed stations,
often located near infrastructure, are prone to capturing localized emissions from sources
such as vehicle exhaust, industrial operations, and building heat dissipation, which can
introduce biases in temperature measurements [67,68]. Mobile transects, while offering
broader spatial coverage, are susceptible to transient influences, such as momentary emis-
sions from passing vehicles or varying industrial activity along the route [69,70]. These
factors can create variability in the data, complicating direct comparisons. This study
highlights the need to consider such anthropogenic contributions when interpreting UHI
measurements and suggests integrating both methodologies to better capture the spatial
and temporal distributions of waste heat influences.

Finally, future research should address the socio-economic dimensions of UHI mit-
igation, considering that heat impacts disproportionately affect vulnerable populations.
Integrating equity frameworks into UHI studies will enhance the relevance of findings
across diverse urban settings and guide inclusive urban planning in Temuco and beyond.
Advanced remote sensing and predictive modeling should also be explored to refine UHI
assessments and support evidence-based policy decisions [34].

5. Conclusions

This study examined the combined use of mobile transects and fixed stations to ana-
lyze atmospheric urban heat islands (UHIs’a) in Temuco, Chile. The methodologies were
validated through a comparative analysis, demonstrating moderate compatibility with
correlation coefficients of 0.55, 0.61, and 0.62 for three separate transect routes. Average
temperature differences between the two methods were 0.72 ◦C, 1.6 ◦C, and 1.2 ◦C, respec-
tively, while standard deviations ranged from 0.5 to 0.91 ◦C. These results confirm that both
methodologies can be reliably used, either independently or complementarily, to assess
UHI intensity.

Mobile transects enabled the detailed mapping of temperature gradients across urban
zones, while fixed stations provided continuous temporal data and a broader perspective
on UHI behavior. For example, fixed station data highlighted significant diurnal variations,
with maximum temperatures in urban zones reaching 33.1 ◦C at 14:00, compared to 25.4 ◦C
at the rural Maquehue station. These temperature differences translate to UHI intensities
classified as weak to moderate within the city (0.5 ◦C to 3.4 ◦C). However, when compared
to rural areas, intensities ranged from 10.1 ◦C to 13 ◦C, categorizing Temuco’s UHI as
extremely strong. Such intensities represent one of the highest values reported in global
UHI studies and pose a significant risk to public health, particularly during heatwave
conditions.

The study identified four zones within Temuco exhibiting pronounced UHI characteristics,
influenced by high traffic congestion and reduced vegetation cover. For instance, Z-1 recorded
some of the highest temperatures due to impervious surfaces and limited green infrastructure,
while Z-4 experienced significant heat retention from heavy traffic. These findings align with
global trends, where compact high-density urban areas consistently display elevated UHI
intensities.

The fixed station methodology further facilitated the creation of isothermal maps
and fluctuation plots, which revealed patterns such as higher afternoon temperatures and
rapid cooling at night in zones with abundant vegetation. These maps not only validated

Sensors 2025, 25, 1251

15 of 18

the mobile transect routes but also provided critical data for visualizing UHI dynamics
over 24-h cycles. In Temuco, the strongest UHI intensities occurred during the afternoon,
deviating from typical evening peaks observed in many other cities, emphasizing the
importance of localized studies to account for unique climatic and urban factors.

By comparing and validating two complementary methodologies, the study estab-
lishes a robust framework for UHI analysis in diverse urban contexts. The integration
of mobile transects and fixed stations provides a cost-effective and scalable approach for
high-resolution spatial and temporal assessments. Moreover, the findings underscore
the importance of addressing urban heat as part of broader urban planning and public
health strategies. In Temuco, targeted interventions such as increasing vegetation cover
in high-risk zones like Z-1 and Z-4 could mitigate extreme temperatures and improve
thermal comfort.

The comparison between fixed station and mobile transect methodologies highlights
the complementary strengths and limitations of each approach. Fixed stations offer contin-
uous temporal data, allowing for the detailed analysis of diurnal and seasonal temperature
variations under controlled conditions [71,72]. However, their limited spatial coverage
may overlook localized temperature gradients within urban areas [73]. Conversely, mobile
transects provide high spatial resolution, capturing urban-to-rural transitions and localized
thermal dynamics that fixed stations may miss [74,75]. Despite these strengths, mobile
measurements are subject to greater operational variability, including the need for frequent
calibration and transient environmental influences [76]. The integration of these method-
ologies addresses these individual limitations, offering a more comprehensive framework
for UHI analysis.

Future research should explore the socio-economic implications of UHIs, including
their impact on energy consumption, public health, and social equity. Expanding this
framework to other cities with similar climatic and urban characteristics would enhance the
generalizability of the findings. Additionally, integrating advanced technologies such as
remote sensing and machine learning could improve the accuracy and predictive capacity
of UHI assessments. These efforts will be critical for developing adaptive strategies to
mitigate UHI effects and enhance urban resilience in the face of climate change.

Author Contributions: A.M.-S.: Methodology, validation, formal analysis, research, and supervision.
M.V.-F.: Conceptualization, research, and writing—original draft. P.V.-T.: Review and editing.
A.M.-R.: Conceptualization and simulation of urban heat islands. M.S.: Review and editing. All
authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable because this study did not involve humans.

Data Availability Statement: Martinez-Soto, Aner (2022): Urban Heat Island Temuco. figshare.
Dataset. https://doi.org/10.6084/m9.figshare.20186816.v1.

Acknowledgments: We wish to thank the Office of Research of the Faculty of Engineering and Science
of the Universidad de La Frontera for the financial support in the development of this study.

Conflicts of Interest: The authors declare no conflicts of interest.

References

1.

2.

de Steffens, A.C.; Piccolo, M.C.; Gonzalez, J.H.; Navarrete, G.; Lara, R.M.R. La Isla de Calor en Temuco, Chile: Situacion invernal.
Rev. Geofis. 1997, 46, 49–60.
Oke, T.R. City size and the urban heat island. Atmos. Environ. 1967, 7, 1973. [CrossRef]

Sensors 2025, 25, 1251

16 of 18

3.

4.

5.

6.

7.

8.
9.

10.

Stevovic, S.; Mirjanic, D.; Djuric, N. Theory and smart practice in the reduction of negative effects of urban heat Island. Therm. Sci.
2018, 22, 1011–1031. [CrossRef]
García-Cueto, O.R.; Jáuregui-Ostos, E.; Toudert, D.; Tejeda-Martinez, A. Detection of the urban heat island in Mexicali, B.C.,
México and its relationship with land use. Atmosfera 2007, 20, 113–131.
Pérez, C.A.F. Islas de calor urbano en Tampico, México. Impacto del microclima a la calidad del hábitat. Nova Sci. 2014, 7, 495–515.
[CrossRef]
Contreras, A.; Salas, J.A.; Velásquez, G.; Quevedo, H. Determinación De La Isla De Calor Urbano En Ciudad Juarez Mediante
Programa De Cómputo. Culcyt. Clima Urbano 2008, 26, 3–16.
Jones, P.D.; Lister, D.H.; Li, Q. Urbanization effects in large-scale temperature records, with an emphasis on China. J. Geophys. Res.
Atmos. 2008, 113. [CrossRef]
Fan, Y.; Li, Y.; Bejan, A.; Wang, Y.; Yang, X. Horizontal extent of the urban heat dome flow. Sci Rep 2017, 7, 11681. [CrossRef]
IPCC. Cambio Climático 2014: Informe de síntesis. Contribución de los Grupos I, II y III al Quinto Informe de Evaluación del
Grupo de Expertos sobre el Cambio Climático. Quinto Inf. Evaluación 2014, 4, 1–157.
IPCC. Cambio Climático 2007: Informe de Síntesis. Informe del Grupo INTERGUBERNAMENTAL de Expertos Sobre el Cambio Climático;
IPCC: Geneva, Switzerland, 2007.

11. Angel, L.; Ramirez, A.; Dominguez, E. Isla De Calor Y Cambios Espacio-Temporales De La Temperatura En La Ciudad De Bogotá.

Rev. Acad. Colomb. Cienc. 2010, 34, 173–183.

12. Alomar Garau, G.; Llop Garau, J. La isla de calor urbana de Palma (Mallorca, Islas Baleares): Avance para el estudio del clima

urbano en una ciudad litoral mediterránea. Boletín Asoc. Geógrafos Españoles 2018, 78, 392–418. [CrossRef]

13. Kuznetsova, I.N.; Brusova, N.E.; Nakhaev, M.I. Moscow Urban Heat Island: Detection, boundaries, and variability. Russ. Meteorol.

Hydrol. 2017, 42, 305–313. [CrossRef]
Jauregui, E. Heat island development in Mexico City. Atmos Env. 1997, 31, 3821–3831. [CrossRef]

14.
15. Hawkins, T.W.; Brazel, A.J.; Stefanov, W.L.; Bigler, W.; Saffell, E.M. The role of rural variability in urban heat island determination

16.

for Phoenix, Arizona. J. Appl. Meteorol. 2004, 43, 476–486. [CrossRef]
Stewart, I.D. A systematic review and scientific critique of methodology in modern urban heat island literature. Int. J. Clim. 2011,
31, 200–217. [CrossRef]

17. Martínez Martínez, J. Estudio de la isla de calor de la ciudad de Alicante. Investig. Geográficas 2014, 62, 83–89. [CrossRef]
18. Erell, E.; Williamson, T. Intra-urban differences in canopy layer air temperature at a mid-latitude city. Int. J. Climatol. 2007, 27,

1243–1255. [CrossRef]

19. Konstantinov, P.I.; Grishchenko, M.Y.; Varentsov, M.I. Mapping urban heat islands of arctic cities using combined data on field
measurements and satellite images based on the example of the city of Apatity (Murmansk Oblast). Izv. Atmos. Ocean. Phys. 2015,
51, 992–998. [CrossRef]
Stewart, I.D.; Krayenhoff, E.S.; Voogt, J.A.; Lachapelle, J.A.; Allen, M.A.; Broadbent, A.M. Time Evolution of the Surface Urban
Heat Island. Earths Future 2021, 9, e2021EF002178. [CrossRef]

20.

21. Zhang, Y.; Zhang, J.; Zhang, X.; Zhou, D.; Gu, Z. Analyzing the Characteristics of UHI (Urban Heat Island) in Summer Daytime
Based on Observations on 50 Sites in 11 LCZ (Local Climate Zone) Types in Xi’an, China. Sustainability 2020, 13, 83. [CrossRef]
22. Marquès, E.; Masson, V.; Naveau, P.; Mestre, O.; Dubreuil, V.; Richard, Y. Urban Heat Island Estimation from Crowdsensing

Thermometers Embedded in Personal Cars. Bull. Am. Meteorol. Soc. 2022, 103, E1098–E1113. [CrossRef]

23. Brandsma, T.; Wolters, D. Measurement and Statistical Modeling of the Urban Heat Island of the City of Utrecht (the Netherlands).

24.

25.

J. Appl. Meteorol. Climatol. 2012, 51, 1046–1060. [CrossRef]
Sarricolea, P.; Aliste, E.; Castro, P.; Escobedo, C. Análisis de la máxima intensidad de la isla de calor urbana nocturna de la ciudad
de Rancagua (Chile) y sus factores explicativos. Rev. Climatol. 2008, 8, 71–84.
Sarricolea Espinoza, P.; Martín-Vide, J. El estudio de la Isla de Calor Urbana de Superficie del Área Metropolitana de Santiago de
Chile con imágenes Terra-MODIS y Análisis de Componentes Principales. Rev. Geogr. Norte Gd. 2014, 57, 123–141. [CrossRef]

26. Burger, M.; Gubler, M.; Heinimann, A.; Brönnimann, S. Modelling the spatial pattern of heatwaves in the city of Bern using a land

use regression approach. Urban Clim. 2021, 38, 100885. [CrossRef]

27. Dian, C.; Pongrácz, R.; Incze, D.; Bartholy, J.; Talamon, A. Analysis of the urban heat island intensity based on air temperature

28.

29.
30.
31.

measurements in a renovated part of Budapest (Hungary). Geogr. Pannonica 2019, 23, 277–288. [CrossRef]
Servicio Salud Araucanía Sur. Boletín Demográfico Perfil Socio Demográfico y Sanitario Comuna de Temuco; Servicio Salud Araucanía
Sur: Temuco, Chile, 2020; Available online: https://drive.google.com/file/d/1_a5gbLscPUzsmRTv9lllbm7PMJrqzzuQ/view
(accessed on 5 December 2024).
Instituto Nacional de Estadística. Resultados CENSO 2002; Instituto Nacional de Estadística: Santiago, Chile, 2002.
Instituto Nacional Estadística. Resultados CENSO 2017; Instituto Nacional de Estadística: Santiago, Chile, 2017.
Fuentes Pérez, C.A. Climatología urbana por modificación antropogénica. Alteración del balance de energía natural. Dr. Univ.
Autónoma Tamaulipas 2015, 9, 73–91.

Sensors 2025, 25, 1251

17 of 18

32. Moreno, R.; Zamora, R.; Moreno-García, N.; Galán, C. Effects of composition and structure variables of urban trees in the

reduction of heat islands; case study, Temuco city, Chile. Build. Env. 2023, 245, 110859. [CrossRef]

33. Biblioteca Nacional del Congreso de Chile. Clima y Vegetación Región de la Araucanía. Available online: https://www.bcn.cl/

siit/nuestropais/region9/clima.htm (accessed on 5 December 2024).

34. Montaner-Fernández, D.; Morales-Salinas, L.; Rodriguez, J.S.; Cárdenas-Jirón, L.; Huete, A.; Fuentes-Jaque, G.; Pérez-Martínez,
W.; Cabezas, J. Spatio-Temporal Variation of the Urban Heat Island in Santiago, Chile during Summers 2005–2017. Remote Sens.
2020, 12, 3345. [CrossRef]
Sarricolea, P.; Herrera-Ossandon, M.; Meseguer-Ruiz, Ó. Climatic regionalisation of continental Chile. J. Maps 2017, 13, 66–73.
[CrossRef]

35.

36. Godoy, G. Modelo de la Isla de Calor Atmosférico Superficial: Factores en Común y alteraciones para la mitigación de su Efecto

en la salud humana y medio ambiente urbano. Univ. Concepc. 2014, 25, 1–21. [CrossRef]

37. García, M.D.; Pardo, J.A. El estudio de la isla de calor urbana en el ámbito mediterráneo: Una revisión bibliográfica. Biblio3W Rev.

Bibliográfica Geogr. Cienc. Soc. 2016, 21, 1179.

38. Verichev, K.; Salazar-Concha, C.; Díaz-López, C.; Carpio, M. The influence of the urban heat island effect on the energy
performance of residential buildings in a city with an oceanic climate during the summer period: Case of Valdivia, Chile. Sustain.
Cities Soc. 2023, 97, 104766. [CrossRef]

39. Zühlke, J.P. Die Verbreitung von Wissen zu Controlling-Instrumenten; Springer Fachmedien: Wiesbaden, Germany, 2007. [CrossRef]
40.
41. Amatriain, X.; Pujol, J.M. Data mining methods for recommender systems. In Recommender Systems Handbook, 2nd ed.; Springer:

Serra Pardo, J.A. Estudio de la isla de calor de la ciudad de Ibiza. Investig. Geográficas 2007, 44, 55–73. [CrossRef]

Boston, MA, USA, 2015. [CrossRef]

42. Van Kreveld, M. Algorithms for triangulated terrains. In Lecture Notes in Computer Science; (Including subseries Lecture Notes in

Artificial Intelligence and Lecture Notes in Bioinformatics); Springer: Berlin/Heidelberg, Germany, 1997. [CrossRef]
Fernández García, F. Manual de Climatología Aplicada: Clima, Medio Ambiente y Planificación, 2nd ed.; Síntesis: Madrid, Spain, 1996.
43.
44. Liu, L.; Lin, Y.; Liu, J.; Wang, L.; Wang, D.; Shui, T.; Chen, X.; Wu, Q. Analysis of local-scale urban heat island characteristics using
an integrated method of mobile measurement and GIS-based spatial interpolation. Build. Environ. 2017, 117, 191–207. [CrossRef]
45. Cecilia, A.; Casasanta, G.; Petenko, I.; Conidi, A.; Argentini, S. Measuring the urban heat island of Rome through a dense weather

station network and remote sensing imperviousness data. Urban Clim. 2023, 47, 101355. [CrossRef]

46. Kousis, I.; Pigliautile, I.; Pisello, A.L. Intra-urban microclimate investigation in urban heat island through a novel mobile

47.

monitoring system. Sci. Rep. 2021, 11, 9732. [CrossRef]
Siu, L.W.; Hart, M.A. Quantifying urban heat island intensity in Hong Kong SAR, China. Environ. Monit Assess. 2013, 185,
4383–4398. [CrossRef]

48. Heusinkveld, B.G.; Steeneveld, G.J.; Van Hove, L.W.A.; Jacobs, C.M.J.; Holtslag, A.A.M. Spatial variability of the rotterdam urban

heat island as influenced by urban land use. J. Geophys. Res. 2014, 119, 677–692. [CrossRef]

49. Da Silva, V.J.; Da Silva, C.R.; Almeida, L.D.; Da Silva, C.R.; Carvalho, H.D.P.; De Camargo, R. Mobile transect for identification of

intra-urban heat islands in Uberlandia, Brazil. Rev. Ambiente Agua 2018, 13, e2187. [CrossRef]

50. Liu, L.; Liu, J.; Lin, Y. Spatial-temporal Analysis of the Urban Heat Island of a Subtropical City by Using Mobile Measurement.

Procedia Eng. 2016, 169, 55–63. [CrossRef]

51. Dihkan, M.; Karsli, F.; Guneroglu, N.; Guneroglu, A. Evaluation of urban heat island effect in Turkey. Arab. J. Geosci. 2018, 11, 186.

52.

[CrossRef]
Sun, C.-Y.; Kato, S.; Gou, Z. Application of Low-Cost Sensors for Urban Heat Island Assessment: A Case Study in Taiwan.
Sustainability 2019, 11, 2759. [CrossRef]
Silva, Y.M.N.; Silva, H.M.; De Andrade Silva, R.D.; Marques, E.D.; De Oliveira Gomes, O.V. Identification of the urban heat islands
phenomenon in a small city: The study case of Três Rios/RJ, Brazil. Rev. Bras. Ciências Ambient. 2021, 57, 93–104. [CrossRef]
54. Zeynali, R.; Bitelli, G.; Mandanici, E. Mobile Data Acquisition and Processing In Support Of An Urban Heat Island Study. Int.

53.

Arch. Photogramm. Remote Sens. Spat. Inf. Sci. 2023, 48, 563–569. [CrossRef]

55. Romero Rodríguez, L.; Sánchez Ramos, J.; Sánchez de la Flor, F.J.; Álvarez Domínguez, S. Analyzing the urban heat Island:
Comprehensive methodology for data gathering and optimal design of mobile transects. Sustain. Cities Soc. 2020, 55, 102027.
[CrossRef]

56. Kousis, I.; Manni, M.; Pisello, A.L. Environmental mobile monitoring of urban microclimates: A review. Renew. Sustain. Energy

Rev. 2022, 169, 112847. [CrossRef]

57. Lindberg, F.; Olofson, K.F.G.; Sun, T.; Grimmond, C.S.B.; Feigenwinter, C. Urban storage heat flux variability explored using

satellite, meteorological and geodata. Theor. Appl. Clim. 2020, 141, 271–284. [CrossRef]

58. Li, D.; Yan, S.; Chen, G. Effects of Urban Redevelopment on Surface Urban Heat Island. IEEE J. Sel. Top. Appl. Earth Obs. Remote

Sens. 2023, 16, 2366–2373. [CrossRef]

Sensors 2025, 25, 1251

18 of 18

59. Li, H.; Zhou, Y.; Jia, G.; Zhao, K.; Dong, J. Quantifying the response of surface urban heat island to urbanization using the annual

temperature cycle model. Geosci. Front. 2022, 13, 101141. [CrossRef]

60. Wang, J.; Zhou, W.; Wang, J. Time-series analysis reveals intensified urban heat island effects but without significant urban

warming. Remote Sens. 2019, 11, 2229. [CrossRef]

61. Earl, N.; Simmonds, I.; Tapper, N. Weekly cycles in peak time temperatures and urban heat island intensity. Environ. Res. Lett.

2016, 11, 074003. [CrossRef]

62. Gaffin, S.R.; Rosenzweig, C.; Khanbilvardi, R.; Parshall, L.; Mahani, S.; Glickman, H.; Goldberg, R.; Blake, R.; Slosberg, R.B.; Hillel,
D. Variations in New York city’s urban heat island strength over time and space. Theor. Appl. Clim. 2008, 94, 1–2. [CrossRef]
Schrijvers, P.J.C.; Jonker, H.J.J.; Kenjereš, S.; de Roode, S.R. Breakdown of the night time urban heat island energy budget. Build.
Environ. 2015, 83, 50–64. [CrossRef]

63.

64. Chen, T.; Sun, A.; Niu, R. Effect of land cover fractions on changes in surface urban heat islands using landsat time-series images.

Int. J. Environ. Res. Public Health 2019, 16, 971. [CrossRef]

65. Mathew, A.; Khandelwal, S.; Kaul, N. Analysis of diurnal surface temperature variations for the assessment of surface urban heat

island effect over Indian cities. Energy Build. 2018, 159, 271–295. [CrossRef]

66. Estrada, F.; Perron, P. Disentangling the trend in the warming of urban areas into global and local factors. Ann. N. Y. Acad. Sci.

2021, 1504, 230–246. [CrossRef]

67. Chow, W.T.L.; Salamanca, F.; Georgescu, M.; Mahalov, A.; Milne, J.M.; Ruddell, B.L. A multi-method and multi-scale approach for

estimating city-wide anthropogenic heat fluxes. Atmos. Environ. 2014, 99, 64–76. [CrossRef]

68. Ghaddar, Z.; Ghali, K.; Ghaddar, N. The impact of the air-conditioning systems on the urban microclimate of beirut city. Renew.

Energy Power Qual. J. 2017, 1, 882–885. [CrossRef]

69. Lipson, M.J.; Thatcher, M.; Hart, M.A.; Pitman, A. A building energy demand and urban land surface model. Q. J. R. Meteorol. Soc.

2018, 144, 1572–1590. [CrossRef]

70. Lein, J.K.; Hong, X. Fingerprinting Anthropogenic ‘Waste’ Heat Across an Urban Landscape Using Earth Observational Satellite

Data. J. Environ. Sci. Allied Res. 2017, 2017, 1–10. [CrossRef]

71. Yao, R.; Luo, Q.; Luo, Z.; Jiang, L.; Yang, Y. An integrated study of urban microclimates in Chongqing, China: Historical weather

data, transverse measurement and numerical simulation. Sustain. Cities Soc. 2015, 14, 187–199. [CrossRef]

72. Mandelmilch, M.; Ferenz, M.; Mandelmilch, N.; Potchter, O. Urban spatial patterns and heat exposure in the Mediterranean City

of Tel Aviv. Atmosphere 2020, 11, 963. [CrossRef]

73. Husni, E.; Prayoga, G.A.; Tamba, J.D.; Retnowati, Y.; Fauzandi, F.I.; Yusuf, R.; Yahya, B.N. Microclimate investigation of vehicular

traffic on the urban heat island through IoT-Based device. Heliyon 2022, 8, e11739. [CrossRef]

74. Zou, Z.; Yan, C.; Yu, L.; Jiang, X.; Ding, J.; Qin, L.; Wang, B.; Qiu, G. Impacts of land use/land cover types on interactions between

urban heat island effects and heat waves. Build. Environ. 2021, 204, 108138. [CrossRef]

75. Kousis, I.; Pigliautile, I.; Pisello, A.L. A Mobile Vehicle-Based Methodology for Dynamic Microclimate Analysis. Int. J. Environ.

Res. 2021, 15, 893–901. [CrossRef]

76. Lamer KLuke, E.P.; Walsh Jr, B.; Andrade, S.; Mages, Z.; Zhu, Z.; Leghart, E.; Treserras, B.P.; Emrick, A.; Kollias, P. Going Mobile
to Address Emerging Climate Equity Needs in the Heterogeneous Urban Environment. Bull. Am. Meteorol. Soc. 2022, 103,
E2069–E2080. [CrossRef]

Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

