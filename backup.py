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
tickets_messages = []
# |------------------------------ /VARIABLES -----------------------------|








# |-------------------------------- EVENTS --------------------------------|
@bot.event
async def on_ready():
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
				channel = i[1]["channel_id"]
				print(f'{member} HAVE FARM.\n')
				print(f'{life}  {out}  {mode}  {channel}')

				farmth = Thread(target=Farm, args=(member, i[0], life, out, mode))
				farmth.start()

			else:
				print(f'{member} NO FARMS\n')

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
				items = [50, 35, 25, 20, 15, 10, 'role', 'role1']

				item = random.choice(items)
				print(item)

				if item == 'role':
					getrole = discord.utils.get(guild.roles, id = 890960183155630191)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@бизнесмен`!")

				elif item == 'role1':
					getrole = discord.utils.get(guild.roles, id = 892435708881539103)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Trainer`!")


				else:
					user_balance[str(member.name)]['RUB'] += float(item)
					await member.send(f'Вы выиграли **`{item}` RUB**!')

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
						getrole = discord.utils.get(guild.roles, id = 890960183155630191 )
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@бизнесмен`!")

					elif item == 'role1':
						getrole = discord.utils.get(guild.roles, id = 892435708881539103)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Trainer`!")

					else:
						user_balance[str(member.name)]['RUB'] += float(item)
						await member.send(f'Вы выиграли **`{item}` RUB**!')

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
						getrole = discord.utils.get(guild.roles, id = 890960183155630191 )
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@бизнесмен`!")

					elif item == 'role1':
						getrole = discord.utils.get(guild.roles, id = 892435708881539103)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Trainer`!")

					else:
						user_balance[str(member.name)]['RUB'] += float(item)
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
				items = [80, 50, 55, 40, 20, 10, 'premium16', 'premium10', 'farm', 'jet', 'zap']

				item = random.choice(items)
				print(item)

				if item == 'premium16':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 16 days`!")

				elif item == 'premium10':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 10 days`!")

				elif item == 'farm':
					await CreateFarmChannel(member, 'FARM ПЛАТА')
					await member.send("Вы выиграли ферму `FARM ПЛАТА`!")

				elif item == 'jet':
					getrole = discord.utils.get(guild.roles, id = 890112890722463774)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@:plane:`!")

				elif item == 'zap':
					getrole = discord.utils.get(guild.roles, id = 890099592752939009)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@:zap:`!")

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
					items = [80, 50, 55, 40, 20, 10, 'premium16', 'premium10', 'farm', 'zap', 'jet']

					item = random.choice(items)
					print(item)

					if item == 'premium16':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 16 days`!")

					elif item == 'premium10':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 10 days`!")

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ПЛАТА')
						await member.send("Вы выиграли ферму `FARM ПЛАТА`!")

					elif item == 'jet':
						getrole = discord.utils.get(guild.roles, id = 890112890722463774)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:plane:`!")

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')

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

					elif item == 'premium10':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 10 days`!")

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ПЛАТА')
						await member.send("Вы выиграли ферму `FARM ПЛАТА`!")

					elif item == 'jet':
						getrole = discord.utils.get(guild.roles, id = 890112890722463774)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:plane:`!")

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")

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
				items = [210, 200, 150, 100, 125, 85, 65, 50, 'premium30', 'premium21', 'farm', 'role2', 'role3']

				item = random.choice(items)
				print(item)

				if item == 'premium30':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 30 day`!")

				elif item == 'premium21':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium 21 day`!")

				elif item == 'farm':
					await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')
					await member.send("Вы выиграли ферму `FARM ЗАТЫЧКА`!")

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
					items = [210, 200, 150, 125, 100, 85, 65, 50, 'premium30', 'premium21', 'farm', 'role2', 'role3']

					item = random.choice(items)
					print(item)

					if item == 'premium30':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 30 day`!")

					elif item == 'premium21':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 21 day`!")

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')
						await member.send("Вы выиграли ферму `FARM ЗАТЫЧКА`!")

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

					elif item == 'premium21':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium 21 day`!")

					elif item == 'farm':
						await CreateFarmChannel(member, 'FARM ЗАТЫЧКА')
						await member.send("Вы выиграли ферму `FARM ЗАТЫЧКА`!")

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
				items = [420, 400, 350, 200, 100, 65, 'premium45', 'premium26', 'premium35', 'zap', 'asic']

				item = random.choice(items)
				print(item)

				if item == 'premium45':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium - 45 days`!")

				elif item == 'premium26':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium - 26 days`!")

				elif item == 'premium35':
					getrole = discord.utils.get(guild.roles, id = 888115759933431909)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Premium - 35 days`!")

				elif item == 'zap':
					getrole = discord.utils.get(guild.roles, id = 890587785856155649)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@🌀`!")

				elif item == 'asic':
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
					items = [420, 400, 350, 200, 100, 65, 'premium45', 'premium26', 'premium35', 'zap', 'asic']

					item = random.choice(items)
					print(item)

					if item == 'premium45':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 45 days`!")

					elif item == 'premium26':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 26 days`!")

					elif item == 'premium35':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 35 days`!")

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890587785856155649)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@🌀`!")

					elif item == 'asic':
						await CreateFarmChannel(member, 'FARM ASIC')
						await member.send("Вы выиграли ферму `FARM ASIC`!")

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')

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

					elif item == 'premium26':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 26 days`!")

					elif item == 'premium35':
						getrole = discord.utils.get(guild.roles, id = 888115759933431909)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Premium - 35 days`!")

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890587785856155649)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@🌀`!")

					elif item == 'asic':
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

				elif item == 'zap':
					getrole = discord.utils.get(guild.roles, id = 890099592752939009)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@:zap:`!")

				elif item == 'comet':
					getrole = discord.utils.get(guild.roles, id = 890123446682521621)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@☄`!")

				elif item == 'bussines':
					getrole = discord.utils.get(guild.roles, id = 890960183155630191)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Бизнесмен`!")

				elif item == 'gold':
					getrole = discord.utils.get(guild.roles, id = 890119660488491049)
					await member.add_roles(getrole)
					await member.send("Вы выиграли роль `@Gold`!")

				else:
					user_balance[str(member.name)]['RUB'] += item
					await member.send(f'Вы выиграли **`{item}` RUB**!')

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

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")

					elif item == 'comet':
						getrole = discord.utils.get(guild.roles, id = 890123446682521621)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@☄`!")

					elif item == 'bussines':
						getrole = discord.utils.get(guild.roles, id = 890960183155630191)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Бизнесмен`!")

					elif item == 'gold':
						getrole = discord.utils.get(guild.roles, id = 890119660488491049)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Gold`!")

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')

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

					elif item == 'zap':
						getrole = discord.utils.get(guild.roles, id = 890099592752939009)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@:zap:`!")

					elif item == 'comet':
						getrole = discord.utils.get(guild.roles, id = 890123446682521621)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@☄`!")

					elif item == 'bussines':
						getrole = discord.utils.get(guild.roles, id = 890960183155630191)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Бизнесмен`!")

					elif item == 'gold':
						getrole = discord.utils.get(guild.roles, id = 890119660488491049)
						await member.add_roles(getrole)
						await member.send("Вы выиграли роль `@Gold`!")

					else:
						user_balance[str(member.name)]['RUB'] += item
						await member.send(f'Вы выиграли **`{item}` RUB**!')

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
				mined[str(member)]['mined'] += round(amount, 2)
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 3024000, "out": 0.25, "auto": False, "channel_id": channel.id}
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 2505600, "out": 0.5, "auto": False, "channel_id": channel.id}
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 2505600, "out": 1.0, "auto": False, "channel_id": channel.id}
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 3024000, "out": 1.5, "auto": True, "channel_id": channel.id}
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 2851200, "out": 2.0, "auto": True, "channel_id": channel.id}
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 1728000, "out": 0.3, "auto": False, "channel_id": channel.id}
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 2592000, "out": 4.0, "auto": False, "channel_id": channel.id}
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 3283200, "out": 7.0, "auto": False, "channel_id": channel.id}
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 3196800, "out": 14.0, "auto": True, "channel_id": channel.id}
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 3628800, "out": 25.0, "auto": True, "channel_id": channel.id}
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

		farms['bot']['out_messages_id'].append(message.id)

		farms[str(member.name)]["farms"][f'{str(farm)}'] = {"stats": True, "life_time": 950400, "out": 0.3, "auto": False, "channel_id": channel.id}
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
					log = bot.get_channel(888053213750779934)
					embed1 = discord.Embed(color=0x388E3C, title="АКТИВАЦИЯ ПРОМОКОДА", description=f'**`{ctx.message.author}` Активировал промокод `{code}`**')
					await log.send(embed=embed1)

				elif activations <= 0:
					await ctx.message.author.send('Этот прокод больше нельзя активировать.')

# Create promocodes
@bot.command()
async def addpromo(ctx, type, name, activations=None, mtype=None, money=None, *, farm=None):
	#if ctx.message.author.id == 663424295854407692:
	with open('promocodes.json','r', encoding='utf-8') as f:
		codes = json.load(f)

	if mtype != None and money != None and farm == None and activations != None:
		if mtype == "RUB" or mtype == "NTB":
			codes[str(name)] = {"mtype": f'{mtype}', "money": int(money), "farm": "none", "activations": int(activations)}
			await ctx.message.add_reaction('✅')

		else:
			await ctx.send(f'Валюты {mtype} не существует.')

	elif mtype == None and money == None and farm != None and activations != None:
		codes[str(name)] = {"mtype": "RUB", "money": 0, "farm": f'{farm}', "activations": activations}
		await ctx.message.add_reaction('✅')

	else:
		await ctx.send("Ошибка в синтаксисе команды.")

	with open('promocodes.json','w') as f:
		json.dump(codes,f)

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

	else:
		print("Not man")


@bot.command()
async def bal(ctx, member: discord.Member):
	with open('user_balance.json','r', encoding='utf-8') as f:
		balance = json.load(f)

	rub = balance[str(member.name)]['RUB']
	ntb = balance[str(member.name)]['NTB']

	await ctx.send(f'**{member}**: {rub}RUB **|** {ntb}NTB')


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
					'''
					if stats == True:
						# if box4 filled
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
						'''
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

					'''
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
					'''

				else:
					await ctx.message.author.send("У вас недостаточно средств.")
			else:
				await ctx.message.author.send("Сумма вложения должна быть не менее 1 и не боле 350RUB.")




		else:
			await ctx.message.author.send(f'Копилка с номером {box} не найдена.')


@bot.command()
async def db(ctx):
	guild = bot.get_guild(880008097370865706)
	if ctx.message.guild == guild:
		print('In guild')

	else:
		with open('user_balance.json','r', encoding='utf-8') as f:
			user_balance = json.load(f)

		with open('user_farms.json','r', encoding='utf-8') as f:
			user_farms = json.load(f)

		with open('referal.json','r', encoding='utf-8') as f:
			ref = json.load(f)

		with open('user_bank.json','r', encoding='utf-8') as f:
			bank = json.load(f)

		with open('db.txt','w+', encoding='utf-8') as f:
			f.write(f'user_balance.json:\n{user_balance}\n\n\nuser_farms.json:\n{user_farms}\n\n\nreferal.json:\n{ref}\n\n\nuser_bank.json:\n{bank}')

		member = guild.get_member(677453905227022349)
		await ctx.send(file=discord.File(r'db.txt'))

# ----------------------- /Moderation ------------------------|


