import os
import utils.utility as util
import utils.setting as set

def main():
    # 이름을 정렬하여 숫자증감으로 이름바꾸고 수정된 이미지 저장할 폴더 
    util.makeDir(set.dst_fd)
    orgFiles = util.readFiles(set.src_fd) # 원본이미지를 전체 읽어옴
   
    # 이름을 정렬하여 순서대로 이름변경
    util.changeFileName(orgFiles, set.src_fd, set.dst_fd)

    # 이미지를 일정한 크기로 변경하여 저장할 디렉토리 생성
    resize_fd = os.path.join(set.file_path, 'rszImg/')
    util.makeDir(resize_fd)

    # 이미지를 일정한 크기로 변경하여 저장할 디렉토리 저장
    util.resizeImg(set.dst_fd, resize_fd, 300, 300)

if __name__ == "__main__":
    main()