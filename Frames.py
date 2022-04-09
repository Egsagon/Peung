from os import system, popen

class Frame:
    def __init__(self, pixel: str = None) -> None:
        """A Frame instance."""
        
        length = popen('stty size').read().split()

        self.lenx = int(length[0])
        self.leny = int(length[1])
        self.pixel = '.' if pixel is None else pixel

        self.grid = [[self.pixel for _ in range(self.leny)] for _ in range(self.lenx)]
    
    def make(self, seps=('\n', ''), clear=True) -> None:
        """Display the frame."""

        if clear: system('clear')
        print(seps[0].join(map(seps[1].join, self.grid)))
    
    def set(self, x: int, y: int, value: str, center = False) -> None:
        """Define the value of a pixel."""
        
        if center:
            x += self.leny // 2
            y += self.lenx // 2
        
        self.grid[y][x] = str(value)
        
    def get(self, x: int, y: int, center = False) -> None:
        """Define the value of a pixel."""
        
        if center:
            x += self.leny // 2
            y += self.lenx // 2
        
        return self.grid[y][x]

    def text(self, x: int, y: int, text: str, center = False, colorCode: str = '') -> None:
        """Display a text on the Frame."""
        
        if center: x -= len(text) // 2
        
        for letter in list(text):
            self.set(x, y, f'{colorCode}{letter}\033[0m' , center)
            x += 1
    
    def border(self, char: list, corners: list = None, spacinFromCenter = 0, addSpace: list = None) -> None:
        """Set a border on the Frame."""
        
        addX, addY = [0, 0] if addSpace is None else addSpace
        
        doCenter = bool(spacinFromCenter)
        
        if spacinFromCenter:
            walkX = spacinFromCenter
            walkY = spacinFromCenter
            
            correctX = walkY // 2
            correctY = walkX // 2
        
        else:
            walkX = self.leny - 1
            walkY = self.lenx - 1
            
            correctX = 0
            correctY = 0
        
        for i in range(walkY + 1 + addY * 2):
            self.set(0 - correctX - addX,       i - correctY - addY, char[1], doCenter)
            self.set(walkX - correctX + addX,   i - correctY - addY, char[1], doCenter)
        
        for i in range(walkX + 1 + addX * 2):
            self.set(i - correctX - addX,   0 - correctY - addY,        char[0], doCenter)
            self.set(i - correctX - addX,   walkY - correctY + addY,    char[0], doCenter)
        
        if corners is not None:
            if len(corners) == 1: corners = [corners[0]] * 4
            
            self.set(0 - correctX - addX,     0 - correctY - addY,      corners[0], doCenter)
            self.set(walkX - correctX + addX, 0 - correctY - addY,      corners[1], doCenter)
            self.set(0 - correctX - addX,     walkY - correctY + addY,  corners[2], doCenter)
            self.set(walkX - correctX + addX, walkY - correctY + addY,  corners[3], doCenter)


if __name__ == '__main__':
    main = Frame()

    main.text(0, 0, 'Hello!', True)

    main.border(['-', '|'],
                ['+'],
                4,
                [5, 5])

    main.make()