import arena



arena.init("arena.andrew.cmu.edu", "realm", "sprng-changeme")

prnum = arena.Object(
    objName="prnum-render",
    objType=arena.Shape.text,
    color=(255, 255, 255),
    location=(0, 50, -141),
    scale=(100, 100, 100),
    text="6",
)



input("Press any key to quit SPRNG...")

prnum.delete()

arena.handle_events()
