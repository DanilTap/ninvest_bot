# This Python file uses the following encoding: utf-8
import discord
from discord.ext import commands
from threading import Thread
import json
import time
import random

intents = discord.Intents.default()
intents.members = True
bot = discord.ext.commands.Bot(command_prefix = "!", intents = intents)




# |------------------------------ VARIABLES ------------------------------|
# Reactions lists
farm_messages = []
tickets_messages = []

# |------------------------------ /VARIABLES -----------------------------|








# |-------------------------------- EVENTS --------------------------------|
@bot.event
async def on_ready():
	print('Bot is ready!')
	
	# Start farms
	with open('user_farms.json','r', encoding='utf-8') as f:
		farms = json.load(f)

	for i in farms:
		member = farms[i]['name']
		if farms[i]['farms'] != "none":

			life = farms[i]['life_time']
			out = farms[i]['out']
			mode = farms[i]['auto']
			channel = farms[i]['channel_id']
			print(f'{member} HAVE FARM.')
			print(f'{life} {out} {mode} {channel} \n\n')

			farmth = Thread(target=Farm, args=(member, life, out, mode))
			farmth.start()

		else:
			print(f'{member} NO FARMS')


# ---------------------- Reaction Events ----------------------|
@bot.event
async def on_raw_reaction_add(payload):
	user_id = payload.user_id
	message_id = payload.message_id

	guild = bot.get_guild(payload.guild_id)
	member = guild.get_member(user_id)

	if payload.user_id == bot.user.id:
		return


	# Buy farms
	# Farm 1
	if message_id == 886528458887401473:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 149:
				user_balance[member.name]["RUB"] -= 149
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM ЗАТЫЧКА`**')
				await channel.send(embed=embed)


			elif balance < 149:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)


	# Farm 2
	if message_id == 886528465631862905:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 249:
				user_balance[member.name]["RUB"] -= 249
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM GTX')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM GTX`**')
				await channel.send(embed=embed)

			elif balance < 249:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)

	# Farm 3
	elif message_id == 886528471159930961:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 499:
				user_balance[member.name]["RUB"] -= 499
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM RTX')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM RTX`**')
				await channel.send(embed=embed)

			elif balance < 499:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)


	# Farm 4
	elif message_id == 886528474192437278:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 749:
				user_balance[member.name]["RUB"] -= 749
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM ASIC')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM ASIC`**')
				await channel.send(embed=embed)

			elif balance < 749:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)


	# Farm 5
	elif message_id == 886528476797083668:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 999:
				user_balance[member.name]["RUB"] -= 999
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM MULTI')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM MULTI`**')
				await channel.send(embed=embed)


			elif balance < 999:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)


	# Farm 6
	elif message_id == 886528481381462076:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 999:
				user_balance[member.name]["RUB"] -= 999
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM BOOST')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM BOOST`**')
				await channel.send(embed=embed)


			elif balance < 999:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)


	# Farm 7
	elif message_id == 886528484460097546:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 1499:
				user_balance[member.name]["RUB"] -= 1499
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM TITAN')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM TITAN`**')
				await channel.send(embed=embed)

			elif balance < 1499:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)


	# Farm 8
	elif message_id == 886528488234971207:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 2499:
				user_balance[member.name]["RUB"] -= 2499
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM SERVER')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM SERVER`**')
				await channel.send(embed=embed)

			elif balance < 2499:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)


	# Farm 8
	elif message_id == 886528491078705163:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 4999:
				user_balance[member.name]["RUB"] -= 4999
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM FACTORY')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM FACTORY`**')
				await channel.send(embed=embed)

			elif balance < 4999:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)


	# Farm 9
	elif message_id == 886528493339422774:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 9999:
				user_balance[member.name]["RUB"] -= 9999
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM QUANTUM')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM QUANTUM`**')
				await channel.send(embed=embed)

			elif balance < 9999:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)

	# Farm 11
	elif message_id == 886528504068464640:
		if payload.emoji.name == "💶":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			balance = user_balance[str(member.name)]['RUB']
			if balance >= 79:
				user_balance[member.name]["RUB"] -= 79
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)


				await CreateFarmChannel(member, 'FARM ПЛАТА')

				channel = bot.get_channel(888053213750779934)
				embed = discord.Embed(color=0xff0000, title="ПОКУПКА ФЕРМЫ", description=f'**{member.name} Приобрёл ферму `FARM ПЛАТА`**')
				await channel.send(embed=embed)

			elif balance < 79:
				embed = discord.Embed(title="У вас недостаточно средств", color=0xff0000)
				await member.send(embed=embed)


	# Commands
	# Referal profile
	elif message_id == 881778673496231966:
		if payload.emoji.name == "☑️":
			with open('referal.json','r', encoding='utf-8') as f:
				ref = json.load(f)

			code = ref[str(member.name)]['code']
			invites = ref[str(member.name)]['invites']
			invited_members = ref[str(member.name)]['ivited_members']
			embed = discord.Embed(color=0x3C55FA, title="ВАШ РЕФЕРАЛЬНЫЙ ПРОФИЛЬ", description="[:arrow_right: КАК ЭТО РАБОТАЕТ?](https://discord.com/channels/880008097370865706/880024762942889994/881782385870512198)\n\n:repeat:**- Что бы подтвердить приглашение, введите комаду `!c КОД`.\nПример - `!c 6kkUEC3XA`**\n\nНиже представлена статистика вашего профиля")
			embed.add_field(name = '**ВАШ РЕФЕРАЛЬНЫЙ КОД**', value = f'`{code}`', inline = True)
			embed.add_field(name = '**RUB ЗА ПРИГЛАШЕНИЕ**', value = f'1', inline = True)
			embed.add_field(name = '**ВСЕГО ПРИГЛАШЕНО РЕФЕРАЛОВ:**', value = f'{invites}', inline = True)
			embed.add_field(name = '**ПРИГЛАШЕННЫЕ РЕФЕРАЛЫ:**', value = f'{invited_members}', inline = True)
			ref_message = await member.send(embed=embed)


	# Balance
	elif message_id == 881778669482299402:
		if payload.emoji.name == "☑️":
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			rub = user_balance[str(member.name)]['RUB']
			ntb = user_balance[str(member.name)]['NTB']

			embed = discord.Embed(color=0x3C55FA, title="ВАШ БАЛАНС", description=f':euro:** {ntb} NTB**\n:pound:** {rub} RUB**\n\n`!top` - Пополнить\n`!get` - Вывести\n🔁 - Обновить баланс.')
			embed.set_thumbnail(url="https://i.ibb.co/KyLH153/1.png")
			bal_message = await member.send(embed=embed)	
			await bal_message.add_reaction('🔁')


	# Tickets
	elif message_id == 885617916282830888:
		if payload.emoji.name == "✉️":
			with open('bot_constants.json','r', encoding='utf-8') as f:
				constants = json.load(f)

			tickets = constants['tickets']

			guild = bot.get_guild(880008097370865706)
			category = discord.utils.get(guild.categories, name="▰▰▰Тех.поддержка▰▰▰")

			channel = await guild.create_text_channel(f'ticket-{tickets}', category=category)
			moderation = guild.get_role(880357242346553374)
			support = guild.get_role(881141342959439882)
			await channel.set_permissions(guild.default_role, read_messages=False)
			await channel.set_permissions(moderation, read_messages=True, send_messages=True)
			await channel.set_permissions(support, read_messages=True, send_messages=True)
			await channel.set_permissions(member, read_messages=True, send_messages=True)

			embed = discord.Embed(color=0x00b300, title="Уважаемый Игрок, если у Вас есть проблема ,можете составить заявку на ее решение.", description=f'```\nПостарайтесь максимально подробно описать свою проблему\n```\n\n**Опишите свою проблему.\nСкоро с вами свяжутся!**\n\n**Ваша заявка№{tickets}**')
			message = await channel.send(f'{member.mention}**Добрый день, вас приветствует Техническая поддержка :dash:NEXT Invest:dash: !:tools:**\n<@881141342959439882>', embed=embed)
			await message.add_reaction('🔒')
			tickets_messages.append(message.id)


			logs = guild.get_channel(881203543313367110)
			lembed = discord.Embed(color=0x00a550)
			lembed.set_author(name=member.name, icon_url=member.avatar_url)
			lembed.add_field(name = '**Информация логах**', value = f'Ticket: Ticket-{tickets}\nДействие: Создано', inline = True)
			lembed.add_field(name = '**Панель**', value = f'Техническая поддержка', inline = True)
			await logs.send(embed=lembed)

			constants['tickets'] += 1
			with open('bot_constants.json','w') as f:
				json.dump(constants,f)


	for i in range(len(tickets_messages)):
		if int(message_id) == int(tickets_messages[i]):
			if payload.emoji.name == "🔒":
				channel = bot.get_channel(payload.channel_id)
				await channel.delete()

				with open('bot_constants.json','r', encoding='utf-8') as f:
					constants = json.load(f)

				tickets = constants['tickets']
				exits = constants['exit_tickets']
				logs = guild.get_channel(881203543313367110)
				lembed = discord.Embed(color=0xff0000)
				lembed.set_author(name=member, icon_url=member.avatar_url)
				lembed.add_field(name = '**Информация логах**', value = f'Ticket: Ticket-{tickets}\nДействие: Удален', inline = True)
				lembed.add_field(name = '**Панель**', value = f'Техническая поддержка', inline = True)
				lembed.add_field(name = '**Закрытых обращений**', value = f'{exits + 1}', inline = True)
				await logs.send(embed=lembed)

				constants['exit_tickets'] += 1
				with open('bot_constants.json','w') as f:
					json.dump(constants,f)

			else:
				print("NO Message")

	# Withdraw the mined
	for i in range(len(farm_messages)):
		print(farm_messages[i])
		if message_id == farm_messages[i]:
			if payload.emoji.name == "📤":
				with open('user_balance.json','r', encoding='utf-8') as f:
					mined = json.load(f)

				mined[str(member.name)]['NTB'] += mined[str(member.name)]['mined']
				mined[str(member.name)]['mined'] = 0
				with open('user_balance.json','w') as f:
					json.dump(mined,f)
	

