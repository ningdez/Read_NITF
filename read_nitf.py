from osgeo import gdal
import numpy as np
import os
import cv2
import time
import multiprocessing

data_path = '/media/zeng/Elements/数据集/遥感目标检测与跟踪/WPAFB 2009/source/WPAFB-21Oct2009/Data/TRAIN/NITF/'
write_path = '/media/zeng/dataset/c/train/'
processes = 5

def read_data(file):
    start_time = time.clock()

    data = gdal.Open(data_path+file)

    im = np.zeros([data.RasterYSize,data.RasterXSize],dtype=np.uint8)
    data.ReadAsArray(xoff=0, yoff=0, xsize=data.RasterXSize, ysize=data.RasterYSize, buf_obj=im)
    im_name = '0'+file.split('-')[1][-3:]+'.tif'
    cv2.imwrite(write_path+im_name,im)

    print(im_name,time.clock()-start_time)


if __name__ == "__main__":

    imagenames = []

    for file in os.listdir(data_path):
        if not file.endswith('r0'):
            continue
        imagenames.append(file)

    pool = multiprocessing.Pool(processes=processes)
    pool.map(read_data,imagenames)

    print('finish')
