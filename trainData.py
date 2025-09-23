import os
import utils.utility as util
import utils.setting as set

def main():
    # 학습데이터 저장될 root 디렉토리
    util.makeDir(set.aiData_path)

    # 학습데이터 원 이미지 로드
    orgFiles = util.readFiles(set.img_fd) # 원본이미지를 전체 읽어옴

    # 학습데이터 분리
    train, test, valid = util.splitFiles(orgFiles)
    
    util.splitDataCopy(train, 'train')
    util.splitDataCopy(test, 'test')
    util.splitDataCopy(valid, 'valid')
    
if __name__ == "__main__":
    main()