# Welcome
@bot.event
async def on_member_join(member):
	guild = bot.get_guild(880008097370865706)

	if member.guild == guild:
		channel = bot.get_channel(880027455769944074)

		await channel.send(f'{member.mention}')
		embed = discord.Embed(color=0x3C55FA, title="ДОБРО ПОЖАЛОВАТЬ", description=f'ПРИВЕТСТВУЕМ НА НАШЕМ СЕРВЕРЕ **{member.guild.name}**\n\nКЛИКАЙТЕ:\n**💎 [КАК ПОЛУЧИТЬ ДЕНЬГИ?](https://discord.com/channels/880008097370865706/880024762942889994/881782363191910440)\n:white_check_mark: [У МЕНЯ ОСТАЛИСЬ ВОПРОСЫ](https://discord.com/channels/880008097370865706/880023125062995969/881783726164545566)\n:ng: [НАВИГАЦИЯ](https://discord.com/channels/880008097370865706/880023035262959636/881904501685092382)\n:loud_sound: [НАЧАТЬ ОБЩАТЬСЯ И ЗАРАБАТЫВАТЬ](https://discord.gg/kUYtg9RJjw)**\n\n НАШИ МАГАЗИНЫ:\n**:postbox: [КУПИТЬ МАЙНИНГ ФЕРМУ](https://discord.com/channels/880008097370865706/880025073963122718/886528504068464640)\n:house: [КУПИТЬ НЕДВИЖИМОСТЬ](https://discord.com/channels/880008097370865706/880026116004388894)\n:arrow_double_up: [КУПИТЬ УЛУЧШЕНИЯ](https://discord.com/channels/880008097370865706/880025182343946260)\n:toolbox: [ОТКРЫТЬ КЕЙСЫ](https://discord.com/channels/880008097370865706/880026116004388895)**\n\nПРИГЛАШАЙТЕ ДРУЗЕЙ, ПРОВОДИТЕ ВРЕМЯ И УЧАВСТВУЙТЕ В РОЗЫГРЫШАХ ЗАРАБАТЫВАЯ ДЕНЬГИ ВМЕСТЕ!')
		embed.set_thumbnail(url="https://i.ibb.co/Z2pKbMX/Comp-4-15.gif")
		await channel.send(embed = embed)

		log_channel = bot.get_channel(888053213750779934)
		embed1 = discord.Embed(color=0x008000, title="ПРИСОЕДИНЕНИЕ ПОЛЬЗОВАТЕЛЯ", description=f'**К серверу присоединился `{member}`, его профиль записан в БД.**')
		await log_channel.send(embed=embed1)


		# Write profile
		# Balance
		with open('user_balance.json','r', encoding='utf-8') as f:
			balance = json.load(f)

		if not member.name in balance:
			balance[str(member.name)] = {}
			balance[str(member.name)]['NTB'] = 0
			balance[str(member.name)]['RUB'] = 0
			balance[str(member.name)]['mined'] = 0

			with open('user_balance.json','w') as f:
				json.dump(balance,f)

		# Farms
		with open('user_farms.json','r', encoding='utf-8') as f:
			user_farms = json.load(f)

		if not member.name in user_farms:
			user_farms[str(member.name)] = {}
			user_farms[str(member.name)]['name'] = str(member.name)
			user_farms[str(member.name)]['farms'] = 'none'
			user_farms[str(member.name)]['life_time'] = 0
			user_farms[str(member.name)]['out'] = 0
			user_farms[str(member.name)]['auto'] = False
			user_farms[str(member.name)]['channel_id'] = 0


			with open('user_farms.json','w') as f:
				json.dump(user_farms,f)

		# Referal system
		words = ['A', 'E', 'B', '2', 'C', 'X', '4', 'k', '6', 'U', 'Z', 'I', 'I']
		with open('referal.json','r', encoding='utf-8') as f:
			ref = json.load(f)

		tword = f'{random.choice(words) + random.choice(words) + random.choice(words) + random.choice(words) + random.choice(words) + random.choice(words) + random.choice(words) + random.choice(words) + random.choice(words)}'

		ref[str(member.name)] = {}
		ref[str(member.name)]['name'] = member.name
		ref[str(member.name)]['id'] = member.id
		ref[str(member.name)]['code'] = str(tword)
		ref[str(member.name)]['invites'] = 0
		ref[str(member.name)]['used'] = False
		ref[str(member.name)]['ivited_members'] = []

		with open('referal.json','w') as f:
			json.dump(ref,f)

	else:
		print("Another guild")

