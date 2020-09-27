# -*- coding: utf-8 -*-
##################################################
#
# Created by eDAB
# email: davor.baric@rt-rk.com
#
# Description:
#       FileHandler, sorting files in folder according extension
#
# Usage:
#       run cmd in folder -> python FileHandler.py -p "pathToFolderWithFiles"(use"") -e extensionOfFile
#
##################################################

# import modules
import argparse
import os
import shutil


class file_handler(object):
    def __init__(self, extension, path):
        self.extension = extension
        self.path = path

    @staticmethod
    def get_path_extension():
        argPars = argparse.ArgumentParser(description="Enter the path to the folder")
        argPars.add_argument('-p', '--path', type=str, help="path to the folder")
        argPars.add_argument('-e', '--extension', type=str, help="extension of file")
        args = argPars.parse_args()

        path_to_folder = args.path
        print(path_to_folder)
        extension = args.extension
        if path_to_folder is not None and extension is not None:
            return path_to_folder, extension
        else:
            print("-" * 50)
            print("ERROR: Use -P path and -E extension!!!")
            print("-" * 50)
            exit()

    def sorting_files(self):
        list_files = list()
        for subdir, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(self.extension):
                    list_files.append(os.path.join(subdir, file))

        extension = self.extension[1::]
        new_path = self.path + '\\' + extension + '_files'
        if not os.path.exists(new_path):
            os.makedirs(new_path)
            for item in list_files:
                shutil.move(item, new_path)


if __name__ == '__main__':
    fh_obj = file_handler(path=file_handler.get_path_extension()[0],
                          extension=file_handler.get_path_extension()[1])
    fh_obj.sorting_files()
