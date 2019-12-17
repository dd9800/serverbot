import asyncio
import discord
import random
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(status=discord.Status.online, activity=discord.Game("서버관리"))
 
@client.event
async def on_message(message):
 if message.author == client.user:
    return

 if message.content.startswith("!채널메세지"):
     channel = message.content[7:25]
     msg = message.content[26:]
     await client.get_channel(int(channel)).send(msg)

 if message.content.startswith("!경고"):
     author = message.guild.get_member(int(message.content[4:22]))
     file = openpyxl.load_workbook("경고.xlsx")
     sheet = file.active
     i = 1
     while True:
         if sheet["A" + str(i)].value == str(author.id):
             sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
             file.save("경고.xlsx")
             if sheet["B" + str(i)].value == 7:
                 await message.guild.ban(author)
                 await client.get_channel(650727934910398474).send("경고 7회 누적입니다. 서버에서 추방합니다.")
             else:
                 await client.get_channel(650727934910398474).send("경고를 1회 받았습니다.")
             break
         if sheet["A" + str(i)].value == None:
             sheet["A" + str(i)].value = str(author.id)
             sheet["B" + str(i)].value =1
             file.save("경고.xlsx")
             await client.get_channel(650727934910398474).send("경고를 1회 받았습니다.")
             break
         i += 1

 elif message.content.startswith("!쀽"):
     author = message.guild.get_member(message.content[3:21])
     file = openpyxl.load_workbook("경고.xlsx")
     sheet = file.active
     i=1
     while True:
         if sheet["A" + str(i)].value == str(author.id):
             sheet["B" + str(i)].value = 0
             file.save("경고.xlsx")
             await client.get_channel(650727934910398474).send("경고초기화 완료")
             break
         i += 1


 
client.run('NjU2NDU4ODE1NTQxMzQ2MzU1.Xfi-Zw.TKQKm1-h2Cg8sVZoGtloWl0IQes')