# |--------------------------- /REACTION EVENTS ---------------------------|








# |------------------------------- METHODS --------------------------------|
def Farm(member: discord.Member, life, amount: float, auto: bool):
	print("LOOP JOB")
	out_time = 3600
	m_chance = 0


	start_time = time.time()
	job_time = 0
	stop = False

	while not stop:
		time.sleep(60)

		# Fot mined 1 hour
		out_time -= 60
		if out_time <= 0:
			out_time = 3600

			with open('user_balance.json','r', encoding='utf-8') as f:
				mined = json.load(f)

			# If farm is automatic
			if auto == True:
				mined[str(member.name)]['RUB'] += amount
				with open('user_balance.json','w') as f:
					json.dump(mined,f)

			elif auto == False:
				mined[str(member.name)]['mined'] += amount
				with open('user_balance.json','w') as f:
					json.dump(mined,f)

			# Crash chance
			chance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
			crash = random.choice(chance)
			if crash == 1:
				m_chance += 1
				if m_chance == 15:
					print("Farm is crashed")
					with open('user_farms.json','r', encoding='utf-8') as f:
						farms = json.load(f)

					farms[str(member.name)]['farms'] = "none"
					farms[str(member.name)]['life_time'] = 0
					farms[str(member.name)]['out'] = 0
					farms[str(member.name)]['auto'] = False
					farms[str(member.name)]['channel_id'] = 0
					with open('user_farms.json','w') as f:
						json.dump(farms,f)

					stop = True

			elif crash == 0:
				with open('user_farms.json','r', encoding='utf-8') as f:
					farms = json.load(f)

				farms[str(member.name)]['farms'] = "none"
				farms[str(member.name)]['life_time'] -= 3600
				with open('user_farms.json','w') as f:
					json.dump(farms,f)


		# If Farm die
		job_time = time.time()
		now_time = job_time - start_time
		if now_time >= life:
			print("Farm is died")
			with open('user_farms.json','r', encoding='utf-8') as f:
				farms = json.load(f)

			farms[str(member.name)]['farms'] = "none"
			farms[str(member.name)]['life_time'] = 0
			farms[str(member.name)]['out'] = 0
			farms[str(member.name)]['auto'] = False
			farms[str(member.name)]['channel_id'] = 0
			with open('user_farms.json','w') as f:
				json.dump(farms,f)

			stop = True



