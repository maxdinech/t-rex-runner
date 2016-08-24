# coding: utf8

from master import *

def naive_AI(jump_dist):
    driver.get('http://localhost/t-rex-runner/')
    speed, obs_dist, obs_size, passed, score, crashed = getVars()
    print('\n')
    print('    ╔════════════════════════════════════╗')
    print('    ║T-Rex:        NAIVE IA          v1.0║')
    print('   ╔╩════════════════════════════════════╩╗')
    print('   ║ Jump trigger dist: ' + str(jump_dist) + ' px            ║')
    print('   ║ ' + str(current).rjust(2) + '/' + str(passes) + '           Press Ctrl-C to quit.║')
    print('   ╚╦════════════════════════════════════╦╝')
    try:
        while True and not crashed:
            speed, obs_dist, obs_size, passed, score, crashed = getVars()
            if obs_dist < jump_dist or score == 0:
                jump()
            dispStr = ""
            dispStr += '   ║ ACTUAL: ' + str(score).rjust(4)
            dispStr += '  TOP: ' + str(highscore).rjust(4)
            dispStr += '  AVG: ' + str(average).rjust(4) + " ║"
            print dispStr,
            print '\b' * (len(dispStr) + 2),
            sys.stdout.flush()
    except KeyboardInterrupt:
        print '\n'
    return score


def test_dist_AI(jump_dist, tries = 20):
    global highscore, total, average
    global current
    for j in range(1, 1 + tries):
        current = j
        print(chr(27) + "[2J")
        score = naive_AI(jump_dist)
        total += score
        average = int(total/float(j))
        highscore = max(highscore, score)
    return highscore, average


def test_AI(tries = 20):
    global highscore, total, average
    global passes
    passes = tries
    naive_scores = []
    for i in [140, 150, 160, 165, 170, 175, 180, 185, 190, 200]:
        highscore, total, average = 0, 0, 0
        naive_scores += [i, test_dist_AI(i, tries)]
    print(chr(27) + "[2J")
    print(naive_scores)


highscore, total, average = 0, 0, 0
current = 0
passes = 0
test_AI(20)
