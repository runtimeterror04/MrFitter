#Importing all the required libraries
from dearpygui.dearpygui import *
from time import *
from wit import Wit
import json
import speech_recognition as sr
from subcard import *
import os
from os.path import join, dirname
import pandas as pd

#Required variables
imagesdirlist = []
actualpath = ""
numimages = 0
pathcsv = path = join(dirname(__file__), 'WitFacebook\DatabaseWit.csv')
exercise_list = ['tiptoe walking','pullup','chinup','bicycle','pushup','tip toe walking','leg raises','calve raises','crunches','dips','diamond pushup','supermans','side lunges','plank','squats','bench dips','lunges','decline pushup','scissor','donkey kick','jump squats','incline pushup','mountain climbers', 'pike pushup', 'inverted rows']
muscle_list = ['back','chest','abs','legs','arm','shoulder']

#WitID
client = Wit("AMSAC56N5ZCBQS7F63RAIL34SHYXGNID")

#GUI Main Window
set_main_window_size(1500, 800)
path = join(dirname(__file__),"WitFacebook")
top_left = [75, 0]
bottom_right = [375, 180]
val = ""

ID_INPUT = '##name_input'
add_spacing(count=60)
add_same_line(spacing=150)
add_input_text(ID_INPUT)
add_same_line(spacing = 30)

##Enter button
add_button("Enter", callback="GetWritten")

##Voice input button
add_spacing(count=30)
add_same_line(spacing = 570)
add_button("Use voice instead", callback="AudioInput")

#Function for text button callback
def GetWritten(sender, data):
    text = get_value(ID_INPUT)
    if len(text)==0:
        add_text("Write something baka")
    else:
        resp = client.message(text)
        try:
            val = resp['entities']['type_of_workout:type_of_workout'][0]['value']
            print(val+"yo")
        except Exception:
            try:
                val = resp['entities']['muscle:muscle'][0]['value']
            except Exception:
                val = "random gibberish"
                print("Couldn't find it")
        #Opening the corresponding Exercise window
        if val in exercise_list:
            actualpath, numimages, imagesdirlist = extractingimage(path,val)
            Description = extractingText(pathcsv, val)
            if numimages == 2:
                second_wind(imagesdirlist[0], imagesdirlist[1], Description)

            elif numimages == 1:
                first_wind(imagesdirlist[0], Description)

            elif numimages == 3:
                third_wind(imagesdirlist[0], imagesdirlist[1], imagesdirlist[2], Description)

            elif numimages == 4:
                fourth_wind(imagesdirlist[0], imagesdirlist[1], imagesdirlist[2],  imagesdirlist[3], Description)
        #Opening the corresponding body part workout window
        elif val in muscle_list:
            if val == "chest":
                actualpath, numimages, imagesdirlist = extractingimage(path,"chest")
                chest_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5])
            if val== "abs":
                actualpath, numimages, imagesdirlist = extractingimage(path,"abs")
                abs_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5],imagesdirlist[6])
            if val == "arm":
                actualpath, numimages, imagesdirlist = extractingimage(path,"arm")
                arm_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5])
            if val == "legs":
                actualpath, numimages, imagesdirlist = extractingimage(path,"legs")
                legs_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5],imagesdirlist[6],imagesdirlist[7],imagesdirlist[8],imagesdirlist[9])
            if val == "shoulder":
                actualpath, numimages, imagesdirlist = extractingimage(path,"shoulder")
                shoulder_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5])
            if val == "back":
                actualpath, numimages, imagesdirlist = extractingimage(path,"back")
                back_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5],imagesdirlist[6],imagesdirlist[7])

        else:
            add_text("Your search couldn't yeild any results, please consult the readme doc")

#Listening to the audio
def AudioInput(sender, data):
    add_text("Listening...")
    waitTime = 5
    run_async_function("AudioAsyncListen", waitTime, return_handler="AudioAsyncReturn")