async def CreateFarmChannel(member: discord.Member, farm: str):
	guild = bot.get_guild(880008097370865706)
	category = discord.utils.get(guild.categories, name="Фермы")

	channel = await guild.create_text_channel(f'⛏{member.name}-{farm}', category=category)
	await channel.set_permissions(guild.default_role, read_messages=False)
	await channel.set_permissions(member, read_messages=True, send_messages=True)

	if farm == "FARM ЗАТЫЧКА":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM ЗАТЫЧКА", description=f'Панель управления майнинг фермой "FARM ЗАТЫЧКА"\n\n**ДЛЯ ВЫВОДА NTB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/92f8Cw8/Z.png")
		embed.add_field(name = '**Срок работы:**', value = f'35дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'25 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 3024000
		farms[str(member.name)]['out'] = 0.25
		farms[str(member.name)]['auto'] = False
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 3024000, 0.25, False))
		farmth.start()


	elif farm == "FARM GTX":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM GTX", description=f'Панель управления майнинг фермой "FARM GTX"\n\n**ДЛЯ ВЫВОДА NTB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/RCt8s0K/G.png")
		embed.add_field(name = '**Срок работы:**', value = f'29дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'25 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 2505600
		farms[str(member.name)]['out'] = 0.5
		farms[str(member.name)]['auto'] = False
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 2505600, 0.5, False))
		farmth.start()


	elif farm == "FARM RTX":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM RTX", description=f'Панель управления майнинг фермой "FARM RTX"\n\n**ДЛЯ ВЫВОДА NTB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/z72pGRR/R.png")
		embed.add_field(name = '**Срок работы:**', value = f'29дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'21 день', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 2505600
		farms[str(member.name)]['out'] = 1.0
		farms[str(member.name)]['auto'] = False
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 2505600, 1.0, False))
		farmth.start()


	elif farm == "FARM ASIC":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM ASIC", description=f'Панель управления майнинг фермой "FARM ASIC"\n\n**АВТОМАТИЧЕСКИЙ ВЫВОД**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/RHfBJvm/A.png")
		embed.add_field(name = '**Срок работы:**', value = f'35дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'21 день', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 3888000
		farms[str(member.name)]['out'] = 1.5
		farms[str(member.name)]['auto'] = True
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 3888000, 1.5, True))
		farmth.start()


	elif farm == "FARM MULTI":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM MULTI", description=f'Панель управления майнинг фермой "FARM MULTI"\n\n**АВТОМАТИЧЕСКИЙ ВЫВОД**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/SmQ7bNk/M.png")
		embed.add_field(name = '**Срок работы:**', value = f'40дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'21 день', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 3456000
		farms[str(member.name)]['out'] = 2.0
		farms[str(member.name)]['auto'] = True
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 3456000, 2.0, True))
		farmth.start()


	elif farm == "FARM BOOST":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM BOOST", description=f'Панель управления майнинг фермой "FARM BOOST"\n\n**ДЛЯ ВЫВОДА NTB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/rf67N6Y/B.png")
		embed.add_field(name = '**Срок работы:**', value = f'20дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'14 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 1728000
		farms[str(member.name)]['out'] = 0.3
		farms[str(member.name)]['auto'] = False
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 1728000, 3.0, False))
		farmth.start()


	elif farm == "FARM TITAN":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM TITAN", description=f'Панель управления майнинг фермой "FARM TITAN"\n\n**ДЛЯ ВЫВОДА NTB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/87WYdBB/T.png")
		embed.add_field(name = '**Срок работы:**', value = f'30дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'16 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 2592000
		farms[str(member.name)]['out'] = 4.0
		farms[str(member.name)]['auto'] = False
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 2592000, 4.0, False))
		farmth.start()


	elif farm == "FARM SERVER":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM SERVER", description=f'Панель управления майнинг фермой "FARM SERVER"\n\n**ДЛЯ ВЫВОДА NTB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/0KDHq9W/S.png")
		embed.add_field(name = '**Срок работы:**', value = f'38дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'13 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)	

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 3283200
		farms[str(member.name)]['out'] = 7.0
		farms[str(member.name)]['auto'] = False
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 3283200, 7.0, False))
		farmth.start()


	elif farm == "FARM FACTORY":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM FACTORY", description=f'Панель управления майнинг фермой "FARM FACTORY"\n\n**ВЫВОД АВТОМАТИЧЕСКИЙ**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/NL6qq9w/F.png")
		embed.add_field(name = '**Срок работы:**', value = f'37дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'13 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)	

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 3196800
		farms[str(member.name)]['out'] = 14.0
		farms[str(member.name)]['auto'] = True
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 3196800, 14.0, True))
		farmth.start()


	elif farm == "FARM QUANTUM":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM QUANTUM", description=f'Панель управления майнинг фермой "FARM QUANTUM"\n\n**ВЫВОД АВТОМАТИЧЕСКИЙ**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/JBnsbKS/Q.png")
		embed.add_field(name = '**Срок работы:**', value = f'42дня', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'10 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)	

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 3628800
		farms[str(member.name)]['out'] = 25.0
		farms[str(member.name)]['auto'] = True
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 3628800, 25.0, True))
		farmth.start()


	elif farm == "FARM ПЛАТА":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM ПЛАТА", description=f'Панель управления майнинг фермой "FARM ПЛАТА"\n\n**ДЛЯ ВЫВОДА NTB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/pd6w8dt/plata.png")
		embed.add_field(name = '**Срок работы:**', value = f'14дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'10 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		embed.add_field(name = '**Заработано:**', value = f'0 NTB', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		farm_messages.append(message.id)

		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)	

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 1209600
		farms[str(member.name)]['out'] = 0.3
		farms[str(member.name)]['auto'] = False
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 1209600, 0.3, False))
		farmth.start()

