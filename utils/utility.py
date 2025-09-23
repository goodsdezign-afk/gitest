import os
#확장자 : 원본 이미지의 확장자를 추가해줘라
extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.avif')

def makeDir(dirs):
    os.makedirs(dirs, exist_ok=True)

def readFiles(dirs):
    files = [f for f in os.listdir(dirs) if f.lower().endswith(extensions)]
    return files