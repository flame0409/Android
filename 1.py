import os,shutil


#file = open("E://APK/path_smalie.txt",'r')
str=".smali"

concent=["newapk"]
path_new="E:\\APKs"#新创建的
for root, dirs, files in os.walk("E:\\APK\\newapk", topdown=False):
    for name in files:
        jug=(os.path.join(root,name)).find(str)
        if(jug!=-1):
            file_path=os.path.join(root,name)
            dir_path=path_new+'\\'+file_path.split('\\',5)[2]+"\\"+file_path.split('\\',5)[3]
            isExsits=os.path.exists(dir_path)
            #print (dir_path)
            if not isExsits:
                os.makedirs(dir_path)#创建不存造的文件夹保存smali
            else:
                try:
                    shutil.move(os.path.join(root,name),dir_path)
                except (shutil.Error,OSError,IOError):
                    pass
            #print(dir_path)
            #if os.path.exists()
            print(os.path.join(root, name))

    #for name in dirs:
        #print("   "+os.path.join(root, name))