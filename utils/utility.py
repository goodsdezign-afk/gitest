import os
import shutil
from PIL import Image # !pip install pillow
import cv2
from . import setting as set
import random


# 디렉토리 생성
def makeDir(dirs):
    os.makedirs(dirs, exist_ok=True)

# 디렉토리내  모든 파일 불러오기
def readFiles(dirs):
    files = [f for f in os.listdir(dirs) if f.lower().endswith(set.extensions)]
    return files

# 순서대로 이름변경 ex) test001.jpg -> 0001.jpg, test3455.jpg -> 0002.jpg
def changeFileName(files, src, dst):
    #이미지 정렬
    files.sort()

    for i, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]
        img_path = os.path.join(src, filename)
        if ext != '.jpg':
            img = Image.open(img_path).convert("RGB") # jpg로 바꾸는 함수
            ext = '.jpg'
            
        newname = f"{i:04}{ext}"

        src_path = os.path.join(src, filename)
        dst_path = os.path.join(dst, newname)
        #print(dst_path)
        shutil.copy2(src_path, dst_path)

# 이미지 변경하여 새로운 폴더 저장
def resizeImg(src, dst, width=500, height=500):
    # 이미지 사이즈를 500 x 500
    rsfiles = readFiles(src)

    for file in rsfiles:
        img = cv2.imread(os.path.join(dst, file))
        width, height = img.shape[:2]
        # if img is None:
        #     print('No')
        # else:
        #     print('Yes')

        resize_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(os.path.join(dst, file), resize_img)

# train test valid폴더에 images , label폴더를 생성
def createDataFolder(dirs):
    for name in dirs:
        train_path = os.path.join(set.aiData_path, os.path.join(name, 'images/'))
        os.makedir(train_path)
        lbl_path = os.path.join(set.aiData_path, os.path.join(name, 'labels/'))
        os.makedir(lbl_path)

# train test valid폴더에 데이터 분리저장
def splitFiles(files):
    random.shuffle(files)
    total = len(files)
    num_train = int(total*set.splits['train'])
    num_test = int(total*set.splits['test'])
    num_valid = total - num_train - num_test
    files_train = []
    files_test = []
    files_valid = []
    files_train = files[:num_train]
    files_test = files[num_train:num_train+num_test]
    files_valid = files[num_train+num_test:]

    return files_train, files_test, files_valid

def copy_image_label(file_list, split_name):
    dataimg = split_name + '/images/'
    datalbl = split_name + '/labels/'
    dst_img = os.path.join(set.aiData_path, dataimg)
    dst_lbl = os.path.join(set.aiData_path, datalbl)
    #print(dst_img, dst_lbl)
    for img_file in file_list: # train 72번 test 9번 valid 9번
        shutil.copy2(os.path.join(set.img_fd, img_file), os.path.join(dst_img, img_file))
        
        #라벨 위치
        label_file = f"{os.path.splitext(img_file)[0]:04}.txt"  # name.txt -> name, .txt
        src_lbl_path = os.path.join(set.lbl_fd, label_file)
        dst_lbl_path = os.path.join(dst_lbl, label_file)

        if os.path.exists(src_lbl_path):
            shutil.copy2(src_lbl_path, dst_lbl_path)

def splitDataCopy(files, split):
    copy_image_label(files, split)
        