# |------------------------------- /METHODS -------------------------------|








# |------------------------------ COMMANDS ------------------------------|
@bot.command()
async def c(ctx, *, code):
	guild1 = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild1:
		print('In guild')

	else:
		with open('referal.json','r', encoding='utf-8') as f:
			ref = json.load(f)

		for i in ref:
			if ref[i]['code'] == code:
				print(ref[i])
				if str(ref[i]['name']) != ctx.message.author.name:
					if ref[str(ctx.message.author.name)]['used'] == False:
						guild = bot.get_guild(880008097370865706)

						ref[str(ctx.message.author.name)]["used"] = True

						ref[i]["invites"] += 1
						inviter_member = guild.get_member(int(ref[i]['id']))
						await inviter_member.send(f'**Ваш реферальный код активировал {ctx.message.author}.**')


						code = ref[str(ctx.message.author.name)]['code']
						invites = ref[str(ctx.message.author.name)]['invites']
						invited_members = ref[str(ctx.message.author.name)]['ivited_members']
						await ctx.message.author.send("**Реферальный код активирован.**")
						embed = discord.Embed(color=0x3C55FA, title="ВАШ РЕФЕРАЛЬНЫЙ ПРОФИЛЬ", description="[:arrow_right: КАК ЭТО РАБОТАЕТ?](https://discord.com/channels/880008097370865706/880024762942889994/881782385870512198)\n\n:repeat:**- Что бы подтвердить приглашение, введите комаду `!c КОД`.\nПример - `!c 6kkUEC3XA`**\n\nНиже представлена статистика вашего профиля")
						embed.add_field(name = '**ВАШ РЕФЕРАЛЬНЫЙ КОД**', value = f'`{code}`', inline = True)
						embed.add_field(name = '**RUB ЗА ПРИГЛАШЕНИЕ**', value = f'1', inline = True)
						embed.add_field(name = '**ВСЕГО ПРИГЛАШЕНО РЕФЕРАЛОВ:**', value = f'{invites}', inline = True)
						embed.add_field(name = '**ПРИГЛАШЕННЫЕ РЕФЕРАЛЫ:**', value = f'{invited_members}', inline = True)
						await ctx.message.author.send(embed=embed)

						ref[i]['ivited_members'].append(ctx.message.author.name)
						with open('referal.json','w') as f:
							json.dump(ref,f)

						with open('user_balance.json','r', encoding='utf-8') as f:
							user_balance = json.load(f)

						user_balance[str(ref[i]['name'])]['RUB'] += 1
						user_balance[ctx.message.author.name]['RUB'] += 1

						with open('user_balance.json','w') as f:
							json.dump(user_balance,f)

						code_author = str(ref[i]['name'])
						log = bot.get_channel(888053213750779934)
						embed1 = discord.Embed(color=0x388E3C, title="АКТИВАЦИЯ РЕФЕРАЛЬНОГО КОДА", description=f'**`{ctx.message.author}` Активировал реферальный код пользователя `{code_author}`**')
						await log.send(embed=embed1)

					else:
						print("Used")

				else:
					embed = discord.Embed(color=0x3C55FA, title="Вы не можете активировать свой код.")
					await ctx.send(embed=embed)


			else:
				print("Not found")


