from arena import *

# create library
arena = Arena("arena.andrew.cmu.edu", "realm", "public", "sprng-changeme-13")

@arena.run_once # make this function a task that runs once at startup
def main():
    # make a cube
    cube = Cube(object_id="myCube", position=(0,3,-3), scale=(2,2,2))

    # add the cube to ARENA
    arena.add_object(cube)

# start tasks
arena.run_tasks()
