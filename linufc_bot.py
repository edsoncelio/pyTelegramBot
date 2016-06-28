!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot
import os
import commands
import subprocess

token = <token>
bot = telebot.TeleBot(token)
grupos_liberados = [<id>]

 		 
opt = ['/link', '/sobre','/distro','/eventos','/sites','/nova','/apostilas','/comandos']
dist = ['fedora','mint','arch','ubuntu','elementary','redhat','debian']
cmdsList = ''
for s in opt:
    cmdsList += '[+] '+s+'\n'

distlista = ''
for i in dist:
   distlista+= '[+] '+i+'\n'

msg = {
	
	dist[0]: #fedora
        u'Olá, senhor usuário do Fedora, temos os seguintes\n'
        u'materiais pra você,fique a vontade :\n'
        u'https://www.dropbox.com/sh/tauohoepem3naed/AABRlTTYiB4XnaKjYosQCdb6a?dl=0',
    
    dist[1]: #mint
        u'Olá, senhor usuário do Mint, temos os seguintes\n'
        u'materiais pra você,fique a vontade :\n'
        u'https://www.dropbox.com/sh/yr0a21dfxle13xy/AAAkJdLezgUa7m4s8r_4dZXQa?dl=0', 
    
   dist[2]: #arch
        u'Olá, senhor usuário do Arch, temos os seguintes\n'
        u'materiais pra você,fique a vontade :\n'
        u'https://www.dropbox.com/sh/5c1qu3s98ladhcq/AADPkSKOQCx4Oz3DvashJPy3a?dl=0',
    
   dist[3]: #ubuntu
        u'Olá, senhor usuário do Ubuntu, temos os seguintes\n'
        u'materiais pra você,fique a vontade \n'  
        u'https://www.dropbox.com/sh/vg034222mel05x5/AABrTu70Qa8vcvKhfysmQY0Ma?dl=0', 
        
   dist[4]: #elementary
        u'Olá, senhor usuário do Elementary, temos os seguintes\n'
        u'materiais pra você,fique a vontade :\n'
        u'https://www.dropbox.com/sh/kgyc78bxqfz29ls/AACRkrXP79A6kY_IqdPLDiq-a?dl=0',
   
   dist[5]: #red hat
        u'Olá, senhor usuário do Red Hat, temos os seguintes\n'
        u'materiais pra você,fique a vontade :\n'
        u'https://www.dropbox.com/sh/0k8cqizlcetz3o7/AADJpub7wubDd0DbqVSLS6CBa?dl=0',
   
   dist[6]: #debian
        u'Olá, senhor usuário do Debian, temos os seguintes\n'
        u'materiais pra você,fique a vontade :\n'
        u'https://www.dropbox.com/sh/s3iw3izxrzl8xke/AAA74NeWl-UANJERefvmDTJia?dl=0',             
}

textos = {
    'boas vindas':
        u'Seja bem vindo {name}!\n\n'
        u'Aproveite sua estadia no abrigo dos pinguins\n' 
        u'Usa qual distribuição?\n',

    opt[0]: #link
        u'Olá, você solicitou o link do grupo?\n'
        u'Gnu/Linux UFC\n'
        u'https://telegram.me/gnulinuxufc',


    opt[1]: #Sobre
        u'🐧  Grupo de Estudos Gnu/Linux UFC-Sobral\n'
        u'\n'
        u'Olá, este grupo é voltado para entusiastas do gnu/linux e\n'
        u'aqueles que queiram conhecer sobre esse mundo incrível.\n	'
        u'Para mais informações sobre o funcionamento do bot '
        u'execute o comando /comando.'
        u'\n'
        u'Vida longa e próspera a todos e a todas 🖖🏽',
    
    opt[2]: #Distros
        u'\n'
        u'🐧 Distribuições Disponíveis:\n'
        u'\n'
        u''+distlista,


    opt[3]:
        u'Python Nordeste:\n'
        u'9 a 11 de Junho - Teresina PI\n'
        u'2016.pythonnordeste.org\n',

   
    opt[4]:#Sites
      u'Sites úteis:\n'
      u'\n'
      u'www.vivaolinux.com.br\n'
      u'\n'
      u'sempreupdate.org\n'
      u'\n'
      u'softwarelivre.org\n'
      u'\n'
      u'www.tecmint.com\n'
      u'\n'
      u'www.diolinux.com.br\n'
      u'\n'
      u'http://www.tutorialspoint.com',
   
    opt[5]:
       u'Novas Distros[testes]:\n'
       u'\n'+commands.getoutput('lynx -dump http://distrowatch.com/ | grep -m 3 05/ | cut -c 10- ').decode('utf8'),
   
    opt[6]:
       u'Apostilas e Livros [testes]\n'
       u'Linux em Geral:\n'
       u'link\n'
       u'Shell Script:\n'
       u'link\n'
       u'Diversos:\n'
       u'link',
       
     opt[7]:
       u'📜 Comandos Disponíveis📜 \n'
       u''+cmdsList  
}


def denied(mensagem):
    bot.reply_to(mensagem,'''
    Esse comando está programado para funcionar em apenas 
um grupo,mais informações, falar com @tux_pilgrim''')

@bot.message_handler(commands=['distro'])
def buscar_distro(message):
    if (str(message.chat.id) not in str(grupos_liberados)):
        denied(message)
    else:     
        if (message.text.lower() == '/distro'):
            bot.reply_to(message,textos[message.text.lower()])
        
        elif (message.text.split(' ')[1].lower() in dist):
              bot.reply_to(message,msg[message.text.split(' ')[1].lower()])
        
        else: 
		     bot.reply_to(message,'distro não encontrada, escreveu certo?') 	
		
@bot.message_handler(regexp='acordado?')
def test_message(message):
    bot.reply_to(message, "Sempre!")
'''
@bot.message_handler(regexp='bill gates')
def test_message(message):
    bot.reply_to(message, "herege, hammer of ban !")
'''        
@bot.message_handler(func=lambda m: True)
def on_command(message):
    if (str(message.chat.id) not in str(grupos_liberados)):
        denied(message)
    else:        
        if (message.text.lower() in opt): 
            bot.reply_to(message, textos[message.text.lower()])

    
        

@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    name = message.new_chat_participant.first_name
    if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
        name += u" {}".format(message.new_chat_participant.last_name)
    if hasattr(message.new_chat_participant, 'username') and message.new_chat_participant.username is not None:
        name += u" (@{})".format(message.new_chat_participant.username)
    bot.reply_to(message, textos['boas vindas'].format(name=name))


@bot.message_handler(func=lambda m: True, content_types=['left_chat_participant'])
def user_left(message):
	name = message.left_chat_participant.first_name
	if hasattr(message.left_chat_participant, 'first_name'):
		name += " {}".format(message.left_chat_participant.last_name)
	if hasattr(message.left_chat_participant, 'username') and message.left_chat_participant.username is not None:
		bot.reply_to(message, "que odin o acompanhe  {name}".format(name=name))


bot.polling()
while True: 
    pass


