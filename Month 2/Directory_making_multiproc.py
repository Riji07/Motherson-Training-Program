# !usr/bin/env/python
# coding: utf-8

"""
About: Directory to folder segregation.
Created:  Dec1, 2021
@author: Vinay Vikram
@copyright [2019-2021] by Motherson Innovations Tech Limited.
NOTICE:  All information contained herein is, and remains the property of Motherson Innovations Tech Limited, India. The intellectual and technical concepts contained herein are 
proprietary to  Motherson Innovations Tech Limited and may be covered by India and  Foreign Patents, patents in process, and are protected by trade secret
or copyright law.  Dissemination of this information or reproduction of this material is strictly forbidden unless prior written permission is obtained from Motherson Innovations.
"""

import os,random
import time
import shutil, random, os
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from tqdm import tqdm

def main(dirpath):
    
    # Create directory
    dirName = 'Image_folder'
    # try:
        # Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")
    filenames = random.sample(os.listdir(dirpath), 1000)
    return filenames

def Copy_img(fname):
    # print(fname)
    dirpath = r'D:\Image_data'
    folder_name = fname.split('.')[0]

    os.mkdir(r'.\Image_folder\{0}'.format(folder_name))
    source_file = os.path.join(dirpath,fname)
    # print(source_file)
    dest_path = f'.\Image_folder\{folder_name}'


    shutil.copy(source_file, dest_path)
    for i in range(800):
        output_p = 'Image_folder\{0}\{1}.jpg'.format(folder_name,i)
        shutil.copy(os.path.join(dest_path,os.listdir(dest_path)[0]),output_p)

if __name__ == '__main__':

    
    dirpath = r'D:\Image_data'
    values = main(dirpath)
    # print(values)

    # with ProcessPoolExecutor(max_workers=20) as exe:
    #     _ = list(tqdm(exe.map(Copy_img,values),total = 1000))

    with ProcessPoolExecutor(max_workers=20) as exe:
        _ = list(tqdm(exe.map(Copy_img,values),total = 1000))
