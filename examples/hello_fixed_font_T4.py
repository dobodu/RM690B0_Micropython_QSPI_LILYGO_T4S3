"""
hello.py

    Writes "Hello!" in random colors at random locations on the display.
"""

import random
import utime
import rm690b0
import tft_config_t4
import fonts.vga2_bold_16x32 as font
#import fonts.medium as font

tft = tft_config_t4.config()

def center(text):
    length = 1 if isinstance(text, int) else len(text)
    tft.text(
        font,
        text,
        (tft.width() - length * font.WIDTH) // 2,
        (tft.height() - font.HEIGHT ) // 2,
        rm690b0.WHITE,
        rm690b0.RED)

def main():
    tft_config_t4.TFT_CDE.value(1)
    tft.reset()
    tft.init()
    tft.rotation(3)
    tft.fill(rm690b0.RED)
    
    text = "Hello!"
    length = len(text) * font.WIDTH
    height = font.HEIGHT
    
    # Write center or display
    tft.text(font, text,
        (tft.width() - length) // 2,
        (tft.height() - font.HEIGHT ) // 2,
        rm690b0.WHITE, rm690b0.RED)
    utime.sleep(2)
    tft.fill(rm690b0.BLACK)

    for i in range(40000):
        tft.pixel(random.randint(0, tft.width()),
                  random.randint(0, tft.height()),
                  rm690b0.WHITE)


    while True:
                
        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(0)
            col_max = tft.width() - length
            row_max = tft.height() - height

            for _ in range(128):
                tft.text(
                    font,
                    text,
                    random.randint(0, col_max),
                    random.randint(0, row_max),
                    tft.colorRGB(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)),
                    tft.colorRGB(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)))
                utime.sleep(0.005)
                
            utime.sleep(1)


main()
