import io

file=open('E:\\123.txt','r')
file_input=open("E:\\opcode.txt",'w')

key_word=['move','check','instance','array','invoke','return',
          'goto','switch','if-','aget','put']
while True:
    line=file.readline()
    for x in key_word:
        jug=line.find(x)
        if jug==-1:
            continue
        else:
            line_input=line
            file_input.write(line_input)
    if not line:
        break