#Asynchronous function continued
def AudioAsyncListen(sender, data):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Let's speak something....")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            #print("You said " + text)
        except:
            #print("Sorry coudn't understand")
            text = "No audio detected, please try again"
    return text

#Callback function for transcribed audio
def AudioAsyncReturn(sender, data):
    if data == "No audio detected, please try again":
        add_text(data)
    else:
        #Sending API request to Wit.ai
        resp = client.message(data)
        try:
            val = resp['entities']['type_of_workout:type_of_workout'][0]['value']
        except Exception:
            try:
                val = resp['entities']['muscle:muscle'][0]['value']
            except Exception:
                print("Couldn't find it bruh")

        #Opening the corresponding Exercise window
        if val in exercise_list:
            actualpath, numimages, imagesdirlist = extractingimage(path,val)
            Description = extractingText(pathcsv, val)
            if numimages == 2:
                second_wind(imagesdirlist[0], imagesdirlist[1], Description)

            elif numimages == 1:
                first_wind(imagesdirlist[0], Description)

            elif numimages == 3:
                third_wind(imagesdirlist[0], imagesdirlist[1], imagesdirlist[2], Description)

            elif numimages == 4:
                fourth_wind(imagesdirlist[0], imagesdirlist[1], imagesdirlist[2],  imagesdirlist[3], Description)
        #Opening the corresponding body part workout window
        elif val in muscle_list:
            if val == "chest":
                actualpath, numimages, imagesdirlist = extractingimage(path,"chest")
                chest_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5])
            if val== "abs":
                actualpath, numimages, imagesdirlist = extractingimage(path,"abs")
                abs_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5],imagesdirlist[6])
            if val == "arm":
                actualpath, numimages, imagesdirlist = extractingimage(path,"arm")
                arm_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5])
            if val == "legs":
                actualpath, numimages, imagesdirlist = extractingimage(path,"legs")
                legs_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5],imagesdirlist[6],imagesdirlist[7],imagesdirlist[8],imagesdirlist[9])
            if val == "shoulder":
                actualpath, numimages, imagesdirlist = extractingimage(path,"shoulder")
                shoulder_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5])
            if val == "back":
                actualpath, numimages, imagesdirlist = extractingimage(path,"back")
                back_wind(imagesdirlist[0], imagesdirlist[1],imagesdirlist[2], imagesdirlist[3],imagesdirlist[4],imagesdirlist[5],imagesdirlist[6],imagesdirlist[7])

        else:
            add_text("Your search couldn't yeild any results, please consult the readme doc")


#The configuration of the interface
set_style_window_padding(12.00, 4.00)
set_style_frame_padding(20.00, 20.00)
set_style_item_spacing(6.00, 2.00)
set_style_item_inner_spacing(4.00, 4.00)
set_style_touch_extra_padding(0.00, 0.00)
set_style_indent_spacing(21.00)
set_style_scrollbar_size(18.00)
set_style_grab_min_size(10.00)
set_style_window_border_size(1.00)
set_style_child_border_size(1.00)
set_style_popup_border_size(1.00)
set_style_frame_border_size(1.00)
set_style_tab_border_size(0.00)
set_style_window_rounding(3.00)
set_style_child_rounding(3.00)
set_style_frame_rounding(12.00)
set_style_popup_rounding(3.00)
set_style_scrollbar_rounding(2.00)
set_style_grab_rounding(12.00)
set_style_tab_rounding(3.00)
set_style_window_title_align(0.00, 0.50)
set_style_window_menu_button_position(mvDir_Left)
set_style_color_button_position(mvDir_Right)
set_style_button_text_align(0.50, 0.50)
set_style_selectable_text_align(0.00, 0.00)
set_style_display_safe_area_padding(3.00, 3.00)
set_style_global_alpha(1.00)
set_style_antialiased_lines(True)
set_style_antialiased_fill(True)
set_style_curve_tessellation_tolerance(1.25)
set_style_circle_segment_max_error(1.60)

start_dearpygui()
