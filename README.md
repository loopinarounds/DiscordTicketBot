GUIDE TO USE:

1. You must first host your own Discord Bot and fetch the OAuth Code, enter this at the bottom line of the code file (annotated in file). Guide on how to create your own Discord Bot here: https://discordpy.readthedocs.io/en/stable/discord.html

2. You must now decide how many categories you wish for the ticket bot to send customer support tickets to. The places where these category IDs must go are labelled in the code. I would thoroughly recommend reading all of the driver.py file before making these edits. The whole code is annotated and explains what is happening in a given function. Making these required entries should be very simple once you have a basic understanding of what is going on.

3. You can also edit the embed formats throughout the channel opening and initial message creation functions. These embeds are currently catered to the company I initially made the bot for.

4. Run the program. You are recommended to host this on a low power server. The bot should never crash unless there is a server side issue. In case of a crash, reset the program, it will post a new initial message to the discord channel and all exisiting ticket channels will still interact with the bot correctly.

