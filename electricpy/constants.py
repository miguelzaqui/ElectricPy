################################################################################
"""
`electricpy.constants` - Electrical Engineering Constants.

Defenition of all required constants and matricies for
*electricpy* module.
"""
################################################################################

# Import Supporting Dependencies
import numpy as _np
import cmath as _c

# Define Electrical Engineering Constants
pi = _np.pi #: PI Constant 3.14159...
a = _c.rect(1,_np.radians(120)) #: 'A' Operator for Symmetrical Components
p = 1e-12 #: Pico Multiple      (10^-12)
n = 1e-9 #: Nano Multiple       (10^-9)
u = 1e-6 #: Micro (mu) Multiple (10^-6)
m = 1e-3 #: Mili Multiple       (10^-3)
k = 1e+3 #: Kili Multiple       (10^3)
M = 1e+6 #: Mega Multiple       (10^6)
G = 1e+9 #: Giga Multiple       (10^9)
u0 = 4*_np.pi*10**(-7) #: µ0 (mu-not)       4πE-7
e0 = 8.8541878128e-12  #: ε0 (epsilon-not)  8.854E-12
carson_r = 9.869e-7 #: Carson's Ristance Constant  8.869E-7
De0 = 2160 #: De Constant for Use with Transmission Impedance Calculations      2160
NAN = float('nan')
VLLcVLN = _c.rect(_np.sqrt(3),_np.radians(30)) # Conversion Operator
ILcIP = _c.rect(_np.sqrt(3),_np.radians(30)) # Conversion Operator
WATTS_PER_HP = 745.699872
KWH_PER_BTU = 3412.14

# Define Symmetrical Component Matricies
Aabc = 1/3 * _np.array([[ 1, 1, 1    ],  # Convert ABC to 012
                       [ 1, a, a**2 ],  # (i.e. phase to sequence)
                       [ 1, a**2, a ]])
A012 = _np.array([[ 1, 1, 1    ],        # Convert 012 to ABC
                 [ 1, a**2, a ],        # (i.e. sequence to phase)
                 [ 1, a, a**2 ]])
# Define Clarke Component Matricies
Cabc = _np.sqrt(2/3) * _np.array([[ 1, -1/2, -1/2],         # Convert ABC to alpha/beta/gamma
                                  [ 0, _np.sqrt(3)/2, -_np.sqrt(3)/2],
                                  [ 1/_np.sqrt(2), 1/_np.sqrt(2), 1/_np.sqrt(2)]])
Cxyz = _np.array([[ 2/_np.sqrt(6), 0, 1/_np.sqrt(3)],       # Convert alpha/beta/gamma to ABC
                  [ -1/_np.sqrt(6), 1/_np.sqrt(2), 1/_np.sqrt(3)],
                  [ -1/_np.sqrt(6), -1/_np.sqrt(2), 1/_np.sqrt(3)]])
# Define Park Components Matricies
_rad = lambda th: _np.radians( th )
Pdq0_im = lambda th: _np.sqrt(2/3)*_np.array([[ _np.cos(_rad(th)), _np.cos(_rad(th)-2*pi/3), _np.cos(_rad(th)+2*pi/3)],
                                           [-_np.sin(_rad(th)),-_np.sin(_rad(th)-2*pi/3),-_np.sin(_rad(th)+2*pi/3)],
                                           [ _np.sqrt(2)/2,     _np.sqrt(2)/2,            _np.sqrt(2)/2]])
Pabc_im = lambda th: _np.sqrt(2/3)*_np.array([[ _np.cos(_rad(th)),      -_np.sin(_rad(th)),        _np.sqrt(2)/2],
                                           [_np.cos(_rad(th)-2*pi/3),-_np.sin(_rad(th)-2*pi/3), _np.sqrt(2)/2],
                                           [_np.cos(_rad(th)+2*pi/3),-_np.sin(_rad(th)+2*pi/3), _np.sqrt(2)/2]])
