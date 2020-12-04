# SPRNG

## Shared PsuedoRandom Number Generator

This is an ARENA app that aims to provide simultaneous viewing of a
randomly generated number for multiple remote parties. This can 
facilitate playing some social or simple games via videochat.


## Motivation

During the long quarantine, I wanted to play some boardgames with 
family members. High fidelity simulators such as Tabletop Sim were 
alluring, but not an option for everyone I wanted to play games with.
While there's much more to most boardgames than just dice, having a 
random number generator that all parties involved could see 
simultaneously is an important first step.


## ARENA

ARENA is a platform for creating visual-web apps. It can do far more 
than what SPRNG even attempts, but it is also well-suited for simple
apps like SPRNG. Getting 3D rendering, webcam input/output,e etc. is
useful for many apps, simple or complex.


## Usage

```
pip3 install arena-py
git clone https://github.com/syreal17/sprng
cd sprng
python3 sprng.py
```

[TODO:] scene name should maybe be different, otherwise there will be 
collisions

Point a browser to 
`https://arena.andrew.cmu.edu/?scene=sprng-changeme
