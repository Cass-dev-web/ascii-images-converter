import PIL.Image
import os
import time
#chracters
ASCII_CHARS = ["@","%","#","S","?","*","+",";","/","[","]","'","_","-",":",".",",","=","^","&","(",")","Z","W","0","O","g","!"]
#resize image
def resize_image(image, new_width):
    width,height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width*ratio)
    resized_image= image.resize((new_width,new_height))
    return(resized_image)
#convert to grayscale
def gs(img):
    grIm=img.convert("L")
    return(grIm)
#ascii
def pixels_to_ascii(img):
    pixs=img.getdata()
    chr="".join([ASCII_CHARS[pixel//25] for pixel in pixs])
    return(chr)
def main():
    path=input("Frames doc:\n")
    new_width=int(input("Width:\n"))
    output=input("Output:\n")
    for filename in os.listdir(path):
        time.sleep(.1)
        image=PIL.Image.open(f"{path}/{filename}")
        new_image_data=pixels_to_ascii(gs(resize_image(image,new_width)))
        pixel_count=len(new_image_data)
        ascii_image="\n".join(new_image_data[i:(i+new_width)] for i in range(0,pixel_count,new_width))
        with open(f"{output}/{filename}_ASCII.txt","w") as f:
            f.write(ascii_image)
        print(f"FRAME: '{filename}' CONVERSION:")
        print(ascii_image)
main()