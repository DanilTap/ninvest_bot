# This Python file uses the following encoding: utf-8
import discord
from discord.ext import commands
from threading import Thread
import json
import time
import asyncio
import random

intents = discord.Intents.default()
intents.members = True
bot = discord.ext.commands.Bot(command_prefix = "!", intents = intents)




# |------------------------------ VARIABLES ------------------------------|
# Reactions lists
farm_messages = []
tickets_messages = []
donat1s = False
donat2s = False
membercode = False
gncode = 0
# |------------------------------ /VARIABLES -----------------------------|








# |-------------------------------- EVENTS --------------------------------|
@bot.event
async def on_ready():
	print('----------Bot is ready!----------\n\n')
	
	# Start farms
	with open('user_farms.json','r', encoding='utf-8') as f:
		farms = json.load(f)

	print("----------Loading farms-----------")

	for i in farms: # For all members
		member = farms[i]['name']
		farm_list = farms[i]['farms']


		for i in range(len(farm_list)): # For all farms
			print(f'{farm_list[i]}')
			dict1 = json.loads("'{}'".format(farm_list))
			print(type(dict1)) 

		'''
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
		'''
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

			embed = discord.Embed(color=0x3C55FA, title="ВАШ БАЛАНС", description=f':euro:** {rub} RUB**\n:pound:** {ntb} NTB**\n\n`!top` - Пополнить\n`!get` - Вывести\n🔁 - Обновить баланс.')
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
				items = [220, 140, 100, 50, 35, 20, 10, 'role']

				item = random.choice(items)
				print(item)

				if item == 'role':
					getrole = discord.utils.get(guild.roles, id = 890960183155630191 )
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@бизнесмен`!")

				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')

				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 245:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 245:
				user_balance[str(member.name)]['RUB'] -= 245
				for i in range(5):
					items = [220, 140, 100, 50, 35, 20, 10, 'role']

					item = random.choice(items)
					print(item)

					if item == 'role':
						getrole = discord.utils.get(guild.roles, id = 890960183155630191 )
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@бизнесмен`!")

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')

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
				items = [450, 320, 160, 80, 50, 55, 40, 20, 10, 'premium', 'farm', 'farm2' 'jet']

				item = random.choice(items)
				print(item)

				if item == 'premium':
					getrole = discord.utils.get(guild.roles, id = 890112591395966977)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 14 days`!")

				elif item == 'farm':
					await CreateFarmChannel(member, 'FARM ПЛАТА')
					await member.send("Вы выиграли ферму `FARM ПЛАТА`!")

				elif item == 'farm':
					await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')
					await member.send("Вы выиграли ферму `FARM ЗАТЫЧКА`!")

				elif item == 'jet':
					getrole = discord.utils.get(guild.roles, id = 890112890722463774)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@:plane:`!")

				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')

				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 496:
				await member.send("У вас недостаточно средств для покупки кейса.")

			elif balance >= 496:
				user_balance[str(member.name)]['RUB'] -= 496
				for i in range(5):
					items = [450, 320, 160, 80, 50, 55, 40, 20, 10, 'premium', 'farm', 'farm2' 'jet']

					item = random.choice(items)
					print(item)

					if item == 'premium':
						getrole = discord.utils.get(guild.roles, id = 890112591395966977)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 14 days`!")

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ПЛАТА')
						await member.send("Вы выиграли ферму `FARM ПЛАТА`!")

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')
						await member.send("Вы выиграли ферму `FARM ЗАТЫЧКА`!")

					elif item == 'jet':
						getrole = discord.utils.get(guild.roles, id = 890112890722463774)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:plane:`!")

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')

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
				items = [450, 330, 250, 210, 200, 150, 100, 85, 65, 50, 'premium', 'farm', 'farm1', 'role1', 'role2', 'role3']

				item = random.choice(items)
				print(item)

				if item == 'premium':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 30 day`!")

				elif item == 'farm':
					await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')
					await member.send("Вы выиграли ферму `FARM ЗАТЫЧКА`!")

				elif item == 'farm1':
					await CreateFarmChannel(member, 'FARM GTX')
					await member.send("Вы выиграли ферму `FARM GTX`!")

				elif item == 'role1':
					getrole = discord.utils.get(guild.roles, id = 890119411153911839)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Monopolis`!")

				elif item == 'role2':
					getrole = discord.utils.get(guild.roles, id = 890119660488491049)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Monopolis`!")

				elif item == 'role3':
					getrole = discord.utils.get(guild.roles, id = 890099592752939009)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@:zap:`!")

				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')

				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 995:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 995:
				user_balance[str(member.name)]['RUB'] -= 995
				for i in range(5):
					items = [450, 330, 250, 210, 200, 150, 100, 85, 65, 50, 'premium', 'farm', 'farm1', 'role1', 'role2', 'role3']

					item = random.choice(items)
					print(item)

					if item == 'premium':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 30 day`!")

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')
						await member.send("Вы выиграли ферму `FARM ЗАТЫЧКА`!")

					elif item == 'farm1':
						await CreateFarmChannel(member, 'FARM GTX')
						await member.send("Вы выиграли ферму `FARM GTX`!")

					elif item == 'role1':
						getrole = discord.utils.get(guild.roles, id = 890119411153911839)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Monopolis`!")

					elif item == 'role2':
						getrole = discord.utils.get(guild.roles, id = 890119660488491049)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Monopolis`!")

					elif item == 'role3':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')

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
				items = [3200, 1600, 800, 400, 400, 200, 100, 'premium', 'role', 'farm1', 'farm2', 'farm3']

				item = random.choice(items)
				print(item)

				if item == 'premium':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium - 45 days`!")

				elif item == 'role':
					getrole = discord.utils.get(guild.roles, id = 890587785856155649)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@🌀`!")

				elif item == 'farm1':
					await CreateFarmChannel(member, 'FARM GTX')
					await member.send("Вы выиграли ферму `FARM GTX`!")

				elif item == 'farm2':
					await CreateFarmChannel(member, 'FARM RTX')
					await member.send("Вы выиграли ферму `FARM RTX`!")

				elif item == 'farm3':
					await CreateFarmChannel(member, 'FARM ASIC')
					await member.send("Вы выиграли ферму `FARM ASIC`!")

				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')

				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 2500:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 2500:
				user_balance[str(member.name)]['RUB'] -= 2500
				for i in range(5):
					items = [3200, 1600, 800, 400, 400, 200, 100, 'premium', 'role', 'farm1', 'farm2', 'farm3']

					item = random.choice(items)
					print(item)

					if item == 'premium':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 45 days`!")

					elif item == 'role':
						getrole = discord.utils.get(guild.roles, id = 890587785856155649)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@🌀`!")

					elif item == 'farm1':
						await CreateFarmChannel(member, 'FARM GTX')
						await member.send("Вы выиграли ферму `FARM GTX`!")

					elif item == 'farm2':
						await CreateFarmChannel(member, 'FARM RTX')
						await member.send("Вы выиграли ферму `FARM RTX`!")

					elif item == 'farm3':
						await CreateFarmChannel(member, 'FARM ASIC')
						await member.send("Вы выиграли ферму `FARM ASIC`!")

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')

					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)


	elif message_id == 891665705655746600:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		balance = user_balance[str(member.name)]['RUB']

		if payload.emoji.name == "💷":
			if balance < 25:
				await member.send("У вас недостаточно средств для покупки кейса.")

			elif balance >= 25:
				user_balance[str(member.name)]['RUB'] -= 25
				items = [45, 35, 25, 25, 10, 5, 'role', 'farm', 'role1']

				item = random.choice(items)
				print(item)

				if item == 'role':
					getrole = discord.utils.get(guild.roles, id = 890123446682521621)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@☄️`!")

				elif item == 'role1':
					getrole = discord.utils.get(guild.roles, id = 890960183155630191)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Бизнесмен`!")

				elif item == 'farm':
					await CreateFarmChannel(member, 'FARM ПЛАТА')
					await member.send("Вы выиграли ферму `FARM ПЛАТА`!")

				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')

				with open('user_balance.json','w') as f:
					json.dump(user_balance,f)

		elif payload.emoji.name == "💳":
			if balance < 125:
				await member.send("У вас недостаточно средств для покупки 5 кейсов.")

			elif balance >= 125:
				user_balance[str(member.name)]['RUB'] -= 125
				for i in range(5):
					items = [45, 35, 25, 25, 10, 5, 'role', 'farm', 'role1']

					item = random.choice(items)
					print(item)

					if item == 'role':
						getrole = discord.utils.get(guild.roles, id = 890123446682521621)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@☄️`!")

					elif item == 'role1':
						getrole = discord.utils.get(guild.roles, id = 890960183155630191)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Бизнесмен`!")

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ПЛАТА')
						await member.send("Вы выиграли ферму `FARM ПЛАТА`!")

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')

					with open('user_balance.json','w') as f:
						json.dump(user_balance,f)


	# Bank
	elif message_id == 890961877520240690:
		if payload.emoji.name == "1️⃣":
			await member.send('Сколько вы хотите положить в банк? Введите сумму `!bank1 СУММА`')

		elif payload.emoji.name == "2️⃣":
			await member.send('Сколько вы хотите положить в банк? Введите сумму `!bank2 СУММА`')


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
		farms = json.load(f)
		mlist = farms['bot']['out_messages_id']

	for i in range(len(mlist)):
		print(mlist[i])
		if message_id == mlist[i]:
			if payload.emoji.name == "📤":
				with open('user_balance.json','r', encoding='utf-8') as f:
					mined = json.load(f)

				mined[str(member.name)]['RUB'] += mined[str(member.name)]['mined']
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

	else:
		print("Another guild")

# |--------------------------- /REACTION EVENTS ---------------------------|








# |------------------------------- METHODS --------------------------------|
def Farm(member: discord.Member, life, amount: float, auto: bool):
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
				mined[str(member.name)]['RUB'] += round(amount, 2)
				with open('user_balance.json','w') as f:
					json.dump(mined,f)

			elif auto == False:
				mined[str(member.name)]['mined'] += round(amount, 2)
				with open('user_balance.json','w') as f:
					json.dump(mined,f)

			# Crash chance
			chance = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
			crash = random.choice(chance)
			if crash == 1:
				m_chance += 1
				if m_chance == 15:
					print("----------Farm crashed----------")
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
			print("----------Farm died----------")
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
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM ЗАТЫЧКА", description=f'Панель управления майнинг фермой "FARM ЗАТЫЧКА"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/92f8Cw8/Z.png")
		embed.add_field(name = '**Срок работы:**', value = f'35дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'25 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

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
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM GTX", description=f'Панель управления майнинг фермой "FARM GTX"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/RCt8s0K/G.png")
		embed.add_field(name = '**Срок работы:**', value = f'29дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'25 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

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
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM RTX", description=f'Панель управления майнинг фермой "FARM RTX"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/z72pGRR/R.png")
		embed.add_field(name = '**Срок работы:**', value = f'29дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'21 день', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

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
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

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
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

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
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM BOOST", description=f'Панель управления майнинг фермой "FARM BOOST"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/rf67N6Y/B.png")
		embed.add_field(name = '**Срок работы:**', value = f'20дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'14 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

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
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM TITAN", description=f'Панель управления майнинг фермой "FARM TITAN"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/87WYdBB/T.png")
		embed.add_field(name = '**Срок работы:**', value = f'30дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'16 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

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
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM SERVER", description=f'Панель управления майнинг фермой "FARM SERVER"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/0KDHq9W/S.png")
		embed.add_field(name = '**Срок работы:**', value = f'38дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'13 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

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
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

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
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

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
		embed = discord.Embed(color=0x3C55FA, title="ПАНЕЛЬ УПРАВЛЕНИЯ FARM ПЛАТА", description=f'Панель управления майнинг фермой "FARM ПЛАТА"\n\n**ДЛЯ ВЫВОДА RUB НАЖМИТЕ НА 📤**\n\n')
		embed.set_thumbnail(url="https://i.ibb.co/pd6w8dt/plata.png")
		embed.add_field(name = '**Срок работы:**', value = f'11дней', inline = True)
		embed.add_field(name = '**Срок окупаемости:**', value = f'10 дней', inline = True)
		embed.add_field(name = '**До вывода осталось:**', value = f'60 минут', inline = True)
		message = await channel.send(embed=embed)
		await message.add_reaction('📤')
		with open('user_farms.json','r', encoding='utf-8') as f:
			farms = json.load(f)

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]['farms'] = f'{farm}'
		farms[str(member.name)]['life_time'] = 950400
		farms[str(member.name)]['out'] = 0.3
		farms[str(member.name)]['auto'] = False
		farms[str(member.name)]['channel_id'] = channel.id
		with open('user_farms.json','w') as f:
			json.dump(farms,f)

		farmth = Thread(target=Farm, args=(member, 950400, 0.3, False))
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

# |------------------------------- /METHODS -------------------------------|








# |------------------------------ COMMANDS ------------------------------|
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
	global donat1s
	global donat2s
	global membercode
	global gncode
	guild = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild:
		print('In guild')

	else:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		if code == "donat1":
			if donat1s == False:
				await CreateFarmChannel(ctx.message.author, 'FARM ПЛАТА')
				await ctx.message.author.send("Вы получили `FARM ПЛАТА`!")

				log = bot.get_channel(888053213750779934)
				embed1 = discord.Embed(color=0x388E3C, title="АКТИВАЦИЯ ПРОМОКОДА", description=f'**`{ctx.message.author}` Активировал промокод `donat1`**')
				await log.send(embed=embed1)
				donat1s = True

			else:
				await ctx.message.author.send("Этот промокод нельзя активировать больше 1 раза.")


		elif code == "donat2":
			if donat2s == False:
				await CreateFarmChannel(ctx.message.author, 'FARM ПЛАТА')
				await ctx.message.author.send("Вы получили `FARM ПЛАТА`!")

				log = bot.get_channel(888053213750779934)
				embed1 = discord.Embed(color=0x388E3C, title="АКТИВАЦИЯ ПРОМОКОДА", description=f'**`{ctx.message.author}` Активировал промокод `donat2`**')
				await log.send(embed=embed1)
				donat2s = True

		elif code == "test5":
			if ctx.message.author.id == 891032252350357565:
				if membercode == False:
					user_balance[str(ctx.message.author.name)]['RUB'] += 5

					log = bot.get_channel(888053213750779934)
					embed1 = discord.Embed(color=0x388E3C, title="АКТИВАЦИЯ ПРОМОКОДА", description=f'**`{ctx.message.author}` Активировал промокод `test5`**')
					await log.send(embed=embed1)
					membercode = True

				else:
					await ctx.message.author.send("Этот промокод нельзя активировать больше 1 раза.")

		elif code == "GONANEXT":
			if gncode < 3:
				user_balance[str(ctx.message.author.name)]['RUB'] += 5

				log = bot.get_channel(888053213750779934)
				embed1 = discord.Embed(color=0x388E3C, title="АКТИВАЦИЯ ПРОМОКОДА", description=f'**`{ctx.message.author}` Активировал промокод `test5`**')
				await log.send(embed=embed1)
				gncode += 1

			elif gncode == 3:
				await ctx.message.author.send("Этот промокод нельзя активировать больше 3 раз.")

			else:
				print("No member activated")

		else:
			await ctx.send("Промокод не найден.")

		with open('user_balance.json','w') as f:
			json.dump(user_balance,f)


# ------------------------ Moderation ------------------------|
# Ban
@bot.command()
@commands.has_any_role(881141342959439882,  881603894449406022, 880357242346553374)
async def ban(ctx, member: discord.Member, time: int, *, about: str):
	await ctx.message.add_reaction('✅')
	getrole = discord.utils.get(ctx.guild.roles, id = 888483227080224779)
	await member.add_roles(getrole)
	embed = discord.Embed(color = 0xff0000, description = f'Вам ограничили доступ к серверу NEXT InvesT по причине: {about} на {time} минут.')
	await member.send(embed = embed)

	log = bot.get_channel(888053213750779934)
	embed1 = discord.Embed(color=0x388E3C, title="БАН", description=f'**`{member}` Был забанен `{ctx.message.author}` на `{time} минут` по причине\n\n```diff\n- {about}\n```**')
	await log.send(embed=embed1)

	await asyncio.sleep(time*60)
	await member.remove_roles(getrole)

# Unban
@bot.command()
@commands.has_any_role(881141342959439882, 881141987108085770)
async def unban(ctx, member: discord.Member):
	await ctx.message.add_reaction('✅')
	getrole = discord.utils.get(ctx.guild.roles, id = 888483227080224779)
	await member.remove_roles(getrole)

	log = bot.get_channel(888053213750779934)
	embed1 = discord.Embed(color=0x388E3C, title="РАЗБАН", description=f'**`{member.name}` Был разбанен `{ctx.message.author}`**')
	await log.send(embed=embed1)

# Mute
@bot.command()
@commands.has_any_role(881141342959439882, 881141987108085770)
async def mute(ctx, member: discord.Member, time: int, *, about: str):
	await ctx.message.add_reaction('✅')
	getrole = discord.utils.get(ctx.guild.roles, id = 888461992824799283)
	await member.add_roles(getrole)
	embed = discord.Embed(color = 0xff0000, description = f'Вам ограничили письменный доступ к серверу NEXT InvesT по причине: {about} на {time} минут.')
	await member.send(embed = embed)

	log = bot.get_channel(888053213750779934)
	embed1 = discord.Embed(color=0x388E3C, title="МЬЮТ", description=f'**`{member.name}` Был замьючен `{ctx.message.author}` на `{time} минут` по причине\n\n```diff\n- {about}\n```**')
	await log.send(embed=embed1)

	await asyncio.sleep(time*60)
	await member.remove_roles(getrole)

# Unmute
@bot.command()
@commands.has_any_role(881141342959439882, 881141987108085770)
async def unmute(ctx, member: discord.Member):
	await ctx.message.add_reaction('✅')
	getrole = discord.utils.get(ctx.guild.roles, id = 888461992824799283)
	await member.remove_roles(getrole)

	log = bot.get_channel(888053213750779934)
	embed1 = discord.Embed(color=0x388E3C, title="РАЗМЬЮТ", description=f'**`{member.name}` Был размьючен `{ctx.message.author}`**')
	await log.send(embed=embed1)


# ubal
@bot.command()
@commands.has_any_role(881141342959439882, 881141987108085770)
async def ubal(ctx, member: discord.Member, ctype, op: str, amount: int):
	await ctx.message.add_reaction('✅')
	with open('user_balance.json','r', encoding='utf-8') as f:
		user_balance = json.load(f)

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
			user_balance[str(member.name)]['NTB'] = amount
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

# ----------------------- /Moderation ------------------------|


@bot.command()
async def upd(ctx):
	guild = bot.get_guild(880008097370865706)

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
	embedf3.add_field(name = '**Производительность:**', value = "1.5RUB/ч", inline = True)
	embedf3.add_field(name = '**Срок окупаемости:**', value = "21 дней", inline = True)

	embedf3.add_field(name = '**Сложность:**', value = "NORM", inline = True)
	embedf3.add_field(name = '**Вывод RUB на баланс:**', value = "Автоматический", inline = True)
	embedf3.add_field(name = '**ЦЕНА:**', value = "**749RUB**", inline = True)
	await m3.edit(embed = embedf3)


	m4 = await farms.fetch_message(886528476797083668)
	embedf4 = discord.Embed(color=0x3C55FA, title="FARM MULTI", description=f'На мощном оборудовании для майнинга\n\n**Для покупки за RUB нажмите :euro:**\n')
	embedf4.set_thumbnail(url="https://i.ibb.co/SmQ7bNk/M.png")
	embedf4.add_field(name = '**Макс срок работы:**', value = "40дней", inline = True)
	embedf4.add_field(name = '**Производительность:**', value = "2RUB/ч", inline = True)
	embedf4.add_field(name = '**Срок окупаемости:**', value = "21 день", inline = True)

	embedf4.add_field(name = '**Сложность:**', value = "NORM", inline = True)
	embedf4.add_field(name = '**Вывод RUB на баланс:**', value = "Автоматический", inline = True)
	embedf4.add_field(name = '**ЦЕНА:**', value = "**999RUB**", inline = True)
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

	'''
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
	'''

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



	'''
	farms = bot.get_channel(880025073963122718)
	m = await farms.fetch_message(886528504068464640)
	embedf10 = discord.Embed(color=0x3C55FA, title="FARM ПЛАТА", description=f'Самая простая видеокарта\n\n**Для покупки за RUB нажмите :euro:**\n')
	embedf10.set_thumbnail(url="https://i.ibb.co/pd6w8dt/plata.png")
	embedf10.add_field(name = '**Макс срок работы:**', value = "11дней", inline = True)
	embedf10.add_field(name = '**Производительность:**', value = "0.3v/ч", inline = True)
	embedf10.add_field(name = '**Срок окупаемости:**', value = "10 дней", inline = True)

	embedf10.add_field(name = '**Сложность:**', value = "EASY", inline = True)
	embedf10.add_field(name = '**Вывод RUB на баланс:**', value = "Ручной", inline = True)
	embedf10.add_field(name = '**ЦЕНА:**', value = "79RUB", inline = True)
	await m.edit(embed = embedf10)

	
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

	m = await channel.fetch_message(890117691388600320)
	embed = discord.Embed(color=0x80F7FF, title=f'PLATINUM CASE', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**850RUB | 650RUB | 500RUB | 420RUB | 400RUB|** 350 RUB| 200RUB | 100RUB | 65 RUB| Premium  45 day\n-FARM GTX\n-FARM RTX\n-FARM ASIC\nУНИКАЛЬНАЯ РОЛЬ 🌀\n\n**НАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:\n**:pound: 1шт - 500RUB\n:credit_card: 5шт - 2500RUB')
	embed.set_thumbnail(url="https://i.ibb.co/1MDfBNc/PLATINUM.png")
	await m.edit(embed = embed)
	

	
	channel = bot.get_channel(889843449300398111)
	m2 = await channel.fetch_message(891665705655746600)
	embed = discord.Embed(color=0x2E62FF, title=f'Кейс открытие', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**500RUB | 350RUB | 120RUB | 45RUB | 35RUB | 25RUB |** 10RUB | 5RUB |\n**Ферма** - FARM ПЛАТА\n**УНИКАЛЬНАЯ РОЛЬ** ☄️; Бизнесмен;\n\nНАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:\n**:pound: 1шт - ~~75RUB~~ 25RUB**\n:credit_card: 5шт - ~~375RUB~~ 125RUB')
	embed.set_thumbnail(url="https://i.ibb.co/1LWW1R8/PREMIUM.png")
	await m2.edit(embed = embed)
	


	m2 = await channel.fetch_message(890117683478147092)
	embed2 = discord.Embed(color=0xFBFF29, title=f'GOLD CASE', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**450RUB | 330RUB | 250RUB | 210RUB | 200RUB |** 150RUB | 100RUB | 85 RUB | 65RUB | 50RUB | Premium  - 30 day\n**-FARM ЗАТЫЧКА\n-FARM GTX\nУНИКАЛЬНАЯ РОЛЬ :zap: Gold Monopolis**\n\n**НАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:\n**:pound: 1шт - 199RUB\n:credit_card: 5шт - 995RUB')
	embed2.set_thumbnail(url="https://i.ibb.co/Kq8j5qT/GOLD.png")
	await m2.edit(embed = embed2)



	m3 = await channel.fetch_message(890117675408322580)
	embed3 = discord.Embed(color=0x949494, title=f'SILVER CASE', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**450RUB | 320RUB | 160RUB | 80RUB |** 55RUB | 40RUB | 20RUB | Premium  - 14 day\n-FARM ПЛАТА\n-FARM ЗАТЫЧКА\nУникальная роль :airplane:\n\n**НАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:\n**:pound: 1шт - 99RUB\n:credit_card: 5шт - 496RUB')
	embed3.set_thumbnail(url="https://i.ibb.co/xXnJTXq/SILVER.png")
	await m3.edit(embed = embed3)



	m4 = await channel.fetch_message(890117667908878347)
	embed4 = discord.Embed(color=0xB88947, title=f'BRONZE CASE', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**300RUB| 220RUB | 140RUB | 100RUB | 50RUB |** 35RUB | 20RUB |  10RUB |\nУникальная роль бизнесмен\n\n**НАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:**\n:pound: 1шт - 49RUB\n:credit_card: 5шт - 245RUB')
	embed4.set_thumbnail(url="https://i.imgur.com/MRvrOW2.png")
	await m4.edit(embed = embed4)
	

	channel1 = bot.get_channel(890982389881384991)
	embed165 = discord.Embed(color=0x2E62FF, description=f'<:dfgf:> :dfgf: :a_::a_::b_::b_::b_::b_::b_::b_::b_: `3/10`')
	await channel1.send(embed = embed165)

	embed168 = discord.Embed(color=0x2E62FF, description=f':l_::a_::a_::a_::a_::b_::b_::b_::b_::b_: `5/10`')
	await channel1.send(embed = embed168)

	embed168 = discord.Embed(color=0x2E62FF, description=f':l_::b_::b_::b_::b_::b_::b_::b_::b_::b_: `1/10`')
	await channel1.send(embed = embed168)
	await channel1.send('<:dfgf:> :dfgf: :a_::a_::b_::b_::b_::b_::b_::b_::b_: `3/10`')
	'''

bot.run('ODc5NjkzNDk5ODQ1NDU1ODcy.YSTcag.KiNpzAVZ_isc-HIdeeLw6FbJZgM')
