import math

class equasion:
    def __init__(self, x=None , y=None, z=None, a=None):
        self.x = x
        self.y = y
        self.z = z
        self.a = a

    def definition(self):
        return self.x, self.y, self.z, self.a
    
    def show(self):
        print(self.x, 'x +', self.y, 'y +', self.z, 'z =',self.a, sep='')

class dot:
    def __init__(self, x=None , y=None, z=None): #empty
        self.x = x
        self.y = y
        self.z = z

    def show(self):
        return print('(',round(self.x,4), ',', round(self.y,4), ',', round(self.z,4), ')', sep = '')

    def definition(self):
        return self.x, self.y, self.z

    '''def mltpV (self, cf): #wrong
        self.x *= cf
        self.y *= cf
        self.z *= cf'''
        
    def length(self):
        return math.sqrt((self.x) **2 + (self.y) **2 + (self.z)**2)   

    def target(self, alpha, beta):
        eq = alpha.length() / beta.length()
        a, b, c = alpha.definition()
        i, j, k = beta.definition()
        self.x = (a + eq * i) / (1 + eq)
        self.y = (b + eq * j) / (1 + eq)
        self.z = (c + eq * k) / (1 + eq)

class var():

    def __init__(self, name, neg, num):
        self.name = name
        self.sign = neg
        self.num = num
    
    def eject(self):
        if self.sign == '-':
            return self.num * (-1)
        else:
            return self.num
        
    def ejectName(self):
        return self.name
    
    def show(self):
        return print(self.name, self.sign, self.num) 
    
    def mltp(self, cf):
        self.name = str(cf) + self.name  
        self.num *= cf
        if cf < 0 and self.num < 0:
            self.num *= (-1)
            self.sign = '+'
    
def methodK(aleph, bet, gimel):
    a1, a2, a3, a4 = aleph.definition()
    b1, b2, b3, b4 = bet.definition()
    g1, g2, g3, g4 = gimel.definition()
    d1 = dot(a1,a2,a3)
    d2 = dot(b1,b2,b3)
    d3 = dot(g1,g2,g3)
    dbase = mixMltp(d1,d2,d3)
    x1 = dot(a4,a2,a3)
    x2 = dot(b4,b2,b3)
    x3 = dot(g4,g2,g3)
    xbase = mixMltp(x1,x2,x3)
    y1 = dot(a1,a4,a3)
    y2 = dot(b1,b4,b3)
    y3 = dot(g1,g4,g3)
    ybase = mixMltp(y1,y2,y3)
    z1 = dot(a1,a2,a4)
    z2 = dot(b1,b2,b4)
    z3 = dot(g1,g2,g4)
    zbase = mixMltp(z1,z2,z3)
    print('d =',dbase, 'dx=',xbase,'dy =', ybase,'dz =', zbase)
    print('x:', xbase/dbase, ', y:', ybase/dbase, ', z:', zbase/dbase)
    
def vector(alpha, beta): 
    a, b, c = alpha.definition()
    i, j, k = beta.definition()
    out = dot(i-a, j-b, k-c)
    return out

def sumV (alpha,beta):
    a, b, c = alpha.definition()
    i, j, k = beta.definition()
    out = dot(a+i, b+j, c+k)
    return out

def mltpV (alpha, cf):
    a, b, c = alpha.definition()
    temp = dot(a*cf, b*cf, c*cf)
    return temp

def mixMltp(alpha, beta, gamma):    
    a, b, c = alpha.definition()
    i, j, k = beta.definition()
    e, f, g = gamma.definition()
    x = (j * g - f * k) * a
    y = (-1)*(i * g - e * k) * b
    z = (i * f - j * e) * c
    return x+y+z

def inverse(alpha):
    a, b, c = alpha.definition()
    temp = dot(-a,-b,-c)
    return temp

def cosine(alpha, beta): #requires a fraction object
    a, b, c = alpha.definition()
    i, j, k = beta.definition()
    return (a * i + b * j + c * k) / (alpha.length() * beta.length())

def ort(alpha):
    a, b, c = alpha.definition()
    l = alpha.length()
    temp = dot(a/l, b/l, c/l)
    return temp

def vecMltp(alpha, beta):   
    a, b, c = alpha.definition()
    i, j, k = beta.definition()
    x = b * k - j * c
    y = (-1)*(a * k - c * i)
    z = a * j - b * i
    temp = dot(x,y,z)
    return temp

def scMltp (alpha, beta):
    a, b, c = alpha.definition()
    i, j, k = beta.definition()
    return a * i + b * j + c * k
def planeByDots(a, b, c):
    cfa =  (((b[1] - a[1]) * (c[2] - a[2])) - ((c[1] - a[1]) * (b[2] - a[2])))
    cfb =  -(((b[0] - a[0]) * (c[2] - a[2])) - ((c[0] - a[0]) * (b[2] - a[2]))) #incl cf_1_2
    cfc =  (((b[0] - a[0]) * (c[1] - a[1])) - ((c[0] - a[0]) * (b[1] - a[1])))
    mltps = [cfa,cfb,cfc]


    cf1 = var('x','-',a[0])
    cf2 = var('y','-',a[1])
    cf3 = var('z','-',a[2])
    cortege = [cf1,cf2,cf3]

    arch = []
    isum = 0
    i = 0
    j = 0

    for item in cortege:
        item.mltp(mltps[i])
        isum += item.eject()
        temp = item.ejectName()
        arch.append(temp)
        i+=1    
    print('plane equasion: ', end='')
    for j in range(len(arch)):
        print (arch[j], end=' ')
        if j == 2:
            if isum > 0:
                print('+', end='')
          
            print(isum, '= 0')

def main():
    #--- Kramer ---
    a = equasion(2, 1, -2, 5)
    b = equasion(1, 2, -4, 7)
    c = equasion(4, -1, 3, -1)
    methodK(a,b,c)
    #--- cosine ---
    a = dot(3, 2, -4)
    b = dot(4, 4, -2)
    c = sumV(a,b)
    d = sumV(b, inverse(a))
    cos = cosine(c,d)
    if cos < 0:
        cos *= -1
    print(cos)
    #--- eq ---
    a = dot(3, -2, 6)
    b = dot(-1, 8, 7)
    c = dot(3, -1, 6)
    aort = ort(a)
    aort.show()
    mltp_a = mltpV(a, 3)
    mltp_c = mltpV(c, -5)
    a_c = sumV(mltp_a, mltp_c)
    a_c_aort = vecMltp(a_c, aort)
    inv_c = inverse(c)
    pre_ans = sumV(a_c_aort, inv_c)
    ans = scMltp(pre_ans, b)
    print(ans)
    #--- triangle ---
    a = dot(1,3,1)
    b = dot(-1,2,1)
    c = dot(-3,-3,1)
    ab = vector(a, b)
    ac = vector(a, c)
    print(vecMltp(ab, ac).length() /2)
    #--- tetrahedron ---
    a = dot(3, -1, -1)
    b = dot(-3, 3, 2)
    c = dot(-3, -3, 4)
    d = dot(1, -1, 2)
    ab = vector(a,b)
    ac = vector(a,c)
    ad = vector(a,d)
    volume = mixMltp(ab,ac,ad) / 6
    square = vecMltp(ab,ac).length() / 2
    print(3 * volume / square)
    #---parametric lines---
    a = dot(2,2,1)
    b = dot(2,-1,2)
    cos = cosine(a,b)
    if cos < 0:
        cos *= -1
    print(cos)
    #---plane by dots---
    a = [4,-4,1]
    b = [6,4,2]
    c = [6,1,2]
    planeByDots(a,b,c)     
    
main() #come what may
