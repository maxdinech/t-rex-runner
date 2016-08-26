# coding: utf8

from master import *
import numpy as np
import random as rd

# indiv = [k, m, "infos"]
# (E) : D + W +k*(S-6) < m

# generation = 20 individuals

mutate_prob = 0.1

max_score = 0
gen_max_score = 0
ind_no = 1
gen_no = 1

def mutate(indiv):
    global gen_no
    if rd.random() < mutate_prob:
        indiv[rd.randint(0,1)] *= (0.5 + rd.random())
        indiv[2] += ('.' + str(gen_no) + 'm')
    return indiv


def crossover(indiv1, indiv2):
    global gen_no
    return [(indiv1[0]+indiv2[0])/2.,(indiv1[1]+indiv2[1])/2.] + [str(gen_no) + 'co']


def randIndiv():
    global gen_no
    return [rd.randint(-40, 40), rd.randint(100, 300)] + [str(gen_no) + 'rd']


def randGen(gen_size = 20):
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
    print('        ╔══════════════════════════════════════╗ ')
    print('        ║T-Rex:        GENETIC AI          v2.0║ ')
    print('       ╔╩══════════════════════════════════════╩╗')
    print('       ║                                        ║')
    print('       ║  (E) :   Dist + Width + '+ str(int(k)).rjust(3) +'(S-6) < '+ str(int(m)).rjust(3) +' ║')
    print('       ║                                        ║')
    print('       ║  GEN n°'+ str(gen_no).rjust(2) +'/20          MAX_SCORE: '+ str(max_score).ljust(4) +'  ║')
    print('       ║  IND n°'+ str(ind_no).rjust(2) +'/20      GEN_MAX_SCORE: '+ str(gen_max_score).ljust(4) +'  ║')
    print('       ║  IND_ID: ' + indiv[2].ljust(29) + ' ║')
    print('       ╚╦══════════════════════════════════════╦╝')
    while not crashed:
        speed, obs_dist, obs_size, passed, score, crashed = getVars()
        if (obs_dist + obs_size + k*(speed - 6) < m) and obs_dist > 40:  # Main equation
            jump()
        dispStr = ""
        dispStr += '       ║ SCORE: ' + str(score).rjust(4)
        dispStr += '   SPEED: ' + (str(speed) + "0000")[:5]
        dispStr += '   JMP:' + str(passed).rjust(3) + " ║"
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
    # affichage des scores de la génération
    str_tab = [""] + [str(i).ljust(4) for i in eval_tab]
    print(chr(27) + "[2J")
    print('        ╔══════════════════════════════════════╗ ')
    print('        ║T-Rex:        GENETIC AI          v2.0║ ')
    print('       ╔╩══════════════════════════════════════╩╗')
    print('       ║             GENERATION n°'+ str(gen_no).ljust(2) +'            ║')
    print('       ║ 1 : '+ str_tab[1] +'  6 : '+ str_tab[6] + '  11: '+ str_tab[11] +'  16: '+ str_tab[16] +' ║')
    print('       ║ 2 : '+ str_tab[2] +'  7 : '+ str_tab[7] + '  12: '+ str_tab[12] +'  17: '+ str_tab[17] +' ║')
    print('       ║ 3 : '+ str_tab[3] +'  8 : '+ str_tab[8] + '  13: '+ str_tab[13] +'  18: '+ str_tab[18] +' ║')
    print('       ║ 4 : '+ str_tab[4] +'  9 : '+ str_tab[9] + '  14: '+ str_tab[14] +'  19: '+ str_tab[19] +' ║')
    print('       ║ 5 : '+ str_tab[5] +'  10: '+ str_tab[10] +'  15: '+ str_tab[15] +'  20: '+ str_tab[20] +' ║')
    print('       ╚╦══════════════════════════════════════╦╝')
    time.sleep(5)
    # os.system('scrot genetic/tab_gen_'+ str(gen_no) +'.png')
    # Choix des 4 parents
    eval_tab = [i**4 for i in eval_tab]  # On accentue les meilleurs
    eval_tab_norm = [float(i)/sum(eval_tab) for i in eval_tab]
    parents_id = []
    while len(parents_id) != 5:
        i = np.random.choice(range(20), 1, p=eval_tab_norm)[0]
        if not  i in parents_id:
            parents_id += [i]
    parents = [generation[i] for i in parents_id]
    # Construction de la génération suivante
        #  1-5 : Parents
        #  5-15: Tous les c-o possibles
        # 16-20: Aléas
    gen_no += 1
    # Ajout des parents
    nextGeneration = parents[:]
    # Ajout des c-o
    for i in range(5):
        for j in range(i+1, 5):
            nextGeneration += [crossover(parents[i], parents[j])]
    # Mutation parents et c-o
    nextGeneration = [mutate(i) for i in nextGeneration]
    # Ajout des rd
    for i in range(5):
        nextGeneration += [randIndiv()]
    return nextGeneration


def EVOLUTION(gen_number = 20):
    global max_score
    driver.get('url')
    gen = randGen()
    for i in range(gen_number):
        gen = nextGen(gen)
    return max_score


EVOLUTION()
