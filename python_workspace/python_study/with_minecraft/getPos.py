from mcpi.minecraft import Minecraft as MC

root = MC.create()

my_id = root.getPlayerEntityId("Jooooook")
print("my_id: ", my_id)

my_pos = root.entity.getPos(my_id)
pos_x = {}
pos_z = {}
pos_y = {}

pos_x["Jooooook"] = my_pos.x
print(pos_x)