Pdq0 = 2/3 * _np.array([[0,-_np.sqrt(3/2),_np.sqrt(3/2)],
                        [1,-1/2,-1/2],
                        [1/2, 1/2, 1/2]])
Pqd0 = 2/3 * _np.array([[1,-1/2,-1/2],
                        [0,-_np.sqrt(3/2),_np.sqrt(3/2)],
                        [1/2, 1/2, 1/2]])
                 
# Define Transformer Shift Correction Matricies
XFMY0 = _np.array([[1,0,0],[0,1,0],[0,0,1]])
XFMD1 = 1/_np.sqrt(3) * _np.array([[1,-1,0],[0,1,-1],[-1,0,1]])
XFMD11 = 1/_np.sqrt(3) * _np.array([[1,0,-1],[-1,1,0],[0,-1,1]])
XFM12 = 1/3 * _np.array([[2,-1,-1],[-1,2,-1],[-1,-1,2]])

# Define Complex Angle Terms
e30 = _c.rect(1,_np.radians(30)) #: 30° Phase Operator
en30 = _c.rect(1,_np.radians(-30)) #: -30° Phase Operator
e60 = _c.rect(1,_np.radians(60)) #: 60° Phase Operator
en60 = _c.rect(1,_np.radians(-60)) #: -60° Phase Operator
e90 = _c.rect(1,_np.radians(90)) #: 90° Phase Operator
en90 = _c.rect(1,_np.radians(-90)) #: -90° Phase Operator
e45 = _c.rect(1,_np.radians(45)) #: 45° Phase Operator
en45 = _c.rect(1,_np.radians(-45)) #: -45° Phase Operator