@bot.command()
async def duel(ctx, member: discord.Member, amount: int):
	players = []
	players.append(ctx.message.author.name)
	players.append(member.name)
	print(players)
	winner = random.choice(players)
	players.remove(str(winner))
	loser = str(players[0])

	with open('user_balance.json','r', encoding='utf-8') as f:
		user_balance = json.load(f)


	author_balance = user_balance[str(ctx.message.author.name)]['NTB']
	member_balance = user_balance[str(member.name)]['NTB']
	if amount < 10:
		await ctx.send(f'{ctx.message.author.mention} Минимальная ставка **10NTB**.')

	else:
		if author_balance < 10:
			await ctx.send(f'{ctx.message.author.mention} У Вас не достаточно средств.')

		elif author_balance >= amount and member_balance >= amount:
			percent = amount / 100 * 10
			money = amount - percent

			user_balance[str(loser)]['NTB'] -= amount
			user_balance[str(member.name)]['NTB'] += money

			embed = discord.Embed(color=0x3C55FA, title="ИТОГИ ПОЕДИНКА", description=f'{winner} ПОБЕДИЛ {loser}\n\nВЫИГРЫШ: **{money}NTB**\nСРЕДСТВА ОТПРАВЛЕНЫ НА СЧЕТ ПОБЕДИТЕЛЮ')
			embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/62/PNG/128/blue_medal_honor_award_12514.png")
			await ctx.send(embed = embed)

			with open('user_balance.json','w') as f:
				json.dump(user_balance,f)

			log = bot.get_channel(888053213750779934)
			embed1 = discord.Embed(color=0x388E3C, title="СХВАТКА В ДУЭЛИ", description=f'**`{winner}` Победил в дуэли {loser}, выигрыш `{amount}`**')
			await log.send(embed=embed1)

		else:
			await ctx.send(f'Не достаточно средств.')



@bot.command()
async def top(ctx):
	guild = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild:
		print('In guild')

	else:
		embed = discord.Embed(color=0x3C55FA, description=f'[**ДЛЯ ПОПОЛНЕНИЯ БАЛАНСА, НАЖМИТЕ НА ЭТО СООБЩЕНИЕ**](https://discord.gg/X3EApHyqBM)\n\n**1. Нажав на синий текст, вы перейдете на сайт\n2. Приобретите код пополнения на сайте\n3. Откройте документ с купленным кодом пополнения, скопируйте команду и отправьте в личные сообщения мне**\n\n__СПОСОБ ОПЛАТЫ КАРТОЙ ДОСТУПЕН ПРИ ВЫБОРЕ МЕТОДА ОПЛАТЫ QIWI__')
		await ctx.send(embed=embed)


@bot.command()
async def get(ctx):
	guild = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild:
		print('In guild')

	else:
		embed = discord.Embed(color=0x3C55FA, title="https://discord.gg/X3EApHyqBM")
		await ctx.send(embed=embed)


@bot.command()
async def promo(ctx, code):
	guild = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild:
		print('In guild')

	else:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		if code == "TESTv1":
			user_balance[str(ctx.message.author.name)]['NTB'] += 1000
			await ctx.send(f'{ctx.message.author.mention} Вы активировали промокод на `1000`NTB!')

			log = bot.get_channel(888053213750779934)
			embed1 = discord.Embed(color=0x388E3C, title="АКТИВАЦИЯ ПРОМОКОДА", description=f'**`{ctx.message.author}` Активировал промокод `TESTv1`**')
			await log.send(embed=embed1)

		elif code != "TESTv1":
			await ctx.send("Промокод не найден.")

		with open('user_balance.json','w') as f:
			json.dump(user_balance,f)


