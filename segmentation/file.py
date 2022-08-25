import cv2
from PIL import Image
import shutil

train_list = list(train_df['new_imagejpg'])
test_list = list(test_df['new_imagejpg'])
# train_mask_dir = os.path.join('D:/jupyter notebook/new_image_mask','train_dir','mask')
# train_ori_dir = os.path.join('D:/jupyter notebook/new_image_mask','train_dir','ori')
# test_mask_dir = os.path.join('D:/jupyter notebook/new_image_mask','test_dir','mask')
# test_ori_dir = os.path.join('D:/jupyter notebook/new_image_mask','test_dir','ori')
# os.mkdir(train_mask_dir)
# os.mkdir(train_ori_dir)
# os.mkdir(test_mask_dir)
# os.mkdir(test_ori_dir)
train_mask_dir = r'D:/jupyter notebook/new_image_mask/train_dir/mask'
train_ori_dir = r'D:/jupyter notebook/new_image_mask/train_dir/ori'
test_mask_dir = r'D:/jupyter notebook/new_image_mask/test_dir/mask'
test_ori_dir = r'D:/jupyter notebook/new_image_mask/test_dir/ori'

filePath = 'D:\jupyter notebook\skin_images'
# maskfilePath= 'D:\jupyter notebook\skin-leison\segmentation-masks\segmentation_masks'
maskfilePath = r'D:\jupyter notebook\mask-image\train_dir\mask_'
filelist = os.listdir(filePath)
maskfilelist = os.listdir(maskfilePath)
for image in train_list:
    if image in filelist:
        file_name = image
        #         print(file_name)
        maskname = data3.loc[lambda data: data["new_imagejpg"] == file_name, "drawn_area"]
        #         print(maskname)
        maskname1 = list(maskname)[0]
        #         print(maskname)
        if maskname1 in maskfilelist:
            ori = os.path.join(r'D:\jupyter notebook\skin_images_mask', file_name)
            mask = os.path.join(r'D:\jupyter notebook\skin-leison\segmentation-masks\segmentation_masks', maskname1)
            train_mask_dir1 = os.path.join(train_mask_dir, file_name)
            shutil.copy(ori, train_ori_dir)
            shutil.copy(mask, train_mask_dir1)
#             im_ori = Image.open(ori)
#             im_mask = Image.open(mask)
#             save_ori_path = os.path.join(train_ori_dir,filename)
#             save_mask_path = os.path.join(train_mask_dir,maskname1)
#             im_mask.save(save_mask_path)
#             im_ori.save(save_ori_path)

#             print(p1.shape,p2.shape)
for image in test_list:
    if image in filelist:
        file_name = image
        #         print(file_name)
        maskname = data3.loc[lambda data: data["new_imagejpg"] == file_name, "drawn_area"]
        #         print(maskname)
        maskname1 = list(maskname)[0]
        #         print(maskname)
        if maskname1 in maskfilelist:
            ori = os.path.join(r'D:\jupyter notebook\skin_images_mask', file_name)
            mask = os.path.join(r''
            D:\jupyter
            notebook\skin - leison\segmentation - masks\segmentation_masks
            ' , maskname1)
            test_mask_dir1 = os.path.join(test_mask_dir, file_name)
            shutil.copy(ori, test_ori_dir)
            shutil.copy(mask, test_mask_dir1)