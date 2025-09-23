import os
import shutil
from PIL import Image # !pip install pillow
import cv2
from . import setting as set


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



