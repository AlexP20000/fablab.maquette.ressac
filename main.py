import subprocess, time
import RPi.GPIO as GPIO
import os
import signal

INPUT_PIN_Button_1 = 3
INPUT_PIN_Button_2 = 5
INPUT_PIN_Button_3 = 7
INPUT_PIN_Button_4 = 11

GPIO.setmode(GPIO.BOARD)  ## Use board pin numbering
GPIO.setup(INPUT_PIN_Button_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(INPUT_PIN_Button_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(INPUT_PIN_Button_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(INPUT_PIN_Button_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

video_started = False
g_process = None
valButton_1 = -1
valButton_2 = -1
valButton_3 = -1
valButton_4 = -1


def playVideo(process, fileName = ""):
    # If a video is playing
    if video_started:
        # Stop the video
        process.stdin.write('q')

    # launch the video
    process = subprocess.Popen(['omxplayer', fileName],
                                   stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   close_fds=True)

    return process










while True:

    if GPIO.input(INPUT_PIN_Button_1) == 0:
        g_process = playVideo(g_process, '/home/pi/Videos/1.mp4')


    if GPIO.input(INPUT_PIN_Button_2) == 0:  # Button pressed
        g_process = playVideo(g_process, '/home/pi/Videos/2.mp4')


    if GPIO.input(INPUT_PIN_Button_3) == 0:  # Button pressed
        g_process = playVideo(g_process, '/home/pi/Videos/3.mp4')


    if GPIO.input(INPUT_PIN_Button_4) == 0:  # Button pressed
        g_process = playVideo(g_process, '/home/pi/Videos/4.mp4')


    # initiate the fact that a video started
    if g_process != None:
        video_started = g_process.poll() == None
    else:
        video_started = False

    time.sleep(0.2)