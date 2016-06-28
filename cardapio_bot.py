#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
from datetime import date
from telebot import types


token = <token>
bot = telebot.TeleBot(token)

markup = types.ReplyKeyboardMarkup(row_width=2)
item1 = types.KeyboardButton('segunda')
item2 = types.KeyboardButton('terca')
item3 = types.KeyboardButton('quarta')
item4 = types.KeyboardButton('quinta')
item5 = types.KeyboardButton('sexta')
markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
markup.add(item1,item2,item3,item4,item5)

dia = ['segunda','terca','quarta','quinta','sexta']
comandos = ['/ajuda','/funcionamento','/sugestao']
data = str(date.today()).split('-')[2]

comandos_textos = {
    
                
    comandos[0]:
		u'Informações:\n'
        u'O Restaurante Universitário, sob a coordenação da Pró-Reitoria de Assuntos Estudantis,\n' 
        u'é uma unidade destinada a oferecer refeições de qualidade a estudantes,\n' 
        u'docentes e servidores técnico-administrativos da UFC,\n' 
        u'além de constituir um espaço de convivência e integração da comunidade universitária.\n',     
    
    comandos[1]:
        u'Olá @{nome}, esse é o Horário de Funcionamento e o Valor:\n'
	u'\n'
        u'Almoço: das 11h às 14h\n'
        u'Jantar:  das 17h30min às 19h30min\n'
        u'\n'
        u'Valor:\n'
        u'Estudante: R$ 1,10\n'
        u'Servidor técnico–administrativo: R$ 1,60\n'
        u'Docente: R$ 2,20\n',
        
    comandos[2]:
		 u'Olá, @{nome} estamos abertos a sugestões de melhorias:\n'
		 u'mais informações falar com @tux_pilgrim\n',   

}
	
textos = {

  dia[0]:
	    u'🍴 Olá,@{nome} o cardapio de {dia} é :\n'
        u'\n'
        u'Cardápio referente a semana do dia {day} do mês {month}\n'
        u'Almoço:\n' 
        
        u'\n'
        u'Jantar:\n'
        
        u'\n',
  
  dia[1]:
	    u'🍴 Olá,@{nome} o cardapio de {dia} é:\n'
        u'\n'
        u'Cardápio referente a semana do dia {day} do mês {month}\n'
        u'Almoço:\n'
        u'\n'
        u'Jantar:\n'

        u'\n',
  dia[2]:
	    u'🍴 Olá,@{nome} o cardapio de {dia} é:\n'
        u'\n'
        u'Cardápio referente a semana do dia {day} do mês {month}\n'
        u'Almoço:\n
        u'\n'
        u'Jantar:\n'
        u'\n',     
  
  dia[3]:
	    u'🍴 Olá,@{nome} o cardapio de {dia} é:\n'
        u'\n'
        u'Cardapio referente a semana do dia {day} do mês {month}\n'
        u'Almoço:\n'
       
        u'\n'
        u'Jantar:\n'
        
        u'\n',
  
  dia[4]:
	    u'🍴 Olá,@{nome} o cardapio de {dia} é:\n'
        u'\n'
        u'Cardápio referente a semana do dia {day} do mes {month}\n'
        u'Almoço:\n'

        u'\n'
        u'Jantar:\n'

        u'\n',

}

@bot.message_handler(commands=['start','help'])
def send_inicio(message):
        ids(message.text,message.chat.id,message.from_user.username)
	bot.reply_to(message,'''Bem vindo ao R.U UFC-Sobral Bot
comandos disponíveis:
/cardapio        cardápio do dia solicitado
/ajuda          informações acerca do R.U
/funcionamento  informações sobre horários de funcionamento e valores
/sugestao       contato para sugestões       
''')


@bot.message_handler(commands=['cardapio'])
def enviar(message):
    bot.send_message(message.chat.id, "escolha o dia :", reply_markup=markup)
    bot.register_next_step_handler(message, send_cardapio)

def send_cardapio(message):
	if (message.text in comandos_textos):
		bot.reply_to(message,comandos_textos[message.text].format(nome=message.from_user.username))
	elif (message.text.lower() in dia):
		bot.reply_to(message,textos[message.text.lower()].format(nome=message.from_user.username,dia=message.text.lower(),day=str(date.today()).split('-')[2],month=str(date.today()).split('-')[1]))
	else:
		bot.reply_to(message,'erro')
	
@bot.message_handler(commands=['ajuda'])
def send_ajuda(message):
    if (message.text in comandos_textos):
		bot.reply_to(message,comandos_textos[message.text].format(nome=message.from_user.username))

@bot.message_handler(commands=['funcionamento'])
def send_horario(message):
    if (message.text in comandos_textos):
		bot.reply_to(message,comandos_textos[message.text].format(nome=message.from_user.username))

@bot.message_handler(commands=['sugestao'])
def send_ajuda(message):
    if (message.text in comandos_textos):
		bot.reply_to(message,comandos_textos[message.text].format(nome=message.from_user.username))
'''
@bot.message_handler(commands=['admin'])
def send_admin(message):
	if (str(message.chat.id) == ''):
		bot.reply_to(message,'Bem Vindo @{}, ultima semana {}'.format(message.from_user.username,data))
	else:
		bot.reply_to(message,'Usuario Sem Permissao !')	
'''
bot.polling()