@bot.command()
async def upd(ctx):
	if ctx.message.author.id == 677453905227022349:

		guild = bot.get_guild(880008097370865706)
		'''
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
		

		

		channel = bot.get_channel(889843449300398111)

		m1 = await channel.fetch_message(890117683478147092)
		embed1 = discord.Embed(color=0xFBFF29, title=f'GOLD CASE', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**450RUB | 330RUB | 250RUB | 210RUB | 200RUB |** 150RUB | 125RUB | 100RUB | 85 RUB | 65RUB | 50RUB |\nPremium 30 day\n Premium 21 day\n-FARM ЗАТЫЧКА\n-FARM GTX\n-FARM RTX\nУНИКАЛЬНАЯ РОЛЬ :zap: Gold Monopolis**\n\n**НАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:\n:pound: 1шт - 199RUB\n:credit_card: 5шт - 995RUB\n:moneybag: 10шт - 1990RUB')
		embed1.set_thumbnail(url="https://i.ibb.co/Kq8j5qT/GOLD.png")
		await m1.edit(embed = embed1)
		await m1.add_reaction('💰')

				
		m = await channel.fetch_message(890117691388600320)
		embed = discord.Embed(color=0x80F7FF, title=f'PLATINUM CASE', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**850RUB | 650RUB | 500RUB | 535RUB | 420RUB | 400RUB|** 350 RUB| 200RUB | 100RUB | 65 RUB|\nPremium 45 day\nPremium 35 day\nPremium 26 day\n-FARM MULTI\n-FARM GTX\n-FARM RTX\n-FARM ASIC\nУНИКАЛЬНАЯ РОЛЬ 🌀\n\n**НАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:\n**:pound: 1шт - 500RUB\n:credit_card: 5шт - 2500RUB\n:moneybag: 10шт - 5000RUB')
		embed.set_thumbnail(url="https://i.ibb.co/1MDfBNc/PLATINUM.png")
		await m.edit(embed = embed)
		await m.add_reaction('💰')

		m2 = await channel.fetch_message(893551335511830649)
		embed2 = discord.Embed(color=0x80F7FF, title=f'LITE CASE', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**625RUB| 500RUB | 350RUB | 120RUB | 45RUB** | 35RUB | 25RUB | 15 RUB| 10RUB | 5RUB |\nPremium 7 days\nФерма - FARM ПЛАТА\nУНИКАЛЬНАЯ РОЛЬ  ⚡; Gold; ☄️; Бизнесмен;\n\n**НАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:\n**:pound: 1шт - ~~125~~RUB **35**RUB\n:credit_card: 5шт - ~~625~~RUB **175**RUB\n:moneybag: 10шт - 350RUB')
		embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/828213712736354305/893521241724563527/PREMIUM.png")
		await m2.edit(embed = embed2)
		await m2.add_reaction('💰')
		
		m3 = await channel.fetch_message(890117675408322580)
		embed3 = discord.Embed(color=0x949494, title=f'SILVER CASE', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**450RUB | 320RUB | 160RUB | 80RUB | 65RUB |** 55RUB | 40RUB | 20RUB |\nPremium 16 days\nPremium 10 days\n-FARM ПЛАТА\n-FARM ЗАТЫЧКА\n-FARM ASIC\nУникальная роль :airplane:\nУникальная роль :zap:\nУникальная роль ☄️\n\n**НАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:\n**:pound: 1шт - 99RUB\n:credit_card: 5шт - 496RUB\n:moneybag: 10шт - 990RUB')
		embed3.set_thumbnail(url="https://i.ibb.co/xXnJTXq/SILVER.png")
		await m3.edit(embed = embed3)
		await m3.add_reaction('💰')
		
		m4 = await channel.fetch_message(890117667908878347)
		embed4 = discord.Embed(color=0xB88947, title=f'BRONZE CASE', description=f'ВОЗМОЖНЫЕ ПРИЗЫ:\n**300RUB| 220RUB | 140RUB | 100RUB | 65RUB | 50RUB |** 35RUB | 25RUB | 20RUB | 15RUB | 10RUB |\nУникальная роль бизнесмен\nУникальная роль Trainer\n\n**НАЖМИТЕ. ЧТОБЫ ОТКРЫТЬ:**\n:pound: 1шт - 49RUB\n:credit_card: 5шт - 245RUB\n:moneybag: 10шт - 490RUB')
		embed4.set_thumbnail(url="https://i.imgur.com/MRvrOW2.png")
		await m4.edit(embed = embed4)
		await m4.add_reaction('💰')
		
		
		channel1 = bot.get_channel(890982389881384991)
		embed165 = discord.Embed(color=0x2E62FF, description=f'<:dfgf:> :dfgf: :a_::a_::b_::b_::b_::b_::b_::b_::b_: `3/10`')
		await channel1.send(embed = embed165)

		embed168 = discord.Embed(color=0x2E62FF, description=f':l_::a_::a_::a_::a_::b_::b_::b_::b_::b_: `5/10`')
		await channel1.send(embed = embed168)

		embed168 = discord.Embed(color=0x2E62FF, description=f':l_::b_::b_::b_::b_::b_::b_::b_::b_::b_: `1/10`')
		await channel1.send(embed = embed168)
		await channel1.send('<:dfgf:> :dfgf: :a_::a_::b_::b_::b_::b_::b_::b_::b_: `3/10`')
		
	
		# SUPER MONEY BOXES
		channel = bot.get_channel(888500024214966282)
		#embed = discord.Embed(color=0x2E62FF, title="**Супер копилка**", description=f'**Супер копилка** - это место, где можно заработать огромные проценты за короткое время.\nСуть данного раздела заключается в том, что каждый игрок может внести свой вклад в общее дело и получить +10% чистого профита после полного заполнения следующей копилки.\n\nТ.е. если коротко, вложил 100 рублей в  копилку №1, после заполнения копилки №2 Вы получите 110 руб. на вывод.')
		#await channel.send(embed = embed)
		'''
		
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

		

	else:
		print("Not man")

