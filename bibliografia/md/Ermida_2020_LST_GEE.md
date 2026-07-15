Article
Google Earth Engine Open-Source Code for Land
Surface Temperature Estimation from the
Landsat Series

Soﬁa L. Ermida 1,2,*
Isabel F. Trigo 1,2

, Patrícia Soares 3, Vasco Mantas 3, Frank-M. Göttsche 4

and

1

Instituto Português do Mar e da Atmosfera (IPMA), 1749-077 Lisbon, Portugal; isabel.trigo@ipma.pt
Instituto Dom Luiz (IDL), Faculdade de Ciências, Universidade de Lisboa, 1749-016 Lisbon, Portugal

2
3 Department of Earth Sciences, Universidade de Coimbra, 3030-790 Coimbra, Portugal;

4

patriciaalsoares12@hotmail.com (P.S.); vasco.mantas@dct.uc.pt (V.M.)
Institute of Meteorology and Climate Research (IMK-ASF), Karlsruhe Institute of Technology (KIT),
76021 Karlsruhe, Germany; frank.goettsche@kit.edu

* Correspondence: soﬁa.ermida@ipma.pt

Received: 21 April 2020; Accepted: 3 May 2020; Published: 6 May 2020

Abstract: Land Surface Temperature (LST) is increasingly important for various studies assessing
land surface conditions, e.g., studies of urban climate, evapotranspiration, and vegetation stress.
The Landsat series of satellites have the potential to provide LST estimates at a high spatial resolution,
which is particularly appropriate for local or small-scale studies. Numerous studies have proposed
LST retrieval algorithms for the Landsat series, and some datasets are available online. However,
those datasets generally require the users to be able to handle large volumes of data. Google Earth
Engine (GEE) is an online platform created to allow remote sensing users to easily perform big
data analyses without increasing the demand for local computing resources. However, high spatial
resolution LST datasets are currently not available in GEE. Here we provide a code repository that
allows computing LSTs from Landsat 4, 5, 7, and 8 within GEE. The code may be used freely by users
for computing Landsat LST as part of any analysis within GEE.

Keywords: Land Surface Temperature; Landsat; Google Earth Engine; ASTER GED; high resolution

1. Introduction

Land Surface Temperature (LST) is an important component of the Earth’s energy budget,
closely linked to the partitioning between sensible and latent heat ﬂuxes. As such, high-resolution
satellite-derived LST is increasingly used in various applications related to the assessment of land
surface conditions, including mapping the urban extent and the intensity of urban micro-climates,
estimating high-resolution evapotranspiration for the management of water resources and assessing
vegetation stress [1–15].

The Landsat series of satellites have the potential to provide LST estimates at a high spatial
resolution that are particularly appropriate for local and small-scale studies. Numerous LST algorithms
for the Landsat series have been proposed [16–30]. While most algorithms are simple to implement,
they require users to provide the necessary input data and calibration coeﬃcients, which are generally
not readily available. Some datasets are available online (e.g., [25,26]); however, they generally require
users to be able to handle large volumes of data. Google Earth Engine (GEE; [31]) is an online
platform created to allow remote sensing users to easily perform big data analyses without the need
for computation resources. All Landsat Level-1 and 2 data are directly available to GEE, including

Remote Sens. 2020, 12, 1471; doi:10.3390/rs12091471

www.mdpi.com/journal/remotesensing

remote sensing  (cid:1)(cid:2)(cid:3)(cid:1)(cid:4)(cid:5)(cid:6)(cid:7)(cid:8)(cid:1)(cid:1)(cid:2)(cid:3)(cid:4)(cid:5)(cid:6)(cid:7)Remote Sens. 2020, 12, 1471

2 of 21

top-of-atmosphere (TOA) and surface reﬂectance (SR) data. However, until now high-resolution LST
datasets from Landsat have been unavailable in GEE.

High-resolution LST may also be derived from the Chinese Huan Jing 1 (HJ-1) Infrared Scanner
(IRS) at about 300 m [32,33] or from the Ecosystem Spaceborne Thermal Radiometer Experiment
on Space Station (ECOSTRESS) thermal infrared sensor at about 70 m [34]. While the former is not
currently available in GEE, the latter is bounded to provide observations over a relatively short period.
The Landsat series, which provides high spatial resolution observations in the thermal infrared (~100 m)
available over 38 years, is among the most wide-spread used sensors for high resolution LST retrievals.
Here we propose a methodology for deriving LST from the Landsat series of satellites (i.e., Landsat
4, 5, 7, and 8), which is fully implemented in GEE. Parastatidis et al. [26] previously proposed a similar
method that resulted in a web application that allowed users to derive LST data with GEE. However,
since the data are only accessible through the web application, this method still requires users to
download large amounts of data if they wish to perform time-series analyses. In contrast, here we
provide a code repository with all the GEE scripts necessary to compute LSTs from Landsat data.
The repository allows users to perform any data analysis they require within GEE without the need to
store data locally. The code is written in Javascript and built with the new ‘GEE modules capability’,
which makes its application easy—users only need to add a “require( . . . )” command to their scripts
to access the code for computing Landsat LST.

The LST is computed using the Statistical Mono-Window (SMW) algorithm developed by the
Climate Monitoring Satellite Application Facility (CM-SAF) for deriving LST climate data records from
Meteosat First and Second Generation (MFG and MSG) [35]. Due to its simplicity, the algorithm is
easy to calibrate and implement. Besides Landsat data, the LST production code makes use of two
other datasets available within GEE, atmospheric data from the re-analyses of the National Center for
Environmental Prediction (NCEP) and National Center for Atmospheric Research (NCAR) [36] and
surface emissivity from the Advanced Spaceborne Thermal Emission and Reﬂection Radiometer Global
Emissivity Database (ASTER GED) developed by the National Aeronautics and Space Administration’s
(NASA) Jet Propulsion Laboratory (JPL) [37].

The quality of the Landsat LST computed with the proposed methodology is assessed with
comparisons against in situ LST, which were derived from radiance measurements from six stations
belonging to the Surface Radiation Budget Network (SURFRAD) [38], the Baseline Surface Radiation
Network (BSRN) [39], and the Karlsruhe Institute of Technology (KIT) network [40].

Section 2 describes the input data used by the LST algorithm (Section 2.1), the LST retrieval
procedure (Section 2.2), and the station data used for validation (Section 2.3). Section 3 shows
the obtained algorithm calibration (Section 3.1), examples of the derived LST and necessary layers
(Section 3.2), and the results of the validation exercises (Section 3.3). Section 4 discusses the results and
Section 5 summarizes the presented work.

2. Materials and Methods

2.1. Input Data

2.1.1. Landsat Data

TOA brightness temperatures for the Landsat’s thermal infrared (TIR) channels are provided
by the United States Geological Survey (USGS) and are fully available and ready to use in GEE for
Landsats 4–8, collection 1. The USGS derives the TOA values from raw orthorectiﬁed digital numbers
data using the respective calibration coeﬃcients [41]. The data from the Landsat series are considered
consistent and inter-calibrated, and all TIR bands have been resampled to 30 m spatial resolution.
The data are organized into Tiers based on their quality. Landsat scenes with the highest available
data quality are placed into Tier 1, being suitable for time-series analysis, while the remainder are
assigned to Tier 2 [42]. The results shown in this work are entirely based on Tier 1 data, but the code
may equally be applied to Tier 2 data. Table 1 describes the properties of the spectral bands used in this

Remote Sens. 2020, 12, 1471

3 of 21

study for each Landsat. Besides the TIR band, the red and near-infrared (NIR) bands are used to derive
the Normalized Diﬀerence Vegetation Index (NDVI), which is calculated from the SR values (instead
of the TOA values, which is less accurate). For Landsat-4 and Landsat-5, data acquisition in the visible
and infrared spectral regions is performed by the Thematic Mapper (TM) sensor, while for Landsat 7,
it is performed by the Enhanced Thematic Mapper Plus (ETM+; an improved version of the TM). For
Landsat 8, the Operational Land Imager (OLI) acquires data in the visible and short-wave infrared
range, and the Thermal Infrared Sensor (TIRS) provides the TIR data. The TIR band of Landsat 7 is
available in low and high gain variants [43]. Here we choose to use the low-gain version, which has
lower radiometric resolution but the higher dynamic range and, therefore, prevents saturation at high
brightness temperatures.

Table 1. Bands, Google Earth Engine dataset, spatial resolution, equatorial crossing time (E.C.T.), and
available date range for each Landsat satellite.

Satellite

Used
Bands

Wavelength
(µm)

Dataset

Spatial
Resolution

E.C.T.

Date Range

Landsat 4
(TM)

Landsat 5
(TM)

Landsat 7
(ETM+)

Landsat 8
(OLI; TIRS)

Red: B3
NIR: B4
TIR: B6

Red: B3
NIR: B4
TIR: B6

Red: B3
NIR: B4
TIR: B61

Red: B4
NIR: B5
TIR: B10

0.63–0.69
0.76–0.90
10.4–12.5

0.63–0.69
0.76–0.90
10.4–12.5

0.63–0.69
0.77–0.90
10.4–12.5

0.64–0.67
0.85–0.88
10.6–11.19

C01/T1_SR
C01/T1_SR
C01/T1_TOA

C01/T1_SR
C01/T1_SR
C01/T1_TOA
C01/T1_SR
C01/T1_SR
C01/T1_TOA
C01/T1_SR
C01/T1_SR
C01/T1_TOA

30 m
30 m
1202 m

30 m
30 m
1202 m

30 m
30 m
602 m

30 m
30 m
1002 m

9:45 am
(16-day)

9:45 am
(16-day)

10:00 am
(16-day)

10:00 am
(16-day)

22 August 1982
to
14 December
1993

1 January 1984
to
5 May 2012

1 January1999
to
present

11 April 2013
to
present

Note: 1 low gain band (B6_VCID_1); 2 resampled to 30 m.

The SR data for each Landsat are also available in GEE, as provided by the USGS. The SR
data from Landsat 8 are generated using the Land Surface Reﬂectance Code (LaSRC) algorithm,
where atmospheric correction is performed using a radiative transfer model, auxiliary atmospheric data
from MODIS, and makes use of the coastal aerosol band for aerosol inversion tests [44]. For Landsat
4-to-7, SRs are derived with the Landsat Ecosystem Disturbance Adaptive Processing System (LEDAPS)
algorithm, which calculates the radiative transfer for atmospheric data from MODIS and NCEP.

Cloud coverage information, including cloud shadowing, can be retrieved from the quality

assessment band (BQA), which is also made available by the USGS through GEE.

2.1.2. Atmospheric Data

Information on the atmospheric water vapor content is required to better account for atmospheric
contributions in the TIR observations. Total Column Water Vapor (TCWV) values from NCEP/NCAR
reanalysis data are available on GEE [36]. Currently, the NCEP/NCAR reanalysis is the only global
TCWV dataset available on GEE that covers the full period of operations of the Landsat series.
The TCWV data are available globally from 1948 to the present, with a six-hourly temporal resolution
and 2.5 degrees spatial resolution. TCWV data from the two closest analyses (available at 00, 06, 12,
and 18 UTC) are linearly interpolated to each Landsat image acquisition time. Only the NCEP/NCAR
grid-boxes containing the respective Landsat pixels are considered.

Remote Sens. 2020, 12, 1471

4 of 21

2.1.3. Surface Emissivity

