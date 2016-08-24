import pyautogui as pg
import time, os, logging, sys, random, copy, time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://localhost/t-rex-runner/")



# Global vars
SPEED = 0
OBS_DIST = 0
OBS_SIZE = 0
PASSED = 0


def saut(t = 0):
	pg.press('space')


def botIdiot(n = 1000):
	pg.click(350, 300)
	for i in range(n):
		saut(100)


def reloadCookies():
	global SPEED, OBS_DIST, OBS_SIZE, PASSED
	cookies = driver.get_cookies()
	for i in range(4):
		cookie = cookies[i]
		if cookie['name'] == u'speed':
			SPEED = float(cookie['value'])
		if cookie['name'] == u'obs_dist':
			OBS_DIST = int(cookie['value'])
		if cookie['name'] == u'obs_size':
			OBS_SIZE = int(cookie['value'])
		if cookie['name'] == u'passed':
			PASSED = int(cookie['value'])
	return
	

def main():
	print('Press Ctrl-C to quit.')
	try:
	    while True:
	    	reloadCookies()
	        varsStr = 'SPEED: ' + str(SPEED).rjust(5) + '  -  OBS DIST: ' + str(OBS_DIST).rjust(3) \
	        			+ '  -  OBS SIZE: ' + str(OBS_SIZE).rjust(2)
	        print varsStr,
	        print '\b' * (len(varsStr) + 2),
	        sys.stdout.flush()
	        if OBS_DIST < 170 and OBS_DIST > 50:
	        	saut()
	except KeyboardInterrupt:
	    print '\n'


main()