import os
import pyautogui
import time 
def joinMeet(link):
    os.system("google-chrome "+link+"?authuser=1")
    meet_join_button = (994,415)
    meet_cross_button = (1320,144)
    meet_mic_off_button = (401,576)
    pyautogui.moveTo(meet_cross_button)
    time.sleep(10)
    pyautogui.click()
    pyautogui.moveTo(meet_mic_off_button)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(meet_join_button)
    pyautogui.click()

def PingPC():
    from subprocess import run
    output = run(["ping","google.com","-c","1"], capture_output=True).stdout
    output = output[133:142]
    return output.decode()
def PlayMusic(playWhat):
    link = f"www.youtube.com/results?search_query="+playWhat
    os.system("google-chrome "+link)
    pyautogui.moveTo(473,360)
    time.sleep(5)
    pyautogui.click()
def Logout():
    pyautogui.hotkey("ctrl","alt","del")
def Battery():
    from subprocess import run
    output = run(["upower","-i","/org/freedesktop/UPower/devices/DisplayDevice"], capture_output=True).stdout
    # output = output[133:142]
    return output.decode()
