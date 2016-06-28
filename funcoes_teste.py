#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import commands           #lib commands não está mais sendo usada, usar subprocess 
import os
from telebot import types
from datetime import date
import random
import glob
import feedparser

erros = ['100','101','200','201','202','204','206','207',
'300','301','302','303','304','305','307',
'400','401','402','404','403','405','406','408','409',
'410','411','412','413','414','415','416','417','418',
'422','423','424','425','426','426','431','444',
'450','451','500','502','503','506','507','508'
'509','599']


token = <token>
bot = telebot.TeleBot(token)

#mostra imagens de gatinhos representando os erros mais comuns de http :)
@bot.message_handler(commands=['erro'])
def send_cat(message):
 try:	
	if (message.text.split(' ')[1] in erros):
		url_cat='https://http.cat/'+ message.text.split(' ')[1]+'.jpg' 
		name_image=message.text.split(' ')[1]+'.jpg'
		down_image=os.system('wget -A .jpg '+url_cat)
		photo=open(name_image,'rb')
		bot.send_photo(message.chat.id,photo)
		os.system('rm '+name_image)
	else:
		bot.reply_to(message,'erro nao encontrado !')	
 except:
	 bot.reply_to(message,'usage : /erro <num error>')
    

#projeto em testes de um manual de comandos Linux
@bot.message_handler(commands=['man'])
def teste_man(message):
    if (len(message.text.split(' ')) == 2 ): 
	entrada = 'man ' + message.text.split(' ')[1]+ ' | grep -m2 '+message.text.split(' ')[1]
	bot.reply_to(message,commands.getoutput(entrada).decode('utf-8'))
    elif (message.text == '/man'):
          bot.reply_to(message,'Manual de comandos Linux, digite /man <comando>')
    else:
         bot.reply_to(message,'erro')

#projeto em testes de uma varredura usando o nmap
@bot.message_handler(commands=['nmap'])
def send_nmap(message):
 try:	
		url_read = message.text.split(' ')[1] 
		search_nmap = 'nmap '+url_read
		bot.reply_to(message,'scanning...')
		format_out = commands.getoutput(search_nmap)
		bot.send_message(message.chat.id,format_out,disable_web_page_preview=True)	
 except:
	 bot.reply_to(message,'erro')


bot.polling()
