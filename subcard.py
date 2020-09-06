#Importing all the Libraries
from dearpygui.dearpygui import *
from time import *
from wit import Wit
import json
import speech_recognition as sr
from os.path import join, dirname
import os
import pandas as pd
import random

#Wit.ai ID
client = Wit("AMSAC56N5ZCBQS7F63RAIL34SHYXGNID")

#Main window configurations
set_main_window_size(1500, 800)

#Required variables
top_left = [75, 0]
bottom_right = [375, 180]
imagesdirlist = []
actualpath = ""
numimages = 0
image1 = ""
image2 = ""
image11 = ""
image22 = ""
pathcsv = path = join(dirname(__file__), 'WitFacebook\DatabaseWit.csv')
i1 = i2= i3 = i4 = ip =0
drawing_name = ""
path = join(dirname(__file__),"WitFacebook")


#Callback function to run Gifs from 2 photos
def onRender(sender, data):
    delta_draw_time = get_data("delta_draw_time")
    draw_speed = get_value("Draw Speed")
    if delta_draw_time > 0.5:
        if True:
            #Show image 1
            if get_data("sprite1"):
                draw_image(drawing_name, image1, top_left, pmax=bottom_right, uv_min=[0, 0], uv_max=[1, 1], tag="sprite")
                add_data("sprite1", False)
            else:
                #show image 2
                draw_image(drawing_name, image2, top_left, pmax=bottom_right, uv_min=[0, 0],
                           uv_max=[1, 1], tag="sprite")
                add_data("sprite1", True)
        add_data("delta_draw_time", 0)
    else:
        add_data("delta_draw_time", delta_draw_time + get_delta_time())

#Function for exercise window
def second_wind(img1, img2, Description):
    #Getting around duplicate items
    global i2
    window_name = "Workout##2" + str(i2)
    global drawing_name
    drawing_name = "Drawing_2" + str(i2)
    for j in range(i2):
        Description= Description + " "
    if is_item_visible(window_name) == None:
        add_window(window_name)
        add_drawing(drawing_name, width=1080, height=200)
        draw_image(drawing_name, img1, top_left, pmax=bottom_right, uv_min=[0, 0], uv_max=[1, 1], tag="sprite")
        #gif function
        set_render_callback("onRender", handler = window_name)
        add_data("delta_draw_time", 0.0)
        add_data("sprite1", True)
        global image1
        image1 = img1
        global image2
        image2 = img2
        add_text(Description)
        end_window("Workout")
        i2 = i2 +1
    else:
        show_item("Workout")

#Function for exercise window
def first_wind(img1, Description):
    global i1
    window_name = "Workout##1" + str(i2)
    global drawing_name
    drawing_name = "Drawing_1" + str(i2)
    if is_item_visible("Workout##1") == None:
        add_window(window_name)
        #image container
        add_drawing(drawing_name, width=1080, height=200)
        draw_image(drawing_name, img1, top_left, pmax=bottom_right, uv_min=[0, 0], uv_max=[1, 1])
        i1 = i1+1
        add_text(Description)
        end_window(window_name)
    else:
        show_item("Workout##1")

#Function for exercise window
def third_wind(img1, img2, img3, Description):
    global i3
    window_name = "Workout##3" + str(i3)
    global drawing_name
    drawing_name = "Drawing_3" + str(i3)
    for j in range(i4):
        Description= Description + " "
    if is_item_visible(window_name) == None:
        add_window(window_name)
        add_drawing(drawing_name, width=1080, height=200)
        draw_image(drawing_name, img1, top_left, pmax=bottom_right, uv_min=[0, 0], uv_max=[1, 1], tag="sprite")
        set_render_callback("onRender3", handler = window_name)
        add_data("delta_draw_time", 0.0)
        add_data("sprite1", True)
        global image1
        image1 = img1
        global image2
        image2 = img2
        global image3
        image3 = img3
        add_text(Description)
        i3 = i3 + 1
    else:
        show_item("Workout##3")

#Callback functin for running Gifs with 3 images
def onRender3(sender, data):
    delta_draw_time = get_data("delta_draw_time")
    draw_speed = get_value("Draw Speed")
    if delta_draw_time > 0.5:
        if True:
            #image 1
            if get_data("sprite1") == 1:
                draw_image(drawing_name, image1, top_left, pmax=bottom_right, uv_min=[0, 0], uv_max=[1, 1], tag="sprite")
                add_data("sprite1", 2)
            elif get_data("sprite1") == 2:
                #image2
                draw_image(drawing_name, image2, top_left, pmax=bottom_right, uv_min=[0, 0],
                           uv_max=[1, 1], tag="sprite")
                add_data("sprite1", 3)
            elif get_data("sprite1") == 3:
                #image 3
                draw_image(drawing_name, image3, top_left, pmax=bottom_right, uv_min=[0, 0],
                           uv_max=[1, 1], tag="sprite")
                add_data("sprite1", 1)
        add_data("delta_draw_time", 0)
    else:
        add_data("delta_draw_time", delta_draw_time + get_delta_time())

