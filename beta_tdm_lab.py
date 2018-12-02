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
#--true--
t_eta = 1.72e-5
t_lambd = 24.1e-3
t_d_eff_o2 = 0.36e-9
t_d_eff_n2 = 0.38e-9

def r(number):
    return round(number, 5)

def main():
    density = p_atm * molarmass /(R*T)
    print('density: ', density)

    eta = (a**4 *density_water*g*K) / (2*L*d**2)
    print('eta:', eta)
    print('eta_err',eta - t_eta,'rel_eta_err',
          abs(eta - t_eta)/t_eta)
    print('D: ', eta/density)
    
    lambd = 1.9 * eta * 5 / 2 * R / molarmass
    print('lambda: ', lambd)
    print('lambda_err',lambd - t_lambd,'rel_lambda_err',
          abs(lambd - t_lambd)/t_lambd)

    d_eff = ((4*molarmass*R*T)/(9*pi**3 * N_av**2 * eta**2))**(1/4)
    print('diam: ', d_eff)
    
    d_eff_o2 = ((4*o2_molarmass*R*T)/(9*pi**3 * N_av**2 * eta**2))**(1/4)
    d_eff_n2 = ((4*n2_molarmass*R*T)/(9*pi**3 * N_av**2 * eta**2))**(1/4)
    print('diam_o2: ',d_eff_o2,'diam_n2:',d_eff_n2)
    print('diam_o2_error:', (d_eff_o2 - t_d_eff_o2),
          'diam_n2_error:', (d_eff_n2 - t_d_eff_n2))
    print('rel_diam_o2_error:', abs((d_eff_o2 - t_d_eff_o2)/t_d_eff_o2),
          'rel_diam_n2_error:', abs((d_eff_n2 - t_d_eff_n2)/t_d_eff_n2))
main()