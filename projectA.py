import math

#RAT1 information
C1 = 10
T1 = 6

#RAT2 information
C2 = 20
T2 = 15

bbu1 = 2 #for voice call
bbu2 = 1 #for data call

arrivalN = 1
arrivalH = 0.5

departureN = 0.5
departureH = 0.5

lN = arrivalN/departureN #Network load as a result of new calls
lH = arrivalH/departureH #Network load as a result of handoff calls

admissible = []

States = 0

blocking1 = 0
blocking2 = 0

dropping1 = 0
dropping2 = 0

#investigating the effects of varying C, T and bbu on RAT1 and RAT2
for n11 in range(T1+1): #n1 = new voice call in RAT1
    for n21 in range(T1 + 1): #n21 = new data call in RAT1
        for h11 in range(C1+1): #h11 = handoff voice call in RAT1
            for h21 in range (C1+1): #h21 = handoff data call in RAT1
                for n12 in range(T2+1): #n12 = new voice call in RAT2
                    for n22 in range (T2+1): #n22 = new data call in RAT2
                        for h12 in range(C2+1): #h12 = handoff voice call in RAT2
                            for h22 in range(C2+1): #h22 = handoff data call in RAT2
                                threshold1 = bbu1*(n11) + bbu2*(n21)
                                capacity1 = bbu1*(n11 + h11) + bbu2*(n21 + h21)
                                threshold2 = bbu1*(n12) + bbu2*(n22)
                                capacity2 = bbu1*(n12 + h12) + bbu2*(n22 + h22)
                                if (threshold1 <= T1) and (capacity1 <= C1) and (threshold2 <= T2) and (capacity2 <= C2):
                                    numerators = ((lN**n11)*(lH**h11)*(lN**n21)*(lH**h21)*(lN**n12)*(lH**h12)*(lN**n22)*(lH**h22))
                                    denominators = ((math.factorial(n11))*(math.factorial(h11))*(math.factorial(n21))*(math.factorial(h21))*(math.factorial(n12))*(math.factorial(h12))*(math.factorial(n22))*(math.factorial(h22)))
                                    prob = numerators/denominators
                                    States += prob
                                    if ((bbu1 + bbu2 + threshold1) > T1): #blocking in RAT1
                                        blocking1 += prob
                                    if ((bbu1 + bbu2 + capacity2) > T1) and ((bbu1 + bbu2 + threshold2) > T2): #blocking in RAT2
                                        blocking2 += prob
                                    if ((bbu1 + bbu2 + capacity1) > C1): #dropping in RAT1
                                        dropping1 += prob
                                    if ((bbu1 + bbu2 + capacity1) > C1) and ((bbu1 + bbu2 + capacity2) > C2): #dropping in RAT2
                                        dropping2 += prob
                                #admissible.append([n11,h11,n21,h21,n12,h12,n22,h22])
                                #print("hello")

print("Blocked new calls in RAT1: {}".format(blocking1/States))
print("Dropped handoff calls in RAT1: {}".format(dropping1/States))

print("Blocked new calls in RAT2: {}".format(blocking2/States))
print("Dropped handoff calls in RAT2: {}".format(dropping2/States))