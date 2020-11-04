import requests

def msBotGetText():
    botToken = '953431250:AAHyzR1UjS9zNPF7z2bMMO6lMG4EVu4aPiI'
    send_text = 'https://api.telegram.org/bot' + botToken + '/getUpdates'
    response = requests.get(send_text)
    return response.json()

def msBotSendtext(status, ms, funct, details):
    
    botToken = '953431250:AAHyzR1UjS9zNPF7z2bMMO6lMG4EVu4aPiI'
    botChatID = '-327175258'
    botMessage = status + ' - ' + ms + ' => ' + funct + ' ====> ' + details
    send_text = 'https://api.telegram.org/bot' + botToken + '/sendMessage?chat_id=' + botChatID + '&parse_mode=Markdown&text=' + botMessage

    response = requests.get(send_text)
    return response.json()

#res = msBotGetText()
#print(res)

def msBot_send_msg(status, ms, funct, details):
    res = msBotSendtext(status, ms, funct, details)


