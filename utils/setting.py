import os
#확장자 : 원본 이미지의 확장자를 추가해줘라
extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.avif')

# 사용할 디렉토리 설정
file_path = 'C:/Users/PC/Documents/dev/study/9-19/'
# 원본이미지 디렉토리 설정
src_fd = os.path.join(file_path, 'sourceImg/') 
# 새로이 만들어질 이미지 저장할 디렉토리
dst_fd = os.path.join(file_path, 'resImg/')

# 원본이미지 디렉토리 설정
img_fd = os.path.join(file_path, 'rszImg/') 

# label 디렉토리
lbl_fd = os.path.join(file_path, 'label/')

# 분리하려는 이름 train, test, valid
splits = {
    'train':0.8,
    'test':0.1,
    'valid':0.1
}

data_dir = ['train/', 'test/','valid/']

aiData_path = os.path.join(file_path, 'wildfireData_1/')







