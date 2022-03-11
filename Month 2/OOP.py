# # !usr/bin/env/python
# # coding: utf-8

# """
# About: Directory to folder segregation.
# Created:  Dec1, 2021
# @author: Vinay Vikram
# @copyright [2019-2021] by Motherson Innovations Tech Limited.
# NOTICE:  All information contained herein is, and remains the property of Motherson Innovations Tech Limited, India. The intellectual and technical concepts contained herein are 
# proprietary to  Motherson Innovations Tech Limited and may be covered by India and  Foreign Patents, patents in process, and are protected by trade secret
# or copyright law.  Dissemination of this information or reproduction of this material is strictly forbidden unless prior written permission is obtained from Motherson Innovations.
# """

import os,random
import time
import shutil, random, os
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
from tqdm import tqdm
class Video_creator:
    """
    This is a class to select n random images from a folder and make n number of copies of each image.

    Attributes:
        dirpath (str): The source file containing the images from which random images are to be chosen.
    """
    def __init__(self,dirpath):
        """
        The constructor for Video_creator class.

        Parameters:
            dirpath (str): The source file containing the images from which random images are to be chosen.
        """


        self.dirpath=dirpath


    def main(self):
        """
        The function to create a folder and also choose 1000 random images from the source folder.

        Returns:
            Filenames: 1000 random images from the source folder.
        """

    
    
        dirName = 'Image_folderr'  # Create directory
        os.mkdir(dirName) # Create target Directory
        print("Directory " , dirName ,  " Created ")
        filenames = random.sample(os.listdir(self.dirpath), 1000)
        return filenames
        # print(fname)

    def Copy_img(self,fname):
        """
        The function to create image specific folder,with 1000 copies of the image,inside the created folder for each image sample.

        Parameters:
            fname (Video_creator): It is the image name to be also taken as the folder name.

        Result:
            Creates 1000 folders with each folder containing 1000 copies of the specified image.
        """
        self.fname=fname
        folder_name = self.fname.split('.')[0]

        os.mkdir(r'.\Image_folderr\{0}'.format(folder_name))
        source_file = os.path.join(self.dirpath,self.fname) # print(source_file)
        dest_path = f'.\Image_folderr\{folder_name}' # print(dest_path)


        shutil.copy(source_file, dest_path)
        for i in range(800):
            output_p = 'Image_folderr\{0}\{1}.jpg'.format(folder_name,i)
            shutil.copy(os.path.join(dest_path,os.listdir(dest_path)[0]),output_p)

if __name__ == '__main__':
    """
    Driver function.
    """

    
    dirpath = r'D:\Image_data'

    values = Video_creator(dirpath)


    result=values.main()

    with ProcessPoolExecutor(max_workers=20) as exe:
       _ = list(tqdm(exe.map(values.Copy_img,result),total = 1000))




