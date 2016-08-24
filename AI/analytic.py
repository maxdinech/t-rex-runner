# coding: utf8

from master import *


def analytic_IA(jump_dist):
    driver.get('http://localhost/t-rex-runner/')
    print('\n')
    print('    ╔════════════════════════════════════╗')
    print('    ║T-Rex:       ANALYTIC IA        v2.0║')
    print('   ╔╩════════════════════════════════════╩╗')
    print('   ║ Eq : Jump if D + W 10*(S-6) + < ' + str(jump_dist)+ '  ║')
    print('   ║                 Press Ctrl-C to quit.║')
    print('   ╚╦════════════════════════════════════╦╝')
    try:
        while True:
            speed, obs_dist, obs_size, passed = getVars()
            if obs_dist + obs_size + 10*(speed - 6) < jump_dist:
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


analytic_IA(210)
