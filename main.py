#/usr/bin/python3

import os

# 使う前に delete を true にしてください
delete = false

path = "./"

def x_file(file):
    textures = []
    path = file[0:file.rfind("/")+1]
    with open(file, encoding='shift_jis') as f:
        for line in f:
            if ((line.endswith('.png";\n')) or (line.endswith('.dds";\n'))):
                s = line.find('"')
                e = line.rfind('"')
                textures.append(path+line[s+1:e])
    return textures

def folder(path):
    textures = {}
    for i in os.listdir(path):
        target = path+"/"+i
        if (os.path.isfile(target)):
            if (target.endswith(".x")):
                for tex in x_file(target):
                    textures[tex] = 1
            elif ((target.endswith(".png")) or (target.endswith(".dds"))):
                textures.setdefault(target, 0)

        elif (os.path.isdir(target)):
            folder(target)
        else:
            print("[EER]"+target)

    for key in textures:
        val = textures.get(key, -1)
        if (val == 0):
            if (delete == true):
                os.remove(key)
                print("[DEL]"+key)
                # print(key + ":" + str(val))

    return 0

folder(path)
