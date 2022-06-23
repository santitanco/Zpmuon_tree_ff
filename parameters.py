# This file was automatically created by FeynRules 2.3.36
# Mathematica version: 12.1.1 for Linux x86 (64-bit) (June 19, 2020)
# Date: Fri 30 Oct 2020 00:13:56



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])




### SM

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MCh = Parameter(name = 'MCh',
                nature = 'external',
                type = 'real',
                value = 50.,
                texname = '\\text{MCh}',
                lhablock = 'MASS',
                lhacode = [ 101 ])

MZpmu = Parameter(name = 'MZpmu',
                  nature = 'external',
                  type = 'real',
                  value = 200,
                  texname = '\\text{MZpmu}',
                  lhablock = 'MASS',
                  lhacode = [ 102 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WZpmu = Parameter(name = 'WZpmu',
                  nature = 'external',
                  type = 'real',
                  value = 0.0005,
                  texname = '\\text{WZpmu}',
                  lhablock = 'DECAY',
                  lhacode = [ 102 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

gZ = Parameter(name = 'gZ',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(g1**2+gw**2)',
                texname = 'g_Z')

### External BSM coupling and charges

gp = Parameter(name = 'gp',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = "g\'",
                 lhablock = 'FRBlock',
                 lhacode = [ 1 ])

qmu = Parameter(name = 'qmu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'Q_{\\mu}',
                 lhablock = 'FRBlock',
                 lhacode = [ 2 ])

qchi = Parameter(name = 'qchi',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'Q_{\\chi}',
                 lhablock = 'FRBlock',
                 lhacode = [ 3 ])                

### Fermion couplings to Z'

gmu = Parameter(name = 'gmu',
                nature = 'internal',
                type = 'real',
                value = 'gp*qmu',
                texname = 'g_{\\mu }')

gchi = Parameter(name = 'gchi',
                 nature = 'internal',
                 type = 'real',
                 value = 'gp*qchi',
                 texname = 'g_{\\chi }')

### Anomalous coefficients 

tZpZZmu = Parameter(name = 'tZpZZmu',
                 nature = 'internal',
                 type = 'real',
                 value = '(2.*(-1./2. + 2.*sw2)**2+1./2.)*qmu',    # eq. (48) paper
                 texname = 't^{Z\'ZZ}_{\\mu }')

tZpZZnumu = Parameter(name = 'tZpZZnumu',
                 nature = 'internal',
                 type = 'real',
                 value = 'qmu',                             # eq. (49) paper
                 texname = 't^{Z\'ZZ}_{\\nu_{\\mu} }')              

# Muon loop integrals in the on-shell case

I3ZZmu = Parameter(name = 'I3ZZmu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'I_{3,\\mu}^{ZZ}',
                 lhablock = 'FRBlock',
                 lhacode = [ 4 ])

I6ZZmu = Parameter(name = 'I6ZZmu',
                 nature = 'internal',
                 type = 'real',
                 value = '-I3ZZmu',
                 texname = 'I_{6,\\mu}^{ZZ}')

I5ZZmu = Parameter(name = 'I5ZZmu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'I_{5,\\mu}^{ZZ}',
                 lhablock = 'FRBlock',
                 lhacode = [ 5 ])

I4ZZmu = Parameter(name = 'I4ZZmu',
                 nature = 'internal',
                 type = 'real',
                 value = '-I5ZZmu',
                 texname = 'I_{4,\\mu}^{ZZ}')              

I0ZZmu = Parameter(name = 'I0ZZmu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'I_{0,\\mu}^{ZZ}',
                 lhablock = 'FRBlock',
                 lhacode = [ 6 ])

# Neutrino loop integrals

I3ZZnumu = Parameter(name = 'I3ZZnumu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'I_{3,\\mu}^{ZZ}',
                 lhablock = 'FRBlock',
                 lhacode = [ 7 ])

I6ZZnumu = Parameter(name = 'I6ZZnumu',
                 nature = 'internal',
                 type = 'real',
                 value = '-I3ZZnumu',
                 texname = 'I_{6,\\mu}^{ZZ}')

I5ZZnumu = Parameter(name = 'I5ZZnumu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'I_{5,\\mu}^{ZZ}',
                 lhablock = 'FRBlock',
                 lhacode = [ 8 ])

I4ZZnumu = Parameter(name = 'I4ZZnumu',
                 nature = 'internal',
                 type = 'real',
                 value = '-I5ZZnumu',
                 texname = 'I_{4,\\mu}^{ZZ}')              

I0ZZnumu = Parameter(name = 'I0ZZnumu',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = 'I_{0,\\mu}^{ZZ}',
                 lhablock = 'FRBlock',
                 lhacode = [ 9 ])


# Rosenberg parametrization coefficients (already on-shell)



A3 = Parameter(name = 'A3',
                 nature = 'internal',
                 type = 'real',
                 value = '2*(tZpZZmu*I3ZZmu+tZpZZnumu*I3ZZnumu)',
                 texname = 'A_3')
                
A4 = Parameter(name = 'A4',
                 nature = 'internal',
                 type = 'real',
                 value = '2*(tZpZZmu*I4ZZmu+tZpZZnumu*I4ZZnumu)',
                 texname = 'A_4')

A5 = Parameter(name = 'A5',
                 nature = 'internal',
                 type = 'real',
                 value = '2*(tZpZZmu*I5ZZmu+tZpZZnumu*I5ZZnumu)',
                 texname = 'A_5')

A6 = Parameter(name = 'A6',
                 nature = 'internal',
                 type = 'real',
                 value = '2*(tZpZZmu*I6ZZmu+tZpZZnumu*I6ZZnumu)',
                 texname = 'A_6')                 

A1t = Parameter(name = 'A1t',
                 nature = 'internal',
                 type = 'real',
                 value = 'MZ**2 * A4 + (MZpmu**2-2*MZ**2)/2 * A3 - tZpZZmu*MMU**2*I0ZZmu',
                 texname = '\tilde{A}_1')           

A2t = Parameter(name = 'A2t',
                 nature = 'internal',
                 type = 'real',
                 value = 'MZ**2 * A5 + (MZpmu**2-2*MZ**2)/2 * A6 + tZpZZmu*MMU**2*I0ZZmu',
                 texname = '\tilde{A}_2')