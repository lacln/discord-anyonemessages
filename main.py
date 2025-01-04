## PYTHON MESSAGING BOT
#
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


load_dotenv(override=True)
token = os.environ['CLIENT_TOKEN']
channels = os.getenv("GUILD_IDS")
# print(token)

# # #Intents --> what the bot intends to receive from the API
# # intents = Intents.default()
# # intents.message_content = True
# # client = Client(intents=intents)

# # #Message Functionality
# # async def send_message(message, user_message):
# #     if not user_message:
# #         print('message not sent user message not filled')
# #         return
    
# #     # := same as isprivate = ... then check if isprivate
# #     if is_private := user_message[0] == '?':
# #         user_message = user_message[1:]

# #     #try to get the responce
# #     try:
# #         response = get_response(user_message)
# #         if is_private:
# #             await message.author.send(response)
# #         else:
# #             await message.channel.send(response)
# #         # await message.author.send(response) if is_private else message.channel.send(response)
# #     except Exception as e:
# #         print(e)



# # def get_response(user_input):
# #     command = user_input.lower()

# #     if command == "":
# #         return "A command would have been nice"
# #     if command == "createnote":
# #         return "OK"
# #     else:
# #         return "Command not found"
    

# # #STARTUP
# # @client.event
# # async def on_ready():
# #     print(str(client.user) + " is now running")


# # #INCOMING MESSAGES
# # @client.event
# # async def on_message(message):
# #     if message.author == client.user:
# #         return
# #     # username = str(message.author)
# #     user_message = message.content
# #     # channel = str(message.channel)

# #     # print()
# #     await send_message(message, user_message)

# # #MAIN
# # if __name__ == "__main__":
# #     client.run(token=token)

bot = commands.Bot()


"""
NEXT UP

get args for the slash command
figure out who wrote the command (author)
get a message id number of messages sent/recieved
"""

@bot.slash_command(
    name="note_create",
    guild_ids=[channels]
)

@bot.slash_command(
    name="note_edit",
    guild_ids=[channels]
)

@bot.slash_command(
    name="note_append",
    guild_ids=[channels]
)

@bot.slash_command(
    name="note_delete_lines",
    guild_ids=[channels]
)

@bot.slash_command(
    name="note_delete",
    guild_ids=[channels]
)

async def note_create(ctx):
    await ctx.respond("note should be created")

async def note_edit(ctx):
    await ctx.respond("note should be edited")

async def note_append(ctx):
    await ctx.respond("note should be edited")

async def note_delete_lines(ctx):
    await ctx.respond("note should have lines deleted")

async def note_delete(ctx):
    await ctx.respond("note should be deleted")

#MAIN
if __name__ == "__main__":
    print("The bot is running...")
    bot.run(token)
    
