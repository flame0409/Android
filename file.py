import os

concent=["Malware"]
path=r"E:\APKs"

list = []
for dir in concent:#读取所有的文件夹的内容
    new_path=path+'\\'+dir
    if (os.path.exists(new_path)):
        #print(new_path)
        files = os.listdir(new_path)
        for file in files:
            m = os.path.join(new_path, file)#获取smali文件的地址
            print (m)
            file_smalis=os.listdir(m)
            if (os.path.isdir(m)):
                h = os.path.split(m)#h【1】存储APK名字
            file_write = "E:\\Smalis"+"\\"+dir+"\\"+h[1]+".smali"
            #print  (file_write)
            write_smali = open(file_write, 'a')  # 创建总文件
            for file_smali in file_smalis:
                print(m+"\\"+file_smali)
                read_smali=open(m+"\\"+file_smali,'r')
                while True:
                    try:
                        str = read_smali.readline()
                        write_smali.write(str)
                    except(UnicodeDecodeError):
                        pass
                    if not str:
                        break
                #print (file_smali)
            #break



