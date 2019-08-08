#coding=utf-8
import csv
import os

fname = "E:\\Smalis\smali.csv"
#fname1="E:\\Smalis\opcode.txt"
path_1="E:\\Smalis"
#path_2="E:\\Smali"#保存opcode序列的文件
concent=["Malware"]
#print (fname)
key_words=['move','return','goto','if','get',
          'put','invoke']#保留七大指令:移动、返回、跳转、判断、取数据、存数据、调用
keys=['M','R','G','I','T','P','V']
#txt_writer=open(fname1,'w')
with open(fname,'w',newline='') as smalifile:#打开文件
    smali_writer = csv.writer(smalifile,delimiter=',')
    headers=['No.','Name','Opcode','Lenth','Class']#头部的属性
    smali_writer.writerow(headers)
    x=0
    for dir in concent:
        path_2=path_1+"\\"+dir#二级地址
        #print(path_2)
        files=os.listdir(path_2)#打开文件夹下的文件
        for file in files:#挨个打开文件夹
            path_smali=os.path.join(path_2,file)#smali文件地址
            file_opcode=path_smali.split(".")[0]+".txt"
            opcode_write=open(file_opcode,'w')
            print(file_opcode)
            read_smali=open(path_smali,'r')#打开smali文件读取
            opcode = ''  # opcode序列
            while True:
                try:
                    str = read_smali.readline()#按行读取smali
                    for key_word in key_words:
                        jug = str.find(key_word)#判断是否有关键词
                        if jug == -1:
                            continue
                        else:
                            index=key_words.index(key_word)#找到k的位置
                            #print(keys[index])
                            opcode=opcode+keys[index]
                            #print(opcode)
                    #print(str)
                except(UnicodeDecodeError):
                    pass
                if not str:
                    #print(opcode)
                    x+=1
                    #write_in=[x,file,opcode,dir]
                    num=len(opcode)
                    write_in = [x, file, opcode, num, dir]
                    #smali_writer.writerow(write_in)
                    opcode_write.write(opcode)
                    #txt_writer.write(file+','+opcode+','+dir)
                    break
