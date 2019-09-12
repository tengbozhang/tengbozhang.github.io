from PIL import Image
import os
def pic_webp(picpath):
   
    outputPath = picpath.replace(picpath.split(".")[-1],"webp")
    if not os.path.isfile(outputPath):
        print(outputPath)
        im = Image.open(picpath) 
        im.save(outputPath)



for (dirpath,dirname,dirfile) in os.walk("./"): 
    for fil in dirfile: 
        if "." in fil: 
            if fil.split(".")[1] in ["png","jpeg","jpg"]: 
                pic_webp(dirpath+"/"+fil) 
