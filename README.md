## GUIDE TO USE:

1. ```client.run("Enter DiscordBot OAuth Here")``` You must first host your own Discord Bot and fetch the OAuth Code, enter this at the bottom line of the code file (annotated in file). Guide on how to create your own Discord Bot here: https://discordpy.readthedocs.io/en/stable/discord.html

2. ```await channel_opener("Category ID Here", guild, interaction, user_channel_name, user_input, message,tick_num)``` You must now decide how many categories you wish for the ticket bot to send customer support tickets to. The places where these category IDs must go are labelled in the code. The categories are listed in the annotated ```channel_opener``` functions. 

3. You can also edit the embed formats throughout the channel opening and initial message creation functions. These embeds are currently catered to the company I initially made the bot for.

4. Run the program. You are recommended to host this on a low power server. The bot should never crash unless there is a server side issue. In case of a crash, reset the program, it will post a new initial message to the discord channel and all exisiting ticket channels will still interact with the bot correctly.



## WHAT DOES THE BOT DO?

When activated, the bot will send an embedded message to the discord channel of your choice. This message will have 5 buttons attached. These buttons, as mentioned above in the guide, can be set to any category you need for your customer services. 

When a button is pressed by a user, it will open a channel that manually adds the user and all staff members of the discord server. The bot will post a message to the channel stating what information the user needs to provide in order to have their query solved as quickly as possible.  The staff are then able to help the user and close the ticket.

When the ticket channel is closed, a full .txt transcript of the messages in the ticket channel will be sent to a staff-only ticket transcipt channel, as well as into the DMs of the user who opened the channel initially. Incase of any accidental closing, the bot will prompt the user if they are sure they would like to close the channel. They may cancel the closing process if they wish by pressing the prompted cancel button.

## Initial Message Example



<img width="740" alt="ticketbot" src="https://user-images.githubusercontent.com/86264161/193656364-0a62731a-0da0-4b79-80a3-ff9938a119b6.png">

The above image shows the message sent to the channel when the bot is activated. The buttons, when pressed, open a ticket channel in the corresponding categories that you have chosen.

## Ticket Transcript Example


[Ticket_content_for__ryan-7777.txt](https://github.com/loopinarounds/DiscordTicketBot/files/9700186/Ticket_content_for__ryan-7777.txt)

Above is an example of the txt file produced by the bot, that is sent to a specified staff channel once a ticket has been closed. This ensures that all staff can be aware of how a ticket was handled in order to act accordingly in the future.




