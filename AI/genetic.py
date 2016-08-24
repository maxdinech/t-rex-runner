# coding: utf8

from master import *
import random as rd

# indiv = [k, m]
# (E) : D + W +k*(S-6) < m

# generation = 12 individus

mutate_prob = 0.2


def mutate(indiv):
    if rd.random() < mutate_prob:
        indiv[rd.randrange(0,2)] *= 2*rd.random()
    return indiv


def crossover(indiv1, indiv2):
    if rd.randrange(0,2) == 0:
        return (indiv1 + indiv2)[1:3][::-1]
    else:
        return (indiv2 + indiv1)[1:3][::-1]


def randIndiv():
    return [rd.randrange(-40, 40), rd.randrange(100, 300)]


def randGen(gen_size = 12):
    return [randIndiv() for i in range(gen_size)]


def evalIndiv(indiv):
    time.sleep(0.3)
    k = indiv[0]
    m = indiv[1]
    time.sleep(0.5)  # Avoids missing evals
    jump()  # Starts the game
    speed, obs_dist, obs_size, passed, score, crashed = getVars()
    print(chr(27) + "[2J")
    print('\n')
    print('        ╔════════════════════════════════════╗')
    print('        ║T-Rex:       GENETIC AI         v1.0║')
    print('       ╔╩════════════════════════════════════╩╗')
    print('       ║ (E) : Dist + Width + '+ str(int(k)).rjust(4) +'(S-6) < '+ str(int(m)).rjust(3) +' ║')
    print('       ║                                      ║')
    print('       ║  GEN n°'+ str(gen_no).rjust(2) +'/20        MAX_SCORE: '+ str(max_score).ljust(4) +'  ║')
    print('       ║  IND n°'+ str(ind_no).rjust(2) +'/12    GEN_MAX_SCORE: '+ str(gen_max_score).ljust(4) +'  ║')
    print('       ║                                      ║')
    print('       ╚╦════════════════════════════════════╦╝')
    while not crashed:
        speed, obs_dist, obs_size, passed, score, crashed = getVars()
        if (obs_dist + obs_size + k*(speed - 6) < m) and obs_dist > 40:  # Main equation
            jump()
        dispStr = ""
        dispStr += '       ║ SCORE: ' + str(score).rjust(4)
        dispStr += '  SPEED: ' + (str(speed) + "0000")[:5]
        dispStr += '  JMP: ' + str(passed).rjust(2) + " ║"
        print dispStr,
        print '\b' * (len(dispStr) + 2),
        sys.stdout.flush()
    return score


def evalGen(generation):
    global gen_max_score, max_score, ind_no
    eval_tab = []
    ind_no = 0
    gen_max_score = 0
    for indiv in generation:
        ind_no += 1
        score = evalIndiv(indiv)
        max_score = max(score, max_score)
        gen_max_score = max(score, gen_max_score)
        eval_tab += [score]
    return eval_tab


def nextGen(generation):
    global gen_no
    eval_tab = evalGen(generation)
    gen_no += 1
    #
    #
    #  INSERT CODE HERE
    #
    #
    return generation


def EVOLUTION(gen_number = 20):
    driver.get('http://localhost/t-rex-runner/')
    gen = randGen()
    for i in range(gen_number):
        nextGen(gen)
    return 0

max_score = 0
gen_max_score = 0
ind_no = 1
gen_no = 1

EVOLUTION()
