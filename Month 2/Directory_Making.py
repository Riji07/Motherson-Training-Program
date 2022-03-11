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
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

def main(dirpath):
    
    # Create directory
    dirName = 'Image_place'
    # try:
        # Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ")

    filenames = random.sample(os.listdir(dirpath), 10)
    for fname in tqdm(filenames):
            # print(fname)
            global folder_name
            folder_name = fname.split('.')[0]
            os.mkdir('.\\Image_place\\{0}'.format(folder_name))
            global source_file
            source_file = os.path.join(dirpath,fname)
            # print(source_file)
            # os.mkdir('Video')
            global dest_path
            dest_path = f'.\\Image_place\\{folder_name}'
            # print(dest_path)


def my_task(i):
    shutil.copy(source_file, dest_path)
    filename = dest_path
    output_p =('Image_place\{0}\{1}.jpg'.format(folder_name,i))
    shutil.copy(os.path.join(dest_path,os.listdir(dest_path)[0]),output_p)
    print("Completed")
            
            # exe=ProcessPoolExecutor(max_workers=5)
            # result=exe.map(my_task,range(10))
                        
        
                
    # except FileExistsError:
    #     print("Directory " , dirName ,  " already exists")  

    # print('.............Done...............')     
       

if __name__ == '__main__':
    start=time.time()
    dirpath = 'D:\Image_data'
    main(dirpath)
    exe=ProcessPoolExecutor(max_workers=5)
    # for _ in range(10):
    # result=exe.submit(my_task,range(10))
    result=exe.map(my_task,range(10))
    # my_task(range(10))
    # my_task(folder_name)
    # executor=ProcessPoolExecutor(max_workers=5)
    # future=executor.submit(folder_name)
    # result=future.result()
    
    # executor=ProcessPoolExecutor(max_workers=5)
    # future=executor.submit(my_task)
    # result=future.result()
    
    
    end=time.time()
    print(f'{end-start}')
