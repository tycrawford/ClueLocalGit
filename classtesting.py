class Character:
    def __init__(self, start_pos, start_room, last_turn_end_room, current_room):
        self.start_pos = start_pos
        self.start_room = start_room
        self.last_turn_end_room = last_turn_end_room
        self.current_room = current_room
    def update_room():
        self.last_turn_end_room = self.current_room
    def player_move(self, movestring):
        for index in range(len(movestring)):
            conflict = False
            entering_room = False
            new_pos = self.start_pos
            if movestring[index] == "D":
                new_pos[1] += 1
            if movestring[index] == "U":
                new_pos[1] += -1
            if movestring[index] == "L":
                new_pos[0] += -1
            if movestring[index] == "R":
                new_pos[0] += 1
            if new_pos in betterdoorways:
                entering_room = True
                print("Entering room")
                break          
plum = Character([7,5],"Corridor", "Corridor", "Corridor")
class Room():
    def __init__(self, anchor, anchor_tile, rooms_index, coveredtiles, doorways, secret_passage, sp_corner, sp_link):
        self.anchor = anchor
        self.anchor_tile = anchor_tile
        self.rooms_index = rooms_index
        self.coveredtiles = coveredtiles
        self.doorways = doorways
        self.secret_passage = secret_passage
        self.sp_corner = sp_corner
        self.sp_link = sp_link
        boardtiles = []
        for i in self.coveredtiles:
            
            new_tile = []
            new_tile.append(self.anchor_tile[0] + i[0])
            new_tile.append(self.anchor_tile[1] + i[1])
            boardtiles.append(new_tile)
        self.boardtiles = boardtiles
        realdoors = []
        for i in self.doorways:
            new_doors = []
            new_doors.append(self.anchor_tile[0] + i[0])
            new_doors.append(self.anchor_tile[1] + i[1])
            realdoors.append(new_doors)
        self.realdoors = realdoors



study = Room("TL", [1,1], 1,[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3],[4,0],[4,1],[4,2],[4,3],[5,0],[5,1],[5,2],[5,3],[6,1],[6,2],[6,3]]
, [[6,3]], True, "TL",2 )
hall_tiles = squareroom(6,7)
hall = ("TL", [10,1],3)

def squareroom(l,h):
    coveredtiles = []
    for i in range(l):
        for j in range(h):
            coveredtiles.append([i,j])
    return coveredtiles

print(squareroom(4,4))


start_positions = ([17,1],[24,8],[15,25],[10,25],[1,18],[1,6])




print(study.realdoors)
betterdoorways = []
#add study doors
betterdoorways.append([7,4])
#Hall doors
betterdoorways.append([10, 5])
betterdoorways.append([12,7])
betterdoorways.append([13,7])
#Lounge Doors
betterdoorways.append([18,6])
#Library Doors
betterdoorways.append([7,9])
betterdoorways.append([4,11])
#Billiard Room
betterdoorways.append([2,13])
betterdoorways.append([6,16])
#Dining room
betterdoorways.append([18,10])
betterdoorways.append([17,13])
#Conservatory
betterdoorways.append([5,20])
#ballroom
betterdoorways.append([9,20])
betterdoorways.append([10,18])
betterdoorways.append([15,18])
betterdoorways.append([16,20])
#Kitchen
betterdoorways.append([20,19])

print(plum.start_pos)
plum.player_move("UURR")
print(plum.start_pos)
