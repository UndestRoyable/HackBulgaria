class Dungeon():

    def __int__(self, dungeon_map):
        f = open('dungeon_map', 'r')
        self.map = f.read()
        f.close

dungeon = Dungeon("basic_dungeon.txt")