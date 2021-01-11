
import json
import random

from arena import *



# DEFs -----------------------------------------------------------------------

def scene_callback(msg):
  print("DEBUG: -1")
  jsonMsg = msg

  print("DEBUG: 0")
  # Detect user click for new num and roll again -->
  if jsonMsg["object_id"] == "a-die1"\
  and jsonMsg["type"] == "mousedown":
    print("DEBUG: 1")
    d6Roll = gen_d6_num()
    print("DEBUG: 2")
    update_die1_text(str(d6Roll))
    print("DEBUG: 3")
    # Log timestamp, user and roll -->
    print(jsonMsg["timestamp"] + ": " + \
          jsonMsg["data"]["source"] + " rolled a " + str(d6Roll))
    print("DEBUG: 4")


def gen_d6_num():
  # Get new random number between 1 - 6
  return random.randint(2, 6)


def update_die1_text(newText):
  # Update die1_text with new random number
  die1_text.update(text=newText)


arena = Arena( "arena.andrew.cmu.edu",
               "realm",
               "sprng-changeme-0.1.0",
               on_msg_callback=scene_callback )
# MAIN -----------------------------------------------------------------------
@arena.run_once # make this function a task that runs once at startup
def main():
    die1 = Cube( object_id="a-die1",
                 color=Color(255, 255, 255),
                 position=Position(0, 50, -140),
                 scale=Scale(25, 25, 25),
                 clickable=True,
                 persist=True )
    arena.add_object(die1)


    dice_light = Light( object_id="a-dice_light",
                        position=Position(0, 50, -115),
                        persist=True )
    arena.add_object(dice_light)


    die1_text = Text( object_id="a-die1_text",
                      color=Color(0, 0, 0),
                      position=Position(0, 50, -125),
                      scale=Scale(100, 100, 100),
                      text="6",
                      persist=True )
    arena.add_object(die1_text)



# start tasks
arena.run_tasks()
