#hacks for minecraft pi

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
    x, y, z = mc.player.getPos()
    block_beneath = mc.getBlock(x, y-1, z)

    if block_beneath == air:#flying press space to fly)
        mc.setBlock(x, y-1, z, oakLeaves) 
    if block_beneath == stone:
        mc.setBlock(x, y-1, z, air) #stone Mining (stand on stone)
        mc.setBlock(x, y, z, air)
    time.sleep(0.05)
