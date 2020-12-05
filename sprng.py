import arena
import json
import random



def scene_callback(msg):
  #print("scene_callback: -->\n", msg)

  jsonMsg = json.loads(msg)

  # Detect user click for new num and roll again -->
  if jsonMsg["object_id"] == "a-die0"\
  and jsonMsg["type"] == "mousedown":
    d6Roll = gen_d6_num()
    update_prnum_text(str(d6Roll))
    # Log timestamp, user and roll -->
    print(jsonMsg["timestamp"] + ": " + \
          jsonMsg["data"]["source"] + " rolled a " + str(d6Roll))


def gen_d6_num():
  # Get new random number between 1 - 6
  return random.randint(1, 6)


def update_prnum_text(newText):
  # Update prnum-render with new random number
  prnum.update(text=newText)



arena.init(
  "arena.andrew.cmu.edu",
  "realm",
  "sprng-changeme",
  scene_callback
)


die0 = arena.Object(
  objName="a-die0",
  objType=arena.Shape.cube,
  color=(255, 255, 255),
  location=(0, 50, -140),
  scale=(25, 25, 25),
  clickable=True,
  persist=True,
)

lightDie = arena.Object(
  objName="a-lightDie",
  objType=arena.Shape.light,
  location=(0, 50, -115),
  persist=True,
)

prnum = arena.Object(
  objName="a-prnum",
  objType=arena.Shape.text,
  color=(0, 0, 0),
  location=(0, 50, -125),
  scale=(100, 100, 100),
  text="6",
  persist=True,
)



arena.handle_events()
