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
  objType=arena.Shape.text,
  color=(255, 255, 255),
  location=(0, 50, -141),
  scale=(100, 100, 100),
  text="6",
  clickable=True,
)



#input("Press any key to quit SPRNG...")

#prnum.delete()

arena.handle_events()
