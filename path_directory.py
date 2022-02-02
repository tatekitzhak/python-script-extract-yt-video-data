import pathlib
import os

ROOT_DIR  = os.path.dirname(os.path.abspath(__file__))

def create_folder(topic_name, st):

    path= ROOT_DIR+'/'+topic_name
    print(path)
    print(topic_name)
    print(st)
    # Check whether the specified path exists or not

    # path_isExist = os.path.exists(path)
    # print('IsExis a tpath : ',path_isExist)

    # if not path_isExist:
      
    #   # Create a new directory because it does not exist 
    #     try:
    #         os.makedirs(path)
    #         print("The new directory is created =>", topic_name)
    #     except OSError as e:
    #         if e.errno != errno.EEXIST:
    #             raise

create_folder('abcd', None)