# Define Material Resistivity (Rho)
resistivity_rho = {
    'silver':       15.9,
    'copper':       16.8,
    'aluminium':    6.5,
    'tungsten':     56,
    'iron':         97.1,
    'platinum':     106,
    'manganin':     482,
    'lead':         220,
    'mercury':      980,
    'nichrome':     1000,
    'constantan':   490,
}
THERMO_COUPLE_DATA = {
    "J": [
        [-6.4936529E+01, 2.5066947E+02, 6.4950262E+02, 9.2510550E+02, 1.0511294E+03],
        [-3.1169773E+00, 1.3592329E+01, 3.6040848E+01, 5.3433832E+01, 6.0956091E+01],
        [2.2133797E+01, 1.8014787E+01, 1.6593395E+01, 1.6243326E+01, 1.7156001E+01],
        [2.0476437E+00, -6.5218881E-02, 7.3009590E-01, 9.2793267E-01, -2.5931041E+00],
        [-4.6867532E-01, -1.2179108E-02, 2.4157343E-02, 6.4644193E-03, -5.8339803E-02],
        [-3.6673992E-02, 2.0061707E-04, 1.2787077E-03, 2.0464414E-03, 1.9954137E-02],
        [1.1746348E-01, -3.9494552E-03, 4.9172861E-02, 5.2541788E-02, -1.5305581E-01],
        [-2.0903413E-02, -7.3728206E-04, 1.6813810E-03, 1.3682959E-04, -2.9523967E-03],
        [-2.1823704E-03, 1.6679731E-05, 7.6067922E-05, 1.3454746E-04, 1.1340164E-03]
    ],
    "K": [
        [-1.2147164E+02, -8.7935962E+00, 3.1018976E+02, 6.0572562E+02, 1.0184705E+03],
        [-4.1790858E+00, -3.4489914E-01, 1.2631386E+01, 2.5148718E+01, 4.1993851E+01],
        [3.6069513E+01, 2.5678719E+01, 2.4061949E+01, 2.3539401E+01, 2.5783239E+01],
        [3.0722076E+01, -4.9887904E-01, 4.0158622E+00, 4.6547228E-02, -1.8363403E+00],
        [7.7913860E+00, -4.4705222E-01, 2.6853917E-01, 1.3444400E-02, 5.6176662E-02],
        [5.2593991E-01, -4.4869203E-02, -9.7188544E-03, 5.9236853E-04, 1.8532400E-04],
        [9.3939547E-01, 2.3893439E-04, 1.6995872E-01, 8.3445513E-04, -7.4803355E-02],
        [2.7791285E-01, -2.0397750E-02, 1.1413069E-02, 4.6121445E-04, 2.3841860E-03],
        [2.5163349E-02, -1.8424107E-03, -3.9275155E-04, 2.5488122E-05, 0.0]
    ],
    "B": [
        [5.0000000E+02, 1.2461474E+03],
        [1.2417900E+00, 7.2701221E+00],
        [1.9858097E+02, 9.4321033E+01],
        [2.4284248E+01, 7.3899296E+00],
        [-9.7271640E+01, -1.5880987E-01],
        [-1.5701178E+01, 1.2681877E-02],
        [3.1009445E-01, 1.0113834E-01],
        [-5.0880251E-01, -1.6145962E-03],
        [-1.6163342E-01, -4.1086314E-06]],
    "E": [
        [-1.1721668E+02, -5.0000000E+01, 2.5014600E+02, 6.0139890E+02, 8.0435911E+02],
        [-5.9901698E+00, -2.7871777E+00, 1.7191713E+01, 4.5206167E+01, 6.1359178E+01],
        [2.3647275E+01, 1.9022736E+01, 1.3115522E+01,
            1.2399357E+01, 1.2759508E+01],
        [1.2807377E+01, -1.7042725E+00, 1.1780364E+00,
            4.3399963E-01, -1.1116072E+00],
        [2.0665069E+00, -3.5195189E-01, 3.6422433E-02,
            9.1967085E-03, 3.5332536E-02],
        [8.6513472E-02, 4.7766102E-03, 3.9584261E-04,
            1.6901585E-04, 3.3080380E-05],
        [5.8995860E-01, -6.5379760E-02, 9.3112756E-02,
            3.4424680E-02, -8.8196889E-02],
        [1.0960713E-01, -2.1732833E-02, 2.9804232E-03,
            6.9741215E-04, 2.8497415E-03],
        [6.1769588E-03, 0.0, 3.3263032E-05, 1.2946992E-05, 0.0]],
    "N": [
        [-5.9610511E+01, 3.1534505E+02, 1.0340172E+03],
        [-1.5000000E+00, 9.8870997E+00, 3.7565475E+01],
        [4.2021322E+01, 2.7988676E+01, 2.6029492E+01],
        [4.7244037E+00, 1.5417343E+00, -6.0783095E-01],
        [-6.1153213E+00, -1.4689457E-01, -9.7742562E-03],
        [-9.9980337E-01, -6.8322712E-03, -3.3148813E-06],
        [1.6385664E-01, 6.2600036E-02, -2.5351881E-02],
        [-1.4994026E-01, -5.1489572E-03, -3.8746827E-04],
        [-3.0810372E-02, -2.8835863E-04, 1.7088177E-06]
    ],
    "R": [
        [1.3054315E+02, 5.4188181E+02, 1.0382132E+03, 1.5676133E+03],
        [8.8333090E-01, 4.9312886E+00, 1.1014763E+01, 1.8397910E+01],
        [1.2557377E+02, 9.0208190E+01, 7.4669343E+01, 7.1646299E+01],
        [1.3900275E+02, 6.1762254E+00, 3.4090711E+00, -1.0866763E+00],
        [3.3035469E+01, -1.2279323E+00, -1.4511205E-01, -2.0968371E+00],
        [-8.5195924E-01, 1.4873153E-02, 6.3077387E-03, -7.6741168E-01],
        [1.2232896E+00, 8.7670455E-02, 5.6880253E-02, -1.9712341E-02],
        [3.5603023E-01, -1.2906694E-02, -2.0512736E-03, -2.9903595E-02],
        [0.0, 0.0, 0.0, -1.0766878E-02]
    ],
    "S": [
        [1.3792630E+02, 4.7673468E+02, 9.7946589E+02, 1.6010461E+03],
        [9.3395024E-01, 4.0037367E+00, 9.3508283E+00, 1.6789315E+01],
        [1.2761836E+02, 1.0174512E+02, 8.7126730E+01, 8.4315871E+01],
        [1.1089050E+02, -8.9306371E+00, -2.3139202E+00, -1.0185043E+01],
        [1.9898457E+01, -4.2942435E+00, -3.2682118E-02, -4.6283954E+00],
        [9.6152996E-02, 2.0453847E-01, 4.6090022E-03, -1.0158749E+00],
        [9.6545918E-01, -7.1227776E-02, -1.4299790E-02, -1.2877783E-01],
        [2.0813850E-01, -4.4618306E-02, -1.2289882E-03, -5.5802216E-02],
        [0.0, 1.6822887E-03, 0.0, -1.2146518E-02]
    ],
    "T": [
        [-1.9243000E+02, -6.0000000E+01, 1.3500000E+02, 3.0000000E+02],
        [-5.4798963E+00, -2.1528350E+00, 5.9588600E+00, 1.4861780E+01],
        [5.9572141E+01, 3.0449332E+01, 2.0325591E+01, 1.7214707E+01],
        [1.9675733E+00, -1.2946560E+00, 3.3013079E+00, -9.3862713E-01],
        [-7.8176011E+01, -3.0500735E+00, 1.2638462E-01, -7.3509066E-02],
        [-1.0963280E+01, -1.9226856E-01, -8.2883695E-04, 2.9576140E-04],
        [2.7498092E-01, 6.9877863E-03, 1.7595577E-01, -4.8095795E-02],
        [-1.3768944E+00, -1.0596207E-01, 7.9740521E-03, -4.7352054E-03],
        [-4.5209805E-01, -1.0774995E-02, 0.0, 0.0]
    ]
}
THERMO_COUPLE_KEYS = ['To', 'Vo', 'P1', 'P2', 'P3', 'P4', 'Q1', 'Q2', 'Q3']

