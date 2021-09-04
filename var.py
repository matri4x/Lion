import requests
import telebot

from time import sleep
bot = telebot.TeleBot('1966791175:AAFm_pe4KwlgTcnU85Hz2Fls-dN51q91Lwk')
@bot.message_handler(commands=['start'])
def start(message):
    first = message.from_user.first_name
    bot.send_message(message.chat.id, text=f"*Hi {first} , Send Your Number Like : +964771********",parse_mode="markdown")
@bot.message_handler(func=lambda m: True)
def Get(message):
    try:
        msg = message.text
        code =  message.text
        cod = code
        bot.send_message(message.chat.id, text="Wait ..")
        phone = msg
        userr  = ""
        #trakos
        passs  = ""
        for x in range(0,3):
        	userr_char = random.choice(chars)
        	userr      = userr + userr_char#trakos
        	for i in range(0,8):
        		passs_char = random.choice(chars)
        		passs      = passs + passs_char   
        		paas   = passs
        		user   = (f'trprogram{userr}')
        		name   = 'By @ttrakos'
        		url1   = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
        		url2   = 'https://www.instagram.com/accounts/send_signup_sms_code_ajax/'
        		url3   = 'https://www.instagram.com/accounts/web_create_ajax/'
        headers = {
            'HOST': "www.instagram.com",
            'KeepAlive' : 'True',#trakos
            'user-agent' : generate_user_agent(),
            'Cookie': cookie,
            'Accept' : "*/*",
            'ContentType' : "application/x-www-form-urlencoded",
            "X-Requested-With" : "XMLHttpRequest",
            "X-IG-App-ID": "936619743392459",
            "X-Instagram-AJAX" : "missing",
            "X-CSRFToken" : "missing",
            "Accept-Language" : "en-US,en;q=0.9"
        }
        data1   = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(paas),
            'phone_number': phone,
            'username': user,
            'first_name': name,
            'month': '1',
            'day': '1',
            'year': '1999',
            'client_id': idd,
            'seamless_login_enabled': '1',
            'opt_into_one_tap': 'fals'
        }
        data2   = {
            'client_id': idd,
            'phone_number': phone,
            'phone_id': '',
           }
        bot.send_message(message.chat.id,'Add Code')
        data3 = {
            'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(paas),
            'phone_number': phone,
            'username': user,
            'first_name': name,
            'month': '1',#trakos
            'day': '1',
            'year': '1999',
            'sms_code': cod,
            'client_id': idd,
            'seamless_login_enabled': '1',
            'tos_version': 'row'
        }
        Make_Acc1 = r.post(url1,headers=head,data=data1)
        Make_Acc2 = r.post(url2,headers=head,data=data2)
        if 'Looks like your phone number may be incorrect.' in Make_Acc2.text:
        	bot.send_message(message.chat.id,'Your Number Error')
        	exit()
        elif 'Please wait a few minutes before you try again.' in Make_Acc2.text:
            bot.send_message(message.chat.id,'Wait To Send Code')
            exit()
        elif 'true' in Make_Acc2.text:
        	bot.send_message(message.chat.id,'Done Send Sms')
        	print(G+'[-]  Done Send Message ')
        	pass
        elif 'true' in Make_Acc3.text:
        	bot.send_message(message.chat.id,f'Done Create Account :\nUser : {user}\nPass : {paas}\nBy : @trprogram')
    except:
        pass#trakos
bot.polling(True)
