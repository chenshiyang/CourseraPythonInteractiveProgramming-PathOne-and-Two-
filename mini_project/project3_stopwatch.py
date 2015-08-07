## A "stopwatch" game

import simplegui

# define global variables
# variable that count the time
time_count = 0

# the times of attempt you have tried
attempt = 0

# the times of succeed
hit = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    time_str = ""
    t = t % 6000# the capacity is 10 minutes
    
    min = t / 600
    
    t = t % 600
    sec = t / 10
    
    t = t % 10
    secth = t
    
    time_str = time_str + str(min)
    if sec < 10 :
        time_str = time_str + ":0" + str(sec)
    else :
        time_str = time_str + ":" + str(sec)
    time_str = time_str + "." + str(secth)
    return time_str
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()

def stop_handler():
    global attempt, hit
    if timer.is_running():
        attempt = attempt + 1
        timer.stop()
        if time_count % 10 == 0:
            hit = hit + 1

def reset_handler():
    global time_count, attempt, hit
    time_count = 0
    attempt = 0
    hit = 0
    timer.stop()
#    timer.start()

# define event handler for timer with 0.1 sec interval
def time_handler():
    global time_count
    time_count = time_count + 1
#    print time_count / 10.0

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(time_count), [125, 155], 24, "White")
    canvas.draw_text(str(hit) + "/" + str(attempt), [230,40], 24, "Yellow")
 
# define "space" key down handler
def key_handler(key):
    global attempt, hit
    if key == 32:# 32 means  the space key
        if timer.is_running():
            attempt = attempt + 1
            if time_count % 10 == 0:
                hit = hit + 1  

# create frame
frame = simplegui.create_frame("my_frame", 300, 300)
frame.add_button("start", start_handler,80)
frame.add_button("stop", stop_handler,80)
frame.add_button("reset", reset_handler,80)
frame.set_keydown_handler(key_handler)
frame.add_label("Tips : You can also hit the space key to play this game without" + 
               " pausing the timer", 200)

# register event handlers
timer = simplegui.create_timer(100, time_handler)
frame.set_draw_handler(draw_handler
                      )
# start frame
frame.start()

