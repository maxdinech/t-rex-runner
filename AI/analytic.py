# coding: utf8

from master import *


def analytic_AI(jump_dist, speed_coef):
    driver.get(url)
    print('\n')
    print('    ╔════════════════════════════════════╗')
    print('    ║T-Rex:       ANALYTIC IA        v2.0║')
    print('   ╔╩════════════════════════════════════╩╗')
    print('   ║ Eq : Jump if D + W '+ str(speed_coef).rjust(3) +'(S-6) + < ' + str(jump_dist)+ '  ║')
    print('   ║                 Press Ctrl-C to quit.║')
    print('   ╚╦════════════════════════════════════╦╝')
    try:
        while True:
            speed, obs_dist, obs_size, passed, score, crashed = getVars()
            if obs_dist + obs_size + speed_coef*(speed - 6) < jump_dist:
                jump()
            dispStr = ""
            dispStr += '    ║ SPEED: ' + str(1000*speed).rjust(5)
            dispStr += '  DIST: ' + str(obs_dist).rjust(3)
            dispStr += '  SIZE: ' + str(obs_size).rjust(2) + " ║"
            print dispStr, '\r',
            sys.stdout.flush()
    except KeyboardInterrupt:
        print '\n'


analytic_AI(210, -15)