#Function for exercsise window
def fourth_wind(img1, img2, img3, img4, Description):
    global i4
    window_name = "Workout##4" + str(i4)
    global drawing_name
    drawing_name = "Drawing_4" + str(i4)
    for j in range(i4):
        Description= Description + " "

    if is_item_visible(window_name) == None:
        add_window(window_name)
        add_drawing(drawing_name, width=1080, height=200)
        draw_image(drawing_name, img1, top_left, pmax=bottom_right, uv_min=[0, 0], uv_max=[1, 1], tag="sprite")
        set_render_callback("onRender4", handler = window_name)
        add_data("delta_draw_time", 0.0)
        add_data("sprite1", True)
        global image1
        image1 = img1
        global image2
        image2 = img2
        global image3
        image3 = img3
        global image4
        image4 = img4
        desc = str(Description)
        add_text(desc)
        print(Description)

        i4 = i4+1
        end_window()

    else:
        show_item(window_name)

#Callback function for Gifs with 4 images
def onRender4(sender, data):
    delta_draw_time = get_data("delta_draw_time")
    draw_speed = get_value("Draw Speed")
    if delta_draw_time > 0.5:
        if True:
            #image 1
            if get_data("sprite1") == 1:
                draw_image(drawing_name, image1, top_left, pmax=bottom_right, uv_min=[0, 0], uv_max=[1, 1], tag="sprite")
                add_data("sprite1", 2)
            elif get_data("sprite1") == 2:
                #image 2
                draw_image(drawing_name, image2, top_left, pmax=bottom_right, uv_min=[0, 0],
                           uv_max=[1, 1], tag="sprite")
                add_data("sprite1", 3)
            elif get_data("sprite1") == 3:
                #image 3
                draw_image(drawing_name, image3, top_left, pmax=bottom_right, uv_min=[0, 0],
                           uv_max=[1, 1], tag="sprite")
                add_data("sprite1", 4)
            elif get_data("sprite1") == 4:
                #image 4
                draw_image(drawing_name, image4, top_left, pmax=bottom_right, uv_min=[0, 0],
                           uv_max=[1, 1], tag="sprite")
                add_data("sprite1", 1)
        add_data("delta_draw_time", 0)
    else:
        add_data("delta_draw_time", delta_draw_time + get_delta_time())

