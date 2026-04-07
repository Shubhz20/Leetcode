from typing import List

class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0  # 0=East, 1=North, 2=West, 3=South
        
        self.cycle = 2 * (self.w + self.h - 2)

    def step(self, num: int) -> None:
        if self.cycle == 0:
            return
        
        num %= self.cycle
        
        # special case: if full cycle, direction becomes South
        if num == 0:
            num = self.cycle
        
        for _ in range(num):
            if self.dir == 0:  # East
                if self.x + 1 < self.w:
                    self.x += 1
                else:
                    self.dir = 1  # turn North
                    self.y += 1
                    
            elif self.dir == 1:  # North
                if self.y + 1 < self.h:
                    self.y += 1
                else:
                    self.dir = 2  # turn West
                    self.x -= 1
                    
            elif self.dir == 2:  # West
                if self.x - 1 >= 0:
                    self.x -= 1
                else:
                    self.dir = 3  # turn South
                    self.y -= 1
                    
            else:  # South
                if self.y - 1 >= 0:
                    self.y -= 1
                else:
                    self.dir = 0  # turn East
                    self.x += 1

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return ["East", "North", "West", "South"][self.dir]