import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from itertools import cycle

def read_image_pixels(image_path):
    img = Image.open(image_path)
    width, height = img.size
    pixels = list(img.getdata())
    return width, height, pixels

def pixels_to_hex(pixels):
    hex_val = [f'#{r:02x}{g:02x}{b:02x}' for r, g, b, _ in pixels]
    
    
    return hex_val

def create_color_mapping(hex_val):
    
    print(hex_val)
    colorDict = {}
    charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
    
    i = 9;
    
    unique_colors = [color for color in hex_val if color != '0x0000']
    for color in unique_colors:
        if color not in colorDict:
            colorDict[color] = charList[i];
            i += 1;
    return colorDict

def apply_color_mapping(hex_val, colorDict):
    textImg = []
    for hex_color in hex_val:
        textImg.append(colorDict.get(hex_color, '0'))
    return textImg

def hex_to_rgb565(hex_color):
    
  i  = 0

  for pixel in hex_color:
      
      # Extract individual color components (RGB888 format)
      red = (int(pixel[1:3], 16) >> 3) & 0x1F
      green = (int(pixel[3:5], 16) >> 2) & 0x3F
      blue = (int(pixel[5:7], 16) >> 3) & 0x1F

      # Combine color components to get RGB565 format
      rgb565 = (red << 11) | (green << 5) | blue

      # Format as a hexadecimal string and return
      hex_pixel =  f"0x{rgb565:04X}"

      hex_color[i] = hex_pixel
      
      i+= 1
      
  return hex_color
    
def plot_text_image(textImg, width):
    cnt = 0
    for i in textImg:
        if cnt % width == 0:
            print('L', end="")
        cnt += 1
        print(i, end="")
        
def plot_text_image2(textImg, width):
    cnt = 0
    for i in textImg:
        if cnt % width == 0:
            print('L')
        cnt += 1
        print(i, end="")     
        
def print_switch_case(colorDict):
    for color_key in colorDict:
       print('case',"'{}'".format(colorDict[color_key]),':')
       print('return',"{}".format(color_key),";")
        
def main():
    image_path = 'soda_can.png'
    width, height, pixels = read_image_pixels(image_path)
    hex_val = pixels_to_hex(pixels)
    rgb_val = hex_to_rgb565(hex_val)
    colorDict = create_color_mapping(rgb_val)
    textImg = apply_color_mapping(hex_val, colorDict)
    plot_text_image(textImg, width)  # Pass 'width' to the plot_text_image function
    plot_text_image2(textImg, width)  # Pass 'width' to the plot_text_image function
    print(colorDict)
    print_switch_case(colorDict)
if __name__ == "__main__":
    main()

