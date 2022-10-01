# install and import discord and discord_components
import discord
from discord_components import DiscordComponents, Button
import discord.ext.commands as commands
from datetime import datetime


# ----------------------- FUNCTIONS ----------------------#
# Function that handles all actions after a channel is created
async def channel_opener(id_category, guild, interaction, user_channel_name, user_input, message,tick_num):
    global channel_ids
    # Channel Permissions overwrite, for user opening ticket
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True),
        user_input: discord.PermissionOverwrite(read_messages=True)}
    # Fetches the needed ticket category and chanel name
    ticket_category = discord.utils.get(guild.categories, id=id_category)
    user_channel_name = user_channel_name + "-" + str(tick_num)
    new_channel = await guild.create_text_channel(user_channel_name, overwrites=overwrites,
                                                  category=ticket_category)

    new_channel_id = new_channel.id
    channel_ids.append(str(new_channel_id))

    # Creation of the ticket closing embed
    await interaction.respond(
        content=f"Channel Created <#{new_channel_id}>\n", ephemeral=True)
    embed_close = discord.Embed(title="Rampage Retail",
                                description="Support will be with you shortly.\n\n To close this "
                                            "ticket react with 🔒.", author="Rampage Retail",
                                timestamp=datetime.utcnow())
    # Sends the ticket closing embed, as well as a custom parameter 'message' dependent on what ticket was opened
    await new_channel.send(
        content=message,
        embed=embed_close, components=[Button(style="4", emoji="🔒", custom_id=str(new_channel_id))])
    text_channel_list.append(user_channel_name)
    print(text_channel_list)
    return id_category, guild, interaction, user_channel_name, user_input, new_channel


async def text_channel_checker():
    global text_channel_list
    text_channel_list = []
    for server in client.guilds:
        for channel in server.channels:
            if str(channel.type) == 'text':
                text_channel_list.append(channel.name)
    print(text_channel_list)


# -----------------------------------------------------------##

client = commands.Bot("!")
DiscordComponents(client)

# send a message with Button components
# involve some attributes
# recieve an interaction

# Defines the embed for the ticket message
embed_opener = discord.Embed(title="**Tickets Please**", description="Press the button below that matches your "
                                                                     "particular "
                                                                     "needs:\n\n "
                                                                     "**Invoices**: To request an invoice.\n\n"
                                                                     "**Subscription + Refunds**: For help with "
                                                                     "subscription "
                                                                     "handling and refunds.\n\n "
                                                                     "**ISP/DCs**: For assistance with "
                                                                     "ISPs/DCs "
                                                                     "as well as help with related issues.\n\n "
                                                                     "**General Help + Giveaway Claim**: For any "
                                                                     "questions "
                                                                     "and "
                                                                     "queries, as well as claiming giveaway data.\n\n"
                                                                     "**Data Issues**: If you are having issues with "
                                                                     "recently "
                                                                     "purchased data not topping-up",
                             timestamp=datetime.utcnow(),
                             author="Rampage Retail")


