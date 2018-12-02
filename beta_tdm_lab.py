#--input--
K = 12
#--consts--
pi = 3.1415
density_water = 1000
g = 9.81
R = 8.31
N_av = 6.022e23
L = 0.5
a = 0.31e-3
d = 7.8e-3
p_atm = 104200
T = 24 + 273
molarmass = 29e-3 #air
n2_molarmass = 28e-3
o2_molarmass = 32e-3
eta = (a**4 *density_water*g*K) / (2*L*d**2)
print('eta:', eta)
d_eff = ((4*molarmass*R*T)/(9*pi**3 * N_av**2 * eta**2))**(1/4)
print('diam: ', d_eff)
lambd = 1.9 * eta * 5 / 2 * R / molarmass
print('lambda: ', lambd)
density = p_atm * molarmass /(R*T)
print('density: ', density)
print('D: ', eta/density)



