import os
import glob
directory = '/Users/yuanzhuang/Downloads/Udemy/the-complete-web-development-bootcamp/'

folder_list = glob.glob(directory+'*')
# file_list = os.walk(directory)
for i in range(len(folder_list)):
    srt_list = glob.glob(folder_list[i]+'/*.srt')
    for j in range(len(srt_list)):
        if srt_list[j][-6:] != 'en.srt':
            os.remove(srt_list[j])