#Chest workout window
def chest_wind(img1, img2,img3, img4, img5, img6):
    window_name = "Chest Workout"
    global drawing_name
    drawing_name = "Drawing_chest"
    window_name = "Chest Workout"
    if is_item_visible(window_name) == None:
        add_window(window_name,525, 650)
        add_drawing(drawing_name, width=1080, height=150)
        draw_image(drawing_name, img1, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image(drawing_name, img2, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        add_data("delta_draw_time", 0.0)
        add_data("sprite1", True)
        text = extractingText(pathcsv, "pushup")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_2", width=1080, height=200)
        draw_image("drawing_2", img3, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_2", img4, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "incline pushup")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_3", width=1080, height=200)
        draw_image("drawing_3", img5, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_3", img6, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "decline pushup")
        add_text(text)
        end_window()
    else:
        show_item(window_name)

#Arms workout window
def arm_wind(img1, img2,img3, img4, img5, img6):
    window_name = "Arms Workout"
    drawing_name = "Drawing_arms"
    if is_item_visible(window_name) == None:
        add_window(window_name,525, 650)
        add_drawing(drawing_name, width=1080, height=200)
        draw_image(drawing_name, img1, [0,0], pmax=[175,200], uv_min=[0, 0], uv_max=[1, 1])
        draw_image(drawing_name, img2, [195,0], pmax=[370,200], uv_min=[0, 0], uv_max=[1, 1])
        add_data("delta_draw_time", 0.0)
        add_data("sprite1", True)
        text = extractingText(pathcsv, "chinup")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_arm_2", width=1080, height=200)
        draw_image("drawing_arm_2", img3, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_arm_2", img4, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "bench dips")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_arm_3", width=1080, height=200)
        draw_image("drawing_arm_3", img5, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_arm_3", img6, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "diamond pushup")
        add_text(text)
        end_window()
    else:
        show_item(window_name)

#Abs workout window
def abs_wind(img1, img2,img3, img4, img5, img6, img7):
    window_name = "Abs Workout"
    drawing_name = "Drawing_abs"
    if is_item_visible(window_name) == None:
        add_window(window_name,525, 650)
        add_drawing(drawing_name, width=1080, height=200)
        draw_image(drawing_name, img1, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image(drawing_name, img2, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        add_data("delta_draw_time", 0.0)
        text = extractingText(pathcsv, "leg raises")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_abs_2", width=1080, height=200)
        draw_image("drawing_abs_2", img3, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_abs_2", img4, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "bicycle")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_abs_3", width=1080, height=200)
        draw_image("drawing_abs_3", img5, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_abs_3", img6, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "mountain climbers")
        add_text(text)
        add_drawing("drawing_abs_4", width=1080, height=200)
        draw_image("drawing_abs_4", img7, [75, 0], pmax=[375,180], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "plank")
        add_text(text)
        end_window()
    else:
        show_item(window_name)

#Legs workout window
def legs_wind(img1, img2,img3, img4, img5, img6, img7, img8, img9, img10):
    window_name = "Legs Workout"
    drawing_name = "Drawing_legs    "
    if is_item_visible(window_name) == None:
        add_window(window_name,525, 650)
        add_drawing(drawing_name, width=1080, height=200)
        draw_image(drawing_name, img1, [0,0], pmax=[235,180], uv_min=[0, 0], uv_max=[1, 1])
        draw_image(drawing_name, img2, [245,0], pmax=[485,180], uv_min=[0, 0], uv_max=[1, 1])
        add_data("delta_draw_time", 0.0)
        text = extractingText(pathcsv, "squats")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_legs_2", width=1080, height=200)
        draw_image("drawing_legs_2", img3, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_legs_2", img4, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_legs_2", img5, [495,0], pmax=[735,150], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "lunges")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_legs_3", width=1080, height=200)
        draw_image("drawing_legs_3", img6, [0,0], pmax=[180,160], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_legs_3", img7, [210,0], pmax=[390,160], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_legs_3", img8, [420,0], pmax=[600,160], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "side lunges")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_legs_4", width=1080, height=200)
        draw_image("drawing_legs_4", img9,[0,0], pmax=[245,180], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_legs_4", img10, [255,0], pmax=[505,180], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "donkey kick")
        add_text(text)
        end_window(window_name)
    else:
        show_item(window_name)

#Shoulder workout window
def shoulder_wind(img1, img2,img3, img4, img5, img6):
    window_name = "Shoulder Workout"
    global drawing_name
    drawing_name = "Drawing_shoulder"
    if is_item_visible(window_name) == None:
        add_window(window_name,525, 650)
        add_drawing(drawing_name, width=1080, height=150)
        draw_image(drawing_name, img1, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image(drawing_name, img2, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        add_data("delta_draw_time", 0.0)
        add_data("sprite1", True)
        text = extractingText(pathcsv, "decline pushup")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_shoulder_2", width=1080, height=200)
        draw_image("drawing_shoulder_2", img3, [0,0], pmax=[225,200], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_shoulder_2", img4, [245,0], pmax=[475,200], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "dips")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_shoulder_3", width=1080, height=200)
        draw_image("drawing_shoulder_3", img5, [0,0], pmax=[235,150], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_shoulder_3", img6, [245,0], pmax=[485,150], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "pike pushup")
        add_text(text)
        end_window(window_name)
    else:
        show_item(window_name)

#Back workout window
def back_wind(img1, img2,img3, img4, img5, img6, img7, img8):
    window_name = "Back Workout"
    global drawing_name
    drawing_name = "Drawing_back"
    if is_item_visible(window_name) == None:
        add_window(window_name,525, 650)
        add_drawing(drawing_name, width=1080, height=230)
        draw_image(drawing_name, img1, [0,0], pmax=[235,230], uv_min=[0, 0], uv_max=[1, 1])
        draw_image(drawing_name, img2, [245,0], pmax=[485,230], uv_min=[0, 0], uv_max=[1, 1])
        add_data("delta_draw_time", 0.0)
        add_data("sprite1", True)
        text = extractingText(pathcsv, "inverted rows")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_back_2", width=1080, height=220)
        draw_image("drawing_back_2", img3, [0,0], pmax=[225,220], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_back_2", img4, [245,0], pmax=[475,220], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "chinup")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_back_3", width=1080, height=200)
        draw_image("drawing_back_3", img5, [0,0], pmax=[235,180], uv_min=[0, 0], uv_max=[1, 1])
        draw_image("drawing_back_3", img6, [245,0], pmax=[485,180], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "pullup")
        add_text(text)
        add_spacing(count=20)
        add_drawing("drawing_back_4", width=1080, height=155)
        draw_image("drawing_back_4", img7, [0,0], pmax=[390,150], uv_min=[0, 0], uv_max=[1, 1])
        add_drawing("drawing_back_5", width=1080, height=155)
        draw_image("drawing_back_5", img8, [0,0], pmax=[390,150], uv_min=[0, 0], uv_max=[1, 1])
        text = extractingText(pathcsv, "supermans")
        add_text(text)
        end_window(window_name)
    else:
        show_item(window_name)

#Function for extracting images from folder
def extractingimage(path,value):
    imagesdir = []
    exercisepath = os.path.join(path,value)
    numofimage = len(os.listdir(exercisepath))
    li = os.listdir(exercisepath)
    for i in li:
        imag = os.path.join(exercisepath,i)
        imagesdir.append(imag)
    return exercisepath, numofimage, imagesdir

#Function for extracting the text from csv database
def extractingText(pathcsv,workout):
    database = pd.read_csv(pathcsv,encoding='latin1')

    ExerciseName = database['Name'].tolist()
    Details = database['Text'].tolist()
    ind = ExerciseName.index(workout)
    return Details[ind]
