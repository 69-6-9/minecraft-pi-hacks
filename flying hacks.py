#flying hacks for pi edition 
#note only works on modded versions of minecraft pi that have servival mode
#connect to minecraft pi
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.player.getPos()
#other random stuff
import time

#difine block ids
grass = 2
flower = 38
air = 0
stone = 1
oakLeaves = 18

#code
while True:
    x, y, z = mc.player.getPos()  # player position (x, y, z)
    block_beneath = mc.getBlock(x, y-1, z)  # block ID

    if block_beneath == air:
        mc.setBlock(x, y-1, z, oakLeaves)
    time.sleep(0.01)
