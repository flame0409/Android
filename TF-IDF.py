import csv
import os

fname = "E:\\Smalis\\TF-IDF.csv"#文件地址
path_1="E:\\Smalis"#一级路径
concent=["Benign-APKs","Malware"]
header=['Name','Class','Lenth']
keys=['M','R','G','I','T','P','V']
n=2
dict={}#存放序列
dict1={}#TF-IDF
for a in range(0, 7):
    for b in range(0, 7):
        #for c in range(0, 7):
            word = keys[a] + keys[b] #+ keys[c]
            # print(a+b+c)
            if word not in dict:
                dict[word] = 0
                dict1[word] = 0
#print(dict)
with open(fname,'w',newline='') as smalifile:#打开csv文件
    ngram_write = csv.writer(smalifile,delimiter=',')#创建写对象
    for dir in concent:#读入文件夹
        path_2 = path_1 + "\\" + dir  # 二级地址
        files = os.listdir(path_2)  # 打开文件夹下的文件
        for file in files:  # 挨个打开文件夹
            path_smali = os.path.join(path_2, file)  # smali文件地址
            read_smali = open (path_smali,'r')
            print(path_smali)
            num=49#343

            #循环寻找序列
            for a in range(0, 7):
                for b in range(0, 7):
                    #for c in range(0, 7):
                        word = keys[a] + keys[b] #+ keys[c]
                        dict[word] = 0
            #print(dict)
            while True:
                line = read_smali.readline()
                for x in range(0,len(line)+1-n):
                    sequence=line[x:(x+n)]
                    #print(sequence)
                    if dict[sequence]==0:
                        num=num-1
                    dict[sequence]+=1
                    x+=1
                if not line:
                    break
            #print(dict)
            dict_1 = sorted(dict.items(), key=lambda x: x[1], reverse=True)  # 按键值从大到小排序
            for item in dict:
                #print(item)
                if dict[item]!=0:
                    dict1[item]+=1;
            #print(dict1)
    for item in dict1:
        flame = []
        flame.append(item)
        flame.append(dict1[item])
        ngram_write.writerow(flame)



            #write_row.append(num)#添加数量
            #print(len(dict))
            #print(num)
            #ngram_write.writerow(write_row)


