import datetime
from database import *
import time
from vkwave.bots import SimpleLongPollBot, SimpleBotEvent
TOKEN = "f416d70bbbde0e16e75a18fea1a4f45d37f0c1303756c2d2e558dba8f2bd851bcc238cffc789148f06be2"
GROUP_ID = 207042058

#-------------
para1_m = sql.execute(f'SELECT para1 FROM Monday').fetchone()[0]
para2_m = sql.execute(f'SELECT para2 FROM Monday').fetchone()[0]
para3_m = sql.execute(f'SELECT para3 FROM Monday').fetchone()[0]
para4_m = sql.execute(f'SELECT para4 FROM Monday').fetchone()[0]
para5_m = sql.execute(f'SELECT para5 FROM Monday').fetchone()[0]
para6_m = sql.execute(f'SELECT para6 FROM Monday').fetchone()[0]
para1_tu = sql.execute(f'SELECT para1 FROM Tuesday').fetchone()[0]
para2_tu = sql.execute(f'SELECT para2 FROM Tuesday').fetchone()[0]
para3_tu = sql.execute(f'SELECT para3 FROM Tuesday').fetchone()[0]
para4_tu = sql.execute(f'SELECT para4 FROM Tuesday').fetchone()[0]
para5_tu = sql.execute(f'SELECT para5 FROM Tuesday').fetchone()[0]
para6_tu = sql.execute(f'SELECT para6 FROM Tuesday').fetchone()[0]
para1_we = sql.execute(f'SELECT para1 FROM Wednesday').fetchone()[0]
para2_we = sql.execute(f'SELECT para2 FROM Wednesday').fetchone()[0]
para3_we = sql.execute(f'SELECT para3 FROM Wednesday').fetchone()[0]
para4_we = sql.execute(f'SELECT para4 FROM Wednesday').fetchone()[0]
para5_we = sql.execute(f'SELECT para5 FROM Wednesday').fetchone()[0]
para6_we = sql.execute(f'SELECT para6 FROM Wednesday').fetchone()[0]
para1_th = sql.execute(f'SELECT para1 FROM Thursday').fetchone()[0]
para2_th = sql.execute(f'SELECT para2 FROM Thursday').fetchone()[0]
para3_th = sql.execute(f'SELECT para3 FROM Thursday').fetchone()[0]
para4_th = sql.execute(f'SELECT para4 FROM Thursday').fetchone()[0]
para5_th = sql.execute(f'SELECT para5 FROM Thursday').fetchone()[0]
para6_th = sql.execute(f'SELECT para6 FROM Thursday').fetchone()[0]
para1_fr = sql.execute(f'SELECT para1 FROM Friday').fetchone()[0]
para2_fr = sql.execute(f'SELECT para2 FROM Friday').fetchone()[0]
para3_fr = sql.execute(f'SELECT para3 FROM Friday').fetchone()[0]
para4_fr = sql.execute(f'SELECT para4 FROM Friday').fetchone()[0]
para5_fr = sql.execute(f'SELECT para5 FROM Friday').fetchone()[0]
para6_fr = sql.execute(f'SELECT para6 FROM Friday').fetchone()[0]

para_time = ["8:00:00", "9:50:00", "11:30:00", "13:20:00", "15:00:00", "16:40:00"]

#-------------
monday = ("Понедельник:\n"
			"1: " + para1_m + "\n" +
			"2: " + para2_m + "\n" +
			"3: " + para3_m + "\n" +
			"4: " + para4_m + "\n" +
			"5: " + para5_m + "\n" +
			"6: " + para6_m + "\n" + "\n")

thusday = ("Вторник:\n"
			"1: " + para1_tu + "\n" +
			"2: " + para2_tu + "\n" +
			"3: " + para3_tu + "\n" +
			"4: " + para4_tu + "\n" +
			"5: " + para5_tu + "\n" +
			"6: " + para6_tu + "\n" + "\n")

Wednesday = ("Среда:\n"
			"1: " + para1_we + "\n" +
			"2: " + para2_we + "\n" +
			"3: " + para3_we + "\n" +
			"4: " + para4_we + "\n" +
			"5: " + para5_we + "\n" +
			"6: " + para6_we + "\n" + "\n")

Thersday = ("Четверг:\n"
			"1: " + para1_th + "\n" +
			"2: " + para2_th + "\n" +
			"3: " + para3_th + "\n" +
			"4: " + para4_th + "\n" +
			"5: " + para5_th + "\n" +
			"6: " + para6_th + "\n" + "\n")

Friday = ("Пятница:\n"
			"1: " + para1_fr + "\n" +
			"2: " + para2_fr + "\n" +
			"3: " + para3_fr + "\n" +
			"4: " + para4_fr + "\n" +
			"5: " + para5_fr + "\n" +
			"6: " + para6_fr + "\n" + "\n")

bot = SimpleLongPollBot(tokens=TOKEN, group_id=GROUP_ID)

@bot.message_handler(bot.command_filter(commands="рассписание", prefixes="+"))
async def echo(event: SimpleBotEvent) -> str:

	await event.answer(monday + thusday + Wednesday + Thersday + Friday)
@bot.message_handler(bot.command_filter(commands="сегодня", prefixes="+"))
async def echo(event: bot.SimpleBotEvent) -> str:
	datenow = datetime.datetime.now().weekday()
	if datenow == 0:
		await event.answer(monday)
	elif datenow == 1:
		await event.answer(thusday)
	elif datenow == 2:
		await event.answer(Wednesday)
	elif datenow == 3:
		await event.answer(Thersday)
	elif datenow == 4:
		await event.answer(Friday)
	else:
		await event.answer("Сегодня нет пар")

@bot.message_handler(bot.command_filter(commands="звонки", prefixes="+"))
async def echo(event: bot.SimpleBotEvent) -> str:
	await event.answer("Рассписание звонков: \n 1 пара 8:00-9:30\n2 пара 9:50-11:20\n3 пара 11:30-13:00\n4 пара 13:20:14:50\n5 пара 15:00-16:30\n6 пара 16:40 -18:10")
@bot.message_handler(bot.command_filter(commands="команды", prefixes="+"))
async def echo(event: bot.SimpleBotEvent) -> str:
	await event.answer("Списко команд: \n 1: +рассписание(сбрасываю рассписание на всю неделю) \n 2: +сегодня(Кидаю сегодняшнее расписание) \n 3: +звонки(Кидаю список звонков на пары)")

bot.run_forever()





