import arena



arena.init("arena.andrew.cmu.edu", "realm", "sprng-changeme")

prnum = arena.Object(
    objType=arena.Shape.text,
    color=(255, 255, 255),
    location=(0, 2, 0),
    text="6",
)



input("Press any key to quit SPRNG...")

prnum.delete()

arena.handle_events()
