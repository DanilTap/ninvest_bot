# This Python file uses the following encoding: utf-8
import discord
from discord.ext import commands
from threading import Thread
import json
import time
import asyncio
import random
import datetime

intents = discord.Intents.default()
intents.members = True
bot = discord.ext.commands.Bot(command_prefix = "!", intents = intents)



# |------------------------------ VARIABLES ------------------------------|
# Reactions lists
tickets_messages = []
# |------------------------------ /VARIABLES -----------------------------|



# Welcome to the world of crutches and crooked OOP!

# |-------------------------------- EVENTS --------------------------------|
bot.remove_command('help')
@bot.event
async def on_ready():
	guild = bot.get_guild(880008097370865706)
	print('----------Bot is ready!----------\n\n')
	
	# Start farms
	with open('user_farms.json','r', encoding='utf-8') as f:
		farms = json.load(f)

	print("----------Loading farms-----------\n")

	for i in farms:
		member = farms[i]['name']
		farm_list = farms[i]['farms']

		for i in farm_list.items():
			if i[1]['stats'] != False:
				life = i[1]["life_time"]
				out = i[1]["out"]
				mode = i[1]["auto"]
				print(f'{member} HAVE FARM.\n')
				print(f'{life}  {out}  {mode}')

				farmth = Thread(target=Farm, args=(member, i[0], life, out, mode))
				farmth.start()

			else:
				print(f'{member} NO FARMS\n')


	with open('user_farms.json','r', encoding='utf-8') as f:
		lfarms = json.load(f)


	print("----------Loading done!----------\n\n\n")


	# Start deposits
	with open('user_bank.json','r', encoding='utf-8') as f:
		bank = json.load(f)

	print("----------Loading deposits-----------")
	for i in bank:
		member = bank[i]['name']
		if bank[i]['deposit'] != "none":

			depos = bank[i]['deposit']
			amount = bank[i]['amount']
			ltime = bank[i]['ltime']
			if depos == 1:
				deposit = Thread(target=Deposit, args=(member, int(amount), 10, ltime))
				deposit.start()
				print(f'{member} HAVE DEPOSIT.')
				print(f'{ltime} {amount} {depos} \n\n')

			elif depos == 2:
				deposit = Thread(target=Deposit, args=(member, int(amount), 20, ltime))
				deposit.start()
				print(f'{member} HAVE DEPOSIT.')
				print(f'{ltime} {amount} {depos} \n\n')

		else:
			print(f'{member} NO DEPOSIT')

	print("----------Loading done!----------\n\n")



	# Update users DB
	print("----------Writing new users:----------")
	for member in guild.members:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		with open('user_farms.json','r', encoding='utf-8') as f:
			user_farms = json.load(f)

		with open('referal.json','r', encoding='utf-8') as f:
			ref = json.load(f)

		with open('user_bank.json','r', encoding='utf-8') as f:
			bank = json.load(f)

		with open('user_sales.json','r', encoding='utf-8') as f:
			sales = json.load(f)

		with open('user_profile.json','r', encoding='utf-8') as f:
			profile = json.load(f)

		if not member.name in user_balance and not member.name in user_farms and member.name in ref and not member.name in bank and not member.name in sales and not member.name in profile:
			print(member.name)
			# Balance
			user_balance[str(member.name)] = {}
			user_balance[str(member.name)]['NTB'] = 0
			user_balance[str(member.name)]['RUB'] = 0
			with open('user_balance.json','w') as f:
				json.dump(user_balance,f)

			# Farms
			user_farms[str(member.name)] = {}
			user_farms[str(member.name)]['name'] = str(member.name)
			user_farms[str(member.name)]['farms'] = {}
			with open('user_farms.json','w') as f:
				json.dump(user_farms,f)

			# Referal system
			words = ['A', 'E', 'B', '2', 'C', 'X', '4', 'k', '6', 'U', 'Z', 'I', 'I']
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

			# User bank
			bank[str(member.name)] = {}
			bank[str(member.name)]['name'] = member.name
			bank[str(member.name)]['deposit'] = "none"
			bank[str(member.name)]['amount'] = 0
			bank[str(member.name)]['ltime'] = 0
			with open('user_bank.json','w') as f:
				json.dump(bank,f)

			# Sales
			sales[str(member.name)] = {}
			sales[str(member.name)]['name'] = str(member.name)
			sales[str(member.name)]['sales'] = {}
			with open('user_sales.json','w') as f:
				json.dump(sales,f)

			# User Profile
			profile[str(member.name)] = {}
			profile[str(member.name)]['time'] = 0
			profile[str(member.name)]['stats'] = True
			with open('user_profile.json','w') as f:
				json.dump(profile,f)
	
	print("----------Update user DB is done!----------")		



