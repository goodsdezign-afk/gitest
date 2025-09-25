import os
import utils.utility as util
import utils.setting as set

def main():
   for name in ['train/', 'test/']:
       file_name = []
       dfire_lbl_path = os.path.join(set.dfire_path, os.path.join(name, 'labels/'))

       files = util.readFiles(dfire_lbl_path, 'txt') #img이면 'img'

       for file in files:
           file_path =os.path.join(dfire_lbl_path,file)
           with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read().strip()
                if len(content) > 0:
                   file_name.append(file)
        
       #print(file_name)

       # 학습데이터 저장될 root 디렉토리
       root_dir = os.path.join(set.dfire_path, 'delNullfire/')
       util.makeDir(root_dir)
   
       img_path = os.path.join(root_dir, os.path.join(name, 'images/'))
       util.makeDir(img_path)
       lbl_path = os.path.join(root_dir, os.path.join(name, 'labels/'))
       util.makeDir(lbl_path)

       util.nullLabelDelete(file_name, name)
       
    
if __name__ == "__main__":
    main()