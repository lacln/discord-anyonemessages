## PYTHON MESSAGING BOT
#
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message


load_dotenv(override=True)
token = os.environ['CLIENT_TOKEN']
print(token)

#Intents --> what the bot intends to receive from the API
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

#Message Functionality
async def send_message(message, user_message):
    if not user_message:
        print('message not sent user message not filled')
        return
    
    # := same as isprivate = ... then check if isprivate
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    #try to get the responce
    try:
        response = get_response(user_message)
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
        # await message.author.send(response) if is_private else message.channel.send(response)
    except Exception as e:
        print(e)



def get_response(user_input):
    command = user_input.lower()

    if command == "":
        return "A command would have been nice"
    if command == "createnote":
        return "OK"
    else:
        return "Command not found"
    

#STARTUP
@client.event
async def on_ready():
    print(str(client.user) + " is now running")


#INCOMING MESSAGES
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # username = str(message.author)
    user_message = message.content
    # channel = str(message.channel)

    # print()
    await send_message(message, user_message)

#MAIN
if __name__ == "__main__":
    client.run(token=token)