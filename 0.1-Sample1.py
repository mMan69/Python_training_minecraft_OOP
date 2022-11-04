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


class House:
    def __init__(self, x, y, z, r, m):
        self.x = x
        self.y = y
        self.z = z
        self.r = r
        self.material = m

    def build(self):
        self._build(self.r, self.material)

    def _build(self, r, material):
        self.r = r
        # Строим дом
        # цикл постройки пола
        r = self.r
        for n in range(r):
            for k in range(r):
                mc.setBlock(self.x + k, self.y, self.z + n, material)

        # # Постройка стен
        for n in range(r):
            for k in range(r - 2):
                mc.setBlock(self.x, (self.y + 1) + k, self.z + n, material)

        for n in range(r):
            for k in range(r - 2):
                mc.setBlock(self.x + self.r - 1, (self.y + 1) + k, self.z + n, material)

        for n in range(r):
            for k in range(r - 2):
                mc.setBlock(self.x + n, (self.y + 1) + k, self.z, material)

        for n in range(r):
            for k in range(r - 2):
                mc.setBlock(self.x + n, (self.y + 1) + k, self.z + self.r - 1, material)

        # # Постройка потолка
        for k in range(r):
            for n in range(r):
                mc.setBlock(self.x + n, self.y + self.r - 1, self.z + k, material)


    def clear(self):
        self._build(self.r, 0)


    def increase_size(self, l):
        self.clear()
        self.r = self.r * l
        self.build()



house = House(3, 0, 0, 4, 5)
# house.clear()
# house.build()
house.increase_size(3)