# ------------------------ Moderation ------------------------|
# Ban
@bot.command()
@commands.has_any_role(881141342959439882,  881603894449406022, 880357242346553374)
async def ban(ctx, member: discord.Member, time: int, *, about: str):
	getrole = discord.utils.get(ctx.guild.roles, id = 888483227080224779)
	await member.add_roles(getrole)
	embed = discord.Embed(color = 0xff0000, description = f'Вам ограничили доступ к серверу **NEXT InvesT**(бан) по причине: **`{about}`** на **`{time}`** минут.')
	await member.send(embed = embed)

	log = bot.get_channel(888053213750779934)
	embed1 = discord.Embed(color=0x388E3C, title="БАН", description=f'**`{member}` Был забанен `{ctx.message.author}` на `{time} минут` по причине\n\n```diff\n- {about}\n```**')
	await log.send(embed=embed1)

	await time.sleep(time*60)
	await member.remove_roles(getrole)

# Mute
@bot.command()
@commands.has_any_role(880357827699433513)
async def mute(ctx, member: discord.Member, time: int, *, about: str):
	getrole = discord.utils.get(ctx.guild.roles, id = 888461992824799283)
	await member.add_roles(getrole)
	embed = discord.Embed(color = 0xff0000, description = f'Вам ограничили доступ к серверу **NEXT InvesT** по причине: **`{about}`** на **`{time}`** минут.')
	await member.send(embed = embed)

	log = bot.get_channel(888053213750779934)
	embed1 = discord.Embed(color=0x388E3C, title="МЬЮТ", description=f'**`{member}` Был замьючен `{ctx.message.author}` на `{time} минут` по причине\n\n```diff\n- {about}\n```**')
	await log.send(embed=embed1)

	await time.sleep(time*60)
	await member.remove_roles(getrole)

# ----------------------- /Moderation ------------------------|


