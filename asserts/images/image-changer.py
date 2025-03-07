import PIL
from PIL import Image
import os
from os.path import join
if os.path.exists('Chinese-chess-board.png'):
    print("yes")
else:
    print("no")
chessboard=Image.open("Chinese-chess-board.png")

    
new_size=(chessboard.size()//8)
for x in range(13):
    while x<9:
        image=Image.open(f'Chinese-chess/asserts/images/00{x+1}.png')
        new_image=image.resize((new_size))
    image=join('asserts','images',f'0.png')
    print()
    