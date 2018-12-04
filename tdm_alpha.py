#go to line 355
import sys
import math
import numpy as np
import matplotlib.pylab as plt

class process:
    def __init__(self, values_before, values_after, type):

        self.vb = values_before
        self.va = values_after
        if 'pvta'.find(type) != -1:
            self.type = type
        else: 
            print(type, 'is a wrong process')
            sys.exit()

    def getAttribute(self):
        return self.type

    def getValues(self):
        return self.vb, self.va

    def showValues(self):
        print(self.vb)

def definition(act):
    sign = False
    vb, va = act.getValues()

    for counter in range(len(vb)):
        if vb[counter] == None or va[counter] == None:
            sign = True #rationality of execution
    socket = getSocket(act.getAttribute())
    if sign and socket != 3:
        vb[socket], va[socket] = assignment(vb[socket], va[socket])
    return 0

def show(legend): 
    print(legend)
    for i in range(l): #just fixed
        for k in range(len(processes[i][0])):
            temp_elem = processes[i][0][k]
            if temp_elem != None:
                temp_elem = r(temp_elem)
            print(temp_elem, end='   ')
        print('')

def r(num): #round
    r_attr = 4 #default
    if abs(num) > 100:
        r_attr = 1
    return round(num, r_attr)

def getError():
    print('Error. Processes are undefined.')
    sys.exit()
    return 0

def solve(matrix, pos, typeOfProcess): #inverse - type of dependence()
    if typeOfProcess == 2:
        if   pos == [0,0]:
            return matrix[1][0] * matrix[1][1] / matrix[0][1]
        elif pos == [0, 1]:
            return matrix[1][0] * matrix[1][1] / matrix[0][0]
        elif pos == [1,0]:
            return matrix[0][0] * matrix[0][1] / matrix[1][1]
        elif pos == [1,1]:
            return matrix[0][1] * matrix[0][0] / matrix[1][0]
    else:
        if   pos == [0,0]:
            return matrix[0][1] * matrix[1][0] / matrix[1][1]
        elif pos == [0, 1]:
            return matrix[0][0] * matrix[1][1] / matrix[1][0]
        elif pos == [1,0]:
            return matrix[0][0] * matrix[1][1] / matrix[0][1]
        elif pos == [1,1]:
            return matrix[0][1] * matrix[1][0] / matrix[0][0]
    pass

def ad_calculation(matrix, pos, c):
    #solution patterns are non-equal
    if c == 0:
        temp_gamma = gamma
    elif c == 1: 
        temp_gamma = 1/(gamma-1)
    else: 
        temp_gamma = (1-gamma) / gamma
        
    inversed_temp_gamma = 1/temp_gamma
        
    if pos == [0,0]:
        return matrix[1][0] * (matrix[1][1] / matrix[0][1]) ** temp_gamma
    elif pos == [0,1]:
        return matrix[1][1] * (matrix[1][0] / matrix[0][0]) ** inversed_temp_gamma
    elif pos == [1,0]:
        return matrix[0][0] * (matrix[0][1] / matrix[1][1]) ** temp_gamma
    elif pos == [1,1]:
        return matrix[0][1] * (matrix[0][0] / matrix[1][0]) ** inversed_temp_gamma
        
    pass

def assignment(vb, va):
    if va == None or vb == None:
        if vb != None:
            va = vb
        else:
            vb = va
    return vb, va

def getSocket(type):
    if type == 'p':
        return 0
    elif type == 'v':
        return 1
    elif type == 't':
        return 2
    else: #a
        return 3

def scan(matrix):
    pos = [None, None]
    None_counter = 0
    for i in range(len(matrix)):

        for j in range(len(matrix)):
            if matrix[i][j] == None:
                pos = [i, j] 
                None_counter += 1

    return pos, None_counter

def invoke_laws(outcome):

    for main_counter in range(len(outcome)): 
        None_counter = 0

        pr = process(outcome[main_counter][0], outcome[main_counter][1], outcome[main_counter][2])
        typeOfProcess = getSocket(pr.getAttribute()) 
        vb, va = pr.getValues()
    
        if typeOfProcess == 0: #v-const
            matrix = [[vb[1], vb[2]],[va[1],va[2]]]

        elif typeOfProcess == 1: #p-const
            matrix = [[vb[0], vb[2]],[va[0],va[2]]]

        elif typeOfProcess == 2: #t-const
            matrix = [[vb[0], vb[1]],[va[0],va[1]]]

        else: #ad

            for c in range(3):
                interrupt_criteria = 0
                matrix = []
                if c == 2:
                    c_incr = 0
                else:
                    c_incr = c + 1

                matrix = [[vb[c], vb[c_incr]],[va[c],va[c_incr]]]
                pos, interrupt_criteria = scan(matrix)

                if interrupt_criteria == 1:
                    matrix[pos[0]][pos[1]] = ad_calculation(matrix, pos, c)
                    break

            [[vb[c], vb[c_incr]],[va[c],va[c_incr]]] = matrix

        #instructions below are the same for other types of processes
        if typeOfProcess != 3:
            pos, None_counter = scan(matrix)

        if pos != [None,None] and None_counter == 1: #rationality of execution
            matrix[pos[0]][pos[1]] = solve(matrix, pos, typeOfProcess)

        if typeOfProcess == 0: #v=const
            [[vb[1], vb[2]],[va[1],va[2]]] = matrix

        elif typeOfProcess == 1: #p=const
            [[vb[0], vb[2]],[va[0],va[2]]] = matrix

        elif typeOfProcess == 2: #t-const
            [[vb[0], vb[1]],[va[0],va[1]]] = matrix
    return 0

