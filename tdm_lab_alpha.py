import math
import matplotlib.pylab as plt
import numpy as np

p_atm = 104200
p_atm_error = 50
T = 24
T_error = 0.5
R = 8.31

def r(number):
    return round(number,5)

def table_processing(values):
    water_density = 1000
    g = 9.81
    pi = 3.1415
    diam = 0.0078 #m
    
    const_values = [x*20 for x in range(16)]
    dp_data = []
    dv_data = []
    column = []
    difference = []

    for j in range(16):  
        print(j+1, ' column:')
        d = values[j] - const_values[j]
        print('diff =', d)
        
        dp = water_density * g * d * 0.001
        dp_data.append(dp)
        print('dp =', r(dp))
        
        dv = values[j] * 0.001 * pi * diam**2 / 4 * 10**6 #in m3 * 10**-6
        dv_data.append(dv)
        print('dv =', r(dv))  
    return dp_data, dv_data

def coefficient(dp, dv):
    print(':::')
    mean_dp = 0
    mean_dv = 0
    
    for i in range(16):
        mean_dp += dp[i]
        mean_dv += dv[i]   
    
    mean_dp /= 16
    mean_dv /= 16
        
    up_sum = 0
    down_sum = 0
    
    for j in range(16):
        up_sum += (dv[j]-mean_dv)*(dp[j]-mean_dp)
        down_sum += (dv[i]-mean_dv)**2

    b = up_sum / down_sum
    a = mean_dp - b * mean_dv
    print('b =', r(b), '::: a =', r(a))

    d_sum = 0
    for k in range(16):
        d_sum += (dp[k] - (a + b * dv[k]))**2
    disp_b = math.sqrt((1 / down_sum) * (d_sum/ 14))
    disp_a = math.sqrt((1/16 + (mean_dv**2)/down_sum) * (d_sum) / 14)
    #print('disp_b =', r(disp_b),'::: disp_a =', r(disp_a))

    error_b = disp_b * 2
    error_a = disp_a * 2
    print('error_b =', r(error_b),'::: error_a =', r(error_a))

    rel_error_b = -error_b / b * 100
    rel_error_a = -error_a / a * 100
    print('rel_b =', r(rel_error_b),'::: rel_a =', r(rel_error_a), '(in %)')
    
    return b, rel_error_b

def rel_p_atm():
    return p_atm_error / p_atm * 100

def volume_zero(ob, rel_error_b):
    print(':::')
    ob *= 10**(6) #standard

    rel_v_zero = math.sqrt(rel_p_atm()**2 + rel_error_b)
    v_zero = -p_atm/ob
    v_zero_error = rel_v_zero * v_zero / 100
    
    print('V0 =', r(-p_atm/ob), '::: V0_error =', r(v_zero_error), '::: rel_V0 =', r(rel_v_zero))   
    
def nu(ob, rel_error_b):
    ob *= 10**(6) #standard
    
    rel_T_error = T_error / T * 100
    nu = p_atm**2/(R*(T+273.15)*ob)*(-1)
    rel_nu_error = math.sqrt((2*rel_p_atm())**2 + rel_T_error**2 + rel_error_b**2)
    nu_error = nu * rel_nu_error / 100
     
    print('nu =', r(nu), '::: nu_error =', r(nu_error), '::: rel_nu =', r(rel_nu_error))

def make_a_plot(dv_values, dp_values):
    #x = np.array(dv_values)
    #f = -116*x - 458
    plt.axis([0,dv_values[-1],dp_values[-1],dp_values[0]])
    plt.plot(dv_values, dp_values)
    plt.plot(dv_values, dp_values, 'ro') #'ro'
    #plt.plot(x, f)
    plt.xlabel('V, m^3 *e-6')
    plt.ylabel('p, Pa')
    plt.show()

values = [4,13,22,29,38,45,54,62,70,79,86,95,102,110,119,126]
dp_data, dv_data = table_processing(values)
b, rel_error_b = coefficient(dp_data, dv_data)
volume_zero(b, rel_error_b)
nu(b, rel_error_b)
make_a_plot(dv_data, dp_data)
