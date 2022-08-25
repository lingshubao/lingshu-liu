import os

path = r"C:/Users/liudeao\pythonProject/new_image_mask1/test/mask"
filelist = os.listdir(path)
count = 1
# for file in filelist:
#     print(file)
for file in filelist:
    Olddir = os.path.join(path, file)
    if os.path.isdir(Olddir):
        continue
    filename = os.path.splitext(file)[0]
    filetype = os.path.splitext(file)[1]
    Newdir = os.path.join(path, str(count).zfill(4) + filetype)
    os.rename(Olddir, Newdir)
    print(Newdir)

    count += 1