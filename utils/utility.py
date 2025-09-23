import os
import shutil
from PIL import Image # !pip install pillow

#확장자 : 원본 이미지의 확장자를 추가해줘라
extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.avif')

# 디렉토리 생성
def makeDir(dirs):
    os.makedirs(dirs, exist_ok=True)

# 디렉토리내  모든 파일 불러오기
def readFiles(dirs):
    files = [f for f in os.listdir(dirs) if f.lower().endswith(extensions)]
    return files

# 순서대로 이름변경 ex) test001.jpg -> 0001.jpg, test3455.jpg -> 0002.jpg
def changeFileName(files, src, dst):

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