def iterate():
    state_c = 0
    for iter in range(len(states) * 3): #main counter
        temp_act = process(processes[state_c][0], processes[state_c][1], processes[state_c][2])
        definition(temp_act)

        if state_c == (len(processes)-1):
            state_c = 0
        else:
            state_c +=  1
    return 0

def initial_stage():

    error = 0        
    for i in range(l):

        sb = states[i]
        if i == (len(states)-1):
            sa = states[0]
        else: sa = states[i+1]
        processes.append([sb, sa, types[i]])

        if (states[i][0] == None 
            and states[i][1] == None 
            and states[i][2] == None):
            error += 1

    if error == l:
        getError()
        #fix

    iterate()
    return processes

def amount_of_sub(): 
    try:
        nu = processes[0][0][0]*processes[0][0][1]/(processes[0][0][2]*R)
    except:
        print('Error. Not enough data.')
        sys.exit()
    return nu

def getTemperatures():
    temps = []
    for i in range(l):
        temps.append(processes[i][0][2])
    temps.sort()
    return temps[0], temps[-1] #min and max

def Q_calc():
    nu = amount_of_sub() #nu
    Q_sum = 0
    fridgeQ = 0
    heaterQ = 0
    S_sum = 0

    for process_counter in range(l):
        Q = 0 
        U = 0
        A = 0
        S = 0
        process_type = processes[process_counter][2]
    
        if process_type == 'p':
            U = getdU(process_counter)
            A = (processes[process_counter][1][1] - processes[process_counter][0][1]) * processes[process_counter][0][0]
            S = nu * (i+2)/2 * R * math.log(processes[process_counter][1][2] / processes[process_counter][0][2])
        elif process_type == 'v':
            U = getdU(process_counter)
            S = nu * i/2 * R * math.log(processes[process_counter][1][2] / processes[process_counter][0][2])
        elif process_type == 't':
            A = nu * R * processes[process_counter][0][2] * math.log(processes[process_counter][1][1] / processes[process_counter][0][1])
            S = nu * R * math.log(processes[process_counter][1][1] / processes[process_counter][0][1])
        else:
            U = getdU(process_counter)
            A = -U

        Q = U + A
        Q_sum += Q
        if Q > 0:
            heaterQ += Q
        else:
            fridgeQ += Q

        if process_counter == l-1:
            temp_process_counter = 1
        else:
            temp_process_counter = process_counter + 2
        print('Q, U, A, S for p.', process_counter+1, '-', temp_process_counter, ': ', r(Q) , ' ~ ', r(U), ' ~ ', r(A), ' ~ ', r(S), sep='')
    return Q_sum, heaterQ, fridgeQ


def getdU(process_counter):
    try:
        return i / 2 * R * amount_of_sub() * (processes[process_counter][1][2] - processes[process_counter][0][2])
    except:
        getError()

def efficiency(attr1, attr2):
    return (attr2 - attr1) / attr2 * 100

def f_efficiency(attr1, attr2):
    return 100 * attr1 / (attr2 - attr1)

def compare(bf, af):
    if data[bf][1] > data[af][1]:
        return data[af][1], data[bf][1]
    else:
        return data[bf][1], data[af][1]

def determiner(beforestate, afterstate):

    t = types[beforestate]
    temp_min_arg, temp_max_arg = compare(beforestate, afterstate)

    if t == 'p':
        arg = np.linspace(temp_min_arg, temp_max_arg, 32)
        func = np.array([data[beforestate][0] for generate in range(len(arg))])
        clr = 'm'
    #excl for type-v
    elif t == 't':
        arg = np.linspace(temp_min_arg, temp_max_arg, 32)
        func = data[afterstate][0] * data[afterstate][1] / arg
        clr = 'r'
    elif t == 'a': #ad
        const_ad = data[afterstate][0] * data[afterstate][1]**gamma
        arg = np.linspace(temp_min_arg, temp_max_arg, 32)
        func = const_ad/arg**gamma
        clr = 'c'

    return arg, func, clr

def make_a_plot(data_plot):  
    afterstate = 0

    for beforestate in range(l):
        if beforestate == l-1:
            afterstate = 0
        else:
            afterstate = beforestate + 1
        
        if types[beforestate] != 'v':
            x, y, key = determiner(beforestate, afterstate)
            plt.plot(x, y, key)
        else:
            plt.axvline(x=data[beforestate][1],color ='g') #borders!

    plt.show()
    return 0
#fuck the types
def main(): 

    for surety_counter in range(3*l):
        invoke_laws(outcome)
        iterate()
     
    show('p-V-T:')
    sumQ, hQ, fQ = Q_calc()
    minT, maxT = getTemperatures()
    print('Min and max T''s:', minT, '~', maxT)
    print('Q_sum = A_sum:', r(sumQ), ' U_sum = S_sum: 0')
    print('Q+:', r(hQ), 'Q-:', r(fQ), 'Efficiency: ', r(efficiency(abs(fQ), hQ)), '%')
    print('Efficiency for Karno_c:', r(efficiency(minT, maxT)), '%')
    print('Refr. Efficiency: ', r(f_efficiency(abs(fQ), hQ)), '%')

    return states

# --input-zone begins--
# number of processes = 3 or 4
# the values must be given in Pa, m3, K
# if the value is undefined => type 'None'
# if you got error => your data is wrong
number_of_processes = 4
s1 = [None,None,None]
s2 = [None,None,None]
s3 = [None,None,None]
s4 = [None,None,None]
types = 'pavt'
i = 5 
# --input-zone ends--

states = [s1,s2,s3]
if number_of_processes == 4:
    states.append(s4)
gamma = (i+2) / i
R = 8.31
l = len(states)
if len(types) != l:
    getError()
processes = []
outcome = initial_stage()
data = np.array(main())
make_a_plot(data)