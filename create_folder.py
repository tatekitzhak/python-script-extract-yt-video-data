import os, errno

table_name1 = 'video'
path= '/Users/eli/git_repos/python-script-extract-yt-video-data/'+table_name1

# Check whether the specified path exists or not
path_isExist = os.path.exists(path)
print('IsExis a tpath : ',path_isExist)


if not path_isExist:
  
  # Create a new directory because it does not exist 
    try:
        os.makedirs(path)
        print("The new directory is created!")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise