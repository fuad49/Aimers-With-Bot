def saveit(name, text,path):
    with open(f'{path}\{name}.txt', 'w',encoding='utf-8') as finalString:
        finalString.write(text)