# ------------------------ Voice Timer ------------------------|
timerstats = True
@bot.event
async def on_voice_state_update(member, before, after):
	global timerstats
	if before.channel is None and after.channel is not None:

		with open('user_balance.json','r', encoding='utf-8') as f:
			balance = json.load(f)

		while timerstats:
			await asyncio.sleep(1800)#1800
			balance[str(member.name)]["NTB"] += 0.5
			with open('user_balance.json','w') as f:
				json.dump(balance,f)

	elif before.channel is not None and after.channel is None:
		timerstats = False

 
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

			embed = discord.Embed(color=0x3C55FA, title="ВАШ БАЛАНС", description=f':euro:** {round(rub, 2)} RUB**\n:pound:** {round(ntb, 2)} NTB**\n\n`!top` - Пополнить\n`!get` - Вывести\n🔁 - Обновить баланс.')
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

	#await embedm4.add_reaction('💷')
	#await embedm4.add_reaction('💳')
	#await embedm4.add_reaction('💰')

	# Cases
	elif message_id == 890117667908878347:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		balance = user_balance[str(member.name)]['RUB']

		if payload.emoji.name == "💷":
			if balance < 49:
				await member.send("У вас недостаточно средств для покупки кейса.")

			elif balance >= 49:
				user_balance[str(member.name)]['RUB'] -= 49
				items = [50, 35, 25, 20, 15, 10, 'role', 'role1']

				item = random.choice(items)
				print(item)

				if item == 'role':
					getrole = discord.utils.get(guild.roles, id = 890960183155630191)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@бизнесмен`! </easter code egg>")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс BRONZE и выиграл роль бизнесмен.</easter code egg>')
					await log.send(embed=embed)

				elif item == 'role1':
					getrole = discord.utils.get(guild.roles, id = 892435708881539103)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Trainer`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс BRONZE и выиграл роль Trainer.')
					await log.send(embed=embed)
					
				else:
					user_balance[str(member.name)]['RUB'] += float(item)
					await member.send(f'Вы выиграли **`{item}` RUB**!')
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс BRONZE и выиграл {item}RUB.')
					await log.send(embed=embed)
					

				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 245:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 245:
				user_balance[str(member.name)]['RUB'] -= 245
				for i in range(5):
					items = [50, 35, 25, 20, 10, 'role', 'role1']

					item = random.choice(items)
					print(item)

					if item == 'role':
						getrole = discord.utils.get(guild.roles, id = 890960183155630191)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@бизнесмен`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс BRONZE и выиграл роль бизнесмен.</easter code egg>')
						await log.send(embed=embed)

					elif item == 'role1':
						getrole = discord.utils.get(guild.roles, id = 892435708881539103)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Trainer`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс BRONZE и выиграл роль Trainer.')
						await log.send(embed=embed)
						
					else:
						user_balance[str(member.name)]['RUB'] += float(item)
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс BRONZE и выиграл {item}RUB.')
						await log.send(embed=embed)

					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)

		elif payload.emoji.name == "💰":
			if balance < 490:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 490:
				user_balance[str(member.name)]['RUB'] -= 490
				for i in range(10):
					items = [50, 35, 25, 20, 10, 'role', 'role1']

					item = random.choice(items)
					print(item)

					if item == 'role':
						getrole = discord.utils.get(guild.roles, id = 890960183155630191)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@бизнесмен`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс BRONZE и выиграл роль бизнесмен.')
						await log.send(embed=embed)

					elif item == 'role1':
						getrole = discord.utils.get(guild.roles, id = 892435708881539103)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Trainer`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс BRONZE и выиграл роль Trainer.')
						await log.send(embed=embed)
						
					else:
						user_balance[str(member.name)]['RUB'] += float(item)
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс BRONZE и выиграл {item}RUB.')
						await log.send(embed=embed)

					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)


	elif message_id == 890117675408322580:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		balance = user_balance[str(member.name)]['RUB']

		if payload.emoji.name == "💷":
			if balance < 99:
				await member.send("У вас недостаточно средств для покупки кейса.")

			elif balance >= 99:
				user_balance[str(member.name)]['RUB'] -= 99
				items = [80, 50, 55, 40, 20, 10, 'premium16', 'premium10', 'farm', 'jet', 'zap']

				item = random.choice(items)
				print(item)

				if item == 'premium16':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 16 days`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 16 days.')
					await log.send(embed=embed)

				elif item == 'premium10':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 10 days`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 10 days.')
					await log.send(embed=embed)

				elif item == 'farm':
					await CreateFarmChannel(member, 'FARM ПЛАТА')
					await member.send("Вы выиграли ферму `FARM ПЛАТА`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл ферму FARM ПЛАТА.')
					await log.send(embed=embed)

				elif item == 'jet':
					getrole = discord.utils.get(guild.roles, id = 890112890722463774)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@:plane:`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль :plane:.')
					await log.send(embed=embed)

				elif item == 'zap':
					getrole = discord.utils.get(guild.roles, id = 890099592752939009)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@:zap:`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль :zap:.')
					await log.send(embed=embed)

				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и {item}RUB')
					await log.send(embed=embed)

				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 496:
				await member.send("У вас недостаточно средств для покупки кейса.")

			elif balance >= 496:
				user_balance[str(member.name)]['RUB'] -= 496
				for i in range(5):
					items = [80, 50, 55, 40, 20, 10, 'premium16', 'premium10', 'farm', 'zap', 'jet']

					item = random.choice(items)
					print(item)

					if item == 'premium16':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 16 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 16 days.')
						await log.send(embed=embed)

					elif item == 'premium10':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 10 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 10 days.')
						await log.send(embed=embed)

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ПЛАТА')
						await member.send("Вы выиграли ферму `FARM ПЛАТА`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл ферму FARM ПЛАТА.')
						await log.send(embed=embed)

					elif item == 'jet':
						getrole = discord.utils.get(guild.roles, id = 890112890722463774)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:plane:`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль :plane:.')
						await log.send(embed=embed)

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль :zap:.')
						await log.send(embed=embed)

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и {item}RUB')
						await log.send(embed=embed)

					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)


		elif payload.emoji.name == "💰":
			if balance < 990:
				await member.send("У вас недостаточно средств для покупки кейса.")

			elif balance >= 990:
				user_balance[str(member.name)]['RUB'] -= 990
				for i in range(10):
					items = [80, 50, 55, 40, 20, 10, 'premium16', 'premium10', 'farm', 'zap', 'jet']

					item = random.choice(items)
					print(item)

					if item == 'premium16':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 16 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 16 days.')
						await log.send(embed=embed)

					elif item == 'premium10':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 10 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 10 days.')
						await log.send(embed=embed)

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ПЛАТА')
						await member.send("Вы выиграли ферму `FARM ПЛАТА`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл ферму FARM ПЛАТА.')
						await log.send(embed=embed)

					elif item == 'jet':
						getrole = discord.utils.get(guild.roles, id = 890112890722463774)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:plane:`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль :plane:.')
						await log.send(embed=embed)

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль :zap:.')
						await log.send(embed=embed)

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и {item}RUB')
						await log.send(embed=embed)

					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)


	elif message_id == 890117683478147092:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		balance = user_balance[str(member.name)]['RUB']

		if payload.emoji.name == "💷":
			if balance < 199:
				await member.send("У вас недостаточно средств для покупки кейса.")

			elif balance >= 199:
				user_balance[str(member.name)]['RUB'] -= 199
				items = [210, 200, 150, 100, 125, 85, 65, 50, 'premium30', 'premium21', 'farm', 'role2', 'role3']

				item = random.choice(items)
				print(item)

				if item == 'premium30':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 30 day`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 30 days.')
					await log.send(embed=embed)

				elif item == 'premium21':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 21 day`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 21 days.')
					await log.send(embed=embed)

				elif item == 'farm':
					await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')
					await member.send("Вы выиграли ферму `FARM ЗАТЫЧКА`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл ферму FARM ЗАТЫЧКА.')
					await log.send(embed=embed)

				elif item == 'role2':
					getrole = discord.utils.get(guild.roles, id = 890119660488491049)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Monopolis`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Monopolis.')
					await log.send(embed=embed)

				elif item == 'role3':
					getrole = discord.utils.get(guild.roles, id = 890099592752939009)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@:zap:`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль :zap:.')
					await log.send(embed=embed)

				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл {item}RUB.')
					await log.send(embed=embed)


				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 995:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 995:
				user_balance[str(member.name)]['RUB'] -= 995
				for i in range(5):
					items = [210, 200, 150, 125, 100, 85, 65, 50, 'premium30', 'premium21', 'farm', 'role2', 'role3']

					item = random.choice(items)
					print(item)

					if item == 'premium30':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 30 day`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 30 days.')
						await log.send(embed=embed)

					elif item == 'premium21':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 21 day`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 21 days.')
						await log.send(embed=embed)

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')
						await member.send("Вы выиграли ферму `FARM ЗАТЫЧКА`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл ферму FARM ЗАТЫЧКА.')
						await log.send(embed=embed)

					elif item == 'role2':
						getrole = discord.utils.get(guild.roles, id = 890119660488491049)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Monopolis`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Monopolis.')
						await log.send(embed=embed)

					elif item == 'role3':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль :zap:.')
						await log.send(embed=embed)

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл {item}RUB.')
						await log.send(embed=embed)


					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)


		elif payload.emoji.name == "💰":
			if balance < 1990:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 1990:
				user_balance[str(member.name)]['RUB'] -= 1990
				for i in range(10):
					items = [210, 200, 150, 125, 100, 85, 65, 50, 'premium30', 'premium21', 'farm', 'role2', 'role3']

					item = random.choice(items)
					print(item)

					if item == 'premium30':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 30 day`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 30 days.')
						await log.send(embed=embed)

					elif item == 'premium21':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 21 day`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Premium 21 days.')
						await log.send(embed=embed)

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')
						await member.send("Вы выиграли ферму `FARM ЗАТЫЧКА`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл ферму FARM ЗАТЫЧКА.')
						await log.send(embed=embed)

					elif item == 'role2':
						getrole = discord.utils.get(guild.roles, id = 890119660488491049)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Monopolis`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль Monopolis.')
						await log.send(embed=embed)

					elif item == 'role3':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл роль :zap:.')
						await log.send(embed=embed)

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс SILVER и выиграл {item}RUB.')
						await log.send(embed=embed)


					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)


	elif message_id == 890117691388600320:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		balance = user_balance[str(member.name)]['RUB']

		if payload.emoji.name == "💷":
			if balance < 500:
				await member.send("У вас недостаточно средств для покупки кейса.")

			elif balance >= 500:
				user_balance[str(member.name)]['RUB'] -= 500
				items = [420, 400, 350, 200, 100, 65, 'premium45', 'premium26', 'premium35', 'zap', 'asic']

				item = random.choice(items)
				print(item)

				if item == 'premium45':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium - 45 days`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 45 days.')
					await log.send(embed=embed)

				elif item == 'premium26':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium - 26 days`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 26 days.')
					await log.send(embed=embed)

				elif item == 'premium35':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium - 35 days`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 35 days.')
					await log.send(embed=embed)

				elif item == 'zap':
					getrole = discord.utils.get(guild.roles, id = 890587785856155649)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@🌀`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль 🌀.')
					await log.send(embed=embed)

				elif item == 'asic':
					await CreateFarmChannel(member, 'FARM ASIC')
					await member.send("Вы выиграли ферму `FARM ASIC`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл FARM ASIC.')
					await log.send(embed=embed)

				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл {item}RUB.')
					await log.send(embed=embed)

				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 2500:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 2500:
				user_balance[str(member.name)]['RUB'] -= 2500
				for i in range(5):
					items = [420, 400, 350, 200, 100, 65, 'premium45', 'premium26', 'premium35', 'zap', 'asic']

					item = random.choice(items)
					print(item)

					if item == 'premium45':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 45 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 45 days.')
						await log.send(embed=embed)

					elif item == 'premium26':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 26 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 26 days.')
						await log.send(embed=embed)

					elif item == 'premium35':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 35 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 35 days.')
						await log.send(embed=embed)

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890587785856155649)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@🌀`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль 🌀.')
						await log.send(embed=embed)

					elif item == 'asic':
						await CreateFarmChannel(member, 'FARM ASIC')
						await member.send("Вы выиграли ферму `FARM ASIC`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл FARM ASIC.')
						await log.send(embed=embed)

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл {item}RUB.')
						await log.send(embed=embed)

					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)


		elif payload.emoji.name == "💰":
			if balance < 5000:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 5000:
				user_balance[str(member.name)]['RUB'] -= 5000
				for i in range(10):
					itemss = [420, 400, 350, 200, 100, 65, 'premium45', 'premium26', 'premium35', 'zap', 'asic']

					item = random.choice(itemss)
					print(item)

					if item == 'premium45':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 45 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 45 days.')
						await log.send(embed=embed)

					elif item == 'premium26':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 26 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 26 days.')
						await log.send(embed=embed)

					elif item == 'premium35':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 35 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 35 days.')
						await log.send(embed=embed)

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890587785856155649)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@🌀`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль 🌀.')
						await log.send(embed=embed)

					elif item == 'asic':
						await CreateFarmChannel(member, 'FARM ASIC')
						await member.send("Вы выиграли ферму `FARM ASIC`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл FARM ASIC.')
						await log.send(embed=embed)

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл {item}RUB.')
						await log.send(embed=embed)


					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)


	# LITE CASE
	elif message_id == 893551335511830649:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		balance = user_balance[str(member.name)]['RUB']

		if payload.emoji.name == "💷":
			if balance < 35:
				await member.send("У вас недостаточно средств для покупки кейса.")

			elif balance >= 35:
				user_balance[str(member.name)]['RUB'] -= 35
				items = [35, 35, 25, 15, 10, 5, 'premium7', 'zap', 'comet', 'bussines', 'gold']

				item = random.choice(items)
				print(item)

				if item == 'premium7':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 7 days`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 7 days.')
					await log.send(embed=embed)

				elif item == 'zap':
					getrole = discord.utils.get(guild.roles, id = 890099592752939009)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@:zap:`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль :zap:.')
					await log.send(embed=embed)
					
				elif item == 'comet':
					getrole = discord.utils.get(guild.roles, id = 890123446682521621)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@☄`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль ☄.')
					await log.send(embed=embed)
					
				elif item == 'bussines':
					getrole = discord.utils.get(guild.roles, id = 890960183155630191)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Бизнесмен`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Бизнесмен.')
					await log.send(embed=embed)
					
				elif item == 'gold':
					getrole = discord.utils.get(guild.roles, id = 890119660488491049)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Gold`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль GOLD.</easter egg>')
					await log.send(embed=embed)
					
				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл {item}RUB.')
					await log.send(embed=embed)
					
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 175:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 175:
				user_balance[str(member.name)]['RUB'] -= 175
				for i in range(5):
					items = [35, 35, 25, 15, 10, 5, 'premium7', 'zap', 'comet', 'bussines', 'gold']

					item = random.choice(items)
					print(item)

					if item == 'premium7':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 7 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 7 days.')
						await log.send(embed=embed)

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль :zap:.')
						await log.send(embed=embed)
						
					elif item == 'comet':
						getrole = discord.utils.get(guild.roles, id = 890123446682521621)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@☄`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль ☄.')
						await log.send(embed=embed)
						
					elif item == 'bussines':
						getrole = discord.utils.get(guild.roles, id = 890960183155630191)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Бизнесмен`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Бизнесмен.')
						await log.send(embed=embed)
						
					elif item == 'gold':
						getrole = discord.utils.get(guild.roles, id = 890119660488491049)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Gold`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль GOLD.</easter egg>')
						await log.send(embed=embed)
						
					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл {item}RUB.')
						await log.send(embed=embed)
						

					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)

		elif payload.emoji.name == "💰":
			if balance < 350:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 350:
				user_balance[str(member.name)]['RUB'] -= 350
				for i in range(10):
					items = [35, 35, 25, 15, 10, 5, 'premium7', 'zap', 'comet', 'bussines', 'gold']

					item = random.choice(items)
					print(item)

					if item == 'premium7':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 7 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Premium 7 days.')
						await log.send(embed=embed)

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль :zap:.')
						await log.send(embed=embed)
						
					elif item == 'comet':
						getrole = discord.utils.get(guild.roles, id = 890123446682521621)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@☄`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль ☄.')
						await log.send(embed=embed)
						
					elif item == 'bussines':
						getrole = discord.utils.get(guild.roles, id = 890960183155630191)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Бизнесмен`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль Бизнесмен.')
						await log.send(embed=embed)
						
					elif item == 'gold':
						getrole = discord.utils.get(guild.roles, id = 890119660488491049)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Gold`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл роль GOLD.</easter egg>')
						await log.send(embed=embed)
						
					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс PLATINUM и выиграл {item}RUB.')
						await log.send(embed=embed)
					

					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)

	# New Year
	elif message_id == 926887879786000464:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		balance = user_balance[str(member.name)]['RUB']

		if payload.emoji.name == "💷":
			if balance < 10:
				await member.send("У вас недостаточно средств для покупки кейса.")

			elif balance >= 10:
				user_balance[str(member.name)]['RUB'] -= 10
				items = [125, 75, 35, 15, 5, 0, 'premium7', 'premium10', 'ded', 'sneg', 'inf']

				item = random.choice(items)
				print(item)

				if item == 'premium7':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 7 days`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль Premium 7 days.')
					await log.send(embed=embed)

				elif item == 'premium10':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 7 days`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль Premium 10 days.')
					await log.send(embed=embed)
					
				elif item == 'ded':
					getrole = discord.utils.get(guild.roles, id = 924792031669280828)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@🎅`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль 🎅.')
					await log.send(embed=embed)
					
				elif item == 'sneg':
					getrole = discord.utils.get(guild.roles, id = 924792230026281030)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@☃️`!")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль ☃️.')
					await log.send(embed=embed)
					
				elif item == 'inf':
					getrole = discord.utils.get(guild.roles, id = 890119660488491049)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@❄️`!</easter egg>")
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль ❄️.')
					await log.send(embed=embed)
					
				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')
					log = bot.get_channel(908678594753089547)
					embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл {item}RUB.')
					await log.send(embed=embed)
					
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 50:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 50:
				user_balance[str(member.name)]['RUB'] -= 50
				for i in range(5):
					items = [125, 75, 35, 15, 5, 0, 'premium7', 'premium10', 'ded', 'sneg', 'inf']

					item = random.choice(items)
					print(item)

					if item == 'premium7':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 7 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль Premium 7 days.')
						await log.send(embed=embed)

					elif item == 'premium10':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 7 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль Premium 10 days.')
						await log.send(embed=embed)
						
					elif item == 'ded':
						getrole = discord.utils.get(guild.roles, id = 924792031669280828)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@🎅`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль 🎅.')
						await log.send(embed=embed)
						
					elif item == 'sneg':
						getrole = discord.utils.get(guild.roles, id = 924792230026281030)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@☃️`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль ☃️.')
						await log.send(embed=embed)
						
					elif item == 'inf':
						getrole = discord.utils.get(guild.roles, id = 890119660488491049)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@❄️`!</easter egg>")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль ❄️.')
						await log.send(embed=embed)
						
					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл {item}RUB.')
						await log.send(embed=embed)
						
					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)

		elif payload.emoji.name == "💰":
			if balance < 100:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 100:
				user_balance[str(member.name)]['RUB'] -= 100
				for i in range(10):
					items = [125, 75, 35, 15, 5, 0, 'premium7', 'premium10', 'ded', 'sneg', 'inf']

					item = random.choice(items)
					print(item)

					if item == 'premium7':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 7 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль Premium 7 days.')
						await log.send(embed=embed)

					elif item == 'premium10':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 7 days`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль Premium 10 days.')
						await log.send(embed=embed)
						
					elif item == 'ded':
						getrole = discord.utils.get(guild.roles, id = 924792031669280828)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@🎅`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль 🎅.')
						await log.send(embed=embed)
						
					elif item == 'sneg':
						getrole = discord.utils.get(guild.roles, id = 924792230026281030)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@☃️`!")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль ☃️.')
						await log.send(embed=embed)
						
					elif item == 'inf':
						getrole = discord.utils.get(guild.roles, id = 890119660488491049)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@❄️`!</easter egg>")
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл роль ❄️.')
						await log.send(embed=embed)
						
					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')
						log = bot.get_channel(908678594753089547)
						embed = discord.Embed(color=0x00a550, title="Покупка кейса", description=f'{member.name} купил кейс NEW YEARs CASE и выиграл {item}RUB.')
						await log.send(embed=embed)
						
					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)


	# Super money boxes
	elif message_id == 893397579663044629:
		embed = discord.Embed(description="Укажите количество валюты для вложения в копилку **№1** от 1 до 250RUB.\nКомандой: `!box 1 СУММА`")
		await member.send(embed = embed)

	elif message_id == 893397582523547678:
		embed = discord.Embed(description="Укажите количество валюты для вложения в копилку **№2** от 1 до 350RUB.\nКомандой: `!box 2 СУММА`")
		await member.send(embed = embed)

	elif message_id == 894214944034279435:
		embed = discord.Embed(description="Укажите количество валюты для вложения в копилку **№3** от 1 до 450RUB.\nКомандой: `!box 3 СУММА`")
		await member.send(embed = embed)

	elif message_id == 894214947473588255:
		embed = discord.Embed(description="Укажите количество валюты для вложения в копилку **№4** от 1 до 650RUB.\nКомандой: `!box 4 СУММА`")
		await member.send(embed = embed)


	# Bank
	elif message_id == 890961877520240690:
		if payload.emoji.name == "1️⃣":
			await member.send('Сколько вы хотите положить в банк? Введите сумму `!bank1 СУММА`')

		elif payload.emoji.name == "2️⃣":
			await member.send('Сколько вы хотите положить в банк? Введите сумму `!bank2 СУММА`')


	# Trade
	elif message_id == 902561833037209610:
		with open('user_balance.json','r', encoding='utf-8') as f:
			balance = json.load(f)

		ntb = balance[str(member.name)]['NTB']
		rub = balance[str(member.name)]['RUB']

		with open('bot_constants.json','r', encoding='utf-8') as f:
			constants = json.load(f)

		clist = constants['trade_list']
		buyntb = 0

		if not member.name in clist:
			constants['trade_list'] = {f'{member.name}': 0}

		else:
			for i in clist.items():
				if member.name == i[0]:
					buyntb = i[1]
					print(buyntb)

			if buyntb >= 1000:
				await member.send('Вы не можете купить больше 1000NTB')


		if payload.emoji.name == "💴":
			if rub >= 50:
				balance[str(member.name)]['RUB'] -= 50
				balance[str(member.name)]['NTB'] += 50
				await member.send('Вы купили 50NTB за 50RUB')

				last = buyntb + 50

				constants['trade_list'] = {f'{member.name}': last}

			else:
				await member.send('У вас недостаточно средств.')

		elif payload.emoji.name == "💶":
			if rub >= 150:
				balance[str(member.name)]['RUB'] -= 150
				balance[str(member.name)]['NTB'] += 150
				await member.send('Вы купили 150NTB за 150RUB')

				last = buyntb + 150

				constants['trade_list'] = {f'{member.name}': last}

			else:
				await member.send('У вас недостаточно средств.')

		elif payload.emoji.name == "💷":
			if rub >= 250:
				balance[str(member.name)]['RUB'] -= 250
				balance[str(member.name)]['NTB'] += 250
				await member.send('Вы купили 250NTB за 250RUB')

				last = buyntb + 250

				constants['trade_list'] = {f'{member.name}': last}


			else:
				await member.send('У вас недостаточно средств.')

		with open('user_balance.json','w') as f:
			json.dump(balance ,f)

		with open('bot_constants.json','w') as f:
			json.dump(constants ,f)


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
	with open('user_farms.json','r', encoding='utf-8') as f:
		lfarms = json.load(f)

	for i in lfarms.items():
		if member.name == i[0]:
			farm_list = i[1]["farms"]
			for i in farm_list.items():
				message = i[1]["message_id"]
				for b in message:
					if message_id == b:
						print(f'{member.name} out farm money.')
						mined = int(i[1]["mined"])
						with open('user_balance.json','r', encoding='utf-8') as f:
							balance = json.load(f)

						mined = i[1]["mined"]

						log_channel = bot.get_channel(888053213750779934)
						embed1 = discord.Embed(color=0x008000, title="ВЫВОД С ФЕРМЫ", description=f'**Участник {member} вывел {mined} со своей фермы.**')
						await log_channel.send(embed=embed1)
						await member.send(f'Вы вывели `{mined}`RUB с своей фермы.')

						balance[str(member.name)]["RUB"] += mined
						with open('user_balance.json','w') as f:
							json.dump(balance,f)

						i[1]["mined"] = 0
						with open('user_farms.json','w') as f:
							json.dump(lfarms,f)



	# Buy
	with open('user_sales.json','r', encoding='utf-8') as f:
		sales = json.load(f)

	for i in sales:
		smember = sales[i]['name']
		slist = sales[i]['sales']

		for i in slist.items():
			print(i)

			if message_id == int(i[0]):
				if payload.emoji.name == "✅":
					vtype = i[1]["vtype"]
					ntb = i[1]["ntb"]
					rub = i[1]["rub"]
					st = i[1]["stats"]

					if vtype == "NTB":
						with open('user_balance.json','r', encoding='utf-8') as f:
							balance = json.load(f)

						mntb = balance[str(smember)]["NTB"]
						mrub = balance[str(smember)]["RUB"]
						brub = balance[str(member.name)]["RUB"]

						if mntb >= ntb:
							if brub >= rub:
								i[1]["stats"] = False

								balance[str(smember)]["NTB"] -= ntb
								balance[str(smember)]["RUB"] += rub

								balance[str(member.name)]["NTB"] += ntb
								balance[str(member.name)]["RUB"] -= rub

								with open('user_balance.json','w') as f:
									json.dump(balance,f)

								i[1]["buy"].append(member.name)
								with open('user_sales.json','w') as f:
									json.dump(sales,f)

								await member.send(f'Вы приобрели {ntb}NTB у {smember}.')
								log_channel = bot.get_channel(898204390412943451)
								embed1 = discord.Embed(color=0x008000, title="ПОКУПКА ВАЛЮТЫ", description=f'**{member} Купил {ntb}NTB у {smember}\n[ПРЕДЛОЖЕНИЕ](https://discord.com/channels/880008097370865706/896752866759409705/{int(i[0])})**')
								await log_channel.send(embed=embed1)

								channel = bot.get_channel(900380294161502229)
								smessage = await channel.fetch_message(message_id)
								await smessage.delete()


							else:
								await member.send('У вас недостаточно средств для покупки этого количества валюты.')

						else:
							channel = bot.get_channel(900380294161502229)
							smessage = await channel.fetch_message(message_id)
							await smessage.delete()

							await member.send("У автора этого предложения недостаточно валюты для ее продажи.")

							log_channel = bot.get_channel(898204390412943451)
							embed1 = discord.Embed(color=0x008000, title="ЗАКРЫТИЕ ПРЕДЛОЖЕНИЯ", description=f'**У {smember} нет выставленных на продажу средств, предложение было закрыто.**')
							await log_channel.send(embed=embed1)


					elif vtype == "RUB":
						with open('user_balance.json','r', encoding='utf-8') as f:
							balance = json.load(f)

						mntb = balance[str(smember)]["NTB"]
						mrub = balance[str(smember)]["RUB"]
						brub = balance[str(member.name)]["RUB"]

						if mrub >= rub:
							if brub >= rub:
								i[1]["stats"] = False

								balance[str(smember)]["NTB"] -= ntb
								balance[str(smember)]["RUB"] += rub

								balance[str(member.name)]["NTB"] += ntb
								balance[str(member.name)]["RUB"] -= rub

								with open('user_balance.json','w') as f:
									json.dump(balance,f)

								i[1]["buy"].append(member.name)
								with open('user_sales.json','w') as f:
									json.dump(sales,f)

								await member.send(f'Вы продали 4NTB за 5RUB Валерий Крут')
								log_channel = bot.get_channel(898204390412943451)
								embed1 = discord.Embed(color=0x008000, title="ПОКУПКА ВАЛЮТЫ", description=f'**{member} Купил {rub}RUB у {smember}\n[ПРЕДЛОЖЕНИЕ](https://discord.com/channels/880008097370865706/896752866759409705/{int(i[0])})**')
								await log_channel.send(embed=embed1)

								channel1 = bot.get_channel(900380324880597032)
								smessage = await channel1.fetch_message(message_id)
								await smessage.delete()


							else:
								await member.send('У вас недостаточно средств для покупки этого количества валюты.')

						else:
							channel1 = bot.get_channel(900380324880597032)
							smessage = await channel1.fetch_message(message_id)
							await smessage.delete()

							await member.send("У автора этого предложения недостаточно валюты для ее продажи.")

							log_channel = bot.get_channel(898204390412943451)
							embed1 = discord.Embed(color=0x008000, title="ЗАКРЫТИЕ ПРЕДЛОЖЕНИЯ", description=f'**У {smember} нет выставленных на продажу средств, предложение было закрыто.**')
							await log_channel.send(embed=embed1)


				elif payload.emoji.name == "❌":
					if member.name == smember:
						i[1]["stats"] = False
						
						try:
							channel = bot.get_channel(900380294161502229)
							smessage = await channel.fetch_message(int(i[0]))
							await smessage.delete()

							log_channel = bot.get_channel(888053213750779934)
							embed1 = discord.Embed(color=0x008000, title="ЗАКРЫТИЕ ПРЕДЛОЖЕНИЯ", description=f'**{smember} удалил свое предложение.**')
							await log_channel.send(embed=embed1)		

							with open('user_sales.json','w') as f:
								json.dump(sales,f)

						except:
							channel1 = bot.get_channel(900380324880597032)
							smessage2 = await channel1.fetch_message(int(i[0]))
							await smessage2.delete()

							log_channel = bot.get_channel(888053213750779934)
							embed1 = discord.Embed(color=0x008000, title="ЗАКРЫТИЕ ПРЕДЛОЖЕНИЯ", description=f'**{smember} удалил свое предложение.**')
							await log_channel.send(embed=embed1)		

							with open('user_sales.json','w') as f:
								json.dump(sales,f)


# Welcome
@bot.event
async def on_member_join(member):
	guild = bot.get_guild(880008097370865706)

	if member.guild == guild:
		channel = bot.get_channel(880027455769944074)

		await channel.send(f'{member.mention}')
		embed = discord.Embed(color=0x3C55FA, title="ДОБРО ПОЖАЛОВАТЬ", description=f'ПРИВЕТСТВУЕМ НА НАШЕМ СЕРВЕРЕ **{member.guild.name}**\n\nКЛИКАЙТЕ:\n**💎 [КАК ПОЛУЧИТЬ ДЕНЬГИ?](https://discord.com/channels/880008097370865706/880024762942889994/881782363191910440)\n:white_check_mark: [У МЕНЯ ОСТАЛИСЬ ВОПРОСЫ](https://discord.com/channels/880008097370865706/880023125062995969/881783726164545566)\n:ng: [НАВИГАЦИЯ](https://discord.com/channels/880008097370865706/880023035262959636/881904501685092382)\n:loud_sound: [НАЧАТЬ ОБЩАТЬСЯ И ЗАРАБАТЫВАТЬ](https://discord.gg/kUYtg9RJjw)**\n\n НАШИ МАГАЗИНЫ:\n**:postbox: [КУПИТЬ МАЙНИНГ ФЕРМУ](https://discord.com/channels/880008097370865706/880025073963122718/886528504068464640)\n:toolbox: [ОТКРЫТЬ КЕЙСЫ](https://discord.com/channels/880008097370865706/889843449300398111/890117698636365824)**\n\nПРИГЛАШАЙТЕ ДРУЗЕЙ, ПРОВОДИТЕ ВРЕМЯ И УЧАВСТВУЙТЕ В РОЗЫГРЫШАХ ЗАРАБАТЫВАЯ ДЕНЬГИ ВМЕСТЕ!')
		embed.set_thumbnail(url="https://cdn.discordapp.com/icons/880008097370865706/e72eb2ad7dcc6e1beca542792fdf88c7.png?size=256")
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

			with open('user_balance.json','w') as f:
				json.dump(balance,f)

		# Farms
		with open('user_farms.json','r', encoding='utf-8') as f:
			user_farms = json.load(f)

		if not member.name in user_farms:
			user_farms[str(member.name)] = {}
			user_farms[str(member.name)]['name'] = str(member.name)
			user_farms[str(member.name)]['farms'] = {}

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

		# User bank
		with open('user_bank.json','r', encoding='utf-8') as f:
			bank = json.load(f)

		bank[str(member.name)] = {}
		bank[str(member.name)]['name'] = member.name
		bank[str(member.name)]['deposit'] = "none"
		bank[str(member.name)]['amount'] = 0
		bank[str(member.name)]['ltime'] = 0
		with open('user_bank.json','w') as f:
			json.dump(bank,f)

		# Sales
		with open('user_sales.json','r', encoding='utf-8') as f:
			sales = json.load(f)

		if not member.name in sales:
			sales[str(member.name)] = {}
			sales[str(member.name)]['name'] = str(member.name)
			sales[str(member.name)]['sales'] = {}

			with open('user_sales.json','w') as f:
				json.dump(sales,f)


		# User Profile
		with open('user_profile.json','r', encoding='utf-8') as f:
			profile = json.load(f)

		if not member.name in sales:
			profile[str(member.name)] = {}
			profile[str(member.name)]['time'] = 0
			profile[str(member.name)]['stats'] = True

			with open('user_profile.json','w') as f:
				json.dump(profile,f)


	else:
		print("Another guild")

# |--------------------------- /REACTION EVENTS ---------------------------|








# |------------------------------- METHODS --------------------------------|
def Farm(member, name, life, amount: float, auto: bool):
	print(f'----------Farm started----------')
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
				mined[str(member)]['RUB'] += round(amount, 2)
				with open('user_balance.json','w') as f:
					json.dump(mined,f)

			elif auto == False:
				with open('user_farms.json','r', encoding='utf-8') as f:
					lfarms = json.load(f)

				for i in lfarms.items():
					if member == i[0]:
						farm_list = i[1]["farms"]
						for i in farm_list.items():
							if i[0] == name:
								i[1]["mined"] += round(amount, 2)
								with open('user_farms.json','w') as f:
									json.dump(lfarms,f)


			# Crash chance
			chance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
			crash = random.choice(chance)
			if crash == 1:
				m_chance += 1
				if m_chance == 15:
					print("----------Farm crashed----------")
					with open('user_farms.json','r', encoding='utf-8') as f:
						farms = json.load(f)

					farm_list = farms[str(member)]['farms']

					for i in farm_list.items():
						if i[0] == str(name):
							i[0] = "none"

					with open('user_farms.json','w') as f:
						json.dump(farms,f)

					stop = True

			elif crash == 0:
				with open('user_farms.json','r', encoding='utf-8') as f:
					farms = json.load(f)

				farm_list = farms[str(member)]['farms']

				for i in farm_list.items():
					if i[0] == str(name):
						i[1]["life_time"] -= 3600

				with open('user_farms.json','w') as f:
					json.dump(farms,f)


		# If Farm die
		job_time = time.time()
		now_time = job_time - start_time
		if now_time >= life:
			print("----------Farm died----------")
			with open('user_farms.json','r', encoding='utf-8') as f:
				farms = json.load(f)

			farm_list = farms[str(member)]['farms']

			for i in farm_list.items():
				if i[0] == str(name):
					i[1]['stats'] = False

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
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM ЗАТЫЧКА", description=f'Панель управления майнинг фермой "FARM ЗАТЫЧКА"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/92f8Cw8/Z.png")
		embed.add_field(name = '**Срок работы:**', value = f'35дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'25 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 3024000, "out": 0.25, "auto": False, "message_id": message.id}
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 3024000, 0.25, False))
		farmth.start()


	elif farm == "FARM GTX":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM GTX", description=f'Панель управления майнинг фермой "FARM GTX"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/RCt8s0K/G.png")
		embed.add_field(name = '**Срок работы:**', value = f'29дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'25 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)


		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 2505600, "out": 0.5, "auto": False, "message_id": message.id}
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 2505600, 0.5, False))
		farmth.start()


	elif farm == "FARM RTX":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM RTX", description=f'Панель управления майнинг фермой "FARM RTX"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/z72pGRR/R.png")
		embed.add_field(name = '**Срок работы:**', value = f'29дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'21 день', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)


		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 2505600, "out": 1.0, "auto": False, "message_id": message.id}
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 2505600, 1.0, False))
		farmth.start()


	elif farm == "FARM ASIC":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM ASIC", description=f'Панель управления майнинг фермой "FARM ASIC"\n\n**АВТОМАТИЧЕСКИЙ ВЫВОД**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/RHfBJvm/A.png")
		embed.add_field(name = '**Срок работы:**', value = f'35дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'21 день', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)


		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 3024000, "out": 1.5, "auto": True, "message_id": message.id}
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 3024000, 1.5, True))
		farmth.start()


	elif farm == "FARM MULTI":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM MULTI", description=f'Панель управления майнинг фермой "FARM MULTI"\n\n**АВТОМАТИЧЕСКИЙ ВЫВОД**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/SmQ7bNk/M.png")
		embed.add_field(name = '**Срок работы:**', value = f'33дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'26 день', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)


		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 2851200, "out": 2.0, "auto": True, "message_id": message.id}
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 2851200, 2.0, True))
		farmth.start()


	elif farm == "FARM BOOST":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM BOOST", description=f'Панель управления майнинг фермой "FARM BOOST"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/rf67N6Y/B.png")
		embed.add_field(name = '**Срок работы:**', value = f'20дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'14 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)


		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 1728000, "out": 0.3, "auto": False, "message_id": message.id}
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 1728000, 3.0, False))
		farmth.start()


	elif farm == "FARM TITAN":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM TITAN", description=f'Панель управления майнинг фермой "FARM TITAN"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/87WYdBB/T.png")
		embed.add_field(name = '**Срок работы:**', value = f'30дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'16 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)


		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 2592000, "out": 4.0, "auto": False, "message_id": message.id}
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 2592000, 4.0, False))
		farmth.start()


	elif farm == "FARM SERVER":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM SERVER", description=f'Панель управления майнинг фермой "FARM SERVER"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/0KDHq9W/S.png")
		embed.add_field(name = '**Срок работы:**', value = f'38дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'13 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)


		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 3283200, "out": 7.0, "auto": False, "message_id": message.id}
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 3283200, 7.0, False))
		farmth.start()


	elif farm == "FARM FACTORY":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM FACTORY", description=f'Панель управления майнинг фермой "FARM FACTORY"\n\n**ВЫВОД АВТОМАТИЧЕСКИЙ**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/NL6qq9w/F.png")
		embed.add_field(name = '**Срок работы:**', value = f'37дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'13 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)


		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 3196800, "out": 14.0, "auto": True, "message_id": message.id}
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 3196800, 14.0, True))
		farmth.start()


	elif farm == "FARM QUANTUM":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM QUANTUM", description=f'Панель управления майнинг фермой "FARM QUANTUM"\n\n**ВЫВОД АВТОМАТИЧЕСКИЙ**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/JBnsbKS/Q.png")
		embed.add_field(name = '**Срок работы:**', value = f'42дня', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'10 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)


		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 3628800, "out": 25.0, "auto": True, "message_id": message.id}
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 3628800, 25.0, True))
		farmth.start()


	elif farm == "FARM ПЛАТА":
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM ПЛАТА", description=f'Панель управления майнинг фермой "FARM ПЛАТА"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/pd6w8dt/plata.png")
		embed.add_field(name = '**Срок работы:**', value = f'11дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'10 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		if str(farm) in farms[str(member.name)]["farms"]:
			print('IN')


			farms[str(member.name)]["farms"][f'{str(farm)}']["out"] += 0.3
			farms[str(member.name)]["farms"][f'{str(farm)}']["message_id"].append(message.id)

		else:
			print('NO')
			farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "mined": 0, "life_time": 950400, "out": 0.3, "auto": False, "message_id": [message.id]}


		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member.name, farm, 950400, 0.3, False))
		farmth.start()


def Deposit(member, amount, percent, ltime):
	time.sleep(ltime)

	percent1 = amount / 100 * percent
	money = amount + percent1

	with open('user_balance.json','r', encoding='utf-8') as f:
		user_balance = json.load(f)

	user_balance[str(member)]['RUB'] += round(money, 2)

	with open('user_balance.json','w') as f:
		json.dump(user_balance,f)

	with open('user_bank.json','r', encoding='utf-8') as f:
		bank = json.load(f)

	bank[str(member)] = {}
	bank[str(member)]['deposit'] = "none"
	with open('user_bank.json','w') as f:
		json.dump(bank,f)


# Sending a random images
async def RandomImages():
	while True:
		await asyncio.sleep(30)
		timezone = datetime.timezone(datetime.timedelta(hours=3))

		date = datetime.datetime.now(timezone)
		if int(date.hour) == 21 and date.minute == 46:
			channel = bot.get_channel(881634315514019881)
			with open('bot_constants.json','r', encoding='utf-8') as f:
				constants = json.load(f)

			images = constants["images"]
			image = images[2]
			constants["act_image"] = image
			print(f'Send image: {image}')

			await channel.send(image)

			with open('bot_constants.json','w') as f:
				json.dump(constants,f)

			await asyncio.sleep(30)

		elif int(date.hour) == 21 and date.minute == 39:
			channel = bot.get_channel(896752866759409705)
			with open('bot_constants.json','r', encoding='utf-8') as f:
				constants = json.load(f)

			images = constants["images"]
			image = images[1]
			constants["act_image"] = image
			print(f'Send image: {image}')

			await channel.send(image)

			with open('bot_constants.json','w') as f:
				json.dump(constants,f)

			await asyncio.sleep(30)

		elif int(date.hour) == 21 and date.minute == 35:
			channel = bot.get_channel(896752866759409705)
			with open('bot_constants.json','r', encoding='utf-8') as f:
				constants = json.load(f)

			images = constants["images"]
			image = images[0]
			constants["act_image"] = image
			print(f'Send image: {image}')

			await channel.send(image)

			with open('bot_constants.json','w') as f:
				json.dump(constants,f)

			await asyncio.sleep(30)

		elif int(date.hour) == 3 and date.minute == 50:
			channel = bot.get_channel(896752866759409705)
			with open('bot_constants.json','r', encoding='utf-8') as f:
				constants = json.load(f)

			images = constants["images"]
			image = images[3]
			constants["act_image"] = image
			print(f'Send image: {image}')

			await channel.send(image)

			with open('bot_constants.json','w') as f:
				json.dump(constants,f)

			await asyncio.sleep(30)



# |------------------------------- /METHODS -------------------------------|








# |------------------------------ COMMANDS ------------------------------|
@bot.command()
async def act(ctx):
	with open('bot_constants.json','r', encoding='utf-8') as f:
		constants = json.load(f)

	image = constants["act_image"]
	await ctx.send(str(image))


@bot.command()
async def bank1(ctx, amount):
	guild1 = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild1:
		print('In guild')

	else:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		balance = user_balance[str(ctx.message.author.name)]['RUB']

		if int(amount) >= 20 and int(amount) <= 500:
			if user_balance[str(ctx.message.author.name)]['RUB'] >= int(amount):
				user_balance[str(ctx.message.author.name)]['RUB'] -= round(int(amount), 2)
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

				with open('user_bank.json','r', encoding='utf-8') as f:
					bank = json.load(f)

				bank[str(ctx.message.author.name)]['deposit'] = 1
				bank[str(ctx.message.author.name)]['amount'] = int(amount)
				bank[str(ctx.message.author.name)]['ltime'] = 2160000

				with open('user_bank.json','w') as f:
					json.dump(bank,f)

				deposit = Thread(target=Deposit, args=(ctx.message.author.name, int(amount), 10, 2160000))
				deposit.start()

				await ctx.message.author.send(f'Вы положили {int(amount)}RUB под {10}%')
				log = bot.get_channel(888053213750779934)
				embed1 = discord.Embed(color=0x388E3C, title="ДЕПОЗИТ", description=f'**`{ctx.message.author}` Положил `{int(amount)}`RUB под `{10}%`**')
				await log.send(embed=embed1)

			elif user_balance[str(ctx.message.author.name)]['RUB'] < int(amount):
				await ctx.message.author.send('У вас недостаточно средств.')

		else:
			await ctx.message.author.send('Сумма должна быть не меньше 20 RUB, и не больше 500 RUB.')

@bot.command()
async def bank2(ctx, amount):
	guild1 = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild1:
		print('In guild')

	else:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		balance = user_balance[str(ctx.message.author.name)]['RUB']

		if int(amount) >= 400 and int(amount) <= 2000:
			if balance >= 400:
				user_balance[str(ctx.message.author.name)]['RUB'] -= round(int(amount), 2)
				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

				bank[str(ctx.message.author.name)]['deposit'] = 1
				bank[str(ctx.message.author.name)]['amount'] = int(amount)
				bank[str(ctx.message.author.name)]['ltime'] = 2160000
				with open('user_bank.json','w') as f:
					json.dump(bank,f)

				deposit = Thread(target=Deposit, args=(ctx.message.author.name, int(amount), 20, 3888000))
				deposit.start()

				await ctx.message.author.send(f'Вы положили {int(amount)}RUB под {20}%')
				log = bot.get_channel(888053213750779934)
				embed1 = discord.Embed(color=0x388E3C, title="ДЕПОЗИТ", description=f'**`{ctx.message.author}` Положил `{int(amount)}`RUB под `{10}%`**')
				await log.send(embed=embed1)

			elif balance <= 400:
				await ctx.message.author.send('У вас недостаточно средств.')

		else:
			await ctx.message.author.send('Сумма должна быть не меньше 300 RUB, и не больше 1000 RUB.')



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
		embed = discord.Embed(color=0x3C55FA, description=f'[**ДЛЯ ПОПОЛНЕНИЯ БАЛАНСА, НАЖМИТЕ НА ЭТО СООБЩЕНИЕ**](https://discord.com/channels/880008097370865706/882644436608241715/887765170846314506)\n\n1.Нажав на синий текст, вы перейдете в спец.канал\n2.Откройте чат с менеджером, перейдите по ссылке пополнения баланса.\n3.После пополнения отпишите  в тот же чат что вы пополнили баланс\n4. В течении часа ваши средства придут на счет\n\n*Возможна задержка пополнения баланса, это связанно с видом платежной системы\nСреднее время  обработки  30 мин  - 5 часов\n\n__СПОСОБ ОПЛАТЫ КАРТОЙ ДОСТУПЕН ПРИ ВЫБОРЕ МЕТОДА ОПЛАТЫ QIWI__')
		await ctx.send(embed=embed)


@bot.command()
async def get(ctx):
	guild = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild:
		print('In guild')

	else:
		embed = discord.Embed(color=0x3C55FA, description="[**ДЛЯ ВЫВОДА БАЛАНСА, НАЖМИТЕ НА ЭТО СООБЩЕНИЕ**](https://discord.com/channels/880008097370865706/882644436608241715/887765170846314506)\n\n1.Нажав на синий текст, вы перейдете в спец.канал\n2.Откройте чат с менеджером, напишите сумму реквизиты\n3.Для подтверждения вывода укажите доп.Информацию - пополняли когда-либо баланс, выводили когда-либо баланс?\n4. В течении нескольких часов ваши средства придут на счет\n\n*Возможна задержка вывода баланса, это связанно с видом платежной системы и скорости обработки вашей заявки\nСреднее время  обработки  30 мин - 7 часов")
		await ctx.send(embed=embed)


@bot.command()
async def promo(ctx, code):
	guild = bot.get_guild(880008097370865706)
	with open('promocodes.json','r', encoding='utf-8') as f:
		codes = json.load(f)

	if ctx.message.guild == guild:
		print('In guild')

	else:
		for i in codes.items():
			if code == i[0]:
				with open('user_balance.json','r', encoding='utf-8') as f:
					user_balance = json.load(f)

				mtype = i[1]["mtype"]
				money = i[1]['money']
				activations = i[1]['activations']
				farm = i[1]['farm']
				if activations > 0:

					if money != 0:
						user_balance[str(ctx.message.author.name)][f'{mtype}'] += money
						i[1]['activations'] -= 1

						with open('user_balance.json','w') as f:
							json.dump(user_balance,f)

					elif farm != "none":
						await CreateFarmChannel(ctx.message.author, str(farm))
						i[1]['activations'] -= 1

					with open('promocodes.json','w') as f:
						json.dump(codes,f)

					await ctx.message.author.send(f'Вы активировали промокод `{code}`')
					log = bot.get_channel(923934134177497178)
					embed1 = discord.Embed(color=0x388E3C, title="АКТИВАЦИЯ ПРОМОКОДА", description=f'**`{ctx.message.author}` Активировал промокод `{code}`**')
					await log.send(embed=embed1)

				elif activations <= 0:
					await ctx.message.author.send('Этот промокод больше нельзя активировать.')

# Create promocodes
@bot.command()
async def addpromo(ctx, ctype, name, activations, mtype=None, money=None):
	if ctx.message.author.id == 663424295854407692:
		with open('promocodes.json','r', encoding='utf-8') as f:
			codes = json.load(f)

		if ctype == "cash":	
			if  mtype != None and money != None :
				if mtype == "RUB" or mtype == "NTB":
					codes[str(name)] = {"mtype": f'{mtype}', "money": int(money), "farm": "none", "activations": int(activations)}
					await ctx.message.add_reaction('✅')

				else:
					await ctx.send(f'Валюты {mtype} не существует.')

		elif ctype == "farm":
			if mtype != None and money == None:
				codes[str(name)] = {"mtype": "RUB", "money": 0, "farm": f'FARM {mtype}', "activations": int(activations)}
				await ctx.message.add_reaction('✅')

		else:
			await ctx.send("Ошибка в синтаксисе команды.\nДля валюты: `!addpromo cash Название Активации Валюта Количество`\nДля фермы: `!addpromo farm Название Активации Ферма`")

		with open('promocodes.json','w') as f:
			json.dump(codes,f)

	else:
		print("addpromo: Not member")


# Time control
timelist = []
supportlist =[]
hmalist = []
def TimeControl(member):
	print(f'TimeControl(): Start Thread for {member}')
	stats = False
	while not stats:
		time.sleep(60)
		with open('user_profile.json','r', encoding='utf-8') as f:
			profile = json.load(f)

		stats = profile[str(member)]["stats"]

		profile[str(member)]["time"] += 1

		with open('user_profile.json','w') as f:
			json.dump(profile,f)


@bot.command()
#@commands.has_any_role(881603894449406022, 895761325236564008, 881141342959439882, 882611860027867136, 881141987108085770, 880357242346553374, 880357827699433513)
async def start(ctx):
	guild = bot.get_guild(880008097370865706)
	with open('user_profile.json','r', encoding='utf-8') as f:
		profile = json.load(f)
		
	ustats = profile[str(ctx.message.author.name)]["stats"]
	profile[str(ctx.message.author.name)]["stats"] = False

	if ustats != False:
		moderation = guild.get_role(880357242346553374)
		helper = guild.get_role(880357827699433513)
		support = guild.get_role(881141342959439882)
		with open('user_profile.json','w') as f:
			json.dump(profile,f)	

		newtimer = Thread(target=TimeControl, args=[str(ctx.message.author.name)])
		newtimer.start()
		await ctx.message.add_reaction('✅')
		embed = embed = discord.Embed()

		if len(timelist) == 0:
			if support in ctx.message.author.roles:
				embed = discord.Embed(color=0x2E62FF, title="Рабочая смена", description=f'Сотрудники на смене:\n\nSupport\n-[{ctx.message.author.name}]')
				supportlist.append(ctx.message.author.name)

			elif moderation in ctx.message.author.roles or helper in ctx.message.author.roles:
				embed = discord.Embed(color=0x2E62FF, title="Рабочая смена", description=f'Сотрудники на смене:\n\nSupport\n{supportlist}\n\nHelper, moderator, administrator\n-[{ctx.message.author.name}]')
				hmalist.append(ctx.message.author.name)

			log = bot.get_channel(907906146633936899)
			log1 = bot.get_channel(908698309466685471)
			await log.send(embed = embed)
			await log1.send(embed=embed)
			timelist.append(ctx.message.author.name)

		elif len(timelist) > 0:
			if support in ctx.message.author.roles:
				supportlist.append(ctx.message.author.name)

			elif moderation in ctx.message.author.roles or helper in ctx.message.author.roles:
				hmalist.append(ctx.message.author.name)

			log = bot.get_channel(907906146633936899)
			log1 = bot.get_channel(908698309466685471)
			embed = discord.Embed(color=0x2E62FF, title="Рабочая смена", description=f'Сотрудники на смене:\n\nSupport\n{supportlist}\n\nHelper, moderator, administrator\n-{hmalist}')
			await log.send(embed = embed)
			await log1.send(embed=embed)
			timelist.append(ctx.message.author.name)
	else:
		print("start(): ustats = True")
		

@bot.command()
@commands.has_any_role(881603894449406022, 895761325236564008, 881141342959439882, 882611860027867136, 881141987108085770, 880357242346553374, 880357827699433513)
async def stime(ctx, *, member = None):
	guild = bot.get_guild(880008097370865706)
	if member != None:
		if ctx.message.author.id == 663424295854407692:
			with open('user_profile.json','r', encoding='utf-8') as f:
				profile = json.load(f)

			minutes = profile[str(member)]["time"]
			hours = round(minutes / 60)
			nminutes = round(minutes - hours * 60)

			
			if hours < 1 or hours == 0:
				await ctx.send(f'{member} Отработал:\nЧасы: `0`\nМинуты: `{minutes}`')

			elif hours >= 1:
				await ctx.send(f'{member} Отработал:\nЧасы: `{hours}`\nМинуты: `{nminutes}`')

		else:
			await ctx.send('Ошибка в синтаксисе команды.')

	else:
		with open('user_profile.json','r', encoding='utf-8') as f:
			profile = json.load(f)

		minutes = profile[str(ctx.message.author.name)]["time"]
		hours = round(minutes / 60)
		nminutes = round(minutes - hours * 60)

		
		if hours < 1 or hours == 0:
			await ctx.send(f'{ctx.message.author.mention} Отработал:\nЧасы: `0`\nМинуты: `{minutes}`')

		elif hours >= 1:
			await ctx.send(f'{ctx.message.author.mention} Отработал:\nЧасы: `{hours}`\nМинуты: `{nminutes}`')


@bot.command()
#@commands.has_any_role(881603894449406022, 895761325236564008, 881141342959439882, 882611860027867136, 881141987108085770, 880357242346553374, 880357827699433513)
async def stop(ctx):
	guild = bot.get_guild(880008097370865706)
	with open('user_profile.json','r', encoding='utf-8') as f:
		profile = json.load(f)

	profile[str(ctx.message.author.name)]["stats"] = True
	with open('user_profile.json','w') as f:
		json.dump(profile,f)

	await ctx.message.add_reaction('✅')

	timelist.remove(str(ctx.message.author.name))
	supportlist.remove(str(ctx.message.author.name))
	hmalist.remove(str(ctx.message.author.name))

	log = bot.get_channel(907906146633936899)
	log1 = bot.get_channel(908698309466685471)
	embed = discord.Embed(color=0x2E62FF, title="Рабочая смена", description=f'Сотрудники на смене:\n\nSupport\n{supportlist}\n\nHelper, moderator, administrator\n-{hmalist}')
	await log.send(embed = embed)
	await log1.send(embed=embed)
	timelist.append(ctx.message.author.name)


@bot.command()
@commands.has_any_role(881603894449406022, 895761325236564008, 881141342959439882, 882611860027867136, 881141987108085770, 880357242346553374, 880357827699433513)
async def clean(ctx, member: discord.Member):
	guild = bot.get_guild(880008097370865706)
	if ctx.member.id == 663424295854407692:
		guild = bot.get_guild(880008097370865706)
		with open('user_profile.json','r', encoding='utf-8') as f:
			profile = json.load(f)

		profile[str(member.name)]["time"] = 0
		with open('user_profile.json','w') as f:
			json.dump(profile,f)

		await ctx.message.add_reaction('✅')

	else:
		print("clean(): not member using.")


@bot.command()
#@commands.has_any_role(881603894449406022, 895761325236564008, 881141342959439882, 882611860027867136, 881141987108085770, 880357242346553374, 880357827699433513)
async def admins(ctx):
	await ctx.send(f'Сотрудники на смене: {timelist}')



# ------------------------ Moderation ------------------------|
# Ban
@bot.command()
@commands.has_any_role(881603894449406022, 880357242346553374, 895761325236564008, 881141342959439882, 881141987108085770)
async def ban(ctx, member: discord.Member, time: int, *, about: str):
	await ctx.message.add_reaction('✅')
	getrole = discord.utils.get(ctx.guild.roles, id = 888483227080224779)
	await member.add_roles(getrole)
	embed = discord.Embed(color = 0xff0000, description = f'Вам ограничили доступ к серверу NEXT InvesT по причине: {about} на {time} минут.')
	await member.send(embed = embed)

	log = bot.get_channel(897546962495225949)
	embed1 = discord.Embed(color=0x388E3C, title="БАН", description=f'**`{member}` Был забанен `{ctx.message.author}` на `{time} минут` по причине\n\n```diff\n- {about}\n```**')
	await log.send(embed=embed1)

	await asyncio.sleep(time*60)
	await member.remove_roles(getrole)

# Unban
@bot.command()
@commands.has_any_role(881141987108085770, 881141342959439882, 895761325236564008, 881603894449406022)
async def unban(ctx, member: discord.Member):
	await ctx.message.add_reaction('✅')
	getrole = discord.utils.get(ctx.guild.roles, id = 888483227080224779)
	await member.remove_roles(getrole)

	log = bot.get_channel(897546962495225949)
	embed1 = discord.Embed(color=0x388E3C, title="РАЗБАН", description=f'**`{member.name}` Был разбанен `{ctx.message.author}`**')
	await log.send(embed=embed1)

# Mute
@bot.command()
@commands.has_any_role(881141342959439882, 881141987108085770, 880357827699433513, 880357242346553374, 881603894449406022, 895761325236564008)
async def mute(ctx, member: discord.Member, time: int, *, about: str):
	await ctx.message.add_reaction('✅')
	getrole = discord.utils.get(ctx.guild.roles, id = 888461992824799283)
	await member.add_roles(getrole)
	embed = discord.Embed(color = 0xff0000, description = f'Вам ограничили письменный доступ к серверу NEXT InvesT по причине: {about} на {time} минут.')
	await member.send(embed = embed)

	log = bot.get_channel(897546962495225949)
	embed1 = discord.Embed(color=0x388E3C, title="МЬЮТ", description=f'**`{member.name}` Был замьючен `{ctx.message.author}` на `{time} минут` по причине\n\n```diff\n- {about}\n```**')
	await log.send(embed=embed1)

	await asyncio.sleep(time*60)
	await member.remove_roles(getrole)

# Unmute
@bot.command()
@commands.has_any_role(881141342959439882, 881141987108085770, 880357242346553374, 895761325236564008, 881603894449406022)
async def unmute(ctx, member: discord.Member):
	await ctx.message.add_reaction('✅')
	getrole = discord.utils.get(ctx.guild.roles, id = 888461992824799283)
	await member.remove_roles(getrole)

	log = bot.get_channel(897546962495225949)
	embed1 = discord.Embed(color=0x388E3C, title="РАЗМЬЮТ", description=f'**`{member.name}` Был размьючен `{ctx.message.author}`**')
	await log.send(embed=embed1)


# ubal
@bot.command()
#@commands.has_any_role(881141342959439882, 881141987108085770)
async def ubal(ctx, member: discord.Member, ctype, op: str, amount: int):
	with open('user_balance.json','r', encoding='utf-8') as f:
		user_balance = json.load(f)
		
	if ctx.message.author.id == 663424295854407692:
		await ctx.message.add_reaction('✅')
		if op == "=":
			if ctype == "RUB":
				user_balance[str(member.name)]['RUB'] = amount
				await ctx.message.add_reaction('✅')

			elif ctype == "NTB":
				user_balance[str(member.name)]['NTB'] = amount
				await ctx.message.add_reaction('✅')

			else:
				await ctx.send('Указан неверный тип валюты.')

		elif op == "+":
			if ctype == "RUB":
				user_balance[str(member.name)]['RUB'] += amount
				await ctx.message.add_reaction('✅')

			elif ctype == "NTB":
				user_balance[str(member.name)]['NTB'] += amount
				await ctx.message.add_reaction('✅')

			else:
				await ctx.send('Указан неверный тип валюты.')

		elif op == "-":
			if ctype == "RUB":
				user_balance[str(member.name)]['RUB'] -= amount
				await ctx.message.add_reaction('✅')

			elif ctype == "NTB":
				user_balance[str(member.name)]['NTB'] -= amount
				await ctx.message.add_reaction('✅')

			else:
				await ctx.send('Указан неверный тип валюты.')

		with open('user_balance.json','w') as f:
			json.dump(user_balance,f)	

	else:
		print("Not man")


@bot.command()
async def bal(ctx, member: discord.Member):
	if ctx.message.author.id == 663424295854407692 or ctx.message.author.id == 677453905227022349:
		with open('user_balance.json','r', encoding='utf-8') as f:
			balance = json.load(f)

		rub = balance[str(member.name)]['RUB']
		ntb = balance[str(member.name)]['NTB']

		await ctx.send(f'**{member}**: {rub}RUB **|** {ntb}NTB')

	else:
		print('bal(): Not member')

# Super money boxes
@bot.command()
async def box(ctx, box: int, amount: int):
	guild = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild:
		print('In guild')

	else:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		balance = user_balance[str(ctx.message.author.name)]['RUB']

		# Box 1
		if box == 1:
			if amount >= 1 and amount <= 250:
				if balance > 1:
					with open('super_boxes.json','r', encoding='utf-8') as f:
						super_boxes = json.load(f)

					target = super_boxes["box1"]["target"]
					invested = super_boxes["box1"]["invested"]
					members = super_boxes["box1"]["members"]
					percent = super_boxes["box1"]["percent"]
					stats = super_boxes["box1"]["stats"]
					ones = super_boxes["box1"]["ones"]

					if stats == True:
						# if box2 filled
						box2t = super_boxes["box2"]["target"]
						box2i = super_boxes["box2"]["invested"]
						if box2i >= box2t:
							# logs
							logs = guild.get_channel(892584515162210324)
							embed = discord.Embed(color=0x00a550, title="ЗАПОЛНЕНИЕ СУПЕР КОПИЛКИ №2 И ВЫВОД №1", description=f'Список вложившихся в супер копилку №1 участников:\n```\n{members}\n```')
							await logs.send(embed=embed)

							for i in members.items():
								user = i[0]
								user_amount = i[1]
								percent1 = user_amount / 100 * percent
								money = user_amount + percent1
								print(money)

								#super_boxes["box1"]["members"][f'{str(ctx.message.author.name)}'] = 0
								#super_boxes["box1"]["stats"] = False
								#with open('super_boxes.json','w') as f:
								#	json.dump(super_boxes,f)

								with open('user_balance.json','r', encoding='utf-8') as f:
									user_balance = json.load(f)
								user_balance[str(user)]['RUB'] += money
								with open('user_balance.json','w') as f:
									json.dump(user_balance,f)


						elif box2i <= box2t:
							super_boxes["box1"]["invested"] += amount

							print(members)
							if not ctx.message.author.name in ones:
								super_boxes["box1"]["members"][f'{str(ctx.message.author.name)}'] = int(amount)
								super_boxes["box1"]["ones"].append(ctx.message.author.name)

							elif ctx.message.author.name in ones:
								super_boxes["box1"]["members"][f'{str(ctx.message.author.name)}'] += int(amount)


							with open('super_boxes.json','w') as f:
								json.dump(super_boxes,f)

							user_balance[str(ctx.message.author.name)]['RUB'] -= amount
							with open('user_balance.json','w') as f:
								json.dump(user_balance,f)

							await ctx.message.author.send(f'Вы вложили {amount}RUB в копилку №1')


							channel = bot.get_channel(888500024214966282)
							m = await channel.fetch_message(893397579663044629)
							ac = round(target / 4)
							at = round(target / 3)
							po = round(target / 2)
							dt = at + at

							with open('super_boxes.json','r', encoding='utf-8') as f:
								super_boxes = json.load(f)

							invested = super_boxes["box1"]["invested"]
							if invested <= ac:# 1/10
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №1", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧⬛⬛⬛⬛⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested > ac and invested < at + 20:# 1/4 -
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №1", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧⬛⬛⬛⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested > at + 20 and invested <= po:# 1/2 -
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №1", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧⬛⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested >= po and invested < dt + 95:# 1/2 +
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №1", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested >= po and invested < dt + 70:# 1/2 +
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №1", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛')
								await m.edit(embed = box)

							elif invested > dt + 95:
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №1", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧')
								await m.edit(embed = box)

							# logs
							logs = guild.get_channel(892584515162210324)
							embed = discord.Embed(color=0x00a550, title="ВКЛАД В СУПЕР КОПИЛКУ", description=f'Участник {ctx.message.author} положил {amount} в копилку №1\n\nДля заполнения копилки осталось вложить `{target - invested}`')
							await logs.send(embed=embed)

					else:
						await ctx.message.author.send("Вы не можете вложится в эту копилку так как она уже заполнена.")	

				else:
					await ctx.message.author.send("У вас недостаточно средств.")
			else:
				await ctx.message.author.send("Сумма вложения должна быть не менее 1 и не боле 250RUB.")





		# Box 2
		elif box == 2:
			if amount >= 1 and amount <= 350:
				if balance > 1:
					with open('super_boxes.json','r', encoding='utf-8') as f:
						super_boxes = json.load(f)

					target = super_boxes["box2"]["target"]
					invested = super_boxes["box2"]["invested"]
					members = super_boxes["box2"]["members"]
					percent = super_boxes["box2"]["percent"]
					stats = super_boxes["box2"]["stats"]
					ones = super_boxes["box2"]["ones"]

					if stats == True:
						# if box3 filled
						box3t = super_boxes["box3"]["target"]
						box3i = super_boxes["box3"]["invested"]
						if box3i >= box3t:

							# logs
							logs = guild.get_channel(892584515162210324)
							embed = discord.Embed(color=0x00a550, title="ЗАПОЛНЕНИЕ СУПЕР КОПИЛКИ №3 И ВЫВОД №2", description=f'Список вложившихся в супер копилку №2 участников:\n```\n{members}\n```')
							await logs.send(embed=embed)

							for i in members.items():
								user = i[0]
								user_amount = i[1]
								percent1 = user_amount / 100 * percent
								money = user_amount + percent1
								print(money)

								#super_boxes["box2"]["members"][f'{str(ctx.message.author.name)}'] = 0
								#super_boxes["box2"]["stats"] = False
								#with open('super_boxes.json','w') as f:
								#	json.dump(super_boxes,f)

								with open('user_balance.json','r', encoding='utf-8') as f:
									user_balance = json.load(f)
								user_balance[str(user)]['RUB'] += money
								with open('user_balance.json','w') as f:
									json.dump(user_balance,f)


						elif box3i <= box3t:
							super_boxes["box2"]["invested"] += amount

							print(members)
							if not ctx.message.author.name in ones:
								super_boxes["box2"]["members"][f'{str(ctx.message.author.name)}'] = int(amount)
								super_boxes["box2"]["ones"].append(ctx.message.author.name)

							elif ctx.message.author.name in ones:
								super_boxes["box2"]["members"][f'{str(ctx.message.author.name)}'] += int(amount)


							with open('super_boxes.json','w') as f:
								json.dump(super_boxes,f)

							user_balance[str(ctx.message.author.name)]['RUB'] -= amount
							with open('user_balance.json','w') as f:
								json.dump(user_balance,f)

							await ctx.message.author.send(f'Вы вложили {amount}RUB в копилку №2')


							channel = bot.get_channel(888500024214966282)
							m = await channel.fetch_message(893397582523547678)
							ac = round(target / 4)
							at = round(target / 3)
							po = round(target / 2)
							dt = at + at

							with open('super_boxes.json','r', encoding='utf-8') as f:
								super_boxes = json.load(f)

							invested = super_boxes["box2"]["invested"]
							if invested <= ac:# 1/10
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №2", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧⬛⬛⬛⬛⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested > ac and invested < at + 20:# 1/4 -
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №2", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧⬛⬛⬛⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested > at + 20 and invested <= po:# 1/2 -
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №2", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧⬛⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested >= po and invested < dt + 95:# 1/2 +
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №2", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested >= po and invested < dt + 70:# 1/2 +
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №2", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛')
								await m.edit(embed = box)

							elif invested > dt + 95:
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №2", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧')
								await m.edit(embed = box)

							# logs
							logs = guild.get_channel(892584515162210324)
							embed = discord.Embed(color=0x00a550, title="ВКЛАД В СУПЕР КОПИЛКУ", description=f'Участник {ctx.message.author} положил {amount} в копилку №2\n\nДля заполнения копилки осталось вложить `{target - invested}`')
							await logs.send(embed=embed)


							# if box2 filled
							if invested >= target:
								members1 = super_boxes["box1"]["members"]
								# logs
								logs = guild.get_channel(892584515162210324)
								embed = discord.Embed(color=0x00a550, title="ЗАПОЛНЕНИЕ СУПЕР КОПИЛКИ №2 И ВЫВОД №1", description=f'Список вложившихся в супер копилку №1 участников:\n```\n{members}\n```')
								await logs.send(embed=embed)

								for i in members1.items():
									user = i[0]
									user_amount = i[1]
									percent1 = user_amount / 100 * percent
									money = user_amount + percent1
									print(money)

									#super_boxes["box1"]["members"][f'{str(ctx.message.author.name)}'] = 0
									#super_boxes["box1"]["stats"] = False
									#with open('super_boxes.json','w') as f:
									#	json.dump(super_boxes,f)

									with open('user_balance.json','r', encoding='utf-8') as f:
										user_balance = json.load(f)
									user_balance[str(user)]['RUB'] += money
									with open('user_balance.json','w') as f:
										json.dump(user_balance,f)


					else:
						await ctx.message.author.send("Вы не можете вложится в эту копилку так как она уже заполнена.")	

				else:
					await ctx.message.author.send("У вас недостаточно средств.")
			else:
				await ctx.message.author.send("Сумма вложения должна быть не менее 1 и не боле 350RUB.")




		# Box 3
		elif box == 3:
			if amount >= 1 and amount <= 450:
				if balance > 1:
					with open('super_boxes.json','r', encoding='utf-8') as f:
						super_boxes = json.load(f)

					target = super_boxes["box3"]["target"]
					invested = super_boxes["box3"]["invested"]
					members = super_boxes["box3"]["members"]
					percent = super_boxes["box3"]["percent"]
					stats = super_boxes["box3"]["stats"]
					ones = super_boxes["box3"]["ones"]

					if stats == True:
						# if box4 filled
						box4t = super_boxes["box4"]["target"]
						box4i = super_boxes["box4"]["invested"]
						if box4i >= box4t:

							# logs
							logs = guild.get_channel(892584515162210324)
							embed = discord.Embed(color=0x00a550, title="ЗАПОЛНЕНИЕ СУПЕР КОПИЛКИ №4 И ВЫВОД №3", description=f'Список вложившихся в супер копилку №3 участников:\n```\n{members}\n```')
							await logs.send(embed=embed)

							for i in members.items():
								user = i[0]
								user_amount = i[1]
								percent1 = user_amount / 100 * percent
								money = user_amount + percent1
								print(money)

								#super_boxes["box2"]["members"][f'{str(ctx.message.author.name)}'] = 0
								#super_boxes["box2"]["stats"] = False
								#with open('super_boxes.json','w') as f:
								#	json.dump(super_boxes,f)

								with open('user_balance.json','r', encoding='utf-8') as f:
									user_balance = json.load(f)
								user_balance[str(user)]['RUB'] += money
								with open('user_balance.json','w') as f:
									json.dump(user_balance,f)


						elif box4i <= box4t:
							super_boxes["box3"]["invested"] += amount

							print(members)
							if not ctx.message.author.name in ones:
								super_boxes["box3"]["members"][f'{str(ctx.message.author.name)}'] = int(amount)
								super_boxes["box3"]["ones"].append(ctx.message.author.name)

							elif ctx.message.author.name in ones:
								super_boxes["box3"]["members"][f'{str(ctx.message.author.name)}'] += int(amount)


							with open('super_boxes.json','w') as f:
								json.dump(super_boxes,f)

							user_balance[str(ctx.message.author.name)]['RUB'] -= amount
							with open('user_balance.json','w') as f:
								json.dump(user_balance,f)

							await ctx.message.author.send(f'Вы вложили {amount}RUB в копилку №3')


							channel = bot.get_channel(888500024214966282)
							m = await channel.fetch_message(894214944034279435)
							ac = round(target / 4)
							at = round(target / 3)
							po = round(target / 2)
							dt = at + at

							with open('super_boxes.json','r', encoding='utf-8') as f:
								super_boxes = json.load(f)

							invested = super_boxes["box3"]["invested"]
							if invested <= ac:# 1/10
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №3", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧⬛⬛⬛⬛⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested > ac and invested < at + 20:# 1/4 -
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №3", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧⬛⬛⬛⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested > at + 20 and invested <= po:# 1/2 -
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №3", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧⬛⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested >= po and invested < dt + 95:# 1/2 +
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №3", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧⬛⬛⬛⬛')
								await m.edit(embed = box)

							elif invested >= po and invested < dt + 70:# 1/2 +
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №2", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛')
								await m.edit(embed = box)

							elif invested > dt + 95:
								box = discord.Embed(color=0x2E62FF, title="Супер копилка №2", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧')
								await m.edit(embed = box)

							# logs
							logs = guild.get_channel(892584515162210324)
							embed = discord.Embed(color=0x00a550, title="ВКЛАД В СУПЕР КОПИЛКУ", description=f'Участник {ctx.message.author} положил {amount} в копилку №2\n\nДля заполнения копилки осталось вложить `{target - invested}`')
							await logs.send(embed=embed)


							# if box3 filled
							if invested >= target:
								members1 = super_boxes["box2"]["members"]
								# logs
								logs = guild.get_channel(892584515162210324)
								embed = discord.Embed(color=0x00a550, title="ЗАПОЛНЕНИЕ СУПЕР КОПИЛКИ №3 И ВЫВОД №2", description=f'Список вложившихся в супер копилку №2 участников:\n```\n{members}\n```')
								await logs.send(embed=embed)

								for i in members1.items():
									user = i[0]
									user_amount = i[1]
									percent1 = user_amount / 100 * percent
									money = user_amount + percent1
									print(money)

									#super_boxes["box1"]["members"][f'{str(ctx.message.author.name)}'] = 0
									#super_boxes["box1"]["stats"] = False
									#with open('super_boxes.json','w') as f:
									#	json.dump(super_boxes,f)

									with open('user_balance.json','r', encoding='utf-8') as f:
										user_balance = json.load(f)
									user_balance[str(user)]['RUB'] += money
									with open('user_balance.json','w') as f:
										json.dump(user_balance,f)


					else:
						await ctx.message.author.send("Вы не можете вложится в эту копилку так как она уже заполнена.")	

				else:
					await ctx.message.author.send("У вас недостаточно средств.")
			else:
				await ctx.message.author.send("Сумма вложения должна быть не менее 1 и не боле 450RUB.")




		# Box 4
		elif box == 4:
			if amount >= 1 and amount <= 650:
				if balance > 1:
					with open('super_boxes.json','r', encoding='utf-8') as f:
						super_boxes = json.load(f)

					target = super_boxes["box4"]["target"]
					invested = super_boxes["box4"]["invested"]
					members = super_boxes["box4"]["members"]
					percent = super_boxes["box4"]["percent"]
					stats = super_boxes["box4"]["stats"]
					ones = super_boxes["box4"]["ones"]
					super_boxes["box4"]["invested"] += amount

					print(members)
					if not ctx.message.author.name in ones:
						super_boxes["box4"]["members"][f'{str(ctx.message.author.name)}'] = int(amount)
						super_boxes["box4"]["ones"].append(ctx.message.author.name)

					elif ctx.message.author.name in ones:
						super_boxes["box4"]["members"][f'{str(ctx.message.author.name)}'] += int(amount)


					with open('super_boxes.json','w') as f:
						json.dump(super_boxes,f)

					user_balance[str(ctx.message.author.name)]['RUB'] -= amount
					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)

					await ctx.message.author.send(f'Вы вложили {amount}RUB в копилку №4')


					channel = bot.get_channel(888500024214966282)
					m = await channel.fetch_message(894214947473588255)
					ac = round(target / 4)
					at = round(target / 3)
					po = round(target / 2)
					dt = at + at

					with open('super_boxes.json','r', encoding='utf-8') as f:
						super_boxes = json.load(f)

					invested = super_boxes["box4"]["invested"]
					if invested <= ac:# 1/10
						box = discord.Embed(color=0x2E62FF, title="Супер копилка №4", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧⬛⬛⬛⬛⬛⬛⬛⬛')
						await m.edit(embed = box)

					elif invested > ac and invested < at + 20:# 1/4 -
						box = discord.Embed(color=0x2E62FF, title="Супер копилка №4", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧⬛⬛⬛⬛⬛⬛⬛')
						await m.edit(embed = box)

					elif invested > at + 20 and invested <= po:# 1/2 -
						box = discord.Embed(color=0x2E62FF, title="Супер копилка №4", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧⬛⬛⬛⬛⬛')
						await m.edit(embed = box)

					elif invested >= po and invested < dt + 95:# 1/2 +
						box = discord.Embed(color=0x2E62FF, title="Супер копилка №4", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧⬛⬛⬛⬛')
						await m.edit(embed = box)

					elif invested >= po and invested < dt + 70:# 1/2 +
						box = discord.Embed(color=0x2E62FF, title="Супер копилка №4", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛')
						await m.edit(embed = box)

					elif invested > dt + 95:
						box = discord.Embed(color=0x2E62FF, title="Супер копилка №2", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: 🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧')
						await m.edit(embed = box)

					# logs
					logs = guild.get_channel(892584515162210324)
					embed = discord.Embed(color=0x00a550, title="ВКЛАД В СУПЕР КОПИЛКУ", description=f'Участник {ctx.message.author} положил {amount} в копилку №4\n\nДля заполнения копилки осталось вложить `{target - invested}`')
					await logs.send(embed=embed)


				else:
					await ctx.message.author.send("У вас недостаточно средств.")
			else:
				await ctx.message.author.send("Сумма вложения должна быть не менее 1 и не боле 350RUB.")




		else:
			await ctx.message.author.send(f'Копилка с номером {box} не найдена.')



@bot.command()
async def sell(ctx, ntb=None, rub=None):
	guild = bot.get_guild(880008097370865706)

	# Sell NTB
	if ntb != None and rub != None:
		if ctx.channel.id == 900380214029324288:
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			ntb_bal = user_balance[str(ctx.message.author.name)]['NTB']
			rub_bal = user_balance[str(ctx.message.author.name)]['RUB']

			if ntb_bal >= int(ntb):
				await ctx.channel.purge(limit=1)
				channel = bot.get_channel(900380294161502229)
				embed = discord.Embed(color=0x008000, title=f'Купить валюту')
				embed.add_field(name = '**Предмет:**', value = f'{ntb}NTB', inline = True)
				embed.add_field(name = '**Цена:**', value = f'{rub}RUB', inline = True)
				message = await channel.send(embed=embed)
				await message.add_reaction('✅')
				await message.add_reaction('❌')

				with open('user_sales.json','r', encoding='utf-8') as f:
					sales = json.load(f)

				sales[str(ctx.message.author.name)]["sales"][message.id] = {"stats": True, "vtype": "NTB", "ntb": int(ntb), "rub": int(rub), "buy": []}
				with open('user_sales.json','w') as f:
					json.dump(sales,f)

				# logs
				logs = guild.get_channel(898204390412943451)
				embed = discord.Embed(color=0x00a550, title="ВЫСТАВКА НА БИРЖЕ", description=f'Участник {ctx.message.author} выставил {ntb}NTB за {rub}RUB.')
				await logs.send(embed=embed)

			else:
				await ctx.channel.purge(limit=1)
				await ctx.message.author.send('У вас недостаточно NTB для продажи.')

		else:
			await ctx.channel.purge(limit=1)

	else:
		await ctx.channel.purge(limit=1)
		await member.send("Ошибка в аргументах команды.")



@bot.command()
async def buy(ctx, ntb=None, rub=None):
	guild = bot.get_guild(880008097370865706)

	# Sell RUB
	if ntb != None and rub != None:
		if ctx.channel.id == 900380214029324288:
			with open('user_balance.json','r', encoding='utf-8') as f:
				user_balance = json.load(f)

			ntb_bal = user_balance[str(ctx.message.author.name)]['NTB']
			rub_bal = user_balance[str(ctx.message.author.name)]['RUB']

			if rub_bal >= int(rub):
				await ctx.channel.purge(limit=1)
				channel = bot.get_channel(900380324880597032)
				embed = discord.Embed(color=0xff0000, title=f'Продать валюту')
				embed.add_field(name = '**Предмет:**', value = f'{ntb}NTB', inline = True)
				embed.add_field(name = '**Цена:**', value = f'{rub}RUB', inline = True)
				message = await channel.send(embed=embed)
				await message.add_reaction('✅')
				await message.add_reaction('❌')

				await ctx.message.author.send(f'Ваше предложение находится [здесь](https://discord.com/channels/880008097370865706/900380324880597032{message.id})\nДля его удаления нажмите ❌ под сообщением.')

				with open('user_sales.json','r', encoding='utf-8') as f:
					sales = json.load(f)

				sales[str(ctx.message.author.name)]["sales"][message.id] = {"stats": True, "vtype": "RUB", "ntb": int(ntb), "rub": int(rub), "buy": []}
				with open('user_sales.json','w') as f:
					json.dump(sales,f)

				# logs
				logs = guild.get_channel(898204390412943451)
				embed = discord.Embed(color=0x00a550, title="ВЫСТАВКА НА БИРЖЕ", description=f'Участник {ctx.message.author} выставил {rub}RUB за {ntb}NTB.')
				await logs.send(embed=embed)


			else:
				await ctx.channel.purge(limit=1)
				await ctx.message.author.send('У вас недостаточно RUB для продажи.')

		else:
			await ctx.channel.purge(limit=1)

	else:
		await ctx.channel.purge(limit=1)
		await member.send("Ошибка в аргументах команды.")


@bot.command()
async def message(ctx, member: discord.Member, before, title, footer, *, description):
	guild = bot.get_guild(880008097370865706)
	if ctx.message.author.id == 663424295854407692:
		if before != "None" or before != "none" or before != "0":
			embed = discord.Embed(color = 0x008000, title=title, description=description)
			embed.set_footer(text=f'{footer}')
			await member.send(before)
			await member.send(embed = embed)
			await ctx.message.add_reaction('✅')

		elif before == "None" or before == "none" or before == "0":
			embed = discord.Embed(color = 0x008000, title=title, description=description)
			embed.set_footer(text=f'{footer}')
			await member.send(embed = embed)
			await ctx.message.add_reaction('✅')

	else:
		print('message(): Not member')


@bot.command()
async def bug(ctx):
	await ctx.send("https://cs12.pikabu.ru/post_img/2021/11/29/7/1638184853181437333.webp")


@bot.command()
async def db(ctx):
	guild = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild:
		print('In guild')

	else:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		print("user_balance.json Done")

		with open('user_farms.json','r', encoding='utf-8') as f:
			user_farms = json.load(f)

		print("user_farms.json Done")

		with open('referal.json','r', encoding='utf-8') as f:
			ref = json.load(f)

		print("referal.json Done")

		with open('user_bank.json','r', encoding='utf-8') as f:
			bank = json.load(f)

		print("user_bank.json Done")

		with open('user_sales.json','r', encoding='utf-8') as f:
			sales = json.load(f)

		print("user_sales.json Done")

		with open('bot_constants.json','r', encoding='utf-8') as f:
			constants = json.load(f)

		print("bot_constants.json Done")

		with open('user_profile.json','r', encoding='utf-8') as f:
			profile = json.load(f)

		print("user_profile.json Done")

		with open('db.txt','w+', encoding='utf-8') as f:
			f.write(f'user_balance.json:\n{user_balance}\n\n\nuser_farms.json:\n{user_farms}\n\n\nreferal.json:\n{ref}\n\n\nuser_bank.json:\n{bank}\n\n\nuser_sales.json:\n{sales}\n\n\nbot_constants.json:\n{constants}\n\n\nuser_profile.json:\n{profile}')

		member = guild.get_member(677453905227022349)
		await ctx.send(file=discord.File(r'db.txt'))

# ----------------------- /Moderation ------------------------|


@bot.command()
async def upd(ctx):
	if ctx.message.author.id == 677453905227022349:

		guild = bot.get_guild(880008097370865706)

		'''
		agr = bot.get_channel(880023332639096853)
		m = await agr.fetch_message(881913060305031189)
		embed = discord.Embed(color=0x3C55FA, title="**ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ**", description=f'**ИСПОЛЬЗОВАНИЕ, НАХОЖДЕНИЕ И ЛЮБОЕ ВЗАИМОДЕЙСТВИЕ НА НАШЕМ СЕРВЕРЕ DISCORD "💨NEXT Invest💨", ПОДРАЗУМЕВАЕТ ПОЛНОЕ СОГЛАСИЕ С НИЖЕПЕРЕЧИСЛЕННЫМИ ПОЛОЖЕНИЯМИ И УСЛОВИЯМИ ПОЛЬЗОВАТЕЛЬСКОГО СОГЛАШЕНИЯ**\n\nВсе внутренние расчеты производятся исключительно с пересчетом на виртуальную внутрисерверную валюту.\n\n**ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ**\nВзаимодействие участников с сервером Discord "{guild.name}" основываются на публичном соглашении. Действие соглашения становится активным в момент его размещения\n\n**Предмет соглашения**\n\nСоглашением регламентировано взаимодействие пользователей с сервером Discord "{guild.name}" в следующих направлениях:\n• Порядок использования сервера\n• Осуществление денежных транзакций в виде конвертирования на реальную и внутрисерверную валюту\n• Порядок осуществления внутрисерверных покупок\n• Взаимодействие с приобретенными услугами на внутрисерверную валюту\n• Проведение ивентов и бонусных программ')
		await m.edit(embed = embed)

		
		farms = bot.get_channel(880025073963122718)
		m = await farms.fetch_message(886528458887401473)
		embedf = discord.Embed(color=0x3C55FA, title="FARM ЗАТЫЧКА", description=f'На слабой видеокарте\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf.set_thumbnail(url="https://i.ibb.co/92f8Cw8/Z.png")
		embedf.add_field(name = '**Макс срок работы:**', value = "35дней", inline = True)
		embedf.add_field(name = '**Производительность:**', value = "0.25RUB/ч", inline = True)
		embedf.add_field(name = '**Срок окупаемости:**', value = "25 дней", inline = True)

		embedf.add_field(name = '**Сложность:**', value = "EASY", inline = True)
		embedf.add_field(name = '**Вывод RUB на баланс:**', value = "Ручной", inline = True)
		embedf.add_field(name = '**ЦЕНА:**', value = "149RUB", inline = True)
		await m.edit(embed = embedf)


		m1 = await farms.fetch_message(886528465631862905)
		embedf1 = discord.Embed(color=0x3C55FA, title="FARM GTX", description=f'На игровой видеокарте\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf1.set_thumbnail(url="https://i.ibb.co/RCt8s0K/G.png")
		embedf1.add_field(name = '**Макс срок работы:**', value = "29дней", inline = True)
		embedf1.add_field(name = '**Производительность:**', value = "0.5RUB/ч", inline = True)
		embedf1.add_field(name = '**Срок окупаемости:**', value = "21 день", inline = True)

		embedf1.add_field(name = '**Сложность:**', value = "EASY", inline = True)
		embedf1.add_field(name = '**Вывод RUB на баланс:**', value = "Ручной", inline = True)
		embedf1.add_field(name = '**ЦЕНА:**', value = "249RUB", inline = True)
		await m1.edit(embed = embedf1)


		m2 = await farms.fetch_message(886528471159930961)
		embedf2 = discord.Embed(color=0x3C55FA, title="FARM RTX", description=f'На мощной видеокарте\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf2.set_thumbnail(url="https://i.ibb.co/z72pGRR/R.png")
		embedf2.add_field(name = '**Макс срок работы:**', value = "29дней", inline = True)
		embedf2.add_field(name = '**Производительность:**', value = "1RUB/ч", inline = True)
		embedf2.add_field(name = '**Срок окупаемости:**', value = "21 день", inline = True)

		embedf2.add_field(name = '**Сложность:**', value = "NORM", inline = True)
		embedf2.add_field(name = '**Вывод RUB на баланс:**', value = "Ручной", inline = True)
		embedf2.add_field(name = '**ЦЕНА:**', value = "**499RUB**", inline = True)
		await m2.edit(embed = embedf2)


		m3 = await farms.fetch_message(886528474192437278)
		embedf3 = discord.Embed(color=0x3C55FA, title="FARM ASIC", description=f'На автоматическом оборудовании для майнинга\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf3.set_thumbnail(url="https://i.ibb.co/RHfBJvm/A.png")
		embedf3.add_field(name = '**Макс срок работы:**', value = "35дней", inline = True)
		embedf3.add_field(name = '**Производительность:**', value = "0.6RUB/ч", inline = True)
		embedf3.add_field(name = '**Срок окупаемости:**', value = "21 дней", inline = True)

		embedf3.add_field(name = '**Сложность:**', value = "NORM", inline = True)
		embedf3.add_field(name = '**Вывод RUB на баланс:**', value = "Автоматический", inline = True)
		embedf3.add_field(name = '**ЦЕНА:**', value = "**299RUB**", inline = True)
		await m3.edit(embed = embedf3)


		m4 = await farms.fetch_message(886528476797083668)
		embedf4 = discord.Embed(color=0x3C55FA, title="FARM MULTI", description=f'На мощном оборудовании для майнинга\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf4.set_thumbnail(url="https://i.ibb.co/SmQ7bNk/M.png")
		embedf4.add_field(name = '**Макс срок работы:**', value = "33дней", inline = True)
		embedf4.add_field(name = '**Производительность:**', value = "0.8RUB/ч", inline = True)
		embedf4.add_field(name = '**Срок окупаемости:**', value = "26 день", inline = True)

		embedf4.add_field(name = '**Сложность:**', value = "NORM", inline = True)
		embedf4.add_field(name = '**Вывод RUB на баланс:**', value = "Автоматический", inline = True)
		embedf4.add_field(name = '**ЦЕНА:**', value = "**499RUB**", inline = True)
		await m4.edit(embed = embedf4)


		m5 = await farms.fetch_message(886528481381462076)
		embedf5 = discord.Embed(color=0x3C55FA, title="FARM BOOST", description=f'На улучшенном оборудовании для майнинга\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf5.set_thumbnail(url="https://i.ibb.co/rf67N6Y/B.png")
		embedf5.add_field(name = '**Макс срок работы:**', value = "20дней", inline = True)
		embedf5.add_field(name = '**Производительность:**', value = "3RUB/ч", inline = True)
		embedf5.add_field(name = '**Срок окупаемости:**', value = "14 дней", inline = True)

		embedf5.add_field(name = '**Сложность:**', value = "HARD", inline = True)
		embedf5.add_field(name = '**Вывод RUB на баланс:**', value = "Ручной", inline = True)
		embedf5.add_field(name = '**ЦЕНА:**', value = "**999RUB**", inline = True)
		await m5.edit(embed = embedf5)


		m6 = await farms.fetch_message(886528484460097546)
		embedf6 = discord.Embed(color=0x3C55FA, title="FARM TITAN", description=f'На мощных видеокартах\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf6.set_thumbnail(url="https://i.ibb.co/87WYdBB/T.png")
		embedf6.add_field(name = '**Макс срок работы:**', value = "30дней", inline = True)
		embedf6.add_field(name = '**Производительность:**', value = "4RUB/ч", inline = True)
		embedf6.add_field(name = '**Срок окупаемости:**', value = "16 дней", inline = True)

		embedf6.add_field(name = '**Сложность:**', value = "HARD", inline = True)
		embedf6.add_field(name = '**Вывод RUB на баланс:**', value = "Ручной", inline = True)
		embedf6.add_field(name = '**ЦЕНА:**', value = "**1499RUB **", inline = True)
		await m6.edit(embed = embedf6)

		
		m7 = await farms.fetch_message(881782363191910440)
		embedf7 = discord.Embed(color=0x3C55FA, title="FARM SERVER", description=f'На серверном оборудовании\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf7.set_thumbnail(url="https://i.ibb.co/0KDHq9W/S.png")
		embedf7.add_field(name = '**Макс срок работы:**', value = "50дней", inline = True)
		embedf7.add_field(name = '**Производительность:**', value = "8RUB/ч", inline = True)
		embedf7.add_field(name = '**Срок окупаемости:**', value = "13 дней", inline = True)

		embedf7.add_field(name = '**Сложность:**', value = "MASTER", inline = True)
		embedf7.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
		embedf7.add_field(name = '**ЦЕНА:**', value = "**2499V**", inline = True)
		await m7.edit(embed = embedf7)
		

		m8 = await farms.fetch_message(886528488234971207)
		embedf8 = discord.Embed(color=0x3C55FA, title="FARM FACTORY", description=f'На автоматическом заводском оборудовании\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf8.set_thumbnail(url="https://i.ibb.co/NL6qq9w/F.png")
		embedf8.add_field(name = '**Макс срок работы:**', value = "37дней", inline = True)
		embedf8.add_field(name = '**Производительность:**', value = "14RUB/ч", inline = True)
		embedf8.add_field(name = '**Срок окупаемости:**', value = "13 дней", inline = True)

		embedf8.add_field(name = '**Сложность:**', value = "EXPERT", inline = True)
		embedf8.add_field(name = '**Вывод RUB на баланс:**', value = "Автоматический", inline = True)
		embedf8.add_field(name = '**ЦЕНА:**', value = "**4999RUB**", inline = True)
		await m8.edit(embed = embedf8)


		m9 = await farms.fetch_message(886528493339422774)
		embedf9 = discord.Embed(color=0x3C55FA, title="FARM QUANTUM", description=f'Мощный квантовый компьютер\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf9.set_thumbnail(url="https://i.ibb.co/JBnsbKS/Q.png")
		embedf9.add_field(name = '**Макс срок работы:**', value = "42дня", inline = True)
		embedf9.add_field(name = '**Производительность:**', value = "25RUB/ч", inline = True)
		embedf9.add_field(name = '**Срок окупаемости:**', value = "10 дней", inline = True)

		embedf9.add_field(name = '**Сложность:**', value = "INSANE", inline = True)
		embedf9.add_field(name = '**Вывод RUB на баланс:**', value = "Автоматический", inline = True)
		embedf9.add_field(name = '**ЦЕНА:**', value = "**9999RUB**", inline = True)
		await m9.edit(embed = embedf9)


		m10 = await farms.fetch_message(886528504068464640)
		embedf10 = discord.Embed(color=0x3C55FA, title="FARM ПЛАТА", description=f'Самая простая видеокарта\n\n**Для покупки за RUB нажмите :euro:**\n')
		embedf10.set_thumbnail(url="https://i.ibb.co/pd6w8dt/plata.png")
		embedf10.add_field(name = '**Макс срок работы:**', value = "14дней", inline = True)
		embedf10.add_field(name = '**Производительность:**', value = "0.3RUB/ч", inline = True)
		embedf10.add_field(name = '**Срок окупаемости:**', value = "11 дней", inline = True)

		embedf10.add_field(name = '**Сложность:**', value = "EASY", inline = True)
		embedf10.add_field(name = '**Вывод RUB на баланс:**', value = "Ручной", inline = True)
		embedf10.add_field(name = '**ЦЕНА:**', value = "79RUB", inline = True)
		await m10.edit(embed = embedf10)



		
		system = bot.get_channel(880024762942889994)
		m = await system.fetch_message(881782363191910440)
		embed = discord.Embed(color=0x3C55FA, title="НАША СИСТЕМА", description=f'**НАША КОНЦЕПЦИЯ**\n:dash:NEXT Invest:dash: - проект основная цель которого дать людям проводить время на сервере общаясь, выполняя какие либо задания, получая за это деньги. Специально для Вас была разработана уникальная система автоматизированного получения прибыли путем так называемого майнинга, позволяющая получать внутрисерверную криптовалюту, всем без исключений, которую в дальнейшем можно обменять на реальные деньги. При входе на сервер, для Вас создаётся личный счёт с нашей валютой. С помощью данного счета, вы можете осуществлять вывод, конвертацию и пополнение средств. Все покупки внутри сервера, включая покупку ферм, не является обязательным условием для нахождения на нашем сервере и носит лишь развлекательный характер.\n\n**Насколько безопасна ваша система?**\nТехнология проекта — имеет проверенный временем высокий уровень безопасности! Система грамотно спроектирована, что не позволит дать доступ к вашей уч.Записи злоумышленникам\nНаша валюта защищена от инфляции и внешних факторов экономики.Благодаря нашей технологии, проект защищен от внешнего контроля и управлением, эмиссия этой криптовалюты происходит в процессе работы ферм, использования нашего ПО.\n\n**ВАРИАНТЫ ПОЛУЧЕНИЯ ВАЛЮТЫ:**\n[▽ ОБЩЕНИЕ В ГОЛОСОВЫХ КАНАЛАХ]()\n[▽ ПРИОБРЕТЕНИЕ МАЙНИНГ ФЕРМ]()\n▽ТОРГОВЛЯ КРИПТОВАЛЮТОЙ\n▽ВЫПОЛНЕНИЕ ЗАДАНИЙ СЕРВЕРА\n▽СЁРФИНГ\n[▽ ТОРГОВЛЯ]()\n[▽ ЕЖЕДНЕВНЫЕ ЗАДАНИЯ]()\n[▽ РЕФЕРАЛЬНАЯ СИСТЕМА]()\n[▽ ОТКРЫТИЕ КЕЙСОВ]()\n[▽ УЧАСТИЕ И ИВЕНТАХ]()\n[▽ УЧАСТИЕ В РОЗЫГРЫШАХ]()\n[▽ S.UP И BUMP СЕРВЕРА]()\n')
		await m.edit(embed=embed)


		
		navigation = bot.get_channel(889216233604526132)
		embed = discord.Embed(color=0x3C55FA, title=f'БАНК', description=f'**Кратко о системе:**\nВ Банке вы можете открыть депозит и ни о чем не париться. Преимущество депозита от покупки ферм в том, что вам не нужно заходить ежедневно и собирать прибыль, при этом у вас ничего не будет ломаться и вы 100% выйдете в плюс . Вы можете не заходить неделями, а чтобы получить начисления по депозиту вам нужно просто наведаться в Банк, и деньги поступят на ваш баланс . Выбирайте тариф, создавайте депозит и получайте ежедневные начисления!\n\n**Выберите инвестиционный план:**\n\n:one:\nДоходность - 110%\nСрок вклада - 25 дней\nсумма вклада - 20-500 рублей\n\n:two:\nДоходность - 120%\nСрок вклада - 45 дней\nсумма вклада - 400-2000 рублей')
		embed.set_thumbnail(url="https://im0-tub-ru.yandex.net/i?id=162008a3587f9cc3f2da4904ce53e275&n=13")
		message = await navigation.send(embed = embed)
		await message.add_reaction('1️⃣')
		await message.add_reaction('2️⃣')
		

		channel = bot.get_channel(889843449300398111)
		m2 = await channel.fetch_message(891665705655746600)
		embed = discord.Embed(color=0x2E62FF, title=f'Кейс открытие', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**500RUB | 350RUB | 120RUB | 45RUB | 35RUB | 25RUB |** 10RUB | 5RUB |\n**Ферма** - FARM ПЛАТА\n**УНИКАЛЬНАЯ РОЛЬ** ☄️; Бизнесмен;\n\nНАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:\n**:pound: 1шт - ~~75RUB~~ 25RUB**\n:credit_card: 5шт - ~~375RUB~~ 125RUB')
		embed.set_thumbnail(url="https://i.ibb.co/1LWW1R8/PREMIUM.png")
		await m2.edit(embed = embed)
		

		
		'''
		channel = bot.get_channel(889843449300398111)
		m1 = await channel.fetch_message(890117683478147092)
		embed1 = discord.Embed(color=0x2f3136, title=f'GOLD CASE', description=f'> Возможные призы:\n**450RUB | 330RUB | 250RUB | 210RUB | 200RUB | 150RUB | 125RUB | 100RUB | 85 RUB | 65RUB | 50RUB |**\n・ Premium 30 day\n・ Premium 21 day\n・ -FARM ЗАТЫЧКА\n・ -FARM GTX\n・ -FARM RTX\n・ УНИКАЛЬНАЯ РОЛЬ :zap: Gold Monopolis**\n\n\n> Для открытия нажмите:\n\n**:pound: | 1шт - 199RUB\n:credit_card: | 5шт - 995RUB\n:moneybag: | 10шт - 1990RUB**')
		embed1.set_thumbnail(url="https://i.ibb.co/Kq8j5qT/GOLD.png")
		await m1.edit(embed = embed1)
		await m1.add_reaction('💰')

		m = await channel.fetch_message(890117691388600320)
		embed = discord.Embed(color=0x2f3136, title=f'PLATINUM CASE', description=f'> Возможные призы:\n\n**850RUB | 650RUB | 500RUB | 535RUB | 420RUB | 400RUB| 350 RUB| 200RUB | 100RUB | 65 RUB|**\n・ Premium 45 day\n・ Premium 35 day\n・ Premium 26 day\n・ -FARM MULTI\n・ -FARM GTX\n・ -FARM RTX\n・ -FARM ASIC\n・ УНИКАЛЬНАЯ РОЛЬ - 🌀\n\n\n> Для открытия нажмите:\n\n**:pound: | 1шт - 500RUB\n:credit_card: | 5шт - 2500RUB\n:moneybag: | 10шт - 5000RUB**')
		embed.set_thumbnail(url="https://i.ibb.co/1MDfBNc/PLATINUM.png")
		await m.edit(embed = embed)
		await m.add_reaction('💰')

		
		m2 = await channel.fetch_message(893551335511830649)
		embed2 = discord.Embed(color=0x2f3136, title=f'LITE CASE', description=f'> Возможные призы:\n\n**625RUB| 500RUB | 350RUB | 120RUB |** 45RUB | 35RUB | 25RUB | 15 RUB| 10RUB | 5RUB |\n・ Premium 7 days\n・ Ферма - **FARM ПЛАТА**\n・ УНИКАЛЬНАЯ РОЛЬ  ⚡; Gold; ☄️; Бизнесмен;\n\n\n> Для открытия нажмите:\n\n**:pound: | 1шт - ~~125~~RUB 35RUB\n:credit_card: | 5шт - ~~625~~RUB 175RUB\n:moneybag: | 10шт - 350RUB**')
		embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/828213712736354305/893521241724563527/PREMIUM.png")
		await m2.edit(embed = embed2)
		await m2.add_reaction('💰')
		
		
		m3 = await channel.fetch_message(890117675408322580)
		embed3 = discord.Embed(color=0x2f3136, title=f'SILVER CASE', description=f'> Возможные призы:\n\n・ Денежный приз:\n**450RUB | 320RUB | 160RUB | 80RUB | 65RUB | 55RUB |** 40RUB | 20RUB |\n・ Premium 16 days\n・ Premium 10 days・ \n-FARM ПЛАТА\n・ -FARM ЗАТЫЧКА\n・ -FARM ASIC\n・ Уникальная роль - :airplane:\n・ Уникальная роль - :zap:\n・ Уникальная роль - ☄️\n\n\n> Для открытия нажмите:\n\n**:pound: | 1шт - 99RUB\n:credit_card: | 5шт - 495RUB\n:moneybag: | 10шт - 990RUB**')
		embed3.set_thumbnail(url="https://i.ibb.co/xXnJTXq/SILVER.png")
		await m3.edit(embed = embed3)
		await m3.add_reaction('💰')
		
		m4 = await channel.fetch_message(890117667908878347)
		embed4 = discord.Embed(color=0x2f3136, title=f'BRONZE CASE', description=f'> Возможные призы:\n\n・ Денежный приз:\n**300RUB| 220RUB | 140RUB | 100RUB | 65RUB | 50RUB |** 35RUB | 25RUB | 20RUB | 15RUB | 10RUB |\n・ Ферма - **FARM CLASSIC**.\n・ Уникальная роль бизнесмен\n・ Уникальная роль Trainer\n\n\n> Для открытия нажмите:\n\n**:pound: | 1шт - 49RUB\n:credit_card: | 5шт - 245RUB\n:moneybag: | 10шт - 490RUB**')
		embed4.set_thumbnail(url="https://i.imgur.com/MRvrOW2.png")
		await m4.edit(embed = embed4)
		
		channel = bot.get_channel(889843449300398111)
		m3 = await channel.fetch_message(926887879786000464)
		embed5 = discord.Embed(color=0x2f3136, title=f"NEW YEAR's CASE", description=f'> Возможные призы:\n\n・ Денежный приз:\n**125RUB | 75RUB | 35RUB | 15RUB |** 10RUB | 5RUB | 0RUB |\n・ @Premium на 10 дней.\n・ @Premium на 7 дней.\n・ Уникальная роль - @🎅.\n・ Уникальная роль - @☃️.\n・ Уникальная роль - @❄️.\n\n\n> Для открытия нажмите:\n\n**:pound: | 1шт - ~~45RUB~~- 10 RUB\n:credit_card: | 5шт - ~~225RUB~~- 50 RUB\n:moneybag: | 10шт - ~~450RUB~~- 100 RUB**')
		embed5.set_thumbnail(url="https://media.discordapp.net/attachments/828213712736354305/893521241724563527/PREMIUM.png")
		await m3.edit(embed = embed5)
		'''
	
		# SUPER MONEY BOXES
		channel = bot.get_channel(888500024214966282)
		#embed = discord.Embed(color=0x2E62FF, title="**Супер копилка**", description=f'**Супер копилка** - это место, где можно заработать огромные проценты за короткое время.\nСуть данного раздела заключается в том, что каждый игрок может внести свой вклад в общее дело и получить +10% чистого профита после полного заполнения следующей копилки.\n\nТ.е. если коротко, вложил 100 рублей в  копилку №1, после заполнения копилки №2 Вы получите 110 руб. на вывод.')
		#await channel.send(embed = embed)
		
		
		channel = bot.get_channel(888500024214966282)
		m1 = await channel.fetch_message(893397579663044629)
		box = discord.Embed(color=0x2E62FF, title="Супер копилка №1", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
		await m1.edit(embed = box)

		m2 = await channel.fetch_message(893397582523547678)
		box2 = discord.Embed(color=0x2E62FF, title="Супер копилка №2", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
		await m2.edit(embed = box2)
	
		m3 = await channel.fetch_message(894214944034279435)
		box3 = discord.Embed(color=0x2E62FF, title="Супер копилка №3", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
		await m3.edit(embed = box3)

		m4 = await channel.fetch_message(894214947473588255)
		box4 = discord.Embed(color=0x2E62FF, title="Супер копилка №4", description=f'Для вложений нажмите на 📤\n\n**Заполнено**: ⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛')
		await m4.edit(embed = box4)
		
		channel = bot.get_channel(888053213750779934)
		embed = discord.Embed(color=0x2E62FF, title="Рабочая смена", description=f'Сотрудники на смене:\nNone')
		message = await channel.send(embed = embed)
		
		
		channel = bot.get_channel(889843449300398111)
		embed = discord.Embed(title=f"NEW YEAR's CASE", description=f'> Возможные призы:\n\n・ Денежный приз:\n**125RUB | 75RUB | 35RUB | 15RUB |** 10RUB | 5RUB | 0RUB |\n・ @Premium на 10 дней.\n・ @Premium на 7 дней.\n・ Уникальная роль - @🎅.\n・ Уникальная роль - @☃️.\n・ Уникальная роль - @❄️.\n\n\n> Для открытия нажмите:\n\n**:pound: | 1шт - ~~45RUB~~- 10 RUB\n:credit_card: | 5шт - ~~225RUB~~- 50 RUB\n:moneybag: | 10шт - ~~450RUB~~- 100 RUB**')
		embed.set_thumbnail(url="https://media.discordapp.net/attachments/828213712736354305/893521241724563527/PREMIUM.png")
		await channel.send(embed = embed)
		

	
		channel = bot.get_channel(889843449300398111)
		m = await channel.fetch_message(926887879786000464)
		await m.add_reaction('💷')
		await m.add_reaction('💳')
		await m.add_reaction('💰')
		'''


	else:
		print("Not man")


# Random images sending
bot.loop.create_task(RandomImages())

bot.run('token')
