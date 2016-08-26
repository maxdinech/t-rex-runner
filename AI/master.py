# coding: utf8

import pyautogui as pg
import time, os, logging, sys, random, copy

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# l = 'http://rawgit.com/17maxd/t-rex-runner/master/index.html'
url = 'http://localhost/t-rex-runner/'

def jump():
    pg.press('space')


def crouch():
    pg.press('down')



def getVars():
    cookies = driver.get_cookies()
    speed, obs_dist, obs_size, passed, score, crashed = 0, 0, 0, 0, 0, 0
    for i in range(6):
        cookie = cookies[i]
        if cookie['name'] == u'speed':
            speed = float(cookie['value'])
        if cookie['name'] == u'obs_dist':
            obs_dist = int(cookie['value'])
        if cookie['name'] == u'obs_size':
            obs_size = int(cookie['value'])
        if cookie['name'] == u'passed':
            passed_obs = int(cookie['value'])
        if cookie['name'] == u'score':
            score = int(cookie['value'])
        if cookie['name'] == u'crashed':
            crashed = (cookie['value'] == u'true')
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
