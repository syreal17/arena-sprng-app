#NOTE: this will come in handy soon! (from gh/ARENA-py/examples/core.py)
## trick: obtain an arena.py Object for an already-existing global scene object named "cameraRig"
## in order to update it's data attributes
#rig = arena.Object(objName="cameraRig")
#rig.update(
#    data='{"animation": {"property": "position", "to": "0 10 20", "easing": "linear", "dur": 1000}}')
#input("")
#rig.update(
#    data='{"animation": {"property": "position", "to": "0 10 -200", "easing": "linear", "dur": 1000}}')



import arena



def prnum_d6_callback(msg):
  print("d6_callback: ", msg)
  
  #TODO: get new random number between 1 - 6
  
  #TODO: update prnum-render with new random number

arena.init(
  "arena.andrew.cmu.edu",
  "realm",
  "sprng-changeme",
  prnum_d6_callback
)

prnum = arena.Object(
  objName="a-prnum",
  objType=arena.Shape.cube,
  color=(255, 255, 255),
  location=(0, 50, -141),
  scale=(100, 100, 100),
  #text="6",
  #persist=True,
  clickable=True,
)



#input("Press any key to quit SPRNG...")

#prnum.delete()

arena.handle_events()
