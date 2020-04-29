from __future__ import print_function

from colordetect import ColorDetect
from PIL import Image, ImageDraw

## Source: https://gist.github.com/zollinger/1722663; https://github.com/MarvinKweyu/ColorDetect

def get_colors(infile, outfile=None, swatchsize=40):
    user_image = ColorDetect(infile)
    # get a dictionary return of color count
    cc = user_image.get_color_count(color_count=4)

    # Save colors to file

    pal = Image.new('RGB', (swatchsize*len(cc), swatchsize))
    draw = ImageDraw.Draw(pal)

    posx = 0
    for count, col in cc.items():
        int_col = (int(col[0]), int(col[1]), int(col[2]))
        draw.rectangle([posx, 0, posx+swatchsize, swatchsize], fill=int_col)
        posx += swatchsize

    del draw
    if outfile is not None:
        pal.save(outfile, "PNG")

    return cc

if __name__ == '__main__':
    cc = get_colors('Images/oxfam-wereldwinkel-boom-1170x878.jpg', 'outfile.png')
    print(cc)



