import os
import utils.utility as util

# 사용할 디렉토리 설정
file_path = 'C:/Users/PC/Documents/dev/study/9-19/'
# 원본이미지 디렉토리 설정
src_fd = os.path.join(file_path, 'sourceImg/') 
# 새로이 만들어질 이미지 저장할 디렉토리
dst_fd = os.path.join(file_path, 'resImg/')


def main():
    # 이름을 정렬하여 숫자증감으로 이름바꾸고 수정된 이미지 저장할 폴더 
    util.makeDir(dst_fd)
    orgFiles = util.readFiles(src_fd) # 원본이미지를 전체 읽어옴
   
    # 이름을 정렬하여 순서대로 이름변경
    util.changeFileName(orgFiles, src_fd, dst_fd)

    # 이미지를 일정한 크기로 변경하여 저장할 디렉토리 생성
    resize_fd = os.path.join(file_path, 'rszImg/')
    util.makeDir(resize_fd)

    # 이미지를 일정한 크기로 변경하여 저장할 디렉토리 저장
    util.resizeImg(dst_fd, resize_fd, 300, 300)

if __name__ == "__main__":
    main()