@bot.command()
async def upd(ctx):
	guild = bot.get_guild(880008097370865706)
	channel = bot.get_channel(889062563952857138)

	#m = await channel.fetch_message(881904501685092382)
	#embed = discord.Embed(color=0x3C55FA, title=f'▰▰▰▰ ДОБРО ПОЖАЛОВАТЬ В {guild.name} ▰▰▰▰', description=f'НАШ СЕРВЕР ПОЗВОЛЯЕТ НЕ ТОЛЬКО ПРИЯТНО ПРОВЕСТИ ВРЕМЯ, НО И ПРИ ЭТОМ ЗАРАБОТАТЬ __РЕАЛЬНЫЕ ДЕНЬГИ__\n\n[:arrow_forward: ОЗНАКОМИТЬСЯ С СИСТЕМОЙ ЗАРАБОТКА](https://discord.com/channels/880008097370865706/880024762942889994/881782363191910440)\n[:arrow_forward: НАЖМИТЕ ЕСЛИ ОСТАЛИСЬ ВОПРОСЫ](https://discord.com/channels/880008097370865706/880023125062995969/880023125062995969)\n\n**ДЛЯ УДОБНОГО ПЕРЕМЕЩЕНИЯ МЕЖДУ КАНАЛАМИ СЕРВЕРА, ИСПОЛЬЗУЙТЕ НАВИГАЦИОННЫЕ КНОПКИ:**\n\n```ИНФОРМАЦИОННЫЕ КАНАЛЫ```\n\n<#880008098000035872> — ВАШИ ОТЗЫВЫ\n<#880023035262959636> — НАВИГАЦИОННЫЙ КАНАЛ\n<#880023125062995969> — ОТВЕТЫ НА ЧАСТЫЕ ВОПРОСЫ\n<#880023332639096853> — ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ\n<#880023390847635476> — СПИСОК ПРАВИЛ\n<#880023473106337854> — РОЗЫГРЫШИ\n<#880023539758034945> — ПУБЛИКАЦИЯ ОБНОВЛЕНИЙ\n<#880023539758034945> — ПУБЛИКАЦИИ, ОБЪЯВЛЕНИЯ И НОВОСТИ\n\n```ИНВЕСТИЦИИ```\n\n<#880024690821853184> — СПИСОК КОМАНД СЕРВЕРА\n<#880024762942889994> — ИНФОРМАЦИЯ О СИСТЕМЕ ЗАРАБОТКА\n<#889062563952857138> — ВЫПОЛНЯЙ ЗАДАНИЕ СЕРВЕРЕ И ПОЛУЧАЙ НЕБОЛЬШУЮ НАГРАДУ\n\n```МАГАЗИНЫ```\n\n<#880025073963122718> — МАГАЗИН ФЕРМ\n\n```КАНАЛЫ ДЛЯ ОБЩЕНИЯ```\n\n<#880027455769944074> — КАНАЛ ПРИВЕТСТВИЯ\n<#880027613261864970> — ОСНОВНОЕ ОБЩЕНИЕ\n<#880027728466837574> — ЗАРАБАТЫВАЙТЕ НА S.UP/BUMP\n\n<#880028018649755668> — ВАШИ ПРЕДЛОЖЕНИЯ\n\n```ТВОРЧЕСТВО```\n\n<#880349406933692416> - ПУБЛИКУЙТЕ МЕМЫ\n\n<#880352375288774667> — КОМАНДА ДЛЯ ЗАКАЗА\n\n```ПРОЧИЕ КАНАЛЫ```\n\n<#881234226714910760> — ОТКРЫТЫЕ ВАКАНСИИ')
	#await m.edit(embed = embed)
	embed = discord.Embed(color=0x21C81E, description="Пригласи 10 человек")
	embed.add_field(name = '**Количество активаций**', value = f'**1**', inline = True)
	embed.add_field(name = '**Оплата**', value = f'**5**', inline = True)
	embed.add_field(name = '**Тип проверки**', value = f'**[Ручная](https://discord.com/channels/880008097370865706/882644436608241715/887765170846314506)**', inline = True)

	embed.set_author(name="Активный Рефовод", icon_url="https://i.ibb.co/3hL4TtV/quests1.png")
	await channel.send(embed = embed)


	embed1 = discord.Embed(color=0x21C81E, description="Пригласи 10 человек,\nкаждый из которых сделает вклад\nминимум в 20 рублей.")
	embed1.add_field(name = '**Количество активаций**', value = f'**1**', inline = True)
	embed1.add_field(name = '**Оплата**', value = f'**30**', inline = True)
	embed1.add_field(name = '**Тип проверки**', value = f'**[Ручная](https://discord.com/channels/880008097370865706/882644436608241715/887765170846314506)**', inline = True)

	embed1.set_author(name="Активный Рефовод", icon_url="https://i.ibb.co/3hL4TtV/quests1.png")
	await channel.send(embed = embed1)


	embed2 = discord.Embed(color=0x21C81E, description="Пригласи 20 человек,\nкаждый из которых сделает вклад\nминимум в 20 рублей.")
	embed2.add_field(name = '**Количество активаций**', value = f'**1**', inline = True)
	embed2.add_field(name = '**Оплата**', value = f'**45**', inline = True)
	embed2.add_field(name = '**Тип проверки**', value = f'**[Ручная](https://discord.com/channels/880008097370865706/882644436608241715/887765170846314506)**', inline = True)

	embed2.set_author(name="Активный Рефовод", icon_url="https://i.ibb.co/3hL4TtV/quests1.png")
	await channel.send(embed = embed2)


	embed3 = discord.Embed(color=0x21C81E, description="Пригласи 50 человек,\nкаждый из которых сделает вклад\nминимум в 20 рублей.")
	embed3.add_field(name = '**Количество активаций**', value = f'**1**', inline = True)
	embed3.add_field(name = '**Оплата**', value = f'**105**', inline = True)
	embed3.add_field(name = '**Тип проверки**', value = f'**[Ручная](https://discord.com/channels/880008097370865706/882644436608241715/887765170846314506)**', inline = True)

	embed3.set_author(name="Рефолов", icon_url="https://i.ibb.co/3sN1M2p/16.png")
	await channel.send(embed = embed3)


	embed5 = discord.Embed(color=0x21C81E, description="Получи бонус 150 руб.\nЗа оборот структуры в 3000 руб.")
	embed5.add_field(name = '**Количество активаций**', value = f'**1**', inline = True)
	embed5.add_field(name = '**Оплата**', value = f'**50**', inline = True)
	embed5.add_field(name = '**Тип проверки**', value = f'**[Ручная](https://discord.com/channels/880008097370865706/882644436608241715/887765170846314506)**', inline = True)

	embed5.set_author(name="Рефолов", icon_url="https://i.ibb.co/3sN1M2p/16.png")
	await channel.send(embed = embed5)


	embed6 = discord.Embed(color=0x21C81E, description="Сделайте видео о нас\nСнимите видео о сервере\nв позитивном ключе и загрузите на ваш YouTube")
	embed6.add_field(name = '**Количество активаций**', value = f'**раз в 10 дней**', inline = True)
	embed6.add_field(name = '**Оплата**', value = f'**50**', inline = True)
	embed6.add_field(name = '**Тип проверки**', value = f'**[Ручная](https://discord.com/channels/880008097370865706/882644436608241715/887765170846314506)**', inline = True)

	embed6.set_author(name="Снимите видео", icon_url="https://i.ibb.co/b17qG9x/12.png")
	await channel.send(embed = embed6)


	embed7 = discord.Embed(color=0x21C81E, description="Напишите статью о нашем\nсервере Next InvesT\nуникальный обзор на вашем\nсервере(блоге) о нашей...")
	embed7.add_field(name = '**Количество активаций**', value = f'**раз в пять дней**', inline = True)
	embed7.add_field(name = '**Оплата**', value = f'**3**', inline = True)
	embed7.add_field(name = '**Тип проверки**', value = f'**[Ручная](https://discord.com/channels/880008097370865706/882644436608241715/887765170846314506)**', inline = True)

	embed7.set_author(name="Написать отзыв", icon_url="https://i.ibb.co/3RY01NK/5.png")
	await channel.send(embed = embed7)

bot.run('ODc5NjkzNDk5ODQ1NDU1ODcy.YSTcag.KiNpzAVZ_isc-HIdeeLw6FbJZgM')