The LST retrieval algorithm used here requires prescribed values of surface emissivity. As in the
operational Landsat LST product [25], we derive the surface emissivity for our LST retrievals from the
ASTER GEDv3 dataset developed by JPL [37]. This dataset includes the emissivity for the ﬁve ASTER
bands in the TIR region and is derived with a Temperature-Emissivity Separation (TES) algorithm from
all clear-sky ASTER images acquired between 2000 and 2008. The emissivity data have a reported
accuracy of ~0.01 and are provided with a spatial resolution of 100 × 100 m2 [45]. The emissivity data
are adjusted to match Landsat’s thermal bands using the coeﬃcients provided by [25].

The ASTER GEDv3 dataset corresponds to the average of all retrievals performed over an
eight-year period; therefore, emissivity variations over time, e.g., due to annual and inter-annual
variations in vegetation density, need to be accounted for. Following [25], we apply a vegetation
adjustment using Landsat derived NDVI and mean ASTER GEDv3 NDVI. The NDVI is commonly used
to derive the fraction of vegetation cover (FVC) [25,26,37,46]. Here we use the relationship proposed
by Carlson and Ripley [46]:

FVC =

(cid:32)

NDVI − NDVIbare
NDVIveg − NDVIbare

(cid:33)2

(1)

where NDVIbare and NDVIveg are the NDVI values of completely bare and fully vegetated pixels,
respectively. Following previous studies (e.g., [17,47–50]), these two threshold values are set to
NDVIbare = 0.2 and NDVIveg = 0.86. Although some studies use NDVIveg = 0.5, Jiménez-Muñoz
et al. [50] showed that for high-resolution images, the values between 0.8 and 0.9 are more appropriate.
Pixels with NDVI below NDVIbare are considered completely bare, while pixels with NDVI above
NDVIveg are considered fully vegetated.

Emissivity values over vegetated areas at any given time, may then be derived using the

Vegetation-Cover method [51,52], which is deﬁned as:

b = FVCε
ε

b,veg + (1 − FVC)ε

b,bare

(2)

b,veg and ε

where ε
b,bare are the emissivity of vegetation and bare ground for a given spectral band b.
The emissivity of vegetated surfaces typically shows relatively small variations in the TIR region and,
therefore, this value is prescribed to εveg = 0.99 [53]. For each pixel, the eﬀective emissivity (ε
b) for
each Landsat band is derived as follows [25]:

(1) ASTER FVC is derived from NDVI using Equation (1);
(2) The bare ground emissivity (ε

b,bare) for each ASTER band is derived from the original ASTER
b) and the corresponding ASTER FVC, using Equation (2) with the prescribed value

