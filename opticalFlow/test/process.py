import os

def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".png"):
                os.remove(os.path.join(root, name))
                
bin = r'..\build\Release\optflow.exe '

dir = "\"C:/Users/megamusz/Desktop/data_stereo_flow/training\""


                
del_files('./')

for i in range(0, 194):
    cmd = '{0} {1} {2}'.format(bin, dir, i)
    print(cmd)
    os.system(cmd)
    

