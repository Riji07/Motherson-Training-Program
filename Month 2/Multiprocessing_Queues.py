import os,random
from queue import Queue
import time
import shutil, random, os
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from tqdm import tqdm
from PIL import Image

q=Queue()
dirName = 'Image_folder'
dirpath = r'D:\Image_data'
def main(dirpath):
    
    if os.path.isdir(os.path.join(os.getcwd(),dirName)):
        pass
    else:
        os.mkdir(dirName)

    filenames = random.sample(os.listdir(dirpath), 10)
    return filenames 
    
    
def resize_img(value):

    
    image = Image.open(dirpath+'\\'+value)
    new_image = image.resize((400, 400))
    new_image.save(os.getcwd()+dirName+'\\'+value)

    q.put(new_image)
    
        
if __name__ == '__main__':
    
    values = main(dirpath)
    with ProcessPoolExecutor(max_workers=20) as exe:
        _ = list(exe.map(resize_img,values))




    