emissivity (ε
of ε

b,veg = 0.99;

(3) The bare ground emissivity for each Landsat TIR band (ε

b,bare) is derived from the ASTER bare

(4)

ground emissivity using the spectral adjustments provided in Table II of [25];
FVC values for the Landsat image are computed from the respective NDVI values using
Equation (1);

(5) The vegetation cover method (2) is used to obtain the actual surface emissivity for each Landsat

TIR band.

For practical purposes, the possibility to directly use the ASTER emissivity corrected for the
Landsat TIR band is also available in the code. Users may then choose whether they wish to apply the
NDVI-based correction or use the instantaneous ASTER emissivity values.

Remote Sens. 2020, 12, 1471

2.2. LST Retrieval

2.2.1. SMW Algorithm

5 of 21

LST is computed with the SMW algorithm developed and used by CM-SAF to derive LST data
records from the MFG and MSG series of satellites. The approach is based on an empirical relationship
between TOA brightness temperatures in a single TIR channel and LST and utilizes simple linear
regression [35,54–56]. The model consists of a linearization of the radiative transfer equation that
maintains an explicit dependence on surface emissivity:

LST = Ai

Tb
ε + Bi

1
ε + Ci

(3)

where Tb is the TOA brightness temperature in the TIR channel, and ε is the surface emissivity for
the same channel. The algorithm coeﬃcients Ai, Bi; and Ci are determined from linear regressions of
radiative transfer simulations performed for 10 classes of TCWV (I = 1, . . . ,10), ranging from 0 to 6 cm
in steps of 0.6 cm, with values of TCWV above 6 cm being assigned to the last class. Unlike for the
analogous algorithms developed by CM-SAF for MFG and MSG, here the coeﬃcients are not stratiﬁed
by satellite view angle, because the Landsat sensors have a considerably narrower the near-nadir ﬁeld
of view (FOV).

2.2.2. Algorithm Calibration

The calibration database used to obtain the coeﬃcients of Equation (3) has been derived using
a dataset of air temperature, water vapor, and ozone proﬁles compiled by Borbas et al. [57] and its
procedure follows Martins et al. [57]. The Borbas dataset comprises over 15,000 proﬁles and includes
ancillary variables such as surface pressure, spectral emissivity, skin temperature, and elevation.
To achieve a uniform coverage of surface and atmospheric conditions in the calibration exercise,
a sub-set of proﬁles is selected as follows:

(1) We deﬁne classes of LST ranging from 200 K to 330 K in steps of 5 K, and classes of TCWV from 0

(2)

(3)

to 6 cm in steps of 0.3 cm. TCWV values above 6 cm are assigned to the last class.
The Borbas database is iterated to randomly attribute a single clear-sky proﬁle to each TCWV/LST
class. At each new iteration, proﬁle selection is limited to those with a great-circle distance to
already selected proﬁles greater than 15 degrees. This guarantees a more extensive geographical
coverage of the calibration database.
For each of the selected proﬁles, surface conditions are varied to ensure a wide range of conditions
are included in the database: following [57], LST is set with respect to air temperature (Tair),
namely to the diﬀerence between LST and air temperature (LST-Tair) ranging from -15 K to +15 K
in steps of 5 K. Surface emissivity values are varied between 0.9 and 0.99 in steps of 0.01.

The selection procedure leads to a set of 257 proﬁles. For each proﬁle, seven values of LST and
10 values of emissivity are prescribed, which yields a total of 17,990 cases for the calibration exercise,
with sample sizes varying between 1260 and 2450 for each TCWV class considered for the coeﬃcient
derivation (Section 2.2.1). The obtained coeﬃcients are validated using the full Borbas dataset with the
provided LST and emissivity values.

For both, the calibration and validation databases, the respective brightness temperatures that
would be observed by the Landsat sensors are computed in the Radiative Transfer for the TIROS
Operational Vertical Sounder (RTTOV) version 12 developed by the Numerical Weather Prediction
Satellite Application Facility (NWP-SAF) [58].

2.2.3. Processing Chain

Landsat LST values are produced using the algorithm described in Section 2.2.1, with the
coeﬃcients determined with the calibration procedure described in Section 2.2.2 and the datasets

Remote Sens. 2020, 12, 1471

6 of 21

presented in Section 2.1. The production chain was fully coded in JavaScript using the Code Editor
Platform. The code is available from the GEE or Git repositories, respectively:

•
•

https://code.earthengine.google.com/?accept_repo=users/soﬁaermida/landsat_smw_lst
https://earthengine.googlesource.com/users/soﬁaermida/landsat_smw_lst

Figure 1 illustrates the processing chain for generating Landsat LSTs. The users ﬁrst provide
the date range, the Landsat satellite (4, 5, 7, or 8), the region of interest to process, and an NDVI ﬂag
indicating if they wish to apply the NDVI-based correction to emissivity. Based on this information,
the main module, Landsat_LST, loads the respective collections of TOA brightness temperatures
(BT) and Surface Reﬂectance (SR). A cloud mask is applied to both using the quality information
bands (module cloudmask). For each TOA BT image, the two closest TCWV NCEP analysis times are
selected and interpolated to the Landsat observation time (NCEP_TPW). The SR data are, in turn,
used to compute NDVI (compute_NDVI), which is then converted to FVC values as described in
Section 2.1.3 (compute_FVC). These FVC values are then used together with previously computed
ASTER emissivity values for bare ground (ASTER_bare_emiss) to obtain the corresponding Landsat
emissivity (compute_emissivity). Finally, the SMW algorithm is applied to the TOA TB of the Landsat
TIR band (SMWalgorithm); the algorithm coeﬃcients are mapped onto the Landsat image based on
TWVC from NCEP and taking the classes deﬁned in Section 2.2.1. The code and the LUT containing
the coeﬃcients are available to the users in the indicated repository (module SMW_coeﬀcients).

Figure 1. Google Earth Engine (GEE) processing chain for retrieving Landsat Land Surface Temperature
(LST). The blue text indicates coded functions in modules. The gray text indicates GEE datasets used in
the production.

Remote Sens. 2019, 11, x FOR PEER REVIEW 6 of 21 (compute_FVC). These FVC values are then used together with previously computed ASTER emissivity values for bare ground (ASTER_bare_emiss) to obtain the corresponding Landsat emissivity (compute_emissivity). Finally, the SMW algorithm is applied to the TOA TB of the Landsat TIR band (SMWalgorithm); the algorithm coefficients are mapped onto the Landsat image based on TWVC from NCEP and taking the classes defined in Section 2.2.1. The code and the LUT containing the coefficients are available to the users in the indicated repository (module SMW_coeffcients). In the same repository, we provide two scripts with examples demonstrating the usage of the modules for spatial and temporal analysis.  Figure 1. Google Earth Engine (GEE) processing chain for retrieving Landsat Land Surface Temperature (LST). The blue text indicates coded functions in modules. The gray text indicates GEE datasets used in the production. 2.3. In situ Data The quality of the LST data retrieved with the algorithm described above is evaluated by comparing the retrievals with in-situ LST from validation stations. In this study, we use six stations from the SURFRAD network, two stations from the BSRN network, and three stations from the KIT network. Table 2 shows the location, land cover type, and period of observation of each station. The SURFRAD network was established in 1993 with the purpose of providing continuous long-term measurements of the surface radiation budget over the United States [38], and their data have been widely used in validation and quality assessment exercises of satellite LST [25,59–62]. The BSRN is a global network of surface radiation stations managed by the Data and Assessments Panel from the Global Energy and Water Cycle Experiment (GEWEX) under the framework of the World Climate Research Program (WCRP) [39]. From the full BSRN network, we selected two stations that had the necessary variables and were located in sufficiently homogeneous areas. Both the SURFRAD and Remote Sens. 2020, 12, 1471

7 of 21

In the same repository, we provide two scripts with examples demonstrating the usage of the

modules for spatial and temporal analysis.

2.3. In situ Data

The quality of the LST data retrieved with the algorithm described above is evaluated by comparing
the retrievals with in-situ LST from validation stations. In this study, we use six stations from the
SURFRAD network, two stations from the BSRN network, and three stations from the KIT network.
Table 2 shows the location, land cover type, and period of observation of each station. The SURFRAD
network was established in 1993 with the purpose of providing continuous long-term measurements
of the surface radiation budget over the United States [38], and their data have been widely used in
validation and quality assessment exercises of satellite LST [25,59–62]. The BSRN is a global network
of surface radiation stations managed by the Data and Assessments Panel from the Global Energy
and Water Cycle Experiment (GEWEX) under the framework of the World Climate Research Program
(WCRP) [39]. From the full BSRN network, we selected two stations that had the necessary variables
and were located in suﬃciently homogeneous areas. Both the SURFRAD and BSRN stations provide
broadband hemispherical upwelling and downwelling infrared radiance measurements performed
−2. The KIT stations are speciﬁcally dedicated
by pyrgeometers with an uncertainty of about 5 Wm
to LST validation [40]. At these stations, Heitronics KT15.85 IIP radiometers (KT15; full-view angle
) measure upwelling and downwelling radiances in the 9.6–11.5 µm spectral region, with an
of 8.3
accuracy of 0.3 K in equivalent brightness temperature [40]. At the EVO and KAL sites, upwelling
radiance is measured by two radiometers, one facing the ground and another a nearby tree. These two
measurements allow the upscaling of the upwelling radiances to the satellite FOV [40,63,64].

◦

Table 2. Location, land cover type, and start date of the records of the SURFRAD, BSRN, and KIT
stations used to assess the quality of the Landsat LST retrievals.

Site Location

ID

Coordinates

Elevation

Land Cover

Start Date

Bondville, IL

BND

Desert rock, NV

DRA

Fort Peck, MT

FPK

Goodwin Creek, MS

GWN

Penn State Un., PA

PSU

Sioux Falls, SD

SXF

Table Mountain, CO

TBL

Cabauw, Netherlands

CAB

Gobabeb, Namibia

GOB

Evora, Portugal

EVO

Gobabeb, Namibia

GBB

Kalahari, Namibia

KAL

SURFRAD

◦

◦

◦

40.051
◦
88.373
36.623
116.020
48.308
105.102
34.255
89.873
40.720
77.931
43.734
96.623
40.126
105.238

N
W
◦
N
◦
W
N
◦
W
N
W
◦
N
W
◦
N
W
◦
N
◦
W

◦

◦

◦

213 m

Grassland

1 April 1994

1004 m

Shrubland

1 March 1998

636 m

Grassland

1 November 1994

96 m

Grassland

1 December 1994

373 m

483 m

Cropland

1 June 1998

Grassland

1 June 2003

1692 m

Grassland

1 July 1995

BSRN

◦
N
51.9711
◦
E
4.9267
◦
23.519504
◦
15.083229

S
E

0 m

Grassland

1 December 2005

407 m

Desert

15 December 2012

◦

38.540
◦
8.003
23.551
15.051
22.933
17.992

N
W
◦
S
E
◦
S
E

◦

◦

KIT

230 m

406 m

Savanna

1 January 2009

Desert

1 January 2009

1380 m

Shrubland

1 January 2011

Remote Sens. 2020, 12, 1471

8 of 21

Station measurements are resampled from the one-minute frequency to satellite observation time

by averaging observations performed within ±3 min from the Landsat image acquisition time.

2.3.1. In situ LST Derivation

The pyrogeometers used at SURFRAD and BSRN stations provide broadband radiances in the
infrared wavelength range of 4–50 µm. In the case of broadband measurements, the radiative transfer
equation may be approximated by the Stefan–Boltzmann law:

(cid:115)
LST = 4

Lu − (1 − εBB)Ld
εBBσ

SB

(4)

where Lu and Ld are the measured upward and downward longwave radiances, respectively, εBB is the
broadband emissivity of the surface, and σ
SB is the Stefan–Boltzmann constant. Following Malakar
et al. [25], the broadband emissivity of each site is derived from the ASTER GEDv3 product:

εBB = 0.128 + 0.014ε

A10 + 0.145ε

A11 + 0.241ε

A12 + 0.467ε

A13 + 0.004ε

A14

(5)

where ε
Ai, j = 10 − 14 denote the ASTER narrowband emissivities of bands 10 to 14, respectively.
To account for vegetation dynamics at the site, each ASTER band emissivity is ﬁrst corrected using the
actual Landsat FVC at the time of observation (see Section 2.1.3). The respective broadband value for
each Landsat pixel is then obtained with Equation (5).

For the KIT sites, LST is derived from Planck’s law using a simpliﬁed version of the radiative

transfer equation [40]:

Bλ(LST) =

Lλ,u

− (1 − ελ)Lλ,d

ελ

(6)

where Bλ(LST) represents Planck’s function for wavelength λ, and ελ is the respective surface emissivity.
Lλ,d is the downwelling radiance measured by the upward-facing radiometer. For GBB, the upwelling
radiance, Lλ,u, is directly obtained from the ground-facing radiometer. For EVO and KAL, Lλ,u is
a simple weighted average of the radiances measured by the ground and tree-facing radiometers,
where the fractions of trees/shrubs and ground are used as weights [40,63,64]. To ﬁnd adequate
fractions of trees/shrubs for the Landsat’s FOV, we use high-resolution ﬂight imagery available on
GEE. A perimeter of 30 m is deﬁned around the stations, and trees/shrubs are identiﬁed manually,
yielding values of 45% and 37% for EVO and KAL, respectively. For the GBB station, the emissivity
of the site was determined by Goettsche et al. [65], yielding a value of 0.94 for the KT15 radiometer
band. For EVO and KAL, in order to account for vegetation dynamics, we use the emissivity values
derived for the Landsats, given that the TIR bands are spectrally close to that of the KT15 radiometer.
Due to the narrow band of the KT15 radiometers, a central wavelength of 10.55 µm may be considered
without signiﬁcant loss of accuracy [40], and LST is obtained by inverting Plank’s function.

2.3.2. Statistical Metrics

The obtained Landsat LST is assessed using robust statistics, as recommended by the Committee
on Earth Observation Satellites Working Group (CEOS) on Calibration and Validation—Land Product
Validation (LPV) Subgroup for the validation of Land Surface Temperature Products [66]. The so-called
accuracy is given by the median error, which is the robust equivalent to the bias and computed as:

µ = median(LSTsatellite

− LSTinsitu)

(7)

where LSTsatellite and LSTinsitu are the satellite and in situ LSTs, respectively. The robust equivalent to
the error standard deviation is the so-called precision, given by the median of absolute residuals:
(cid:16)(cid:12)(cid:12)(cid:12)(LSTsatellite

− LSTinsitu) − µ(cid:12)(cid:12)(cid:12)

σ = median

(8)

(cid:17)

Remote Sens. 2020, 12, 1471

9 of 21

As an estimate of the total uncertainty of the product, we also compute the root mean squared

(cid:115)

(LSTsatellite

RMSE =

− LSTinsitu)2
N

(9)

error (RMSE):

where N is the sample size.

3. Results

3.1. Algorithm Calibration

Algorithm coeﬃcients (A, B, and C of Equation (3)) are obtained by the ordinary least square
ﬁtting against the calibration database described in Section 2.2.2. The database is subdivided in classes
of TCWV from 0 to 6 cm in steps of 0.6 cm, yielding a total of 10 sets of (A, B, C) coeﬃcients. Due to
the diﬀerent spectral response functions of the sensors, the calibration must be performed for each
Landsat separately. Figure 2 shows the coeﬃcients obtained for the SMW algorithm and Figure 3 shows
the LST error distribution of Equation (3) when applied to the validation database. The coeﬃcients
determined for the four Landsat sensors are very similar (Figure 2), which is to be expected given their
nearly identical TIR bands. As generally seen in LST retrieval algorithms, the retrieval uncertainty
increases with TCWV (Figure 3), which is due to the increased atmospheric contribution of the TOA
BT. This contribution also impacts the 95% conﬁdence intervals of the coeﬃcients, i.e., they become
wider for higher values of TCWV (Figure 2). For Landsat 4 and 7, there is a slight increase of bias with
TCWV, with the LST being generally overestimated and biases reaching 0.9 K and 1.4 K, respectively,
for very moist atmospheres (Figure 3). For Landsat 5, the increase of the bias with TCWV is particularly
high, reaching 2.5 K for TCWV values above 5.4 cm. For Landsat 8, the bias is negligible, and its error
dispersion is also lower.

Figure 2. Coeﬃcients A (left), B (center), and C (right) of the SMW algorithm (Equation (3)) per class
of total column water vapor (TCWV; cm) for Landsat 4 (L4), 5 (L5), 7 (L7), and 8 (L8). The error bars
indicate the 95% conﬁdence interval of the coeﬃcients.

Figure 3. LST errors of for Landsat 4 (L4), 5 (L5), 7 (L7), and 8 (L8) for the SMW validation database
with ten classes of total column water vapor (TCWV; cm). Boxes indicate the inter-quartile distance,
red lines indicate the median, and whiskers indicate the 5% and 95% percentiles.

Remote Sens. 2019, 11, x FOR PEER REVIEW 9 of 21 (cid:3)coefficients determined for the four Landsat sensors are very similar (Figure 2), which is to be expected given their nearly identical TIR bands. As generally seen in LST retrieval algorithms, the retrieval uncertainty increases with TCWV (Figure 3), which is due to the increased atmospheric contribution of the TOA BT. This contribution also impacts the 95% confidence intervals of the coefficients, i.e., they become wider for higher values of TCWV (Figure 2). For Landsat 4 and 7, there is a slight increase of bias with TCWV, with the LST being generally overestimated and biases reaching 0.9 K and 1.4 K, respectively, for very moist atmospheres (Figure 3). For Landsat 5, the increase of the bias with TCWV is particularly high, reaching 2.5 K for TCWV values above 5.4 cm. For Landsat 8, the bias is negligible, and its error dispersion is also lower.   Figure 2. Coefficients A (left), B (center), and C (right) of the SMW algorithm (equation (3)) per class of total column water vapor (TCWV; cm) for Landsat 4 (L4), 5 (L5), 7 (L7), and 8 (L8). The error bars indicate the 95% confidence interval of the coefficients.  Figure 3. LST errors of for Landsat 4 (L4), 5 (L5), 7 (L7), and 8 (L8) for the SMW validation database with ten classes of total column water vapor (TCWV; cm). Boxes indicate the inter-quartile distance, red lines indicate the median, and whiskers indicate the 5% and 95% percentiles. 3.2. LST Retrieval Figure 4 shows an example of some of the layers generated by the LST production chain for each Landsat image; the data were acquired on the 17th of May 2018 in a region in central Portugal close to Coimbra city, located at approximately 40.2oN and 8.4oW. The region is characterized by extensive forest areas to the west of Coimbra and crop fields in the plains around the banks of the River Mondego. The crop fields are clearly visible in the RGB composite (Figure 4a) in brown tones and correspond mainly to maize, which is generally sown in April and harvested in August or September [67]. In the western part of the Mondego River (close to the river mouth), there are also extensive rice fields. Rice is sown around April/May, and the harvesting takes place around September/October [67]. Close to the seashore, there are also large forest areas, but a larger portion was burned by wildfires in October 2017. The scar of the burned area is also visible in the RGB composite (Figure 4a) as a light brown/yellowish area extending parallel to the coast, from about 40.2oN to 40.4oN.  The first step in the LST production is to match TCVW estimates from NCEP reanalysis data to the Landsat observation time. However, due to the coarse resolution of the model, TCWV values are practically constant over the selected area and, therefore, are not shown. The TIR surface emissivity Remote Sens. 2019, 11, x FOR PEER REVIEW 9 of 21 (cid:3)coefficients determined for the four Landsat sensors are very similar (Figure 2), which is to be expected given their nearly identical TIR bands. As generally seen in LST retrieval algorithms, the retrieval uncertainty increases with TCWV (Figure 3), which is due to the increased atmospheric contribution of the TOA BT. This contribution also impacts the 95% confidence intervals of the coefficients, i.e., they become wider for higher values of TCWV (Figure 2). For Landsat 4 and 7, there is a slight increase of bias with TCWV, with the LST being generally overestimated and biases reaching 0.9 K and 1.4 K, respectively, for very moist atmospheres (Figure 3). For Landsat 5, the increase of the bias with TCWV is particularly high, reaching 2.5 K for TCWV values above 5.4 cm. For Landsat 8, the bias is negligible, and its error dispersion is also lower.   Figure 2. Coefficients A (left), B (center), and C (right) of the SMW algorithm (equation (3)) per class of total column water vapor (TCWV; cm) for Landsat 4 (L4), 5 (L5), 7 (L7), and 8 (L8). The error bars indicate the 95% confidence interval of the coefficients.  Figure 3. LST errors of for Landsat 4 (L4), 5 (L5), 7 (L7), and 8 (L8) for the SMW validation database with ten classes of total column water vapor (TCWV; cm). Boxes indicate the inter-quartile distance, red lines indicate the median, and whiskers indicate the 5% and 95% percentiles. 3.2. LST Retrieval Figure 4 shows an example of some of the layers generated by the LST production chain for each Landsat image; the data were acquired on the 17th of May 2018 in a region in central Portugal close to Coimbra city, located at approximately 40.2oN and 8.4oW. The region is characterized by extensive forest areas to the west of Coimbra and crop fields in the plains around the banks of the River Mondego. The crop fields are clearly visible in the RGB composite (Figure 4a) in brown tones and correspond mainly to maize, which is generally sown in April and harvested in August or September [67]. In the western part of the Mondego River (close to the river mouth), there are also extensive rice fields. Rice is sown around April/May, and the harvesting takes place around September/October [67]. Close to the seashore, there are also large forest areas, but a larger portion was burned by wildfires in October 2017. The scar of the burned area is also visible in the RGB composite (Figure 4a) as a light brown/yellowish area extending parallel to the coast, from about 40.2oN to 40.4oN.  The first step in the LST production is to match TCVW estimates from NCEP reanalysis data to the Landsat observation time. However, due to the coarse resolution of the model, TCWV values are practically constant over the selected area and, therefore, are not shown. The TIR surface emissivity Remote Sens. 2020, 12, 1471

3.2. LST Retrieval

10 of 21

◦

Figure 4 shows an example of some of the layers generated by the LST production chain for each
Landsat image; the data were acquired on the 17th of May 2018 in a region in central Portugal close to
◦
Coimbra city, located at approximately 40.2
W. The region is characterized by extensive
N and 8.4
forest areas to the west of Coimbra and crop ﬁelds in the plains around the banks of the River Mondego.
The crop ﬁelds are clearly visible in the RGB composite (Figure 4a) in brown tones and correspond
mainly to maize, which is generally sown in April and harvested in August or September [67]. In the
western part of the Mondego River (close to the river mouth), there are also extensive rice ﬁelds. Rice is
sown around April/May, and the harvesting takes place around September/October [67]. Close to the
seashore, there are also large forest areas, but a larger portion was burned by wildﬁres in October 2017.
The scar of the burned area is also visible in the RGB composite (Figure 4a) as a light brown/yellowish
◦
area extending parallel to the coast, from about 40.2

◦
N to 40.4

N.

Figure 4. Cont.

Remote Sens. 2019, 11, x FOR PEER REVIEW 10 of 21 (cid:3)needed to compute LST is derived from the ASTER GEDv3 dataset. Figure 4b shows the corresponding emissivity map of ASTER band 14, which approximates the Landsat TIR band best. ASTER NDVI values are used to compute the respective FVC, which is shown in Figure 4c. FVC and emissivity values are quite homogeneous over the selected area. FVC is generally quite low, with values between 0.3 and 0.5 for most of the region. The resulting bare ground emissivity map shows values around 0.96–0.97, which matches those typically found in spectral libraries for the 11(cid:912)m region [53]. Figure 4d shows the respective bare ground emissivity for band 14 derived with equation (2) from the original emissivity values and the FVC. The FVC values for the Landsat image are also derived from the respective NDVI (Figure 4e). The instantaneous FVC map for Landsat shows considerably more variability than for ASTER. The cropland and burned areas show a clear pattern in the FVC map. Furthermore, the rice fields in the westernmost part of the river had very low NDVI values typically associated with water and, therefore, were masked out. The resulting TIR emissivity values for Landsat are displayed in Figure 4f. Areas with low vegetation density have values close to 0.97, while the emissivity values of densely vegetated areas reach values close to 0.99, both in agreement with typical values in spectral libraries [53]. This example emphasizes the importance of using vegetation cover to derive dynamic emissivity values. Figure 4g shows Landsat TOA brightness temperature values, and Figure 4h the corresponding LST values. For the daytime Landsat scene analyzed here, LST is higher over croplands and burned areas than over forests.     Remote Sens. 2020, 12, 1471

11 of 21

Figure 4. Layers of the LST estimation process for the Landsat-8 image retrieved on the 17th of May 2018
over central Portugal (Coimbra). (a) Natural Color (RGB) composite of the red, green, and blue bands
of Landsat-8; (b) ASTER emissivity of band 14; (c) ASTER fraction of vegetation cover (FVC) derived
from ASTER NDVI using Equation (1); (d) Bare ground emissivity of ASTER band 14 derived using
Equation (2); (e) Landsat-8 FVC derived from NDVI using Equation (1); (f) Landsat-8 TIR emissivity
derived with Equation (2) and bare ground emissivity and FVC; (g) brightness temperature (BT; Kelvin)
of Landsat-8 TIR band (B10); (h) land surface temperature (LST; Kelvin) derived for Landsat-8 using
the SMW algorithm.

The ﬁrst step in the LST production is to match TCVW estimates from NCEP reanalysis data to
the Landsat observation time. However, due to the coarse resolution of the model, TCWV values are
practically constant over the selected area and, therefore, are not shown. The TIR surface emissivity
needed to compute LST is derived from the ASTER GEDv3 dataset. Figure 4b shows the corresponding
emissivity map of ASTER band 14, which approximates the Landsat TIR band best. ASTER NDVI
values are used to compute the respective FVC, which is shown in Figure 4c. FVC and emissivity values
are quite homogeneous over the selected area. FVC is generally quite low, with values between 0.3 and
0.5 for most of the region. The resulting bare ground emissivity map shows values around 0.96–0.97,
which matches those typically found in spectral libraries for the 11µm region [53]. Figure 4d shows the
respective bare ground emissivity for band 14 derived with Equation (2) from the original emissivity
values and the FVC. The FVC values for the Landsat image are also derived from the respective NDVI
(Figure 4e). The instantaneous FVC map for Landsat shows considerably more variability than for
ASTER. The cropland and burned areas show a clear pattern in the FVC map. Furthermore, the rice
ﬁelds in the westernmost part of the river had very low NDVI values typically associated with water
and, therefore, were masked out. The resulting TIR emissivity values for Landsat are displayed in
Figure 4f. Areas with low vegetation density have values close to 0.97, while the emissivity values of
densely vegetated areas reach values close to 0.99, both in agreement with typical values in spectral
libraries [53]. This example emphasizes the importance of using vegetation cover to derive dynamic
emissivity values. Figure 4g shows Landsat TOA brightness temperature values, and Figure 4h the
corresponding LST values. For the daytime Landsat scene analyzed here, LST is higher over croplands
and burned areas than over forests.

3.3. Validation with in situ LST

The quality of derived Landsat LST is assessed with in situ LST derived from twelve validation
stations. Since in situ data were unavailable for Landsat-4, comparisons were only performed for
Landsat 5, 7, and 8. We found a considerable number of Landsat LST values, much lower than the
in situ estimates, which is probably due to cloud contamination. Besides producing outliers and
yielding a bias, cloud contamination also aﬀects NDVI and, therefore, emissivity estimation. Indeed,
NDVI values over clouds are generally considerably lower, which results in lower FVC values and,
consequently, lower emissivity; however, the dominant eﬀect is the impact on BT. To assess the quality
of the satellite LST with a minimum of cloud contamination, we applied a “3σ-Hampel identiﬁer” to

Remote Sens. 2019, 11, x FOR PEER REVIEW 11 of 21 (cid:3)   Figure 4. Layers of the LST estimation process for the Landsat-8 image retrieved on the 17th of May 2018 over central Portugal (Coimbra). (a) Natural Color (RGB) composite of the red, green, and blue bands of Landsat-8; (b) ASTER emissivity of band 14; (c) ASTER fraction of vegetation cover (FVC) derived from ASTER NDVI using equation (1); (d) Bare ground emissivity of ASTER band 14 derived using equation (2); (e) Landsat-8 FVC derived from NDVI using equation (1); (f) Landsat-8 TIR emissivity derived with equation (2) and bare ground emissivity and FVC; (g) brightness temperature (BT; Kelvin) of Landsat-8 TIR band (B10); (h) land surface temperature (LST; Kelvin) derived for Landsat-8 using the SMW algorithm. 3.3. Validation with in situ LST The quality of derived Landsat LST is assessed with in situ LST derived from twelve validation stations. Since in situ data were unavailable for Landsat-4, comparisons were only performed for Landsat 5, 7, and 8. We found a considerable number of Landsat LST values, much lower than the in situ estimates, which is probably due to cloud contamination. Besides producing outliers and yielding a bias, cloud contamination also affects NDVI and, therefore, emissivity estimation. Indeed, NDVI values over clouds are generally considerably lower, which results in lower FVC values and, consequently, lower emissivity; however, the dominant effect is the impact on BT. To assess the quality of the satellite LST with a minimum of cloud contamination, we applied a “3(cid:919)-Hampel identifier” to remove potential outliers [68,69]. Figure 5 shows scatterplots between Landsat LST and in situ LST for each of the twelve sites. For each Landsat, the 3(cid:919) limit is indicated by dashed lines, and the provided statistics are derived after the outliers’ removal. Table 3 presents the corresponding statistics for each site (black figures—original data, grey figures—outliers removed).  The accuracy/bias ((cid:912)) is generally better than or close to 1 K, except for FPK, TBL, and GOB stations, with values varying between -1.2 and 1.3 K. The bias is highest at the GOB station but it is very low at GBB, which is located in the same area. Apart from FPK, TBL, and GOB, the RMSE values range between 1.4 K and 2.5 K. The lower RMSE values are found in KAL e DRA, and the best precision ((cid:919)) values are found in DRA, CAB, and KAL, which are all located in very homogeneous areas. There is no evident pattern when comparing between Landsats; Figure 3 suggests that Landsat 8 might perform slightly better for extremely moist atmospheres (essentially when total column water vapor reaches values above 5 cm), which, outside the tropics, is rare under clear skies. Without considering FPK, TBL, and GOB stations, the overall accuracy of the Landsat 5, 7, and 8 is 0.5 K, 0.0(3) K and 0.3 K, respectively, which meet the threshold accuracy proposed by Guillevic et al. [66]. The overall precision (RMSE) is 1.3 (2.0) K, 1.1 (2.0) K, and 1.0 (1.9) K for Landsat 5, 7, and 8, respectively.  Remote Sens. 2020, 12, 1471

12 of 21

remove potential outliers [68,69]. Figure 5 shows scatterplots between Landsat LST and in situ LST for
each of the twelve sites. For each Landsat, the 3σ limit is indicated by dashed lines, and the provided
statistics are derived after the outliers’ removal. Table 3 presents the corresponding statistics for each
site (black ﬁgures—original data, grey ﬁgures—outliers removed).

Figure 5. Landsat 5 (L5), 7 (L7), and 8 (L8) LST against in situ LST (K) for the full period of available
data over each validation site. The dashed lines show the ±3σ limits used to ﬁlter outliers while colors
indicate the Landsat number (see legends). The respective statistics, namely accuracy (µ; K), precision
(σ; K), and RMSE (K), are shown in the same color as their corresponding Landsat.

Remote Sens. 2019, 11, x FOR PEER REVIEW 12 of 21 (cid:3)            Figure 5. Landsat 5 (L5), 7 (L7), and 8 (L8) LST against in situ LST (K) for the full period of available data over each validation site. The dashed lines show the ±3(cid:919) limits used to filter outliers while colors indicate the Landsat number (see legends). The respective statistics, namely accuracy ((cid:912); K), precision ((cid:919); K), and RMSE (K), are shown in the same color as their corresponding Landsat. Table 3. Validation statistics for Landsat 5 (L5), 7 (L7), and 8 (L8) over each site, namely accuracy ((cid:912); K), precision ((cid:919); K), RMSE (K), and the number of observations (N). The black figures are the statistics Remote Sens. 2020, 12, 1471

13 of 21

Table 3. Validation statistics for Landsat 5 (L5), 7 (L7), and 8 (L8) over each site, namely accuracy (µ; K),
precision (σ; K), RMSE (K), and the number of observations (N). The black ﬁgures are the statistics after
removing outliers with the 3σ-rule. The gray ﬁgures are the statistics for the original (unﬁltered) data.

Station

BND

DRA

FPK

GWN

PSU

SXF

TBL

CAB

GOB

EVO

GBB

KAL

µ (K)

σ (K)

RMSE (K)

L5

1.2
1.1
0.1
0.1
1.9
1.8
0.3
0.3

0.6
0.5
2.7
2.5

0.3
−0.1
0.2
0.2

L7

0.9
0.9
−0.6
−0.7
3.0
3.0
0.5
0.5
0.2
0.2
0.9
0.8
2.6
2.4
−1.2
−1.4
2.9
3.2
−1.2
−1.2
0.6
0.6
0.1
0.1

L8

1.3
1.1
−0.4
−0.6
2.4
2.4
0.0
−0.1
0.2
0.2
1.0
1.4
2.0
1.7
−0.6
−0.6
2.3
2.4
−0.3
−0.4
1.3
1.4
0.3
0.2

L5

1.4
1.5
1.0
1.0
1.1
1.4
1.2
1.2

1.1
1.2
1.5
1.7

1.4
1.3
1.5
1.5

L7

1.3
1.4
0.8
1.0
1.8
1.9
0.9
1.1
1.0
1.1
1.3
1.4
1.9
1.9

0.9
1.4
1.6
1.6

1.3
1.3
1.4
1.5
1.1
1.2

L8

1.1
1.3
1.0
1.2
1.7
1.8
1.1
1.2
1.1
1.1
1.0
1.2
2.1
2.1

0.9
1.1
1.3
1.6

1.1
1.2
1.0
1.0
0.8
0.9

L5

2.5
3.2
1.7
6.6
2.6
8.8
2.0
3.4

1.7
3.2
3.6
4.5

2.3
3.7
1.9
1.9

L7

2.4
3.7
1.6
4.1
3.9
5.4
1.9
3.8
1.7
1.9
2.3
3.5
3.7
4.8

2.3
5.0
3.7
4.2

2.2
3.0
2.2
2.4
1.6
2.7

L8

2.4
4.3
2.0
2.9
3.4
3.6
1.8
2.9
2.0
2.0
2.1
2.6
3.7
5.4

1.8
3.0
2.9
3.8

2.1
3.2
1.9
2.5
1.4
3.7

L5

98
102
109
115
110
123
146
155
0
0
50
54
119
123

0
0
0
0

29
31
11
11
0
1

N

L7

177
190
189
209
242
250
211
227
23
24
100
107
208
219

46
56
97
103

113
119
106
108
70
74

L8

115
133
201
215
172
174
115
124
22
22
115
123
140
145

79
86
131
140

94
104
102
109
86
92

The accuracy/bias (µ) is generally better than or close to 1 K, except for FPK, TBL, and GOB
stations, with values varying between -1.2 and 1.3 K. The bias is highest at the GOB station but it is very
low at GBB, which is located in the same area. Apart from FPK, TBL, and GOB, the RMSE values range
between 1.4 K and 2.5 K. The lower RMSE values are found in KAL e DRA, and the best precision (σ)
values are found in DRA, CAB, and KAL, which are all located in very homogeneous areas. There is no
evident pattern when comparing between Landsats; Figure 3 suggests that Landsat 8 might perform
slightly better for extremely moist atmospheres (essentially when total column water vapor reaches
values above 5 cm), which, outside the tropics, is rare under clear skies. Without considering FPK,
TBL, and GOB stations, the overall accuracy of the Landsat 5, 7, and 8 is 0.5 K, 0.0(3) K and 0.3 K,
respectively, which meet the threshold accuracy proposed by Guillevic et al. [66]. The overall precision
(RMSE) is 1.3 (2.0) K, 1.1 (2.0) K, and 1.0 (1.9) K for Landsat 5, 7, and 8, respectively.

4. Discussion

This work presents a methodology to derive LST from the Landsat series with GEE.
We implemented the single-channel empirical algorithm proposed by Duguay-Tetzlaﬀ et al. [35]
because it combines simplicity with reasonable accuracy. Furthermore, the CM-SAF used this algorithm
to generate a climate data record of LST for the Meteosat series of satellites and, therefore, has been
extensively analyzed. A similar algorithm (without explicit dependence on emissivity) is used by the
Copernicus Global Land Service to generate LST from the Geostationary Operational Environmental
Satellites (GOES) and the Multi-Function Transport Satellite (MTSAT) [55]; a detailed quality assessment
of this product is performed continuously and available at https://land.copernicus.eu/global/products/lst.
The algorithm uncertainty (Figure 3) obtained here are similar to those obtained by Duguay-Tetzlaﬀ
et al. [35] and Freitas et al. [55]. Landsat 5 shows the largest errors, followed by Landsat 7, 4,
and 8—these discrepancies are related to the diﬀerent spectral characteristics of the sensors. While the

Remote Sens. 2020, 12, 1471

14 of 21

TIR bands of Landsat 4, 5, and 7 have similar widths, their spectral response functions diﬀer slightly.
Of the three satellites, the TIR signal measured by Landsat 5 has the highest weight around 12 µm,
followed by Landsat 7 and 4. Since water vapor absorption/emission in the 12 µm spectral region
is higher than in the 10–11 µm region, a larger contribution from the 12 µm region decreases the
algorithm’s retrieval performance. The TIR band of Landsat 8 is considerably narrower than for the
other Landsats, and excludes the 12 µm region, which allows retrieving LST with better accuracy.
Algorithms using both TIR bands of Landsat 8 (such as split-window algorithms) could provide better
estimates of LST; unfortunately, a calibration problem of the TIRS sensor identiﬁed by USGS introduces
large calibration uncertainty into the 12 µm band [70]. We conﬁrmed this with independent Landsat
8 LST retrievals with a split-window algorithm, which showed a substantial degradation of retrieval
quality over the GBB station (not shown).

The quality of the LST retrievals was further assessed in comparisons with in situ LST estimates
from 12 stations obtained from the SURFRAD, BSRN, and KIT networks. The KIT network includes
three stations dedicated to LST retrieval located on sites that are homogeneous at the satellite’s pixel scale.
At these stations, radiance measurements are performed by radiometers with spectral and directional
characteristics similar to those typical of satellite sensors. SURFRAD and BSRN stations provide
hemispherical measurements of broadband infrared radiative ﬂux. Despite providing high-quality
observations, several authors pointed out several limitations of the SURFRAD measurements for
validating satellite LST, most importantly, a lack of spatial representativeness [59,62]. The BSRN sites,
CAB and GOB, are located in highly homogeneous areas and have been previously used for validating
satellite-derived LST (e.g., [70–72]).

In order to study and better understand the impact of land cover heterogeneity on the LST
comparisons, we obtained Google high-resolution images for each site (Figure 6). Within GEE, circles
with 30 m and 100 m radius were superimposed on the images. The 30 m circle is used to represent the
resampled spatial resolution of the Landsat’s TIR bands, while the 100 m circle approximates their
original resolution. The 30 m circles correspond to the geometries used in GEE to extract the Landsat
LST time-series used in the validation exercise. It should be noted that these geometries are not meant
to represent the actual shape of the Landsat pixels. In fact, the actual areas of the circles (with widths of
60 m and 200 m) are larger than both the resampled and original pixel areas. Since the actual position of
Landsat pixels varies between overpasses and to account for geolocation uncertainties, we’ve selected
a slightly larger area. For some stations, these areas are slightly distanced from the station location in
order to encompass more homogeneous surfaces. For instance, at BND shifting the circle slightly to
the northeast ensures that most Landsat signal is coming from the grass patch where the station is
located (Figure 6a).

4.1. SURFRAD Stations

Statistics at BND, SXF, PSU, and GWN suggest good quality of the LST retrievals and agree well
with those obtained by Malakar et al. [25]. Some overestimation at higher LST values is noticeable (above
~305 K; Figure 5). The algorithm validation exercise suggests that the SMW slightly overestimates
high LST values for Landsat 5 and 7 and slightly underestimates high LSTs for Landsat 8 (not shown).
However, the same bias is not observed at DRA, GBB, or KAL stations where even higher LST values
are observed. This suggests a likely underestimation of surface emissivity during the warm season
when LSTs are higher. Although the same method is used to obtain Landsat and in situ emissivity,
the impact of emissivity uncertainties on LST estimates is diﬀerent in each case. Empirical LST retrieval
algorithms, such as the SMW are generally more sensitive to emissivity errors than methods that derive
in situ LST directly with Planck’s or Stefan–Boltzmann law.

Some authors found large biases when validating satellite-derived LST with in situ LST from DRA
station (e.g., [25,59,62,73]). In contrast, we found good agreement between Landsat LST and DRA
station LST, with bias values within ±0.5 K. DRA station is located in a desert area with sparse shrub
cover. This seems to indicate that the station is more representative of Landsat’s spatial scale than

Remote Sens. 2020, 12, 1471

15 of 21

satellite sensors with a lower spatial resolution, e.g., MODIS. However, for Landsat, Malakar et al. [25]
obtained a large positive bias over DRA. Looking at Figure 13 in Malakar et al. [25], we found that the
area we selected for the time-series retrieval is slightly north of the respective area used by Malakar
et al. Figure 7 shows LST values from Landsat-8 at DRA averaged for the years 2017 to 2019. The LST
values extracted from our selected area (black circle) are on average 1 K lower than the corresponding
LST extracted slightly further south (purple circle), which might explain the lower bias.

At the FPK station, the biases are slightly larger (1.3 K, 1.9 K, and 1.8 K for Landsat 5, 7, and 8,
respectively) than at most SURFRAD stations (Table 3). The bias seems to be mainly caused by LST
observations above 300 K. As mentioned above, this overestimation at high LSTs could be related to
an underestimation of emissivity during the warm season. We also obtain large biases at TBL station
(2.3 K, 2.1 K, and 1.6 K for Landsat 5, 7, and 8, respectively). Analyses of the average LST retrieved
from 2017 to 2019 with Landsat-8 (Figure 7), indicate that there are strong LST variations (almost 10 K)
around the station, which are likely due to diﬀerences in soil and vegetation. The area selected to
extract the Landsat LSTs (black circle) generally has slightly lower LST values than the area directly
around the station (purple circle). However, the bias values are still quite high (Table 3), and the
high spatial heterogeneity at this small scale makes it diﬃcult to select a single representative area for
the station.

4.2. BSRN Stations

The bias obtained at GOB station is quite high (2.3 K and 1.9 K for Landsat 7 and 8, respectively),
while at GBB, which is located in the same area, the bias is much lower (0.1 K, -0.1 K, and 1.1 K
for Landsat 5, 7, and 8, respectively). At GOB, the downwelling radiance sensor is located near the
Gobabeb Research and Training Center, while the upwelling sensor is located approximately 7 km
northeast. Since the upwelling radiance is most relevant for LST derivation, we’ve extracted the LST
times-series for the Landsat at the location of the upwelling sensor. Nevertheless, the distance between
the two sensors may introduce additional uncertainty into the estimation of the in situ LST.

4.3. KIT Stations

Landsat LST shows good agreement with the KIT stations. While EVO and KAL are very
homogeneous in terms of land cover, they are heterogeneous when considering the diﬀerent surface
elements. Therefore, a proper upscaling of their in situ LSTs is required [40,63,64]. Given Landsat’s
high spatial resolution, we assume that the temperature contrasts between trees/shrubs and sunlit
ground are most relevant and neglect possible shadowing eﬀects. This assumption may lead to a slight
increase in the in situ LST uncertainty. Also, the upscaling methodology is sensitive to the prescribed
fraction of trees/shrubs, particularly at EVO, where LST contrasts between tree crowns and sunlit
ground are the highest. Ermida et al. [64] reported that a 5% error in the fraction of tree crown cover
could lead to an additional LST uncertainty up to 1.4 K in summer.

The GBB site has been carefully characterized in order to provide very accurate LST estimations
for validation exercises. The instrument characteristics are similar to those generally seen in TIR
satellite sensors and therefore is likely to provide LST estimates closer to the satellite estimates.
Also, the emissivity of the site was obtained experimentally, increasing the accuracy of the in situ
LST estimates.

When comparing the three Landsats, we were not able to identify a clear pattern of one sensor
outperforming the other. Although we found a slightly poorer algorithm performance for Landsat-7,
the general statistics do not indicate a lower LST retrieval quality for this sensor. This may be due to
the higher spatial resolution of Landsat 7, which partially compensates the lower radiometric accuracy
by reducing problems associated with site heterogeneity. However, when considering only the most
homogeneous and stable stations GBB, CAB, and GOB, Landsat-7 LSTs show higher RMSE values
that are suspected to be related to limitations in the atmospheric correction. Moreover, the algorithm

Remote Sens. 2020, 12, 1471

16 of 21

performance is only slightly reduced for extremely moist atmospheres (Figure 3; TCWV above 5 cm),
which rarely occur under clear skies outside the tropics.

It was not possible to validate Landsat-4 LST retrievals since in situ data are unavailable for its
period of operation. However, given the nearly identical instrument characteristics of Landsat 4 and 5,
we expect the quality of the Landsat-4 LST retrievals to closely resemble that of Landsat-5.

Figure 6. High-resolution natural color imagery for each validation site (from Google Earth Engine).
The pins indicate the station locations. The smaller black circles (30 m radius) represent the areas
selected to retrieve the LST time-series. The larger circles (100 m radius) represent Landsats TIR band’s
eﬀective spatial resolution.

Remote Sens. 2019, 11, x FOR PEER REVIEW 16 of 21 (cid:3)(cid:258)(cid:895)(cid:3)(cid:17)(cid:69)(cid:24)(cid:3)(cid:3)(cid:271)(cid:895)(cid:3)(cid:24)(cid:90)(cid:4)(cid:3)(cid:3)(cid:272)(cid:895)(cid:3)(cid:38)(cid:87)(cid:60)(cid:3)(cid:3)(cid:282)(cid:895)(cid:3)(cid:39)(cid:116)(cid:69)(cid:3)(cid:3)(cid:286)(cid:895)(cid:3)(cid:87)(cid:94)(cid:104)(cid:3)(cid:3)(cid:296)(cid:895)(cid:3)(cid:94)(cid:121)(cid:38)(cid:3)(cid:3)(cid:336)(cid:895)(cid:3)(cid:100)(cid:17)(cid:62)(cid:3)(cid:3)(cid:346)(cid:895)(cid:3)(cid:18)(cid:4)(cid:17)(cid:3)(cid:3)(cid:349)(cid:895)(cid:3)(cid:39)(cid:75)(cid:17)(cid:3)(cid:3)(cid:361)(cid:895)(cid:3)(cid:28)(cid:115)(cid:75)(cid:3)(cid:3)(cid:364)(cid:895)(cid:3)(cid:39)(cid:17)(cid:17)(cid:3)(cid:3)(cid:373)(cid:895)(cid:3)(cid:60)(cid:4)(cid:62)(cid:3) Figure 6. High-resolution natural color imagery for each validation site (from Google Earth Engine). The pins indicate the station locations. The smaller black circles (30 m radius) represent the areas selected to retrieve the LST time-series. The larger circles (100 m radius) represent Landsats TIR band’s effective spatial resolution. (cid:3) Remote Sens. 2020, 12, 1471

17 of 21

Figure 7. Landsat-8 2017–2019 average LST at the DRA and TBL sites. The black circles indicate the
areas selected to retrieve the LST time-series, while the purple circles are centered on the stations.
Both circles have a 30 m radius.

5. Conclusions

High-resolution LST estimates are increasingly used in small-scale studies. The Landsat series of
satellites is particularly appropriate for such studies as it provides imagery at a high spatial resolution
that is suitable for a broad range of applications. Although various algorithms for deriving Landsat LST
have been proposed, such data are not easily available and generally lack consistency for the diﬀerent
Landsat satellites. Furthermore, the existing Landsat LST datasets require users to store the involved
data locally, and the data processing and analysis may be computationally demanding. Making use of
the computational resources of Google’s servers, the new GEE online platform allows remote sensing
data users to easily analyze large amounts of data. This study provides a GEE repository with all the
code necessary to derive LST from Landsat. Furthermore, users are not required to download any
data: simply by accessing the code, they can perform all their analyses within GEE. Users can also
edit the code to better meet their needs, and improvements may be implemented over time. The GEE
repository is publicly available at:

https://code.earthengine.google.com/?accept_repo=users/soﬁaermida/landsat_smw_lst.
The LST values are estimated using the SMW algorithm developed by CM-SAF. For each
Landsat, the algorithm coeﬃcients were derived using the same calibration database, thereby ensuring
consistency between the satellites. All inputs to the algorithm are obtained from the GEE catalog, i.e.,
the water vapor content from NCEP/NCAR reanalysis data and emissivity from the ASTER GEDv3
dataset with an NDVI-based correction for vegetation dynamics. A validation exercise with in situ LST
obtained from 12 stations indicated an overall accuracy of 0.5 K, -0.1 K, and 0.2 K and overall RMSE of
2.0 K, 2.1 K, and 2.1 K for Landsat 5, 7, and 8, respectively.

As the code is available publicly, future improvements to this methodology may be implemented

based on user feedback.

Author Contributions: Conceptualization, S.L.E., P.S., V.M. and I.T; methodology, S.L.E.; software, S.L.E.;
validation, S.L.E., F.-M.G. and I.F.T.; formal analysis, S.L.E. and P.S.; investigation, S.L.E. and P.S.; resources, V.M.,
F.-M.G. and I.F.T.; data curation, F.G.; writing—original draft preparation, S.L.E.; writing—review and editing,
P.S., V.M., F.-M.G. and I.F.T.; visualization, S.L.E.; supervision, V.M. and I.F.T.; project administration, I.T.; funding
acquisition, I.F.T. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by Fundação para a Ciência e a Tecnologia (FCT) grant number
PTDC/CTA-MET/28946/2017 (CONTROL).

Acknowledgments: Research work by Soﬁa L. Ermida, Frank M. Göttsche, and Isabel F. Trigo were funded by the
LSA SAF project (http://landsaf.ipma.pt) funded by EUMETSAT.

Remote Sens. 2019, 11, x FOR PEER REVIEW 17 of 21 (cid:3)(cid:24)(cid:90)(cid:4)(cid:3)(cid:3)(cid:100)(cid:17)(cid:62)(cid:3)(cid:3)(cid:3)(cid:3)Figure 7. Landsat-8 2017–2019 average LST at the DRA and TBL sites. The black circles indicate the areas selected to retrieve the LST time-series, while the purple circles are centered on the stations. Both circles have a 30 m radius. 5. Conclusions High-resolution LST estimates are increasingly used in small-scale studies. The Landsat series of satellites is particularly appropriate for such studies as it provides imagery at a high spatial resolution that is suitable for a broad range of applications. Although various algorithms for deriving Landsat LST have been proposed, such data are not easily available and generally lack consistency for the different Landsat satellites. Furthermore, the existing Landsat LST datasets require users to store the involved data locally, and the data processing and analysis may be computationally demanding. Making use of the computational resources of Google’s servers, the new GEE online platform allows remote sensing data users to easily analyze large amounts of data. This study provides a GEE repository with all the code necessary to derive LST from Landsat. Furthermore, users are not required to download any data: simply by accessing the code, they can perform all their analyses within GEE. Users can also edit the code to better meet their needs, and improvements may be implemented over time. The GEE repository is publicly available at: https://code.earthengine.google.com/?accept_repo=users/sofiaermida/landsat_smw_lst  The LST values are estimated using the SMW algorithm developed by CM-SAF. For each Landsat, the algorithm coefficients were derived using the same calibration database, thereby ensuring consistency between the satellites. All inputs to the algorithm are obtained from the GEE catalog, i.e., the water vapor content from NCEP/NCAR reanalysis data and emissivity from the ASTER GEDv3 dataset with an NDVI-based correction for vegetation dynamics. A validation exercise with in situ LST obtained from 12 stations indicated an overall accuracy of 0.5 K, -0.1 K, and 0.2 K and overall RMSE of 2.0 K, 2.1 K, and 2.1 K for Landsat 5, 7, and 8, respectively. As the code is available publicly, future improvements to this methodology may be implemented based on user feedback. Author Contributions: conceptualization, S.E., P.S., V.M. and I.T; methodology, S.E; software, S.E.; validation, S.E., F.-M.G. and I.F.T.; formal analysis, S.E. and P.S.; investigation, S.E. and P.S.; resources, V.M., F.-M.G. and I.F.T.; data curation, F.G.; writing—original draft preparation, S.E.; writing—review and editing, P.S., V.M., F.-M.G. and I.F.T.; visualization, S.E.; supervision, V.M. and I.F.T.; project administration, I.T.; funding acquisition, I.F.T. All authors have read and agreed to the published version of the manuscript. Funding: This research was funded by Fundação para a Ciência e a Tecnologia (FCT) grant number PTDC/CTA-MET/28946/2017 (CONTROL).  Acknowledgments: Research work by Sofia L. Ermida, Frank M. Göttsche, and Isabel F. Trigo were funded by the LSA SAF project (http://landsaf.ipma.pt) funded by EUMETSAT.  Remote Sens. 2020, 12, 1471

18 of 21

Conﬂicts of Interest: The authors declare no conﬂict of interest.

References

2.

1. Mokhtari, A.; Noory, H.; Pourshakouri, F.; Haghighatmehr, P.; Afrasiabian, Y.; Razavi, M.; Fereydooni, F.;
Sadeghi Naeni, A. Calculating potential evapotranspiration and single crop coeﬃcient based on energy
balance equation using Landsat 8 and Sentinel-2. ISPRS J. Photogramm. Remote Sens. 2019, 154, 231–245.
[CrossRef]
Peng, J.; Jia, J.; Liu, Y.; Li, H.; Wu, J. Seasonal contrast of the dominant factors for spatial distribution of land
surface temperature in urban areas. Remote Sens. Environ. 2018, 215, 255–267. [CrossRef]
Tran, D.X.; Pla, F.; Latorre-Carmona, P.; Myint, S.W.; Caetano, M.; Kieu, H.V. Characterizing the relationship
between land use land cover change and land surface temperature. ISPRS J. Photogramm. Remote Sens. 2017,
124, 119–132. [CrossRef]
Estoque, R.C.; Murayama, Y. Monitoring surface urban heat island formation in a tropical mountain city
using Landsat data (1987–2015). ISPRS J. Photogramm. Remote Sens. 2017, 133, 18–29. [CrossRef]
Fu, P.; Weng, Q. A time series analysis of urbanization induced land use and land cover change and its impact
on land surface temperature with Landsat imagery. Remote Sens. Environ. 2016, 175, 205–214. [CrossRef]

3.

5.

4.

7.

6. Maimaitiyiming, M.; Ghulam, A.; Tiyip, T.; Pla, F.; Latorre-Carmona, P.; Halik, Ü.; Sawut, M.; Caetano, M.
Eﬀects of green space spatial pattern on land surface temperature: Implications for sustainable urban
planning and climate change adaptation. ISPRS J. Photogramm. Remote Sens. 2014, 89, 59–66. [CrossRef]
Vlassova, L.; Pérez-Cabello, F.; Mimbrero, M.; Llovería, R.; García-Martín, A. Analysis of the Relationship
between Land Surface Temperature and Wildﬁre Severity in a Series of Landsat Images. Remote Sens. 2014, 6,
6136–6162. [CrossRef]
Rogan, J.; Ziemer, M.; Martin, D.; Ratick, S.; Cuba, N.; DeLauer, V. The impact of tree cover loss on land
surface temperature: A case study of central Massachusetts using Landsat Thematic Mapper thermal data.
Appl. Geogr. 2013, 45, 49–57. [CrossRef]
Zhang, Y.; Odeh, I.O.A.; Ramadan, E. Assessment of land surface temperature in relation to landscape
metrics and fractional vegetation cover in an urban/peri-urban region using Landsat data. Int. J. Remote Sens.
2013, 34, 168–189. [CrossRef]

8.

9.

10. Bindhu, V.M.; Narasimhan, B.; Sudheer, K.P. Development and veriﬁcation of a non-linear disaggregation
method (NL-DisTrad) to downscale MODIS land surface temperature to the spatial scale of Landsat thermal
data to estimate evapotranspiration. Remote Sens. Environ. 2013, 135, 118–129. [CrossRef]

11. Anderson, M.C.; Allen, R.G.; Morse, A.; Kustas, W.P. Use of Landsat thermal imagery in monitoring
evapotranspiration and managing water resources. Remote Sens. Environ. 2012, 122, 50–65. [CrossRef]
12. Amiri, R.; Weng, Q.; Alimohammadi, A.; Alavipanah, S.K. Spatial–temporal dynamics of land surface
temperature in relation to fractional vegetation cover and land use/cover in the Tabriz urban area, Iran.
Remote Sens. Environ. 2009, 113, 2606–2617. [CrossRef]

13. Xiao, H.; Weng, Q. The impact of land use and land cover changes on land surface temperature in a karst

area of China. J. Environ. Manage. 2007, 85, 245–257. [CrossRef] [PubMed]

14. XIAO, R.; OUYANG, Z.; ZHENG, H.; LI, W.; SCHIENKE, E.W.; WANG, X. Spatial pattern of impervious
surfaces and their impacts on land surface temperature in Beijing, China. J. Environ. Sci. 2007, 19, 250–256.
[CrossRef]

15. Xian, G.; Crane, M. An analysis of urban thermal characteristics and associated land cover in Tampa Bay and

Las Vegas using Landsat satellite data. Remote Sens. Environ. 2006, 104, 147–156. [CrossRef]

16. Vlassova, L.; Perez-Cabello, F.; Nieto, H.; Martín, P.; Riaño, D.; de la Riva, J. Assessment of Methods for Land
Surface Temperature Retrieval from Landsat-5 TM Images Applicable to Multiscale Tree-Grass Ecosystem
Modeling. Remote Sens. 2014, 6, 4345–4368. [CrossRef]

17. Wang, F.; Qin, Z.; Song, C.; Tu, L.; Karnieli, A.; Zhao, S. An Improved Mono-Window Algorithm for Land
Surface Temperature Retrieval from Landsat 8 Thermal Infrared Sensor Data. Remote Sens. 2015, 7, 4268–4289.
[CrossRef]

18. Cristóbal, J.; Jiménez-Muñoz, J.C.; Sobrino, J.A.; Ninyerola, M.; Pons, X. Improvements in land surface
temperature retrieval from the Landsat series thermal band using water vapor and air temperature.
J. Geophys. Res. 2009, 114, D08103. [CrossRef]

Remote Sens. 2020, 12, 1471

19 of 21

19. Qin, Z.; Karnieli, A.; Berliner, P. A mono-window algorithm for retrieving land surface temperature from
Landsat TM data and its application to the Israel-Egypt border region. Int. J. Remote Sens. 2001, 22, 3719–3746.
[CrossRef]

20. Zhang, Z.; He, G. Generation of Landsat surface temperature product for China, 2000–2010. Int. J. Remote

Sens. 2013, 34, 7369–7375. [CrossRef]

21. Li, F.; Jackson, T.J.; Kustas, W.P.; Schmugge, T.J.; French, A.N.; Cosh, M.H.; Bindlish, R. Deriving land surface
temperature from Landsat 5 and 7 during SMEX02/SMACEX. Remote Sens. Environ. 2004, 92, 521–534.
[CrossRef]
Sobrino, J.A.; Jiménez-Muñoz, J.C.; Paolini, L. Land surface temperature retrieval from LANDSAT TM 5.
Remote Sens. Environ. 2004, 90, 434–440. [CrossRef]

22.

23. Cristóbal, J.; Jiménez-Muñoz, J.; Prakash, A.; Mattar, C.; Skokovi´c, D.; Sobrino, J. An Improved Single-Channel
Method to Retrieve Land Surface Temperature from the Landsat-8 Thermal Band. Remote Sens. 2018, 10, 431.
[CrossRef]

24. Zhou, J.; Li, J.; Zhang, L.; Hu, D.; Zhan, W. Intercomparison of methods for estimating land surface
temperature from a Landsat-5 TM image in an arid region with low water vapour in the atmosphere. Int. J.
Remote Sens. 2012, 33, 2582–2602. [CrossRef]

25. Malakar, N.K.; Hulley, G.C.; Hook, S.J.; Laraby, K.; Cook, M.; Schott, J.R. An Operational Land Surface
Temperature Product for Landsat Thermal Data: Methodology and Validation. IEEE Trans. Geosci. Remote
Sens. 2018, 56, 5717–5735. [CrossRef]

26. Parastatidis, D.; Mitraka, Z.; Chrysoulakis, N.; Abrams, M. Online Global Land Surface Temperature

27.

Estimation from Landsat. Remote Sens. 2017, 9, 1208. [CrossRef]
Jimenez-Munoz, J.C.; Cristobal, J.; Sobrino, J.A.; Soria, G.; Ninyerola, M.; Pons, X.; Pons, X. Revision of the
Single-Channel Algorithm for Land Surface Temperature Retrieval From Landsat Thermal-Infrared Data.
IEEE Trans. Geosci. Remote Sens. 2009, 47, 339–349. [CrossRef]

28. Meng, X.; Cheng, J.; Zhao, S.; Liu, S.; Yao, Y. Estimating Land Surface Temperature from Landsat-8 Data

using the NOAA JPSS Enterprise Algorithm. Remote Sens. 2019, 11, 155. [CrossRef]

29. Duan, S.-B.; Li, Z.-L.; Wang, C.; Zhang, S.; Tang, B.-H.; Leng, P.; Gao, M.-F. Land-surface temperature retrieval
from Landsat 8 single-channel thermal infrared data in combination with NCEP reanalysis data and ASTER
GED product. Int. J. Remote Sens. 2019, 40, 1763–1778. [CrossRef]

30. Li, S.; Jiang, G.-M. Land Surface Temperature Retrieval From Landsat-8 Data With the Generalized

Split-Window Algorithm. IEEE Access 2018, 6, 18149–18162. [CrossRef]

31. Gorelick, N.; Hancher, M.; Dixon, M.; Ilyushchenko, S.; Thau, D.; Moore, R. Google Earth Engine:

Planetary-scale geospatial analysis for everyone. Remote Sens. Environ. 2017, 202, 18–27. [CrossRef]
32. Zheng, S.; Cao, C.; Wang, M.; Xu, M.; Lu, S. Land surface temperature retrieval using HJ-1B/IRS data
and analysis of its eﬀect. In Proceedings of the 2013 IEEE International Geoscience and Remote Sensing
Symposium - IGARSS, Melbourne, Australia, 21–26 July 2013; pp. 2285–2288.
Sun, L.; Yu, H.; Gao, T.; Tian, X.; Li, X.; Sun, L. Land surface temperature retrieval from HJ-1B IRS
supported by MODIS. In Proceedings of the 2013 Second International Conference on Agro-Geoinformatics
(Agro-Geoinformatics), Fairfax, VA, USA, 12–16 August 2013; pp. 320–324.

33.

34. Hulley, G.; Shivers, S.; Wetherley, E.; Cudd, R. New ECOSTRESS and MODIS Land Surface Temperature Data
Reveal Fine-Scale Heat Vulnerability in Cities: A Case Study for Los Angeles County, California. Remote Sens.
2019, 11, 2136. [CrossRef]

35. Duguay-Tetzlaﬀ, A.; Bento, V.A.; Göttsche, F.M.; Stöckli, R.; Martins, J.P.A.; Trigo, I.; Olesen, F.; Bojanowski, J.S.;
da Camara, C.; Kunz, H. Meteosat land surface temperature climate data record: Achievable accuracy and
potential uncertainties. Remote Sens. 2015, 7, 13139–13156. [CrossRef]

36. Kalnay, E.; Kanamitsu, M.; Kistler, R.; Collins, W.; Deaven, D.; Gandin, L.; Iredell, M.; Saha, S.; White, G.;
Woollen, J.; et al. The NCEP/NCAR 40-Year Reanalysis Project. Bull. Am. Meteorol. Soc. 1996, 77, 437–471.
[CrossRef]

37. Hulley, G.C.; Hook, S.J.; Abbott, E.; Malakar, N.; Islam, T.; Abrams, M. The ASTER Global Emissivity Dataset

(ASTER GED): Mapping Earth’s emissivity at 100 m spatial scale. Geophys. Res. Lett. 2015, 42. [CrossRef]

38. Augustine, J.A.; Hodges, G.B.; Cornwall, C.R.; Michalsky, J.J.; Medina, C.I.; Augustine, J.A.; Hodges, G.B.;
Cornwall, C.R.; Michalsky, J.J.; Medina, C.I. An Update on SURFRAD—The GCOS Surface Radiation Budget
Network for the Continental United States. J. Atmos. Ocean. Technol. 2005, 22, 1460–1472. [CrossRef]

Remote Sens. 2020, 12, 1471

20 of 21

39. Driemel, A.; Augustine, J.; Behrens, K.; Colle, S.; Cox, C.; Cuevas-Agulló, E.; Denn, F.M.; Duprat, T.;
Fukuda, M.; Grobe, H.; et al. Baseline Surface Radiation Network (BSRN): structure and data description
(1992–2017). Earth Syst. Sci. Data 2018, 10, 1491–1501. [CrossRef]

40. Göttsche, F.-M.; Olesen, F.-S.; Trigo, I.F.; Bork-Unkelbach, A.; Martin, M.A. Long term validation of land
surface temperature retrieved from MSG/SEVIRI with continuous in-situ measurements in Africa. Remote Sens.
2016, 8, 410. [CrossRef]

41. Chander, G.; Markham, B.L.; Helder, D.L. Summary of current radiometric calibration coeﬃcients for Landsat

MSS, TM, ETM+, and EO-1 ALI sensors. Remote Sens. Environ. 2009, 113, 893–903. [CrossRef]

42. USGS. Landsat Collection 1 Level 1 Product Deﬁnition, LSDS-1656 version 2.0; USGS: Sioux Falls, South

Dakota, 2019.

43. USGS. Landsat 7 (L7) Data Users Handbook, LSDS-1927 version 2.0; USGS: Sioux Falls, South Dakota, 2019.
44. Vermote, E.; Justice, C.; Claverie, M.; Franch, B. Preliminary analysis of the performance of the Landsat 8/OLI

land surface reﬂectance product. Remote Sens. Environ. 2016, 185, 46–56. [CrossRef]

45. Hulley, G.C.; Hook, S.J.; Baldridge, A.M. Validation of the North American ASTER Land Surface Emissivity
Database (NAALSED) version 2.0 using pseudo-invariant sand dune sites. Remote Sens. Environ. 2009, 113,
2224–2233. [CrossRef]

46. Carlson, T.N.; Ripley, D.A. On the relation between NDVI, fractional vegetation cover, and leaf area index.

Remote Sens. Environ. 1997, 62, 241–252. [CrossRef]

47. Ren, H.; Liu, R.; Qin, Q.; Fan, W.; Yu, L.; Du, C. Mapping ﬁner-resolution land surface emissivity using

Landsat images in China. J. Geophys. Res. Atmos. 2017, 122, 6764–6781. [CrossRef]

48. Prihodko, L.; Goward, S.N. Estimation of air temperature from remotely sensed surface observations.

Remote Sens. Environ. 1997, 60, 335–346. [CrossRef]

49. Tang, R.; Li, Z.-L.; Tang, B. An application of the Ts–VI triangle method with enhanced edges determination
for evapotranspiration estimation from MODIS data in arid and semi-arid regions: Implementation and
validation. Remote Sens. Environ. 2010, 114, 540–551. [CrossRef]
Jiménez-Muñoz, J.; Sobrino, J.; Plaza, A.; Guanter, L.; Moreno, J.; Martinez, P. Comparison Between
Fractional Vegetation Cover Retrievals from Vegetation Indices and Spectral Mixture Analysis: Case Study
of PROBA/CHRIS Data Over an Agricultural Area. Sensors 2009, 9, 768–793. [CrossRef]

50.

51. Rubio, E.; Caselles, V.; Badenas, C. Emissivity measurements of several soils and vegetation types in the

8–14, µm Wave band: Analysis of two ﬁeld methods. Remote Sens. Environ. 1997, 59, 490–521. [CrossRef]

52. Caselles, V.; Valor, E.; Coll, C.; Rubio, E. Thermal band selection for the PRISM instrument: 1. Analysis of

emissivity-temperature separation algorithms. J. Geophys. Res. Atmos. 1997, 102, 11145–11164. [CrossRef]

53. Peres, L.F.; DaCamara, C.C. Emissivity maps to retrieve land-surface temperature from MSG/SEVIRI.

54.

55.

IEEE Trans. Geosci. Remote Sens. 2005, 43, 1834–1844. [CrossRef]
Sun, D.; Pinker, R.T.; Basara, J.B.; Sun, D.; Pinker, R.T.; Basara, J.B. Land Surface Temperature Estimation from
the Next Generation of Geostationary Operational Environmental Satellites: GOES M–Q. J. Appl. Meteorol.
2004, 43, 363–372. [CrossRef]
Freitas, S.C.; Trigo, I.F.; Macedo, J.; Barroso, C.; Silva, R.; Perdigão, R.; Freitas, S.C.; Trigo, I.F.; Macedo, J.;
Barroso, C.; et al. Land surface temperature from multiple geostationary satellites. Int. J. Remote Sens. 2013,
1161, 3051–3068. [CrossRef]

56. Li, Z.-L.; Tang, B.-H.; Wu, H.; Ren, H.; Yan, G.; Wan, Z.; Trigo, I.F.; Sobrino, J. a Satellite-derived land surface

temperature: Current status and perspectives. Remote Sens. Environ. 2013, 131, 14–37. [CrossRef]

57. Martins, J.; Trigo, I.; Bento, V.; da Camara, C. A Physically Constrained Calibration Database for Land Surface

58.

Temperature Using Infrared Retrieval Algorithms. Remote Sens. 2016, 8, 808. [CrossRef]
Saunders, R.; Hocking, J.; Turner, E.; Rayer, P.; Rundle, D.; Brunel, P.; Vidot, J.; Roquet, P.; Matricardi, M.;
Geer, A.; et al. An update on the RTTOV fast radiative transfer model (currently at version 12). Geosci. Model
Dev. 2018, 11, 2717–2737. [CrossRef]

59. Guillevic, P.C.; Biard, J.C.; Hulley, G.C.; Privette, J.L.; Hook, S.J.; Olioso, A.; Göttsche, F.M.; Radocinski, R.;
Román, M.O.; Yu, Y.; et al. Validation of Land Surface Temperature products derived from the Visible
Infrared Imaging Radiometer Suite (VIIRS) using ground-based and heritage satellite measurements. Remote
Sens. Environ. 2014, 154, 19–37. [CrossRef]

60. Li, S.; Yu, Y.; Sun, D.; Tarpley, D.; Zhan, X.; Chiu, L. Evaluation of 10 year AQUA/MODIS land surface

temperature with SURFRAD observations. Int. J. Remote Sens. 2014, 35, 830–856. [CrossRef]

Remote Sens. 2020, 12, 1471

21 of 21

61. Liu, Y.; Yu, Y.; Yu, P.; Göttsche, F.; Trigo, I. Quality Assessment of S-NPP VIIRS Land Surface Temperature

Product. Remote Sens. 2015, 7, 12215–12241. [CrossRef]

62. Martin, M.; Ghent, D.; Pires, A.; Göttsche, F.-M.; Cermak, J.; Remedios, J. Comprehensive In Situ Validation
of Five Satellite Land Surface Temperature Data Sets over Multiple Stations and Years. Remote Sens. 2019,
11, 479. [CrossRef]

63. Guillevic, P.C.; Bork-unkelbach, A.; Göttsche, F.M.; Hulley, G.; Gastellu-Etchegorry, J.-P.; Olesen, F.S.;
Privette, J.L. Directional Viewing Eﬀects on Satellite Land Surface Temperature Products Over Sparse
Vegetation Canopies — A Multisensor Analysis. IEEE Geosci. Remote Sens. Lett. 2013, 10, 1–5. [CrossRef]

64. Ermida, S.L.; Trigo, I.F.; Dacamara, C.C.; Göttsche, F.M.; Olesen, F.S.; Hulley, G. Validation of remotely
sensed surface temperature over an oak woodland landscape — The problem of viewing and illumination
geometries. Remote Sens. Environ. 2014, 148, 16–27. [CrossRef]

65. Göttsche, F.-M.; Hulley, G.C. Validation of six satellite-retrieved land surface emissivity products over two

land cover types in a hyper-arid region. Remote Sens. Environ. 2012, 124, 149–158. [CrossRef]

66. Guillevic, P.; Göttsche, F.; Nickeson, J.; Hulley, G.; Ghent, D.; Yu, Y.; Trigo, I.; Hook, S.; Sobrino, J.A.;
Remedios, J.; et al. Land Surface Temperature Product Validation Best Practice Protocol. In Best Practice for
Satellite-Derived Land Product Validation; Version 1.1; Guillevic, P., Göttsche, F., Nickeson, J., Román, M., Eds.;
Land Product Validation Subgrou, 2018; p. 58. Available online: https://lpvs.gsfc.nasa.gov/PDF/CEOS_LST_
PROTOCOL_Feb2018_v1.1.0_light.pdf (accessed on 1 April 2020).
Speetzen, H.; Bartsch, R. Introducing new Crops and Crop Rotations in the Lower Monde Valley Irrigation
Project, Portugal. Der Tropenlandwirt-Journal Agric. Trop. Subtrop. 1988, 89, 33–43.

67.

68. Davies, L.; Gather, U. The Identiﬁcation of Multiple Outliers. J. Am. Stat. Assoc. 1993, 88, 782–792. [CrossRef]
69. Duan, S.-B.; Li, Z.-L.; Li, H.; Göttsche, F.-M.; Wu, H.; Zhao, W.; Leng, P.; Zhang, X.; Coll, C. Validation of
Collection 6 MODIS land surface temperature product using in situ measurements. Remote Sens. Environ.
2019, 225, 16–29. [CrossRef]

70. Barsi, J.; Schott, J.; Hook, S.; Raqueno, N.; Markham, B.; Radocinski, R. Landsat-8 Thermal Infrared Sensor

(TIRS) Vicarious Radiometric Calibration. Remote Sens. 2014, 6, 11607–11626. [CrossRef]

71. Liu, Y.; Yu, Y.; Yu, P.; Wang, H. Ground validation and uncertainty esitmation of VIIRS land surface
In Proceedings of the 2016 IEEE International Geoscience and Remote Sensing

temperature product.
Symposium (IGARSS), Beijing, China, 10–15 July 2016; pp. 6922–6925.

72. Martins, J.P.; Trigo, I.F.; Freitas, S.C. Copernicus Global Land Operations—Scientiﬁc Quality Evaluation of Land
Surface Temperature, version 1.2, issue 1.00 (CGLOPS1_SQE2018_LST); Copernicus European Union: KS,
USA, 2019.

73. Yu, Y.; Tarpley, D.; Privette, J.L.; Flynn, L.E.; Xu, H.; Chen, M.; Vinnikov, K.Y.; Sun, D.; Tian, Y. Validation
of GOES-R Satellite Land Surface Temperature Algorithm Using SURFRAD Ground Measurements and
Statistical Estimates of Error Properties. IEEE Trans. Geosci. Remote Sens. 2012, 50, 704–713. [CrossRef]

© 2020 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access
article distributed under the terms and conditions of the Creative Commons Attribution
(CC BY) license (http://creativecommons.org/licenses/by/4.0/).

