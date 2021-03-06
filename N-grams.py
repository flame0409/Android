import csv
import os
import pandas as pd
import math

data=csv.reader(open("E:\\Smalis\\TF-IDF.csv"))
dict1={}
for row in data:
    dict1[row[0]]=int(row[1])
    #print(dict1[row[0]])

fname = "E:\\Smalis\\N-gram.csv"#文件地址
path_1="E:\\Smalis"#一级路径
concent=["Benign-APKs","Malware"]
#,
header=['Name','Class','Lenth']
keys=['M','R','G','I','T','P','V']
n=2
for x in range (0,7*7):#csv头部信息
    header.append("Sequence_"+str(x))
    header.append("Ratio_"+str(x))
    header.append("TF-IDF_"+str(x))
print(header)

with open(fname,'w',newline='') as smalifile:#打开csv文件
    ngram_write = csv.writer(smalifile,delimiter=',')#创建写对象
    ngram_write.writerow(header)#写入首行
   # print(header)
    for dir in concent:#读入文件夹
        path_2 = path_1 + "\\" + dir  # 二级地址
        files = os.listdir(path_2)  # 打开文件夹下的文件
        for file in files:  # 挨个打开文件夹
            no=1
            dict={}#存放序列
            path_smali = os.path.join(path_2, file)  # smali文件地址
            read_smali = open (path_smali,'r')
            print(path_smali)
            num = 1
            write_row=[file,dir]
            for a in range(0, 7):
                for b in range(0, 7):
                    #for c in range(0, 7):
                        word = keys[a] + keys[b]#+ keys[c]
                        #print(a+b+c)
                        dict[word] = 0
                            #dict1[word] = 0

            #循环寻找序列
            while True:
                line = read_smali.readline()
               #print(line)
                for x in range(0,len(line)+1-n):
                    sequence=line[x:(x+n)]
                    #print(sequence)
                    if sequence in dict.keys():
                        dict[sequence]+=1
                    x+=1
                    num+=1#序列个数
                if not line:
                    break
            dict_1 = sorted(dict.items(), key=lambda x: x[1], reverse=True)#按键值从大到小排序
            write_row.append(num)#添加数量
            #print(len(dict))
            #print(num)
            y = 1
            for x in dict_1:
                write_row.append(x[0])
                str=x[0]
                write_row.append(x[1]/num)#添加词频TF
                IDF=math.log2(1491/(dict1[x[0]]+1))
                TF_IDF=(x[1]/num)*IDF
                write_row.append(TF_IDF)
            ngram_write.writerow(write_row)
        no+=1
