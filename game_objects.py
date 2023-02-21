import peices

def rankfile_to_index(rank, file):
    files = ["a", "b", "c", "d", "e", "f", "g", "h"]
    gridy = files.index(file.lower())
    gridx = 8-rank
    return gridx, gridy

class Grid: 
    def __init__(self):
        self.grid = [ [None for file in range(8)] for rank in range (8) ]

    def add(self, rank, file, peice):
        gridx, gridy = rankfile_to_index(rank, file)
        self.grid[gridx][gridy] = peice

    def remove(self, rank, file):
        gridx, gridy = rankfile_to_index(rank, file)
        self.grid[gridx][gridy] = None
    
    def move(self, rank, file, peice):
        initx, inity = peice.rank, peice.file
    
    def console_display(self):
        for row in self.grid:
            for item in row:
                if item == None:
                    print("-", end=" ")
                else:
                    print(item.get_token(), end=" ")
            print("")
    
    def reset(self):
        for vertical_symmetry in range(-1, 2, 2):
            vs = vertical_symmetry
            for horozontal_symmetry in range(-1, 2, 2):
                hs = horozontal_symmetry

                self.add()


