import time

from mcpi_e.minecraft import Minecraft

serverAddress="127.0.0.1" # change to your minecraft server
pythonApiPort=4711 #default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName="mMan" # change to your username

mc = Minecraft.create(serverAddress,pythonApiPort, playerName)
pos = mc.player.getPos()

print("pos: x:{},y:{},z:{}".format(pos.x, pos.y, pos.z))

# mc.setBlock(9.5, -3, 0.5, 0)
#
# for x in range(50):
#     for y in range(20):
#         for z in range(50):
#             mc.setBlock(x, y, -z, 0)
# print(dir(mc))
MATERIAL_GLASS = 20
MATERIAL_WOOD = 17
MATERIAL_AIR = 0
MATERIAL_GOLD = 41
MATERIAL_ICE = 79
MATERIAL_DIAMOND = 57


class House:
    def __init__(self, x, y, z, r, m):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.material = m

    def __str__(self):
        return f"House {self.material}"

    def __repr__(self):
        return f"<House {self.material}>"

    def build(self, clear=False):
        # Строим дом
        # цикл постройки пола
        if clear:
            new_material = MATERIAL_AIR
        else:
            new_material = self.material
        for n in range(self.r):
            for k in range(self.r):
                mc.setBlock(self.x + k, self.y, self.z + n, new_material)

        # # Постройка стен
        for n in range(self.r):
            for k in range(self.r - 2):
                mc.setBlock(self.x, (self.y + 1) + k, self.z + n, new_material)

        for n in range(self.r):
            for k in range(self.r - 2):
                mc.setBlock(self.x + self.r - 1, (self.y + 1) + k, self.z + n, new_material)

        for n in range(self.r):
            for k in range(self.r - 2):
                mc.setBlock(self.x + n, (self.y + 1) + k, self.z, new_material)

        for n in range(self.r):
            for k in range(self.r - 2):
                mc.setBlock(self.x + n, (self.y + 1) + k, self.z + self.r - 1, new_material)

        # # Постройка потолка
        for k in range(self.r):
            for n in range(self.r):
                mc.setBlock(self.x + n, self.y + self.r - 1, self.z + k, new_material)

    def clear(self):
        self.build(clear = True)

    def increase_size(self, l):
        self.clear()
        self.r = self.r + l
        self.build()

    def up(self):
        self.clear()
        self.y = self.y + 1
        self.build()


class WoodHouse(House):
    def __init__(self, x, y, z, r):
        super().__init__(x, y, z, r, MATERIAL_WOOD)


class GoldHouse(House):
    def __init__(self, x, y, z, r):
        super().__init__(x, y, z, r, MATERIAL_GOLD)


class Level:
    def __init__(self):
        self.houses = {}

    def add_house(self, key, x, y, z, r, m):
        new_house = House(x, y, z, r, m)
        self.houses[key] = new_house
        print(self.houses)

    def info(self):
        for house in self.houses.values():
            print(house)

    def build_all_houses(self):
        for house in self.houses:
            House.build(self.houses[house])

    def clear_all_houses(self):
        for house in self.houses:
            House.clear(self.houses[house])

    def build_house(self, key):
        House.build(self.houses[key])

    def clear_house(self, key):
        House.clear(self.houses[key])



l = Level()
print(l.houses)
# l.addhouse(3, 0, 0, 3, MATERIAL_GOLD)
# l.addhouse(7, 0, 0, 4, MATERIAL_WOOD)
# l.addhouse(3, 0, 5, 5, MATERIAL_GLASS)
# l.addhouse(7, 0, 6, 6, MATERIAL_ICE)
# l.addhouse(14, 0, 0, 7, MATERIAL_DIAMOND)
# l.info()
# l.buildAll()
# l.clearAll()

while True:
    chatEvents = mc.events.pollChatPosts()
    print(chatEvents)
    for chatEvent in chatEvents:
        message = chatEvent.message.split(" ")
        if message[0] == "build" and message[1] == "all":
            l.build_all_houses()

        elif message[0] == "build":
            l.add_house(message[1], int(message[2]), int(message[3]), int(message[4]), int(message[5]), int(message[6]))
            l.build_house(message[1])

        elif message[0] == "clear" and message[1] == "all":
            l.clear_all_houses()

        elif message[0] == "clear" and message[1] == "zone":
            mc.setBlocks(-50, 0, -50, 50, 50, 50, 0)

        elif message[0] == "clear":
            l.clear_house(message[1])





# mc.setBlocks(-50, 0, -50, 50, 50, 50, 0)

    time.sleep(1)

# woodhouse = WoodHouse(3, 0, 0, 4)
# goldhouse = GoldHouse(3, 0, 0, 4)
# house = House(3, 0, 0, 12, 5)
#
# mc.setBlocks(-50, 0, -50, 50, 50, 50, 0)


# woodhouse.clear()
# while True:
#     time.sleep(1)
#     woodhouse.up()
# goldhouse.build()
# house.increase_size(3)
# woodhouse.build()