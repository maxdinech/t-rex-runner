# coding: utf8

import time, os, logging, sys, random, copy
import websockets


#FIXME: how to access websocket in thoses functions ?
def jump():
    pg.press('space')


def crouch():
    pg.press('down')



last_vars = {'speed': 0, 'obs_dist': 0, 'obs_size': 0, 'passed': 0, 'score': 0, 'crashed': 0}
def gameDataHandler(ws, path):
    packet = ws.recv()
    print(packet)
    msg = json.loads(packet)
    if msg['type'] == 'data':
        kv = msg['content']
        key = kv['key']
        value = kv['value']

        if key == u'speed':
            last_vars['speed'] = float(value)
        if key == u'crashed':
            last_vars['crashed'] = (value == True)
        if key in ['obs_dist', 'obs_size', 'passed', 'score']:
            last_vars[key] = int(value)

def getVars():
    speed = last_vars['speed']
    obs_dist = last_vars['obs_dist']
    obs_size = last_vars['obs_size']
    passed = last_vars['passed_obs']
    score = last_vars['score']
    crashed = last_vars['crashed']
    return speed, obs_dist, obs_size, passed_obs, score, crashed

def write(str):
    sys.stdout.write(str)
    sys.stdout.flush()


def printVars(speed, obs_dist, obs_size):
    dispStr = ""
    dispStr += '    ║ SPEED: ' + str(speed).rjust(5)
    dispStr += '  -  OBS DIST: ' + str(obs_dist).rjust(3)
    dispStr += '  -  OBS SIZE: ' + str(obs_size).rjust(2)
    write(dispStr + '\r')


channel = websockets.serve(gameDataHandler, 'localhost', 4242)


#game_data_channel = threading.Thread(target=start_server)
#
#game_data_channel.start()
#
#time.sleep(10)
#
#game_data_channel.stop()
for i in channel:
    print(i)

