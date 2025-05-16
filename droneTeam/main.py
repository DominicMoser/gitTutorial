from djitellopy import Tello
from logging import log
from drone import *
from behavior import *

log("Drohene bereit machen")
myDrone = getAndInitializeDrone()
log()
dontFlyAgainstWall(myDrone)

