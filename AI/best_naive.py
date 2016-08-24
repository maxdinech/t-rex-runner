# coding: utf8

from master import *

highscore = 0
total = 0
average = 0

def naive_AI(jump_dist):
    driver.get('http://localhost/t-rex-runner/')
    speed, obs_dist, obs_size, passed, score, crashed = getVars()
    print('\n')
    print('    ╔════════════════════════════════════╗')
    print('    ║T-Rex:        NAIVE IA          v1.0║')
    print('   ╔╩════════════════════════════════════╩╗')
    print('   ║ Jump trigger dist: ' + str(jump_dist) + ' px            ║')
    print('   ║                 Press Ctrl-C to quit.║')
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

def test_AI(jump_dist, tries = 20):
    global highscore, total, average
    for i in range(1, 1 + tries):
        print(chr(27) + "[2J")
        score = naive_AI(jump_dist)
        total += score
        average = int(total/float(i))
        highscore = max(highscore, score)

test_AI(170)
