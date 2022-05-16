def text():
    union = ['но','и','а'] # Сюда можно потом добавить ещё союзы
    str1 = ''
    str2 = list()
    with open('file.txt',encoding="utf-8") as f:
        words = f.read().strip().lower().replace(',','').replace('.','').split()

    dict1 = {}
    for w in words:
        if w not in union:
            dict1[w] = dict1.get(w, 0) + 1
    
    print('Введите некоторое число слов через запятую')
    str1 = str(input()).split(",")
    print('Вводите по одному слову, для окончания процесса впишите слово stop')
    while True:
        line = input()
        if line == 'stop':
            break
        else:
            str2.append(line)
    
    with open('file_write.txt','w', encoding="utf-8") as f:
        f.write(str(len(str1)))
        f.write('\n')
        f.write(str(len(str2)))
    
    return max(dict1, key=dict1.get)

print(text())