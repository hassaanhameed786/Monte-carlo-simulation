## what is the probability of 4 coin toss 3Head  1Tail
'''more the number of experiments is, the closer will be this probability,
determined by repeated experiments (simulation), to the actual probability 
(determined using combinatorics)'''

from random import randint
successes = 0
attempts = 10000       #experiments 
for i in range(attempts):
        if randint(0,1)+randint(0,1)+randint(0,1)+randint(0,1) == 3:
                successes += 1
print("No. Of attempts is" , attempts)
print("No. Of successes is", successes)
prob = successes  / attempts 
print("the probability of success is" ,prob)