
import json
import random

from arena import *



# HANDLERS --------------------------------------------------------------------

def die_click_handler(evt):
    global arena
    global die1_text

    print("in die click handler")
    
    if evt.type == "mousedown":
        print("Rolling...")

        new_roll_value = gen_d6_num()

        print("... " + str(new_roll_value) + "!")

        # this line doesn't seem to work --v
        #die1_text.data.text = str( new_roll_value )
        die1_text.update_attributes(text=str(new_roll_value))
        arena.update_object(die1_text)

    # PORT : Old way to log roll data --v 
    # Log timestamp, user and roll -->
    #print(jsonMsg["timestamp"] + ": " + \
    #      jsonMsg["data"]["source"] + " rolled a " + str(d6Roll))



# OTHER DEFs ------------------------------------------------------------------

def gen_d6_num():
  # Get new random number between 1 - 6
  return random.randint(2, 6)



# GLOBALS ---------------------------------------------------------------------

arena = None
die1_text = None



# MAIN ------------------------------------------------------------------------

arena = Arena( "arena.andrew.cmu.edu",
               "realm",
               "sprng-changeme-0.1.0" )

@arena.run_once # make this function a task that runs once at startup
def main():
    die1 = Cube( object_id="a-die1",
                 color=(255, 255, 255),
                 position=Position(0, 50, -140),
                 scale=Scale(25, 25, 25),
                 clickable=True,
                 persist=True,
                 evt_handler=die_click_handler )
    arena.add_object(die1)


    dice_light = Light( object_id="a-dice_light",
                        position=Position(0, 50, -115),
                        persist=True )
    arena.add_object(dice_light)


    global die1_text
    die1_text = Text( object_id="a-die1_text",
                      color=Color(0, 0, 0),
                      position=Position(0, 50, -125),
                      scale=Scale(100, 100, 100),
                      text="i",
                      persist=True )
    arena.add_object(die1_text)



# THREADS ---------------------------------------------------------------------

arena.run_tasks()

