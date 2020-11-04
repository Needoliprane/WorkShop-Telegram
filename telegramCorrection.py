import requests

def msBotGetText():
    botToken = ""
    send_text = 'https://api.telegram.org/bot' + botToken + '/getUpdates'
    response = requests.get(send_text)
    return response.json()

def msBotSendText(botMessage):
    
    botToken = ""
    botChatID = ''
    send_text = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' \
        + botChatID + '&parse_mode=Markdown&text=' + botMessage

    response = requests.get(send_text)
    return response.json()

def msDeleteMessage(msgID):

    botToken = ""
    botChatID = ''
    send_text = 'https://api.telegram.org/bot' + botToken + '/deleteMessage?' \
        'message_id=' + str(msgID) + '&chat_id=' + botChatID 

    response = requests.get(send_text)
    return response.json()

#res = msBotGetText()
#print(res)

#res = msBotSendText("lol")
#print(res)

#res = msDeleteMessage("8")
#print(res)
