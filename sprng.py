
import json
import random
import time

from arena import *



# GLOBALS ---------------------------------------------------------------------

arena = Arena()

dice_light = Light( object_id="a-dice_light",
                    position=Position(0, 50, -115),
                    persist=True )

die1_text = Text( object_id="a-die1_text",
                  color=Color(0, 0, 0),
                  position=Position(0, 50, -125),
                  scale=Scale(100, 100, 100),
                  text="i",
                  persist=True )



# HANDLERS --------------------------------------------------------------------

def die_click_handler(evt):

    if evt.type == "mousedown":
        timestamp = time.ctime(time.clock_gettime(time.CLOCK_REALTIME))
        new_roll_value = gen_d6_num()

        print("AT: "+ timestamp +"--> @"+ evt.data.source +" rolled a "+ \
               str(new_roll_value), flush=True)

        die1_text.data.text = str( new_roll_value )
        arena.add_object(die1_text)



# OTHER DEFs ------------------------------------------------------------------

def gen_d6_num():
  # Get new random number between 1 - 6
  return random.randint(2, 6)



# MAIN ------------------------------------------------------------------------

@arena.run_once # make this function a task that runs once at startup
def main():
    die1 = Box( object_id="a-die1",
                 color=Color(255, 255, 255),
                 position=Position(0, 50, -140),
                 scale=Scale(25, 25, 25),
                 clickable=True,
                 persist=True,
                 evt_handler=die_click_handler )
    arena.add_object(die1)

    arena.add_object(dice_light)
    arena.add_object(die1_text)



# THREADS ---------------------------------------------------------------------

arena.run_tasks()