@client.event
async def on_ready():
    global channel_ids
    global tick_num
    global confirm_ids_yes
    global confirm_ids_no
    channel_ids = []
    confirm_ids_yes = []
    confirm_ids_no = []

    tick_num = 1
    channel = client.get_channel(990293881453158462)

    await text_channel_checker()
    await channel.send(embed=embed_opener, components=[
        [Button(label="Invoices", style="3", emoji="📃", custom_id="Invoices"),
         Button(label="Subscriptions + Refunds", style="3", emoji="💵", custom_id="Subs"),
         Button(label="ISP/DC", style="3", emoji="📡", custom_id="ISP"),
         Button(label="General Help and Giveaway Claim", style="3", emoji="👍", custom_id="Help"),
         Button(label="Data Issues", style="3", emoji="‼️", custom_id="Data Issues"),
         ]
    ])

    @client.event
    async def on_button_click(interaction):
        global channel_ids
        global tick_num
        global confirm_ids_yes
        global confirm_ids_no
        user_input = interaction.author
        user_id = str(user_input)
        user_split = user_id.split('#')
        user_channel_name = user_split[0].lower() + '-' + user_split[1]
        guild = interaction.guild

        if interaction.custom_id == "Invoices":
            message = f'Welcome {user_input.mention}. \n\n In order to speed up the process of creating your ' \
                      f'invoices, ' \
                      f'can you please provide your:\n**Business/Company Name**\n**Business/Company Email**\n' \
                      f'**Respective order numbers you wish to be invoiced for**\n\n Thankyou! A member of staff will ' \
                      f'be with you shortly. '
            await channel_opener(990297093056905216, guild, interaction, user_channel_name, user_input, message,tick_num)
            tick_num += 1
        elif interaction.custom_id == "Subs":
            message = f'Welcome {user_input.mention}. Please help us get the exact help you need by describing what ' \
                      f'you need or what your problem is.\n\n To help us investigate, please provide your:\n **Email ' \
                      f'Address**\n\n Thankyou! A member of staff will be with you shortly. '
            await channel_opener(990297646293979206, guild, interaction, user_channel_name, user_input, message,tick_num)
            tick_num += 1
        elif interaction.custom_id == "ISP":
            message = f'Welcome {user_input.mention}. Please help us get the exact help you need by describing what ' \
                      f'you need or what your problem is.\n\n In order to help us investigate, please provide your:\n ' \
                      f'**Email Address**\n **Related Order Numbers**\n\n Thankyou! A member of staff will be with ' \
                      f'you shortly. '
            await channel_opener(990297747531911168, guild, interaction, user_channel_name, user_input, message,tick_num)
            tick_num += 1
        elif interaction.custom_id == "Help":
            message = f'Welcome {user_input.mention}. Please help us get the exact help you need by describing what ' \
                      f'you need or what your problem is.\n\n' \
                      f'If you are claiming a giveaway win, please provide:\n **The Discord Link to the winning ' \
                      f'message** \n\n ' \
                      f'Thankyou! A member of staff will be with you shortly.'
            await channel_opener(990297842218307634, guild, interaction, user_channel_name, user_input, message,tick_num)
            tick_num += 1
        elif interaction.custom_id == "Data Issues":
            message = f'Welcome {user_input.mention}. Please help us get the exact help you need by describing what ' \
                      f'you need or what your problem is.\n\n' \
                      f'Thankyou! A member of staff will be with you shortly.'
            await channel_opener(990297458347229204, guild, interaction, user_channel_name, user_input, message,tick_num)
            tick_num += 1


        if str(interaction.custom_id) in channel_ids:

            await interaction.respond(content='Are you sure you would like to close this ticket?',
                                      components=[[Button(label='Yes', style="4", custom_id=f"Yes_button_{str(interaction.custom_id)}"),
                                                   Button(label='Cancel', style="2", custom_id=f"No_button_{str(interaction.custom_id)}")]],
                                      ephemeral=False)
            confirm_ids_yes.append(f"Yes_button_{str(interaction.custom_id)}")
            confirm_ids_no.append(f"No_button_{str(interaction.custom_id)}")

        # Find discord channel by user's name... user_channel_name

        if str(interaction.custom_id) in confirm_ids_yes:
            split_custom_id = int(str(interaction.custom_id).split('_')[2])
            new_channel = client.get_channel(split_custom_id)
            ticketfile = f'Ticket_content_for_{user_channel_name}.txt'
            with open(ticketfile, "w") as file:
                ticket_list = []
                async for msg in new_channel.history(limit=None):
                    ticket_list.append(f"{msg.created_at}-{msg.author.display_name}: {msg.clean_content}\n")

                ticket_list.reverse()
                for i in range(len(ticket_list)):
                    file.write(ticket_list[i])

            file = discord.File(ticketfile)
            ticket_channel = client.get_channel(992015624123453540)

            await ticket_channel.send(file=file)
            print(text_channel_list)
            await new_channel.delete()
            # print(str(interaction.custom_id))
            # [confirm_ids_yes.remove(y) for y in confirm_ids_yes if y == str(interaction.custom_id)]
            # confirm_ids_yes.remove(str(interaction.custom_id))
            # confirm_ids_no.remove(f"No_button_{str(split_custom_id)}")
            confirm_ids_yes = list(filter((str(interaction.custom_id)).__ne__, confirm_ids_yes))
            confirm_ids_no = list(filter((f"No_button_{str(split_custom_id)}").__ne__, confirm_ids_no))


        elif str(interaction.custom_id) in confirm_ids_no:
            split_custom_id = int(str(interaction.custom_id).split('_')[2])
            print(split_custom_id)
            new_channel = client.get_channel(split_custom_id)
            msg = await new_channel.history().get(author__id=990295952642429020)
            await msg.delete()

        print(confirm_ids_yes)
        print(confirm_ids_no)

client.run("OTkwMjk1OTUyNjQyNDI5MDIw.GfrWKc.o3jbb2OZRWzkAu9vK5SN3zEzrm_Z29PdetCZTg")
