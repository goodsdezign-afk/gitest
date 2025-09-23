import os
import utils.utility as util

# 사용할 디렉토리 설정
file_path = 'C:/Users/PC/Documents/dev/study/9-19/'
# 원본이미지 디렉토리 설정
src_fd = os.path.join(file_path, 'sourceImg/') 
# 새로이 만들어질 이미지 저장할 디렉토리
dst_fd = os.path.join(file_path, 'resImg/')


def main():
    # 수정된 이미지 저장할 폴더 
    util.makeDir(dst_fd)

    

if __name__ == "__main__":
    main()