COLD_JUNCTION_DATA = {
    "To": [4.2000000E+01, 2.5000000E+01, 2.5000000E+01, 2.5000000E+01, 7.0000000E+00, 2.5000000E+01, 2.5000000E+01, 2.5000000E+01],
    "Vo": [3.3933898E-04, 1.4950582E+00, 1.2773432E+00, 1.0003453E+00, 1.8210024E-01, 1.4067016E-01, 1.4269163E-01, 9.9198279E-01],
    "P1": [2.1196684E-04, 6.0958443E-02, 5.1744084E-02, 4.0514854E-02, 2.6228256E-02, 5.9330356E-03, 5.9829057E-03, 4.0716564E-02],
    "P2": [3.3801250E-06, -2.7351789E-04, -5.4138663E-05, -3.8789638E-05, -1.5485539E-04, 2.7736904E-05, 4.5292259E-06, 7.1170297E-04],
    "P3": [-1.4793289E-07, -1.9130146E-05, -2.2895769E-06, -2.8608478E-06, 2.1366031E-06, -1.0819644E-06, -1.3380281E-06, 6.8782631E-07],
    "P4": [-3.3571424E-09, -1.3948840E-08, -7.7947143E-10, -9.5367041E-10, 9.2047105E-10, -2.3098349E-09, -2.3742577E-09, 4.3295061E-11],
    "Q1": [-1.0920410E-02, -5.2382378E-03, -1.5173342E-03, -1.3948675E-03, -6.4070932E-03, 2.6146871E-03, -1.0650446E-03, 1.6458102E-02],
    "Q2": [-4.9782932E-04, -3.0970168E-04, -4.2314514E-05, -6.7976627E-05, 8.2161781E-05, -1.8621487E-04, -2.2042420E-04, 0.0000000E+00]
}
COLD_JUNCTION_KEYS = ["To", "Vo", "P1", "P2", "P3", "P4", "Q1", "Q2"]
# END OF FILE