# coding: utf8

from master import *

def naive_AI(jump_dist):
    driver.get(url)
    speed, obs_dist, obs_size, passed, score, crashed = getVars()
    print('\n')
    print('    ╔════════════════════════════════════╗')
    print('    ║T-Rex:        NAIVE AI          v1.0║')
    print('   ╔╩════════════════════════════════════╩╗')
    print('   ║ Jump trigger dist: ' + str(jump_dist) + ' px            ║')
    print('   ║                 Press Ctrl-C to quit.║')
    print('   ╚╦════════════════════════════════════╦╝')
    try:
        while True:
            speed, obs_dist, obs_size, passed, score, crashed = getVars()
            if obs_dist < jump_dist:
                jump()
            dispStr = ""
            dispStr += '   ║ SPEED: ' + str(1000*speed).rjust(5)
            dispStr += '  DIST: ' + str(obs_dist).rjust(3)
            dispStr += '  SIZE: ' + str(obs_size).rjust(2) + " ║"
            print dispStr,
            print '\b' * (len(dispStr) + 2),
            sys.stdout.flush()
    except KeyboardInterrupt:
        print '\n'

naive_AI(170)