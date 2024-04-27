import requests
import apptranslate as at
import GetRelativePath as grp

sourceid = ""

def ReadApi():
    with open(grp.resource_path("db\\key\\api.txt"), 'r') as file:
        api = file.read()
    return api

def GetAnswer(question, file_path):
    lang = at.langDetect(question)
    if lang != "en":
        question = at.TranslateIt(question, "en")
    
    global sourceid
    print("path :: " + file_path)
    files = [   
    ('file', ('file', open(file_path,'rb'), 'application/octet-stream'))
]
    headers = { 
    'x-api-key': ReadApi(),
}

    response1 = requests.post(  
    'https://api.chatpdf.com/v1/sources/add-file', headers=headers, files=files)

    if response1.status_code == 200:    
        sourceid = response1.json()['sourceId']
    else:   
        print('Status:', response1.status_code)
        print('Error:', response1.text)

    data = {
        'sourceId': sourceid,
        'messages': [
            {
                'role': "user",
                'content': question,
            }
        ]
    }

    response = requests.post(
        'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)

    if response.status_code == 200:
        if lang != "en":
            return at.TranslateIt(response.json()['content'], lang)
        else:
            return response.json()['content']
    else:
        print('Status:', response.status_code)
        print('Error:', response.text)