bot.run('token')

	'''
	guild = bot.get_guild(880008097370865706)
	navigation = bot.get_channel(880023035262959636)
	embed = discord.Embed(color=0x3C55FA, title=f'▰▰▰▰ ДОБРО ПОЖАЛОВАТЬ В {guild.name} ▰▰▰▰', description=f'НАШ СЕРВЕР ПОЗВОЛЯЕТ НЕ ТОЛЬКО ПРИЯТНО ПРОВЕСТИ ВРЕМЯ, НО И ПРИ ЭТОМ ЗАРАБОТАТЬ __РЕАЛЬНЫЕ ДЕНЬГИ__\n\n[:arrow_forward: ОЗНАКОМИТЬСЯ С СИСТЕМОЙ ЗАРАБОТКА](https://discord.com/channels/880008097370865706/880024762942889994/881782363191910440)\n[:arrow_forward: НАЖМИТЕ ЕСЛИ ОСТАЛИСЬ ВОПРОСЫ](https://discord.com/channels/880008097370865706/880023125062995969/880023125062995969)\n\n**ДЛЯ УДОБНОГО ПЕРЕМЕЩЕНИЯ МЕЖДУ КАНАЛАМИ СЕРВЕРА, ИСПОЛЬЗУЙТЕ НАВИГАЦИОННЫЕ КНОПКИ:**\n\n```ИНФОРМАЦИОННЫЕ КАНАЛЫ         ```\n\n<#880008098000035872> — ВАШИ ОТЗЫВЫ\n<#880023035262959636> — НАВИГАЦИОННЫЙ КАНАЛ\n<#880023125062995969> — ОТВЕТЫ НА ЧАСТЫЕ ВОПРОСЫ\n<#880023332639096853> — ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ\n<#880023390847635476> — СПИСОК ПРАВИЛ\n<#880023473106337854> — РОЗЫГРЫШИ\n<#880023539758034945> — ПУБЛИКАЦИЯ ОБНОВЛЕНИЙ\n<#880023539758034945> — ПУБЛИКАЦИИ, ОБЪЯВЛЕНИЯ И НОВОСТИ\n\n```КАНАЛЫ ПО МАЙНИНГУ```\n\n<#880024690821853184> — СПИСОК КОМАНД СЕРВЕРА\n<#880024762942889994> — ИНФОРМАЦИЯ О СИСТЕМЕ ЗАРАБОТКА\n<#880024820018999386> — ИНФОРМАЦИЯ О ИВЕНТАХ\n<#880024901744996352> — СУЩЕСТВУЮЩИЕ ДОСТИЖЕНИЯ\n\n```МАГАЗИНЫ```\n\n<#880025073963122718> — МАГАЗИН ФЕРМ\n<#880025182343946260> — МАГАЗИН УЛУЧШЕНИЙ\n#╠🧰кейсы — МАГАЗИН КЕЙСОВ\n#╚🎲игры — МАГАЗИН КЛЮЧЕЙ ИГР\n\n```НЕДВИЖИМОСТЬ```\n\n#╔🌐помощь — ИНФОРМАЦИЯ О СИСТЕМЕ\n<#880026196711178250> — СУЩЕСТВУЮЩИЕ ПОСЕЛЕНИЯ\n<#880026304194441256> — АУКЦИОН УЧАСТКОВ\n<#880026435853647973> — ТОРГОВЫЙ КАНАЛ\n\n```NPC```\n\n#🔧механик — МЕХАНИК\n#📟рынок — РЫНОК ДЕТАЛЕЙ ДЛЯ ФЕРМ\n\n```КАНАЛЫ ДЛЯ ОБЩЕНИЯ```\n\n<#880027455769944074> — КАНАЛ ПРИВЕТСТВИЯ\n<#880027613261864970> — ОСНОВНОЕ ОБЩЕНИЕ\n<#880027728466837574> — ЗАРАБАТЫВАЙТЕ НА S.UP/BUMP\n#├🦀помощь — ЗАДАЙТЕ ВОПРОС\n#├📨предложения — ВАШИ ПРЕДЛОЖЕНИЯ\n#└🤺поединки — ПОЕДИНКИ НА ВАЛЮТУ\n\n#▶💬общение  — НЕМОДЕРИРУЕМЫЙ ЧАТ 18+\n<#880355140098482208>  — ИГРОВОЙ ЧАТ\n\n```ТВОРЧЕСТВО```\n\n<#880349406933692416> ПУБЛИКУЙТЕ МЕМЫ\n#├🎭творчество ПУБЛИКУЙТЕ СВОЁ ТВОРЧЕСТВО\n#├🍏еда ОТПРАВЬТЕ ФОТО ЕДЫ\n#└📷медиа РАНДОМНЫЕ МЕДИА ФАЙЛЫ\n\n```ЗАКАЗАТЬ МУЗЫКУ```\n\n<#880352375288774667> — КОМАНДА ДЛЯ ЗАКАЗА\n<#880352647549435955> — МУЗЫКАЛЬНЫЙ ЧАТ\n\n```ПРОЧИЕ КАНАЛЫ```\n\n<#881234226714910760> — ОТКРЫТЫЕ ВАКАНСИИ\n<#📝заявки> — ОСТАВЬТЕ ЗАЯВКУ НА ДОЛЖНОСТЬ')
	await navigation.send(embed = embed)
	'''
	
	'''
	instr = bot.get_channel(880023125062995969)
	embed = discord.Embed(color=0x3C55FA, title="ОТВЕТЫ НА ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ", description=f'**▽ СО СКОЛЬКИ ЛЕТ МОЖНО БЫТЬ НА СЕРВЕРЕ?**\nРегистрировать и использовать аккаунт Discord можно с 13 лет. На нашем сервере, так же можно сидеть с этого возраста, но мы предупреждаем пользователей, что они сами несут ответственность за свои действия и рекомендуем вступать и находиться на сервере лицам старше 16 лет.\n\n**▽ КАК НАЧАТЬ ЗАРАБАТЫВАТЬ?**\n[:arrow_forward: УЗНАТЬ СПОСОБЫ ЗАРАБОТКА](https://discord.com/channels/880008097370865706/880024762942889994/881782363191910440)\n\n**▽ КАК МНЕ ПОПОЛНИТЬ БАЛАНС?**\n[:arrow_forward: ПЕРЕЙТИ В КОМАНДЫ](https://discord.com/channels/880008097370865706/880024690821853184/881778667997528105) и нажмать эмодзи :ballot_box_with_check:, под командой "ОПЕРАЦИИ С БАЛАНСОМ". Бот отправит вам в личные сообщения ваш личный счет. Далее нажмите реакцию :outbox_tray: - Вывести , далее следуйте инструкции, заполняя данные для заявки на вывод средств.\n\n**▽ КАКОЙ КУРС ВАЛЮТ?**\n[:arrow_forward: УЗНАТЬ АКТУАЛЬНЫЙ КУРС ВАЛЮТ](https://discord.com/channels/880008097370865706/880024762942889994/881782364538294303)\n\n**▽ МОЖНО ЛИ ВЫВОДИТЬ WATT?**\nЭту валюту вы можете использовать для покупки бонусов, открытия кейсов, участия в поединках, покупке ферм и т.п. в наших магазинах. Покупая ферму, она будет вам добывать валюту Volt, которую вы сможете вывести в реальные деньги, используя свой личный счет\n\n**▽ МОЖНО ЛИ КОНВЕРТИРОВАТЬ W В V?**\nНа сервере не будет конвертации W в V. Только V в W\n\n**▽ КАКИЕ ЕСТЬ РОЛИ?**\n\n\n**▽ НА ЧЕМ ЗАРАБАТЫВАЕТ СЕРВЕР?**\n[:arrow_forward: КУПИТЬ МАЙНИНГ ФЕРМУ](https://discord.com/channels/880008097370865706/880025073963122718/881544012723519579)\nКаждая купленная вами майнинг ферма, имеет свою сложность в обслуживании. В процессе работы фермы, могут возникать разные рандомизированные события, включая перегрев, поломку и даже полное сгорание фермы. Вы можете преумножить свои финансы. купив ферму, а если вам не удалось выйти в плюс с фермы, эти деньги уйдут на:\n• Выплаты тем кто выходит в плюс с купленных ферм\n• Выплаты пользователям, зарабатывающие валюту в голосовых каналах\n• Проведение розыгрышей, раздач, ивентов и  прочих мероприятий\n• Вклад в развитие сервера и ускорение выхода обновлений\n• Заработные платы персоналу сервера\n• Покрытие затрат на рекламу сервера\n• Оплата технических расходов, для поддержания работы нашего ПО\n\nТак же мы дополнительно зарабатываем с неудач пользователей, при открытии кейсов, продаж игр в магазине и с помощью перепродажи пользователями недвижимости\n\n**▽ КАК УЧАСТВОВАТЬ В РОЗЫГРЫШАХ?**\nСледите за каналом #╠🆓розыгрыши, там публикуются все актуальные розыгрыши.')
	embed1 = discord.Embed(color=0x3C55FA, title="ОТВЕТЫ НА ВОПРОСЫ ПРО ФЕРМЫ", description=f'**▽ КАК МНЕ КУПИТЬ ФЕРМУ?**\n[:arrow_forward: ПЕРЕЙТИ В МАГАЗИН ФЕРМ](https://discord.com/channels/880008097370865706/880025073963122718/881544012723519579)\nи  нажать на реакцию :euro:, под фермой, которую вы хотите приобрести. Если на вашем счете достаточно средств, создаётся личный текстовый канал, с вашим ником, тегом фермы и персональным номером в категории "Фермы", в самом низу списка каналов. Далее вам необходимо подтвердить покупку, нажав на соответствующую реакцию, в созданном канале.\n\n**▽ КАК РАБОТАЕТ ФЕРМА?**\nЕсли ваша ферма запущена, она будет добывать вам валюту сервера, исходя из своих характеристик. В дальнейшем вы можете обменять валюту на реальные деньги. через личный счет\n\n**▽ МОЯ ФЕРМА ОСТАНОВИЛА РАБОТУ. ЧТО ДЕЛАТЬ?**\nЕсли ваша ферма перегрелась. перейдите на канал вашей фермы и нажмите кнопку :arrow_forward:Запустить\n\n**▽ ЧТО БУДЕТ ЕСЛИ ФЕРМУ НЕ ЗАПУСТИТЬ?**\nВаша ферма не будет добывать валюту, а срок работы фермы будет истекать. Чтобы этого не допустить. всегда следите за тем, чтобы статус вашей фермы был :green_circle:. В случае если произошло какое то событие с вашей фермой, наш бот дополнительно уведомляет об этом в личные сообщения.\n\n**▽ МНЕ НЕ ЗАЧИСЛЯЕТСЯ БАЛАНС VOLT, С ФЕРМЫ**\nВаш баланс Volt хранится на канале ферме, чтобы вывести баланс, необходимо нажимать кнопку :arrow_heading_down:** - Вывести**\n\n**▽ КАНАЛ МОЕЙ ФЕРМЫ ПРОПАЛ**\nВероятней всего, срок работы вашей фермы истёк. В случае если срок работы фермы закончился, канал с фермой удаляется.\n\n**▽ БУДЕТ ЛИ РАБОТАТЬ ФЕРМА ЕСЛИ Я НЕ В СЕТИ?**\nДа, фермы работают независимо от вашего статуса сети, они находятся на нашем хостинге.')
	embed2 = discord.Embed(color=0x3C55FA, title="ОТВЕТЫ НА ВОПРОСЫ ПРО РЕФЕРАЛЬНУЮ СИСТЕМУ", description=f'**▽ КАК ЭТО РАБОТАЕТ?**\n[:arrow_forward: ОЗНАКОМИТЬСЯ С РЕФЕРАЛЬНОЙ СИСТЕМОЙ](https://discord.com/channels/880008097370865706/880024762942889994/881782366526386206)\nПользователи которые ввели ваш реферальный код, закрепляются за вами и вы получаете Watt за ввод вашего кода и доход от их пополнений купонами Volt.\n\n*▽ ГДЕ ВЗЯТЬ РЕФЕРАЛЬНЫЙ КОД?**\n[▽ ГДЕ ВЗЯТЬ РЕФЕРАЛЬНЫЙ КОД?](https://discord.com/channels/880008097370865706/880024690821853184/881778673496231966)\n\n**▽ СКОЛЬКО РЕФЕРАЛЬНЫХ КОДОВ МОЖНО ВВЕСТИ?**\nРеферальный код можно ввести только один раз и закрепиться за пользователям навсегда\n\n**▽ СКОЛЬКО РЕФЕРАЛОВ МОЖНО ЗАКРЕПИТЬ ЗА СОБОЙ?**\nКоличество приглашенных и закрепленных за вами рефералов не ограничено\n\n**▽ СУММИРУЮТСЯ ЛИ VOLT ОТ ПОПОЛНЕНИЙ РЕФЕРАЛОВ?**\nЕсли за вами закреплено несколько рефералов, вы будете получать доход от каждых пополнений каждого реферала\n\n**▽ МОЖНО ЛИ ВЫВОДИТЬ ДОХОД ОТ РЕФЕРАЛОВ, НЕ ПОКУПАЯ ФЕРМ?**\nДа. Любой доход полученный не активацией кодами пополнения, зачисляется на ваш счет и может быть выведен в реальные деньги\n\n**▽ МОЖНО ЛИ ОБМЕНИВАТЬСЯ РЕФЕРАЛЬНЫМИ КОДАМИ?**\nЗакрепленный за вами пользователь, не сможет ввести ваш реферальный код\n\n**▽ МОЖНО ЛИ ОТПРАВЛЯТЬ СВОЙ КОД В ЧАТЫ?**\nДа, вы можете делиться своим кодом с другими пользователями')
	embed3 = discord.Embed(color=0x3C55FA, title="ОТВЕТЫ НА ВОПРОСЫ ПРО НЕДВИЖИМОСТЬ", description=f'**▽ КАК ЭТО РАБОТАЕТ?**\n[:arrow_forward: ОЗНАКОМИТЬСЯ С СИСТЕМОЙ НЕДВИЖИМОСТИ](https://discord.com/channels/880008097370865706/880024762942889994)\nПользователи, приобретая недвижимость на #╚🔨аукцион становятся гражданами поселения и получают доход от торговли недвижимостью другими пользователями\n\n**▽ КАК ПОСМОТРЕТЬ ПРОФИЛЬ НЕДВИЖИМОСТИ?**\n[:arrow_forward: ПЕРЕЙТИ В ПРОФИЛЬ](https://discord.com/channels/880008097370865706/880024690821853184/881778670778335253)\nи нажать реакцию :house:\n\n**▽ КАК КУПИТЬ НЕДВИЖИМОСТЬ?**\nПерейти на #╚🔨аукцион и приобрести недвижимость выкупив его за х2 от текущей ставки.\n\n**▽ КАК ПРОДАТЬ НЕДВИЖИМОСТЬ?**\n[:arrow_forward: ПЕРЕЙТИ В ПРОФИЛЬ](https://discord.com/channels/880008097370865706/880024690821853184/881778670778335253)\nи нажать реакцию :house:\n\n**▽ КАК КУПИТЬ НЕДВИЖИМОСТЬ?**\nПерейти на ╚🔨аукцион и приобрести недвижимость выкупив его за х2 от текущей ставки или повышать ставку, играя на аукци\n\n**▽ КАК ПРОДАТЬ НЕДВИЖИМОСТЬ?**\n[:arrow_forward: ПЕРЕЙТИ В ПОМОЩЬ](https://discord.com/channels/880008097370865706/880024690821853184/881778670778335253)\nи нажать реакцию :hotel: под сообщением. Затем отправить номер участка и подобрав необходимые параметры, выставить участок на продажу в аукционе\n\n**▽ КАК ПОСМОТРЕТЬ ДОХОД?**\n[:arrow_forward: ПЕРЕЙТИ В ПРОФИЛЬ](И еще что касаемо недвижимости, как я понял она продается на аукционе) и нажать реакцию :house:, затем в сообщении нажать на реакцию :page_facing_up:\n\n**▽ КАК ОПЛАТИТЬ НАЛОГ?**\n[:arrow_forward: ПЕРЕЙТИ В ПРОФИЛЬ](https://discord.com/channels/880008097370865706/880024690821853184/881778670778335253)\nи нажать реакцию :house:, затем в сообщении нажать на реакцию :red_envelope:\n\n**▽ СКОЛЬКО МОЖНО ИМЕТЬ НЕДВИЖИМОСТИ?**\nЛимитов нет\n\n**▽ КАК УВЕЛИЧИТЬ ДОХОД?**\nПроценты участка статичны и не могут быть изменены. Имея больше участков, ваши проценты будут суммироваться и доход от перепродаж другими пользователями, будет выше\n\n**ОСТАЛИСЬ ВОПРОСЫ? НАПИШИТЕ ЕГО В ├📨предложения С ПОМЕТКОЙ "ДОБАВИТЬ В ИНСТРУКЦИЮ". ЕСЛИ ВОПРОС ДЕЙСТВИТЕЛЬНО ВАЖНЫЙ, МЫ ОТВЕТИМ НА НЕГО В ЭТОМ КАНАЛЕ, А ВЫ ПОЛУЧИТЕ НАГРАДУ**')
	await instr.send(embed = embed)
	await instr.send(embed = embed1)
	await instr.send(embed = embed2)
	await instr.send(embed = embed3)
	'''
	'''
	agr = bot.get_channel(880023332639096853)
	embed = discord.Embed(color=0x3C55FA, title="**ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ**", description=f'**ИСПОЛЬЗОВАНИЕ, НАХОЖДЕНИЕ И ЛЮБОЕ ВЗАИМОДЕЙСТВИЕ НА НАШЕМ СЕРВЕРЕ DISCORD "PROJECT V", ПОДРАЗУМЕВАЕТ ПОЛНОЕ СОГЛАСИЕ С НИЖЕПЕРЕЧИСЛЕННЫМИ ПОЛОЖЕНИЯМИ И УСЛОВИЯМИ ПОЛЬЗОВАТЕЛЬСКОГО СОГЛАШЕНИЯ**\n\nВсе внутренние расчеты производятся исключительно с пересчетом на виртуальную внутрисерверную валюту.\n\n**ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ**\nВзаимодействие участников с сервером Discord "{guild.name}" основываются на публичном соглашении. Действие соглашения становится активным в момент его размещения\n\n**Предмет соглашения**\n\nСоглашением регламентировано взаимодействие пользователей с сервером Discord "{guild.name}" в следующих направлениях:\n• Порядок использования сервера\n• Осуществление денежных транзакций в виде конвертирования на реальную и внутрисерверную валюту\n• Порядок осуществления внутрисерверных покупок\n• Взаимодействие с приобретенными услугами на внутрисерверную валюту\n• Проведение ивентов и бонусных программ')
	embed1 = discord.Embed(color=0x3C55FA, title="**ОСОБЕННОСТИ ВХОДА И ИСПОЛЬЗОВАНИЯ СЕРВЕРА**", description=f'**1.1**. Вступление на сервер Discord, рекомендовано от 16 лет.\n**1.2**. При входе на сервер, пользователь подтверждает, что он знаком с правилами и условиями пользовательского соглашения.\n**1.3**. Пользователь должен понимать. что он несёт полную ответственность за свой Discord аккаунт и необходимость защищать свои данные от его получения другими лицами, включая сотрудников нашего сервера.\n**1.4**. Строго запрещается использовать сервер Discord с целью получить денежный выигрыш сотрудникам сервера, их родственникам, друзьям и другим близким людям, а также участникам партнерских программ. Факт совершения подобного действия приравнивается в мошенничеству. В случае обнаружения подобной активности доступ к серверу будет ограничен.\n**1.5**. Один человек имеет право на вступление на сервер Discord, только с одной учетной записи.\n**1.6**. Если у администрации возникают подозрения, что пользователь, совершает мошеннические действия или другие действия запрещенные на нашем сервере, администрация оставляет за собой право верифицировать личные данные такого пользователя. Если подозрения будут подтверждены, существует вероятность блокировки на нашем сервере, введение ограничений и приостановки денежных выплат в пользу владельца учетной записи.\n**1.7**. Пользователь обязуется следить за новостями, публикуемыми в соответствующем канале сервера\n**1.8**. ТАК КАК ВЗАИМОДЕЙСТВИЕ С НАШИМ СЕРВЕРОМ, ОСУЩЕСТВЛЯЕТСЯ ЧЕРЕЗ ЛИЧНЫЕ СООБЩЕНИЯ ОТ НАШЕГО БОТА, ТО ЧТОБЫ ИСПОЛЬЗОВАТЬ НАШ СЕРВЕР **ПОЛЬЗОВАТЕЛЬ ДОЛЖЕН ВКЛЮЧИТЬ ФУНКЦИЮ В СВОЁМ ПРОФИЛЕ - РАЗРЕШИТЬ ЛИЧНЫЕ СООБЩЕНИЯ ОТ УЧАСТНИКОВ СЕРВЕРА** В ИНОМ СЛУЧАЕ, ДОСТУП К БОЛЬШИНСТВУ ФУНКЦИЙ БУДЕТ НЕ ДОСТУПЕН. ДЛЯ ЭТОГО НЕОБХОДИМО:\n1.ПЕРЕЙТИ В НАСТРОЙКИ ПРОФИЛЯ\n2.ПЕРЕЙТИ В РАЗДЕЛ "КОНФИДЕЦИАЛЬНОСТЬ"\n3.ВКЛЮЧИТЬ ФУНКЦИЮ "РАЗРЕШИТЬ ЛИЧНЫЕ СООБЩЕНИЯ ОТ УЧАСТНИКОВ СЕРВЕРА"')
	embed2 = discord.Embed(color=0x3C55FA, title="**ФИНАНСОВЫЕ ВОПРОСЫ**", description=f'**2.1**. Вступивший на сервер пользователь, принимает на себя полную ответственность за использование программного обеспечения сервера и берет на себя ответственность за возможные финансовые риски при использовании, игре, осуществления покупок и других финансовых взаимодействий с сервером и сторонних сервисов относящихся к серверу.\n**2.2**. Пользователь берет на себя ответственность за то, чтобы использование и нахождение на сервере Discord "{guild.name}"  оставалось в пределах правомерных действий в контексте законов региона в котором проживает пользователь.\n**2.3.**. При пополнении баланса внутрисерверной валюты пользователь обязуется придерживаться инструкции указанной в магазине покупки купонов. Несоблюдение инструкций может привести к тому, что деньги не будут зачислены на баланс. Ответственность за этот факт в таком случае несет пользователь, в одностороннем порядке.\n**2.4.**. В процессе проведения платежа пользователя участвует программное обеспечение сервера и его финансовых партнеров. В случае технической заминки или ошибки, сервер "{guild.name}" обязуется компенсировать или, наоборот, стянуть разницу некорректного перевода на протяжении 7 календарных дней от момента инцидента.\n**2.5.**. При создании заявки на вывод средств, пользователь обязуется указывать корректные данные и готов понести ответственность за совершение ошибки в указанных данных, которые могут повлечь частичный или полный отказ в возмещении средств, из за технических сложностей, которые могут возникнуть в процессе взаимодействия с вашей заявкой на вывод средств\n**2.6.**. Выводы денег с внутрисерверных счетов осуществляются без выходных. Выплата по правильно оформленной заявке осуществляется в срок до 24 часов с момента ее подачи.\nВ зависимости от способа перевода и особенностей работы платежной системы, зачисление денег на реквизиты пользователя может занимать до 4-7 рабочих дней.')
	embed3 = discord.Embed(color=0x3C55FA, title="**ПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ**", description=f'**2.7.**. Для вывода средств могут быть использованы платежные методы, указанные в момент осуществления вывода, при использовании функций нашего программного обеспечения.\n**2.8.**. Сервер {guild.name} не берёт с пользователя скрытые комиссии за ввод или вывод средств. Возможны только комиссии банков или платежных систем.\n**2.9.**. При пополнении баланса личного счета, кодом пополнения, чтобы пользовательские интернет счета и, в частности, их счета на нашем сервере не использовались для отмывания денег, для возможности вывести средства с внутри-серверного счета, пользователь обязан совершить покупку на сумму, которая будет близка к сумме самого пополнения.\n2.10. Если метод покупки купона пополнения отличается от метода вывода денежных средств, пользователь может быть подвергнут идентификации, при котором операторы, могут запросить селфи с паспортом, для подтверждения личности, совершающая вывод средств\n**2.11. Сервер {guild.name}, не несёт ответственность за финансовые потери возникшие из за технических проблем, при использовании пользователями сервера {guild.name}**')
	embed4 = discord.Embed(color=0x3C55FA, title="**ИВЕНТЫ И БОНУСНЫЕ ПРЕДЛОЖЕНИЯ**", description=f'**3.1.** Участие в ивентах - полностью добровольное мероприятие. Вы имеете полное право отказаться от участия в ивентах, осуществляемых на сервере\n**3.2.** Администрация оставляет за собой право менять отдельные детали проходящей акции или ивента в одностороннем порядке.\n**3.3.** Отдельным пользователям может быть отказано в участии в акции / ивенте в одностороннем порядке.\n**3.4.** Условия и правила акции или ивента указаны при публикации объявления на соответствующем канале. Факт участия в том или ином подразумевает, что вы подтверждаете свою осведомленность в правилах и условиях события.')
	embed5 = discord.Embed(color=0x3C55FA, title="**ОТВЕТСТВЕННОСТЬ**", description=f'**Гарантии и ответственность.**\n\n**4.1.** Организатор не гарантирует постоянный и непрерывный доступ к игровой площадке и его услугам в случае возникновения технических неполадок и/или непредвиденных обстоятельств, в числе которых: неполноценная работа или не функционирование интернет–провайдеров, серверов информации, банковских и платёжных систем, а также неправомерных действий третьих лиц. Организатор приложит все усилия по недопущению сбоев, но не несет ответственности за временные технические сбои и перерывы в работе Игры, вне зависимости от причин таких сбоев.\n**4.2.** Участник полностью согласен, что организатор не может нести ответственность за убытки участника, которые возникли в связи с противоправными действиями третьих лиц, направленными на нарушение системы безопасности электронного оборудования и баз данных игры, либо вследствие независящих от организатора перебоев, приостановления или прекращения работы каналов и сетей связи, используемых для взаимодействия с участником, а также неправомерных или необоснованных действий платежных систем, а так же третьих лиц.\n**4.3.** Организатор не несет ответственности за убытки, понесенные в результате использования или не использования участником информации об Игре, игровых правил и самой Игры и не несет ответственности за убытки или иной вред, возникший у участника в связи с его неквалифицированными действиями и незнанием игровых правил или его ошибках в расчетах;\n**4.4.** Участник согласен с тем, что использует игровую площадку по своей доброй воле и на свой собственный риск. Организатор не дает участнику никакой гарантии того, что он извлечет выгоду или пользу от участия в игре. Степень участия в Игре определяется сами участником.\n**4.5.** Организатор не несет ответственности перед участником за действия других участников.\n**4.6.** В случае возникновения споров и разногласий на игровой площадке, решение организатора является окончательным, и участник с ним полностью согласен. Все споры и разногласия, возникающие из настоящего Соглашения или в связи с ним, подлежат разрешению путем переговоров. В случае невозможности достижения согласия путем переговоров, споры, разногласия и требования, возникающие из настоящего Соглашения, подлежат разрешению в соответствии с действующим законодательством Белиза.\n**4.7.**  Организатор может вносить изменения в настоящее Соглашение, правила игровой площадки и другие документы в одностороннем порядке. В случае внесения изменений в документы Организатор размещает последние версии документов на сайте игровой площадки. Все изменения вступают в силу с момента размещения. Участник имеет право расторгнуть настоящее Соглашение в течение 3 дней, если он не согласен с внесенными изменениями. В таком случае расторжение . На Участника возлагается обязанность регулярно посещать официальный Дискорд Проекта с целью ознакомления с официальными документами и новостями.\n**4.8.** Организатор и Участник освобождаются от ответственности в случае возникновения обстоятельств непреодолимой силы (форс-мажорных обстоятельств), к числу которых относятся, но перечнем не ограничиваются: стихийные бедствия, войны, огонь (пожары), наводнения, взрывы, терроризм, бунты, гражданские волнения, акты правительственной или регулирующей власти, хакерские атаки, отсутствия, не функционирование или сбои работы энергоснабжения, поставщиков Интернет услуг, сетей связи или других систем, сетей и услуг. Сторона, у которой возникли такие обстоятельства, должна в разумные сроки и доступным способом оповестить о таких обстоятельствах другую сторону.\n**4.9.** Участник имеет право расторгнуть настоящее Соглашение в одностороннем порядке без сохранения игрового аккаунта. При этом все расходы, связанные с участием в игре, участнику не компенсируются и не возвращаются. Игровой инвентарь (монеты), находящиеся на игровом счете участника, подлежат возврату.\nПосле него вот это сообщение вставьте в соглашение')
	embed6 = discord.Embed(color=0x3C55FA, description=f'**Конфиденциальность.**\n**6.1.** Условие конфиденциальности распространяется на информацию, которую Организатор может получить об Участнике во время его пребывания на сайте Игры и которая может быть соотнесена с данным конкретным пользователем. Организатор автоматически получает и записывает в серверные логи техническую информацию о ваших действиях и т.п. Организатор гарантирует, что данные, сообщенные участником при регистрации в Игре, будут использоваться Организатором только внутри Игры.\n**6.2.** Организатор вправе передать персональную информацию об Участнике третьим лицам только в случаях, если:\n**6.2.1.** Участник изъявил желание раскрыть эту информацию;\n**6.2.2.** Без этого Участник не может воспользоваться желаемым продуктом или услугой, в частности - информация об именах (никах), игровых атрибутах - может быть доступна другим участникам;\n**6.2.3.** Участник нарушает настоящее Соглашение и правила игровой площадки.\n**6.3.** Во всех остальных случаях Сервер :dash:NEXT Invest:dash: гарантирует неразглашение личных данных пользователей третьим лицам, как и проведение таковыми финансовых операций, связанных со счетами пользователей.\n**6.4.** При передаче пользователем его данных доступа к аккаунту Discord третьему лицу какая-либо ответственность с сервера :dash:NEXT Invest:dash: снимается. Сюда относятся и случаи получения доступа к аккаунту путем взлома ящика электронной почты или при использовании стороннего софта.\n**6.5.** Программное обеспечение сервера не может быть использовано пользователями в целях коммерции. Публикация в сети интернет текстового и графического содержания ресурса и / или отдельных его частей без нашего согласия, не допускается. Последний пункт\nИные положения.\n**7.1.** Недействительность части или пункта (подпункта) настоящего соглашения не влечет недействительности всех остальных частей и пунктов (подпунктов).\n**7.2.** Срок действия настоящего Соглашения устанавливается на весь период действия игровой площадки, то есть на неопределенный срок, и не предполагает срока окончания данного соглашения.\n**7.3.** Регистрируясь и находясь на игровой площадке, участник признает, что он прочитал, понял и полностью принимает условия настоящего Соглашения, а также правила игры и иных официальных документов.')
	embed7 = discord.Embed(color=0x3C55FA, description=f'**7.4.** Для получения услуги проекта, Участник полностью принимает все условия настоящего Соглашения. В случае не согласия с каким-либо из условий Соглашения, Участнику предлагается отказаться от использования услуг проекта. С целью исключить введение Участника в заблуждение (обман), Организатор предупреждает до начала принятия согласия Участником использования услуг проекта о том, что предложенные Участнику услуги в виде игры основаны на риске, возникающем между несколькими участниками игры по установленным организатором данной игры правилам. Денежные средства Участника, необходимые для обеспечения игры (приобретение средств для игры, улучшение игроком условий для выигрыша и т.д.), принявшего условия Соглашения, направляются в общий игровой фонд Участников (игроков), из которого складываются, в том числе выигрыши. Соответственно организатор предупреждает вас, что игра частично основана на принципах коммерции  Кроме того, принимая Соглашение, Участник подтверждает свое согласие на пользование игровым фондом Организатором для организации и обслуживания игры среди Участников. Конечным результатом игрового риска является выигрыш. В то же время Организатор обязуется свести к минимально возможному отрицательному последствию риска Участника в игре, с целью привлечения физических лиц к проекту. Одновременно представленная услуга в виде игры направлена на удовлетворение потребностей Участника, которые он путем своего согласия на участие определяет и оценивает самостоятельно. Настоящие условия игры и остальные сведения проекта не имеют цели Организатора побудить в Участнике эмоции, связанные с предвосхищением успеха (азарта).\n**7.5.** Соглашение вступает в силу с момента регистрации участника в проекте.\n**ИСПОЛЬЗОВАНИЕ, НАХОЖДЕНИЕ И ЛЮБОЕ ВЗАИМОДЕЙСТВИЕ НА НАШЕМ СЕРВЕРЕ DISCORD ":dash:NEXT Invest:dash:", ПОДРАЗУМЕВАЕТ ПОЛНОЕ СОГЛАСИЕ С ВЫШЕПЕРЕЧИСЛЕННЫМИ ПОЛОЖЕНИЯМИ И УСЛОВИЯМИ ПОЛЬЗОВАТЕЛЬСКОГО СОГЛАШЕНИЯ**')
	await agr.send(embed = embed)
	await agr.send(embed = embed1)
	await agr.send(embed = embed2)
	await agr.send(embed = embed3)
	await agr.send(embed = embed4)
	await agr.send(embed = embed5)
	
	

	rules = bot.get_channel(880023390847635476)
	embed = discord.Embed(color=0x3C55FA, title=f'ИСПОЛЬЗОВАНИЕ, НАХОЖДЕНИЕ И ЛЮБОЕ ВЗАИМОДЕЙСТВИЕ НА НАШЕМ СЕРВЕРЕ DISCORD "{guild.name}", ПОДРАЗУМЕВАЕТ ПОЛНОЕ СОГЛАСИЕ С ПРАВИЛАМИ')
	embed1 = discord.Embed(color=0x3C55FA, title="ТЕРМИНЫ И ОПРЕДЕЛЕНИЯ", description=f'```\nОСНОВНЫЕ\n```\n**[1] Администрация —** пользователи, наделенные различными полномочиями по управлению и соблюдению порядка на сервере\n**[2] Модерация —** сотрудники администрации, ответственные за порядок и соблюдение правил сервера\n**[3] Операторы  —** сотрудники сервера, занимающиеся финансовыми вопросами, возникших у пользователей сервера\n**[4] Техническая поддержка —** обобщающий термин, касающийся поддержки со стороны сотрудников сервера\n**[5] Пользовательское соглашение -** свод информации включающий в себя условия использования нашего сервера')
	embed2 = discord.Embed(color=0x3C55FA, description=f'```\nТЕРМИНЫ ТЕХНИЧЕСКОГО ХАРАКТЕРА\n```\n\n**[6] ПО или Бот —** программное обеспечение\n**[7] Ферма —** текстовый канал, созданный на определенный срок, осуществляющий добычу внутрисерверной валюты\n**[8] Буст —** приобретаемое внутрисерверное улучшение\n**[9] Майнинг —** способ добычи внутрисерверной валюты, путем приобретения фермы\n**[10] Команды —** список текстовых сообщений или кнопок эмодзи, осуществляемых взаимодействие с ботом и системой сервера\n**[11] Стороннее ПО** - стороннее программное обеспечение, способное влиять на взаимодействие с сервером и пользователями\n**[12] Мультиаккаунты -** дополнительные учётные записи Discord для заработка внутри серверной валюты, обхода наказаний и вредительства серверу\n**[13] Платежная система -** система или ряд сайтов, обеспечивающих финансовые взаимодействия пользователей')
	embed3 = discord.Embed(color=0x3C55FA, description=f'```\nБАЗОВЫЕ ТЕРМИНЫ\n```\n\n**[14] Бан/Мут** — блокировка за нарушение правил или условий пользования сервером\n**[14] Бан/Мут**— однотипные сообщения, включающие в себя: смайлы, символы, ссылки, картинки и т.п. повторяющиеся несколько раз подряд и использование эмодзи вызывающих реакцию ботов\n**[16] Спам** – сообщения включающие в себя сторонние интернет ресурсы, сайты, сервера\n**[17] Афк/офф**  - обобщенный термин, обозначающий отход пользователя от персонального компьютера. Включает молчание, игнорирование, отключение, выход пользователя\n**[17] Оскорбления** — намеренное унижение и затрагивание чувств человека, выраженное в ругательной, матерной форме\n**[18] Неадекватное поведение** — агрессивное или некомфортное для других пользователей поведение, препятствующее общению\n**[19] Провокация** — намеренное негативное действие по отношению к другому человеку, способное у него вызвать ответную реакцию\n**[20] Коммерческая деятельность** – использование ресурсов сервера для ведения коммерческой деятельности\n**[21 ]Посторонние звуки** – любые шумы, мешающие общению\n**[22] Багоюз** – умышленный поиск и использование установленного программного обеспечения, уязвимостей сервера и информации указанных на нём\n**[23] Сторонние ресурсы **— любые ресурсы, прямо не связанные с {guild.name}\n**[24] Непотребный контент** - контент откровенного содержания или вызывающий негативные эмоции, пропагандирующий насилие, жестокое обращение с животными и т.п.')
	embed4 = discord.Embed(color=0x3C55FA, description=f'```\nПРАВИЛА СЕРВЕРА\n```\n\n**Срок наказаний за нарушение правил, устанавливается в индивидуальном порядке, по усмотрению администрации и модерации сервера. В зависимости от тяжести нарушения, может быть выдан в разных форматах, включая: временный или перманентный мут, кик, бан, штрафы, списываемые с пользовательского счета или ограничения доступа к определенным каналам, включая личные каналы, созданные при взаимодействии с нашим сервером**\n\n**МИНИМАЛЬНЫЕ СРОКИ НАКАЗАНИЙ:**\n@BAN VOICECHAT** - 1 час**\n@MUTE** - 15 мин**\n@BAN** - 24 часа**\n\n**МАКСИМАЛЬНЫЕ СРОКИ НАКАЗАНИЙ В СЛУЧАЕ МНОГОКРАТНЫХ НАРУШЕНИЙ:**\n@BAN VOICECHAT** - 7 дней**\n@MUTE** - 24 часа**\n@BAN** - ∞**')
	embed5 = discord.Embed(color=0x3C55FA, description=f'```\nОСНОВНЫЕ\n```\n\n1.1. Запрещено использовать любое программное обеспечение способное вызывать сбой в работе discord сервера и ПО использующегося на нём\n\n1.2. Запрещено намеренное использование и поиск уязвимостей сервера для извлечения прибыли и других корыстных целей\n\n1.3. Быть ознакомленным с правилами сервера и пользовательским соглашением, не знание не освобождает от ответственности\n\n1.4. На сервер запрещено вступать более чем, с 1 аккаунта\n\n1.5. Попрошайничество у персонала сервера\n\n1.6. Запрещен поиск уязвимостей в правилах\n\n1.7. Запрещено представляться под видом персонала сервера\n- Использование никнеймов, аватаров, как у персонала\n- Намеренный ввод в заблуждение пользователей и т.п.\n\n1.8. Покидая сервер, вы можете потерять текущие достижения в виде ролей. В таких ситуациях, персонал сервера не будет вам выдавать достижения и вам придется получать их снова')
	embed6 = discord.Embed(color=0x3C55FA, description=f'```\nПРАВИЛА ПОВЕДЕНИЯ\n```\n\n2.1. Запрещены любые оскорбления в чью-либо сторону, в любой форме, включая:\n- Прямые оскорбления\n- Оскорбления вопросом\n- Завуалированные оскорбления. Пример: «пнх», «муд*к», на другом языке\n- Оскорбление групп пользователей\n- Оскорбление родственников и близких\n- На Сервере также не допустимы оскорбления в виде изображений\n- Оскорбление национальности, расы, цвета кожи, политических и религиозных взглядов и т.д.\n\n2.2. Запрещены оскорбления, негативные и неконструктивные осуждения действий Администрации сервера и самого сервера в общем(Исключением является критика, которая выражена в адекватной манере)\n\n2.3. Запрещен флуд на всех каналах, за исключением не модерируемых и канал ├📢флуд\n\n2.4. Запрещена реклама и спам, в любой форме, без согласования с администрацией, включая:\n- Ссылки или упоминания серверов-конкурентов\n- Призывы идти на другой сервер\n- Призывы перейти, подписаться, проголосовать в социальных сетях\n- Реклама услуг и сторонних ресурсов\n\n2.5. Запрещены провокации и намеренное создание конфликтных ситуаций, включая:\n- Пинг пользователей без причин\n- Преследование\n\n2.6. Мы не запрещаем использовать ненормативную лексику, но когда текст состоит только или в основном из мата, сообщение может быть удалено\n\n2.7. Запрещен непотребный контент, включая:\n- Способы самоубийства, побуждение к самоубийству, обсуждение суицида\n- Разжигание вражды: призыв к насилию или травле человека либо группы лиц\n- Расчленёнка, насилие и жестокость в любом их проявлении\n- Сексуальный контент (ссылки и детальное описание полового акта)\n- Запрещены любые виды пропаганды и т.п.\n\n2.8. Запрещено распространять личную информацию пользователя(ей), без его(их) личного согласия\n\n2.9. Запрещена коммерческая деятельность, в любых её проявлениях\n\n2.10. Запрещены деструктивные действия по отношению к серверу, включающие в себя:\n- неконструктивную критику\n- призывы покинуть сервер\n- попытки и любые действия способствующие ухудшению процесса развития сервера')
	embed7 = discord.Embed(color=0x3C55FA, description=f'```\nПРАВИЛА ПОВЕДЕНИЯ В ГОЛОСОВЫХ КАНАЛАХ\n```\n\n3.1. Любые правила, и условия прописанные так же в пользовательском соглашении, распространяются и на голосовые каналы, за исключением не модерируемых и личных каналов\n\n3.2. Пользователь обязуется осуществлять регулярное общение в оплачиваемых голосовом канале, путём поддержания диалога\n\n3.3. Пользователю запрещено уходить в афк, в оплачиваемых голосовых каналах, более чем на 5 минут. При афк, на срок более 5ти минут, пользователь обязан отключиться от голосового канала или перейти в канал афк\n\n3.4. При осуществлении проверки, со стороны модерации, пользователь обязан отвечать на поставленные вопросы\n\n3.5. Запрещено  использование постороннего ПО, включая стереомишкер вашей операционной системы\n\n3.6. Запрещено использовать микрофон с неправильными настройками, создающий помехи общению пользователей и оказывающие негативное воздействие на пользователей\n\n3.7. Запрещено транслирование звуков, создающих помехи и оказывающие негативное воздействие на пользователей:\n- Посторонние шумы и громкие звуки\n- Громкая музыка, радио, звуки из видео и все их составляющие\n\n3.8. Запрещено препятствовать работе модерации и администрации сервера\n\n3.9. При проверке пользователя на афк, другие пользователи обязаны соблюдать тишину. Запрещено препятствовать деятельности модерации, при осуществлении проверок пользователей\n\n3.10. В купленных приватных каналах, запрещено ограничивать доступ персоналу сервера')
	embed8 = discord.Embed(color=0x3C55FA, description=f'3.10. Так как сервер осуществляет оплату за общение в голосовых каналах, то осуществляется контроль по отношению к общению пользователей сервера, в голосовых каналах (Исключение: не оплачиваемые голосовые каналы и каналы афк) Пояснение: Модераторы обязаны контролировать и осуществлять регулярные проверки голосовых каналов на наличие афк пользователей. При подключении модераторов к голосовым каналам, при наличии подозрения на афк БОЛЕЕ 5 МИНУТ, модератор обязан осуществить проверку пользователя, голосовым вопросом в формате:\n- Пользователь с ником [Имя пользователя], Вы тут? Если пользователь проигнорировал вопрос и не дал ответ в течении 60 секунд, модератор обязан осуществить проверку через текстовое личное сообщение в формате:\n- Проверка на афк, ожидаю ответа на это сообщение Если пользователь ответил на сообщение, модератор обязан уточнить через какое время пользователь выйдет из афк, если это время составляет менее 5 минут и пользователь уложился в срок, проверка прошла успешно.\nЕсли пользователь закрыл возможность обращения через личные сообщения, не ответил на текстовое сообщение или превысил время ожидания 5 минут, то осуществляется исключение из голосового канала.\nЕсли замечено регулярное нарушение, то пользователю может быть ограничен доступ к голосовым каналам на определенный срок.\n\n**ПРОВЕРКА НА АФК, ОСУЩЕСТВЛЯЕТСЯ ВСЕХ ГОЛОСОВЫХ КАНАЛОВ, КРОМЕ НЕ ОПЛАЧИВАЕМЫХ И КАНАЛОВ АФК.\nПРИ ОСУЩЕСТВЛЕНИИ МОДЕРАЦИИ ЛИЧНЫХ ГОЛОСОВЫХ КАНАЛОВ И ОТСУТСТВИЕ ПОДОЗРЕНИЙ НА АФК, МОДЕРАТОР ОБЯЗАН ОСУЩЕСТВЛЯТЬ ПОЛНУЮ ТИШИНУ И ПОКИНУТЬ ЛИЧНЫЙ КАНАЛ В ТЕЧЕНИИ 30 СЕКУНД, С МОМЕНТА ВХОДА**')
	embed9 = discord.Embed(color=0x3C55FA, description=f'**ИСПОЛЬЗОВАНИЕ, НАХОЖДЕНИЕ И ЛЮБОЕ ВЗАИМОДЕЙСТВИЕ НА НАШЕМ СЕРВЕРЕ DISCORD "{guild.name}", ПОДРАЗУМЕВАЕТ ПОЛНОЕ СОГЛАСИЕ С  ПРАВИЛАМИ**')
	await rules.send(embed = embed)
	await rules.send(embed = embed1)
	await rules.send(embed = embed2)
	await rules.send(embed = embed3)
	await rules.send(embed = embed4)
	await rules.send(embed = embed5)
	await rules.send(embed = embed6)
	await rules.send(embed = embed7)
	await rules.send(embed = embed8)
	await rules.send(embed = embed9)
	

	
	
	
	system = bot.get_channel(880024762942889994)
	embeds = discord.Embed(color=0x3C55FA, title="НАША СИСТЕМА", description=f'**НАША КОНЦЕПЦИЯ**\n{guild.name} - проект основная цель которого дать мотивацию людям общаться на сервере, получая за это деньги. Специально для Вас была разработана система, позволяющая получать внутрисерверную валюту, всем без исключений, которую в дальнейшем можно обменять на **реальные** деньги. При входе на сервер, для Вас создаётся личный счёт с нашей валютой. С помощью данного счета, вы можете осуществлять вывод, конвертацию и пополнение средств. Все покупки внутри сервера, включая покупку ферм, не является обязательным условием для нахождения на нашем сервере и носит лишь развлекательный характер.\n\n**ВАРИАНТЫ ПОЛУЧЕНИЯ ВАЛЮТЫ:**\n[▽ ОБЩЕНИЕ В ГОЛОСОВЫХ КАНАЛАХ]()\n[▽ ПРИОБРЕТЕНИЕ МАЙНИНГ ФЕРМ]()\n[▽ ПРИОБРЕТЕНИЕ НЕДВИЖИМОСТИ]()\n[▽ ТОРГОВЛЯ]()\n[▽ ЕЖЕДНЕВНЫЕ ЗАДАНИЯ]()\n[▽ РЕФЕРАЛЬНАЯ СИСТЕМА]()\n[▽ ОТКРЫТИЕ КЕЙСОВ]()\n[▽ УЧАСТИЕ И ИВЕНТАХ]()\n[▽ УЧАСТИЕ В РОЗЫГРЫШАХ]()\n[▽ УЧАСТИЕ В ПОЕДИНКАХ]()\n[▽ S.UP И BUMP СЕРВЕРА]()\n')
	embeds1 = discord.Embed(color=0x3C55FA, title="ИНФОРМАЦИЯ О ВАЛЮТЕ", description=f'**На данный момент на сервере имеются две валюты с следующими курсами:\n1 VOLT (V) = 1 RUB\n10 WATT (W) = 1 VOLT**\n\n**КОМАНДЫ ДЛЯ ПЕРЕДАЧИ ВАЛЮТЫ. ВВОДИТЬ НА КАНАЛЕ** #├💬общение :\n├💬общение:\n-sendw @Nickname 10000 - Передать :euro:WATT (минимум 10) Комиссия 5%\n-sendv @Nickname 10000 - Передать :pound:VOLT (минимум 10) Комиссия 10%')
	embeds2 = discord.Embed(color=0x3C55FA, title="СИСТЕМА ЗАРАБОТКА В ГОЛОСОВЫХ ЧАТАХ", description=f'Для того, чтобы начать получать валюту, с помощью голосового общения. Вам необходимо просто начать общаться с голосовых чатах.\n\nСуществует определенный список правил, который необходимо соблюдать, чтобы гарантированно получать валюту на свой счет\n[:arrow_forward: ОЗНАКОМИТЬСЯ С ПРАВИЛАМИ]()\n\nОплата за общение в голосовых чатах осуществляется по следующим параметрам:\n1 ЧАС ОБЩЕНИЯ В ГОЛОСОВОМ КАНАЛЕ = 4 WATT\n\nПополнение баланса происходит автоматически, каждые 60 минут на Ваш персональный счет.\n\n__Если вы не хотите получать оплату за общение в голосовых каналах, вы можете перейти на каналы из категории КАНАЛЫ БЕЗ ОПЛАТЫ. Данная категория  модерируется, но проверка на афк, со стороны модерации, не осуществляется.__')
	embeds3 = discord.Embed(color=0x3C55FA, title="СИСТЕМА ЗАРАБОТКА НА МАЙНИНГЕ", description=f'На нашем сервере была разработана уникальная система, позволяющая пользователям приобрести фермы за внутрисерверную валюту,  включая валюту, которую Вы получаете общаясь в голосовых чатах.\n\n[:arrow_forward: ПЕРЕЙТИ В МАГАЗИН ФЕРМ](https://discord.com/channels/880008097370865706/880025073963122718/881544012723519579)\n\nПри покупке фермы, создаётся Ваш личный канал фермы на сервере, в категории "ФЕРМЫ" Каждая ферма имеет свой максимальный срок работы и производимое количество валюты в час. Фермы делятся на два типа, с автоматической сборкой валюты и ручной. При ручной, вам необходимо выводить заработанную валюту, нажимая на соответствующую кнопку, на созданном канале фермы.')
	embeds4 = discord.Embed(color=0x3C55FA, title="СИСТЕМА ЗАРАБОТКА НА НЕДВИЖИМОСТИ", description=f'На нашем сервере была разработана уникальная система недвижимости, позволяющая пользователям приобретать участки и получать пассивный доход от торговли недвижимостью между участниками\n\n[:arrow_forward: ПЕРЕЙТИ В  ПОМОЩЬ ПО НЕДВИЖИМОСТИ]()')
	embeds5 = discord.Embed(color=0x3C55FA, title="РЕФЕРАЛЬНАЯ СИСТЕМА", description=f'Данная система позволяет пользователям приглашать рефералов и осуществлять с помощью этого заработок.\n\n*нажмите, чтобы*\n[:arrow_forward: ПЕРЕЙТИ В РЕФЕРАЛЬНЫЙ ПРОФИЛЬ]()\n\nУ каждого пользователя, в реферальном профиле, создаётся код, который вы можете давать другим пользователям, для закрепления их за собой.\n\nПриглашенному вами пользователю, необходимо перейти в свой реферальный профиль и нажать реакцию :arrows_counterclockwise:- Подтвердить приглашение и отправить ваш код боту')
	embeds6 = discord.Embed(color=0x3C55FA, title="ПРОЧЕЕ", description=f'**СИСТЕМА ПОЕДИНКОВ**\nКаждый пользователь может вызывать на поединок пользователя, отправив команду, в чате #└🤺поединки\n\n`-duel @nickname 100`\nгде:\n@nickname - упоминание пользователя ником\n100 - сумма ставки\n\nМинимальный взнос: 10W\n\n**БУДЬТЕ ОСТОРОЖНЫ, ПЕРЕД ОТПРАВКОЙ ВЫЗОВА, ВЫ МОЖЕТЕ ПРОИГРАТЬ ДЕНЬГИ!**\n\n**ВАШ ШАНС ВЫГРАТЬ 50/50**')
	await system.send(embed = embeds)
	await system.send(embed = embeds1)
	await system.send(embed = embeds2)
	await system.send(embed = embeds3)
	await system.send(embed = embeds4)
	await system.send(embed = embeds5)
	await system.send(embed = embeds6)
	
	
	
	# Dinamic
	# Commands
	
	commandsc = bot.get_channel(880024690821853184)
	embed = discord.Embed(color=0x3C55FA, title="**СПИСОК КОМАНД**", description=f'НА ЭТОМ КАНАЛЕ, ВЫ МОЖЕТЕ ВЗАИМОДЕЙСТВОВАТЬ С БОТОМ СЕРВЕРА\n\nТАК КАК ВЗАИМОДЕЙСТВИЕ С НАШИМ СЕРВЕРОМ, ОСУЩЕСТВЛЯЕТСЯ ЧЕРЕЗ ЛИЧНЫЕ СООБЩЕНИЯ ОТ НАШЕГО БОТА, ТО ЧТОБЫ ИСПОЛЬЗОВАТЬ ВСЕ ВОЗМОЖНОСТИ __НЕОБХОДИМО ВКЛЮЧИТЬ ФУНКЦИЮ В СВОЁМ ПРОФИЛЕ - РАЗРЕШИТЬ ЛИЧНЫЕ СООБЩЕНИЯ ОТ УЧАСТНИКОВ СЕРВЕРА__ ДЛЯ ЭТОГО НЕОБХОДИМО:\n1.ПЕРЕЙТИ В НАСТРОЙКИ ПРОФИЛЯ\n2.ПЕРЕЙТИ В РАЗДЕЛ "КОНФИДЕЦИАЛЬНОСТЬ"\n3.ВКЛЮЧИТЬ ФУНКЦИЮ "РАЗРЕШИТЬ ЛИЧНЫЕ СООБЩЕНИЯ ОТ УЧАСТНИКОВ СЕРВЕРА"\n\nВ ИНОМ СЛУЧАЕ, ДОСТУП К БОЛЬШИНСТВУ ФУНКЦИЙ БУДЕТ НЕ ДОСТУПЕН\n\n**ДЛЯ СОВЕРШЕНИЯ ДЕЙСТВИЯ НАЖМИТЕ :ballot_box_with_check:**')
	await commandsc.send(embed = embed)

	embed1 = discord.Embed(color=0x3C55FA, title="**ОПЕРАЦИИ С БАЛАНСОМ**", description=f'Вам будет отправлено сообщение, для взаимодействия с вашим личным счетом, для проверки, пополнения, конвертации и вывода средств')
	mess = await commandsc.send(embed = embed1)

	embed2 = discord.Embed(color=0x3C55FA, title="**ПОСМОТРЕТЬ ПРОФИЛЬ**", description=f'Вам будет отправлено сообщение с информацией о вашем профиле и статистике')
	mess1 = await commandsc.send(embed = embed2)

	embed3 = discord.Embed(color=0x3C55FA, title="**СПИСОК ЛИДЕРОВ**", description=f'Вам будет отправлено сообщение с списком лидеров и их статистикой на сервере')
	mess2 = await commandsc.send(embed = embed3)

	embed4 = discord.Embed(color=0x3C55FA, title="**РЕФЕРАЛЬНЫЙ ПРОФИЛЬ**", description=f'Вам будет отправлено сообщение с вашим профилем в реферальной системе. Используйте эту команду, для получения реферального кода и извлечения из этого прибыли')
	mess3 = await commandsc.send(embed = embed4)

	embed5 = discord.Embed(color=0xff0000, title="**ПОДАТЬ ЖАЛОБУ**", description=f'Вам будет отправлено сообщение с формой заявки, с помощью которой вы можете подать жалобу')
	mess0 = await commandsc.send(embed = embed5)
	await mess0.add_reaction('⛔')
	
	for i in range(4):
		if i == 0:
			await mess.add_reaction('☑️')

		else:
			message = f'{"mess" + str(i)}'
			mmessage = locals().get(message)
			await mmessage.add_reaction('☑️')


	


	farms = bot.get_channel(880025073963122718)
	embedf = discord.Embed(color=0x3C55FA, title="FARM ЗАТЫЧКА", description=f'На слабой видеокарте\n\n**Для покупки за VOLT нажмите :euro:**\n**Для покупки за WATT нажмите на :pound:**\n')
	embedf.set_thumbnail(url="https://i.ibb.co/92f8Cw8/Z.png")
	embedf.add_field(name = '**Макс срок работы:**', value = "35дней", inline = True)
	embedf.add_field(name = '**Производительность:**', value = "0.25v/ч", inline = True)
	embedf.add_field(name = '**Срок окупаемости:**', value = "25 дней", inline = True)

	embedf.add_field(name = '**Сложность:**', value = "EASY", inline = True)
	embedf.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf.add_field(name = '**ЦЕНА:**', value = "149V / 1999W", inline = True)
	embedfm1 = await farms.send(embed = embedf)
	await embedfm1.add_reaction('💶')
	await embedfm1.add_reaction('💷')

	embedf1 = discord.Embed(color=0x3C55FA, title="FARM GTX", description=f'На игровой видеокарте\n\n**Для покупки за VOLT нажмите :euro:**\n**Для покупки за WATT нажмите на :pound:**\n')
	embedf1.set_thumbnail(url="https://i.ibb.co/RCt8s0K/G.png")
	embedf1.add_field(name = '**Макс срок работы:**', value = "30дней", inline = True)
	embedf1.add_field(name = '**Производительность:**', value = "0.5v/ч", inline = True)
	embedf1.add_field(name = '**Срок окупаемости:**', value = "21 днm", inline = True)

	embedf1.add_field(name = '**Сложность:**', value = "EASY", inline = True)
	embedf1.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf1.add_field(name = '**ЦЕНА:**', value = "249V / 2999W", inline = True)
	embedfm2 = await farms.send(embed = embedf1)
	await embedfm2.add_reaction('💶')
	await embedfm2.add_reaction('💷')

	embedf2 = discord.Embed(color=0x3C55FA, title="FARM RTX", description=f'На мощной видеокарте\n\n**Для покупки за VOLT нажмите :euro:****\n')
	embedf2.set_thumbnail(url="https://i.ibb.co/z72pGRR/R.png")
	embedf2.add_field(name = '**Макс срок работы:**', value = "32дней", inline = True)
	embedf2.add_field(name = '**Производительность:**', value = "1v/ч", inline = True)
	embedf2.add_field(name = '**Срок окупаемости:**', value = "21 день", inline = True)

	embedf2.add_field(name = '**Сложность:**', value = "NORM", inline = True)
	embedf2.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf2.add_field(name = '**ЦЕНА:**', value = "**499V**", inline = True)
	embedfm3 = await farms.send(embed = embedf2)
	await embedfm3.add_reaction('💶')

	embedf3 = discord.Embed(color=0x3C55FA, title="FARM ASIC", description=f'На автоматическом оборудовании для майнинга\n\n**Для покупки за VOLT нажмите :euro:**\n')
	embedf3.set_thumbnail(url="https://i.ibb.co/RHfBJvm/A.png")
	embedf3.add_field(name = '**Макс срок работы:**', value = "45дней", inline = True)
	embedf3.add_field(name = '**Производительность:**', value = "1.5v/ч", inline = True)
	embedf3.add_field(name = '**Срок окупаемости:**', value = "21 дней", inline = True)

	embedf3.add_field(name = '**Сложность:**', value = "NORM", inline = True)
	embedf3.add_field(name = '**Вывод V на баланс:**', value = "Автоматический", inline = True)
	embedf3.add_field(name = '**ЦЕНА:**', value = "**749V**", inline = True)
	embedfm4 = await farms.send(embed = embedf3)
	await embedfm4.add_reaction('💶')


	embedf4 = discord.Embed(color=0x3C55FA, title="FARM MULTI", description=f'На мощном оборудовании для майнинга\n\n**Для покупки за VOLT нажмите :euro:**\n')
	embedf4.set_thumbnail(url="https://i.ibb.co/SmQ7bNk/M.png")
	embedf4.add_field(name = '**Макс срок работы:**', value = "40дней", inline = True)
	embedf4.add_field(name = '**Производительность:**', value = "2v/ч", inline = True)
	embedf4.add_field(name = '**Срок окупаемости:**', value = "21 день", inline = True)

	embedf4.add_field(name = '**Сложность:**', value = "NORM", inline = True)
	embedf4.add_field(name = '**Вывод V на баланс:**', value = "Автоматический", inline = True)
	embedf4.add_field(name = '**ЦЕНА:**', value = "**999V**", inline = True)
	embedfm5 = await farms.send(embed = embedf4)
	await embedfm5.add_reaction('💶')


	embedf5 = discord.Embed(color=0x3C55FA, title="FARM BOOST", description=f'На улучшенном оборудовании для майнинга\n\n**Для покупки за VOLT нажмите :euro:**\n')
	embedf5.set_thumbnail(url="https://i.ibb.co/rf67N6Y/B.png")
	embedf5.add_field(name = '**Макс срок работы:**', value = "20дней", inline = True)
	embedf5.add_field(name = '**Производительность:**', value = "3v/ч", inline = True)
	embedf5.add_field(name = '**Срок окупаемости:**', value = "14 дней", inline = True)

	embedf5.add_field(name = '**Сложность:**', value = "HARD", inline = True)
	embedf5.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf5.add_field(name = '**ЦЕНА:**', value = "**999V**", inline = True)
	embedfm6 = await farms.send(embed = embedf5)
	await embedfm6.add_reaction('💶')


	embedf6 = discord.Embed(color=0x3C55FA, title="FARM TITAN", description=f'На мощных видеокартах\n\n**Для покупки за VOLT нажмите :euro:**\n')
	embedf6.set_thumbnail(url="https://i.ibb.co/87WYdBB/T.png")
	embedf6.add_field(name = '**Макс срок работы:**', value = "3дней", inline = True)
	embedf6.add_field(name = '**Производительность:**', value = "4v/ч", inline = True)
	embedf6.add_field(name = '**Срок окупаемости:**', value = "16 дней", inline = True)

	embedf6.add_field(name = '**Сложность:**', value = "HARD", inline = True)
	embedf6.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf6.add_field(name = '**ЦЕНА:**', value = "**1499V**", inline = True)
	embedfm7 = await farms.send(embed = embedf6)
	await embedfm7.add_reaction('💶')


	embedf7 = discord.Embed(color=0x3C55FA, title="FARM SERVER", description=f'На серверном оборудовании\n\n**Для покупки за VOLT нажмите :euro:**\n')
	embedf7.set_thumbnail(url="https://i.ibb.co/0KDHq9W/S.png")
	embedf7.add_field(name = '**Макс срок работы:**', value = "50дней", inline = True)
	embedf7.add_field(name = '**Производительность:**', value = "8v/ч", inline = True)
	embedf7.add_field(name = '**Срок окупаемости:**', value = "13 дней", inline = True)

	embedf7.add_field(name = '**Сложность:**', value = "MASTER", inline = True)
	embedf7.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf7.add_field(name = '**ЦЕНА:**', value = "**2499V**", inline = True)
	embedfm8 = await farms.send(embed = embedf7)
	await embedfm8.add_reaction('💶')


	embedf8 = discord.Embed(color=0x3C55FA, title="FARM FACTORY", description=f'На автоматическом заводском оборудовании\n\n**Для покупки за VOLT нажмите :euro:**\n')
	embedf8.set_thumbnail(url="https://i.ibb.co/NL6qq9w/F.png")
	embedf8.add_field(name = '**Макс срок работы:**', value = "45дней", inline = True)
	embedf8.add_field(name = '**Производительность:**', value = "16v/ч", inline = True)
	embedf8.add_field(name = '**Срок окупаемости:**', value = "13 дней", inline = True)

	embedf8.add_field(name = '**Сложность:**', value = "EXPERT", inline = True)
	embedf8.add_field(name = '**Вывод V на баланс:**', value = "Автоматический", inline = True)
	embedf8.add_field(name = '**ЦЕНА:**', value = "**4999V**", inline = True)
	embedfm9 = await farms.send(embed = embedf8)
	await embedfm9.add_reaction('💶')


	embedf9 = discord.Embed(color=0x3C55FA, title="FARM QUANTUM", description=f'Мощный квантовый компьютер\n\n**Для покупки за VOLT нажмите :euro:**\n')
	embedf9.set_thumbnail(url="https://i.ibb.co/JBnsbKS/Q.png")
	embedf9.add_field(name = '**Макс срок работы:**', value = "50дней", inline = True)
	embedf9.add_field(name = '**Производительность:**', value = "40v/ч", inline = True)
	embedf9.add_field(name = '**Срок окупаемости:**', value = "10 дней", inline = True)

	embedf9.add_field(name = '**Сложность:**', value = "INSANE", inline = True)
	embedf9.add_field(name = '**Вывод V на баланс:**', value = "Автоматический", inline = True)
	embedf9.add_field(name = '**ЦЕНА:**', value = "**9999V**", inline = True)
	embedfm10 = await farms.send(embed = embedf9)
	await embedfm10.add_reaction('💶')


	embedf10 = discord.Embed(color=0x3C55FA, title="FARM ПЛАТА", description=f'Самая простая видеокарта\n\n**Для покупки за RUB нажмите :euro:**\n')
	embedf10.set_thumbnail(url="https://i.ibb.co/pd6w8dt/plata.png")
	embedf10.add_field(name = '**Макс срок работы:**', value = "11дней", inline = True)
	embedf10.add_field(name = '**Производительность:**', value = "0.3v/ч", inline = True)
	embedf10.add_field(name = '**Срок окупаемости:**', value = "10 дней", inline = True)

	embedf10.add_field(name = '**Сложность:**', value = "EASY", inline = True)
	embedf10.add_field(name = '**Вывод RUB на баланс:**', value = "Ручной", inline = True)
	embedf10.add_field(name = '**ЦЕНА:**', value = "79RUB", inline = True)
	await embedfm11.add_reaction('💶')
	await embedfm11.add_reaction('💷')













////////////////////// FARMS EDIT
	channel = bot.get_channel(880025073963122718)

	m = await channel.fetch_message(886528458887401473)
	embedf = discord.Embed(color=0x3C55FA, title="FARM ЗАТЫЧКА", description=f'На слабой видеокарте\n\n**Для покупки за RUB нажмите :euro:**')
	embedf.set_thumbnail(url="https://i.ibb.co/92f8Cw8/Z.png")
	embedf.add_field(name = '**Макс срок работы:**', value = "35дней", inline = True)
	embedf.add_field(name = '**Производительность:**', value = "0.25RUB/ч", inline = True)
	embedf.add_field(name = '**Срок окупаемости:**', value = "25 дней", inline = True)

	embedf.add_field(name = '**Сложность:**', value = "EASY", inline = True)
	embedf.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf.add_field(name = '**ЦЕНА:**', value = "149RUB", inline = True)
	await m.edit(embed = embedf)


	m1 = await channel.fetch_message(886528465631862905)
	embedf1 = discord.Embed(color=0x3C55FA, title="FARM GTX", description=f'На игровой видеокарте\n\n**Для покупки за RUB нажмите :euro:**')
	embedf1.set_thumbnail(url="https://i.ibb.co/RCt8s0K/G.png")
	embedf1.add_field(name = '**Макс срок работы:**', value = "29дней", inline = True)
	embedf1.add_field(name = '**Производительность:**', value = "0.5RUB/ч", inline = True)
	embedf1.add_field(name = '**Срок окупаемости:**', value = "21 день", inline = True)

	embedf1.add_field(name = '**Сложность:**', value = "EASY", inline = True)
	embedf1.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf1.add_field(name = '**ЦЕНА:**', value = "249RUB", inline = True)
	await m1.edit(embed = embedf1)


	m2 = await channel.fetch_message(886528471159930961)
	embedf2 = discord.Embed(color=0x3C55FA, title="FARM RTX", description=f'На мощной видеокарте\n\n**Для покупки за RUB нажмите :euro:**\n')
	embedf2.set_thumbnail(url="https://i.ibb.co/z72pGRR/R.png")
	embedf2.add_field(name = '**Макс срок работы:**', value = "29дней", inline = True)
	embedf2.add_field(name = '**Производительность:**', value = "1RUB/ч", inline = True)
	embedf2.add_field(name = '**Срок окупаемости:**', value = "21 день", inline = True)

	embedf2.add_field(name = '**Сложность:**', value = "NORM", inline = True)
	embedf2.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf2.add_field(name = '**ЦЕНА:**', value = "**499RUB**", inline = True)
	await m2.edit(embed = embedf2)


	m3 = await channel.fetch_message(886528474192437278)
	embedf3 = discord.Embed(color=0x3C55FA, title="FARM ASIC", description=f'На автоматическом оборудовании для майнинга\n\n**Для покупки за RUB нажмите :euro:**\n')
	embedf3.set_thumbnail(url="https://i.ibb.co/RHfBJvm/A.png")
	embedf3.add_field(name = '**Макс срок работы:**', value = "35дней", inline = True)
	embedf3.add_field(name = '**Производительность:**', value = "1.5RUB/ч", inline = True)
	embedf3.add_field(name = '**Срок окупаемости:**', value = "21 дней", inline = True)

	embedf3.add_field(name = '**Сложность:**', value = "NORM", inline = True)
	embedf3.add_field(name = '**Вывод V на баланс:**', value = "Автоматический", inline = True)
	embedf3.add_field(name = '**ЦЕНА:**', value = "**749RUB**", inline = True)
	await m3.edit(embed = embedf3)


	m4 = await channel.fetch_message(886528476797083668)
	embedf4 = discord.Embed(color=0x3C55FA, title="FARM MULTI", description=f'На мощном оборудовании для майнинга\n\n**Для покупки за RUB нажмите :euro:**\n')
	embedf4.set_thumbnail(url="https://i.ibb.co/SmQ7bNk/M.png")
	embedf4.add_field(name = '**Макс срок работы:**', value = "40дней", inline = True)
	embedf4.add_field(name = '**Производительность:**', value = "2RUB/ч", inline = True)
	embedf4.add_field(name = '**Срок окупаемости:**', value = "21 день", inline = True)

	embedf4.add_field(name = '**Сложность:**', value = "NORM", inline = True)
	embedf4.add_field(name = '**Вывод V на баланс:**', value = "Автоматический", inline = True)
	embedf4.add_field(name = '**ЦЕНА:**', value = "**999RUB**", inline = True)
	await m4.edit(embed = embedf4)


	m5 = await channel.fetch_message(886528481381462076)
	embedf5 = discord.Embed(color=0x3C55FA, title="FARM BOOST", description=f'На улучшенном оборудовании для майнинга\n\n**Для покупки за RUB нажмите :euro:**\n')
	embedf5.set_thumbnail(url="https://i.ibb.co/rf67N6Y/B.png")
	embedf5.add_field(name = '**Макс срок работы:**', value = "20дней", inline = True)
	embedf5.add_field(name = '**Производительность:**', value = "3RUB/ч", inline = True)
	embedf5.add_field(name = '**Срок окупаемости:**', value = "14 дней", inline = True)

	embedf5.add_field(name = '**Сложность:**', value = "HARD", inline = True)
	embedf5.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf5.add_field(name = '**ЦЕНА:**', value = "**999RUB**", inline = True)
	await m5.edit(embed = embedf5)


	m6 = await channel.fetch_message(886528484460097546)
	embedf6 = discord.Embed(color=0x3C55FA, title="FARM TITAN", description=f'На мощных видеокартах\n\n**Для покупки за RUB нажмите :euro:**\n')
	embedf6.set_thumbnail(url="https://i.ibb.co/87WYdBB/T.png")
	embedf6.add_field(name = '**Макс срок работы:**', value = "30дней", inline = True)
	embedf6.add_field(name = '**Производительность:**', value = "4RUB/ч", inline = True)
	embedf6.add_field(name = '**Срок окупаемости:**', value = "16 дней", inline = True)

	embedf6.add_field(name = '**Сложность:**', value = "HARD", inline = True)
	embedf6.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf6.add_field(name = '**ЦЕНА:**', value = "**1499RUB**", inline = True)
	await m6.edit(embed = embedf6)


	m7 = await channel.fetch_message(886528488234971207)
	embedf8 = discord.Embed(color=0x3C55FA, title="FARM FACTORY", description=f'На автоматическом заводском оборудовании\n\n**Для покупки за RUB нажмите :euro:**\n')
	embedf8.set_thumbnail(url="https://i.ibb.co/NL6qq9w/F.png")
	embedf8.add_field(name = '**Макс срок работы:**', value = "37дней", inline = True)
	embedf8.add_field(name = '**Производительность:**', value = "14RUB/ч", inline = True)
	embedf8.add_field(name = '**Срок окупаемости:**', value = "13 дней", inline = True)

	embedf8.add_field(name = '**Сложность:**', value = "EXPERT", inline = True)
	embedf8.add_field(name = '**Вывод V на баланс:**', value = "Автоматический", inline = True)
	embedf8.add_field(name = '**ЦЕНА:**', value = "**4999RUB**", inline = True)
	await m7.edit(embed = embedf8)


	m8 = await channel.fetch_message(886528493339422774)
	embedf9 = discord.Embed(color=0x3C55FA, title="FARM QUANTUM", description=f'Мощный квантовый компьютер\n\n**Для покупки за RUB нажмите :euro:**\n')
	embedf9.set_thumbnail(url="https://i.ibb.co/JBnsbKS/Q.png")
	embedf9.add_field(name = '**Макс срок работы:**', value = "42дня", inline = True)
	embedf9.add_field(name = '**Производительность:**', value = "25RUB/ч", inline = True)
	embedf9.add_field(name = '**Срок окупаемости:**', value = "10 дней", inline = True)

	embedf9.add_field(name = '**Сложность:**', value = "INSANE", inline = True)
	embedf9.add_field(name = '**Вывод V на баланс:**', value = "Автоматический", inline = True)
	embedf9.add_field(name = '**ЦЕНА:**', value = "**9999RUB**", inline = True)
	await m8.edit(embed = embedf9)


	m9 = await channel.fetch_message(886528504068464640)
	embedf10 = discord.Embed(color=0x3C55FA, title="FARM ПЛАТА", description=f'Самая простая видеокарта\n\n**Для покупки за RUB нажмите :euro:**')
	embedf10.set_thumbnail(url="https://i.ibb.co/pd6w8dt/plata.png")
	embedf10.add_field(name = '**Макс срок работы:**', value = "14дней", inline = True)
	embedf10.add_field(name = '**Производительность:**', value = "0.3RUB/ч", inline = True)
	embedf10.add_field(name = '**Срок окупаемости:**', value = "10 дней", inline = True)

	embedf10.add_field(name = '**Сложность:**', value = "EASY", inline = True)
	embedf10.add_field(name = '**Вывод V на баланс:**', value = "Ручной", inline = True)
	embedf10.add_field(name = '**ЦЕНА:**', value = "79RUB", inline = True)
	await m9.edit(embed = embedf10)



	'''
