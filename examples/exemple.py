
import random
import utime
import rm690b0
import tft_config_t4
import fonts.large as font

tft = tft_config_t4.config()

def main():
    tft_config_t4.TFT_CDE.value(1)
    tft.reset()
    tft.init()
    tft.rotation(3)
    tft.brightness(0)
    tft.jpg("/bmp/smiley.jpg",10,10)
    for i in range(255):
        tft.brightness(i)
        utime.sleep(0.05)
    utime.sleep(1)
    tft.fill(rm690b0.BLACK)
    utime.sleep(1)
    
    text = "Hello!"
    length = tft.write_len(font,text)
    height = font.HEIGHT

    while True:

        for rotation in range(4):
            tft.rotation(rotation)
            tft.fill(rm690b0.BLACK)
            col_max = tft.width()
            row_max = tft.height()
            
            filled = random.randint(0,1)
            kind = random.randint(0,3)

            for _ in range(128):
                xpos = random.randint(0, col_max)
                ypos = random.randint(0, row_max)
                xpos_max = tft.width() - length -1
                ypos_max = tft.height() - height -1
                length = random.randint(0, col_max - xpos) // 2
                height = random.randint(0, row_max - ypos) // 2
                radius = random.randint(0, min(col_max - xpos, xpos, row_max - ypos, ypos )) // 2
                color = tft.colorRGB(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8))
                color2 = tft.colorRGB(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8))
                
                if kind == 0 :
                    if filled :
                        tft.fill_circle(xpos,ypos,radius, color)
                    else :
                        tft.circle(xpos, ypos, radius, color)
                
                if kind == 1 :
                    if filled :
                        tft.fill_rect(xpos,ypos,length, height, color)
                    else :
                        tft.rect(xpos,ypos,length, height, color)
                
                if kind == 2 :
                    if filled :
                        tft.fill_bubble_rect(xpos,ypos,length, height, color)
                    else :
                        tft.bubble_rect(xpos,ypos,length, height, color)
                        
                if kind == 3 :
                    if filled :
                        tft.write(font,text, random.randint(0, xpos_max), random.randint(0, ypos_max), color,color2)
                    else :
                        tft.write(font,text, random.randint(0, xpos_max), random.randint(0, ypos_max), color)
               
            utime.sleep(2)
       
main()
