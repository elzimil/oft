import math

def approx(xdata, ydata):
    y_mean = 0
    x_mean = 0
    
    if len(xdata) == len(ydata):
        n = len(xdata)
    else:
        sys.exit()

    for i in range(n):
        y_mean += ydata[i]
        x_mean += xdata[i]   
    
    y_mean /= n
    x_mean /= n
    up_sum = 0
    down_sum = 0
    
    for j in range(n):
        up_sum += (xdata[j]-x_mean)*(ydata[j]-y_mean)
        down_sum += (xdata[j]-x_mean)**2

    b = up_sum / down_sum
    a = y_mean - b * x_mean
    print('b =', b, '::: a =', a)

    d_sum = 0
    for k in range(n):
        d_sum += (ydata[k] - (a + b * xdata[k]))**2
    disp_b = math.sqrt((1 / down_sum) * (d_sum/ (n-2)))
    disp_a = math.sqrt((1/n + (x_mean**2)/down_sum) * (d_sum) / (n-2))
    print('disp_b =', disp_b, '::: disp_a =', disp_a)

    error_b = disp_b * 2
    error_a = disp_a * 2
    print('error_b =', error_b,'::: error_a =', error_a)

    rel_error_b = abs(error_b / b) * 100
    rel_error_a = abs(error_a / a) * 100
    print('rel_b =', rel_error_b,'::: rel_a =', rel_error_a, '(in %)')
   
    return b, a
#input data:
xs = [0.19112885999999998, 0.6211687950000001, 1.05120873, 1.385684235, 1.8157241699999997, 2.150199675, 2.5802396099999996, 2.9624973299999997, 3.3447550500000003, 3.7747949849999998, 4.10927049, 4.539310425, 4.87378593, 5.25604365, 5.686083585, 6.02055909]
ys = [39.24, -68.67, -176.58, -304.11, -412.02, -539.55, -647.46, -765.1800000000001, -882.9, -990.8100000000001, -1118.34, -1226.25, -1353.78, -1471.5, -1579.41, -1706.94] 
approx(xs, ys)