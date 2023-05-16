import disnake
import asyncio
from disnake.ext import tasks, commands
from datetime import datetime
import json

msgU = {} # msgU["Dixxe"] кол-во сообщений от юзера
badU = {} # кол-во матов от юзера

msgC = {} # msgC["Основной"] кол-во сообщений в чате
badC = {} # кол-во матов в чате
                        # users[1]["Dixxe"]
users = [msgU, badU] ## [1] - кол-во сообщений [2] - кол-во матов
chats = [msgC, badC] ## [1] - кол-во сообщений [2] - кол-во матов


data = [users, chats] # для сохранки
date = {} # 'число' : data

cursewords = ["пизда", "уебище", "конч", "блять", "ебать", "залупа", "сука", "хуй", "пиздец", "еба", "ахуеть", "пидор", "бля", "сучка", "выебу", "eбал"]

global slash_inter
slash_inter = disnake.ApplicationCommandInteraction
intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents, help_command=None)


###--- function------#


#---saving sanity----#
def bad(user=None, chan=None):
    if user:
        if user.mention in badU:
            badU[f'{user.mention}'] = int(badU[f'{user.mention}']) + 1
        else: 
            badU[f'{user.mention}'] = '1'
            
    if chan:
        if str(chan.id) in badC:
            badC[f"{chan.id}"] = int(badC[f"{chan.id}"]) + 1
        else:
            badC[f"{chan.id}"] = '1'

###########

def msg(user=None, chan=None):
    if user:
        if user.mention in msgU:
            msgU[f'{user.mention}'] = int(msgU[f'{user.mention}']) + 1
        else: 
            msgU[f'{user.mention}'] = '1'
        
    if chan:
        if str(chan.id) in msgC:
            msgC[f"{chan.id}"] = int(msgC[f"{chan.id}"]) + 1
        else:
            msgC[f"{chan.id}"] = '1'
#---saving sanity----#

def ExportData(data):
    with open('data.json', 'w') as rough:
        json.dump(data, rough)

def ExportDay(date):
    with open('dayLOG.json', 'w') as log:
        json.dump(date, log)

###--- function------#

@bot.event ## works when it ready
async def on_ready():
    print(f'All systems nominal, welcome {bot.user}')
    await asyncio.gather(save.start(data), saveDATE.start(data))

@bot.slash_command(description='Показать собранную дату') ## tool for debugging values
async def debug(slash_inter):
    await slash_inter.send('Please wait...')
    await slash_inter.edit_original_response(data)
    
@bot.slash_command(description='Пожаловаться на плохое слово, выполнять с осторожностью') ## tool learning
async def rep(slash_inter, word:str, member:disnake.Member):
    await slash_inter.send('Please wait...')
    bad(member)
    cursewords.append(str(word))
    await slash_inter.edit_original_response(f"{member} has been reported using bad words")


@bot.event ## messages from users
async def on_message(message):
    try:
        msg_content = message.content.lower()
        if (message.author == bot.user): ## проверка чтобы не было цикла
            return

        #---messages---#
        elif any(word in msg_content for word in cursewords):
            bad(message.author, message.channel)
        elif (message.author != bot.user):
            msg(message.author, message.channel)
        #---messages---#

        
        await bot.process_commands(message)
    except Exception as e:
        print(e)

##--------------TASKS--------------------------##

@tasks.loop(minutes=1.0) ## цикл сохранения переменных в файл линия 180
async def save(data):
    try:
        ExportData(data)
    except Exception as error:
        print(error)

@tasks.loop(minutes=1.0) ## цикл сохранения переменных в файл линия 180
async def saveDATE(data):
    try:
        date[f"{datetime.date(datetime.now())}"] = data
        ExportDay(date)
    except Exception as err:
        print(err)
    

##-----------END_TASKS-------------------------##
bot.run('TOKEN_HERE')