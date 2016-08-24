# coding: utf8

import pyautogui as pg
import time, os, logging, sys, random, copy

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


def jump():
    pg.press('space')


def getVars():
    cookies = driver.get_cookies()
    for i in range(4):
        cookie = cookies[i]
        if cookie['name'] == u'speed':
            speed = float(cookie['value'])
        if cookie['name'] == u'obs_dist':
            obs_dist = int(cookie['value'])
        if cookie['name'] == u'obs_size':
            obs_size = int(cookie['value'])
        if cookie['name'] == u'passed':
            passed = int(cookie['value'])
    return speed, obs_dist, obs_size, passed


def printVars(speed, obs_dist, obs_size, passed):
    dispStr = ""
    dispStr += '   ║ SPEED: ' + str(speed).rjust(5)
    dispStr += '  -  OBS DIST: ' + str(obs_dist).rjust(3)
    dispStr += '  -  OBS SIZE: ' + str(obs_size).rjust(2)
    print dispStr,
    print '\b' * (len(dispStr) + 2),
    sys.stdout.flush()
