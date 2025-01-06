## PYTHON MESSAGING BOT
#
import os
import json
from dotenv import load_dotenv
import discord
from discord import option
from discord.ext import commands

load_dotenv(override=True)
token = os.environ['CLIENT_TOKEN']
channels = os.getenv("GUILD_IDS")
# print(token)

bot = commands.Bot()


## BACKEND.JSON IN FORMAT
"""
messages:{[ARR]}

ARR OF
{
messageid:0000000
creator:username
contents:TEXT HERE
}
"""


"""
NEXT UP

get args for the slash command
figure out who wrote the command (author)
get a message id number of messages sent/recieved


BACKEND IN JSON FORMAT IN EXTERNAL FLAT FILE
"""

@bot.slash_command(
    name="note_create",
    description="Create a new note",
    guild_ids=[channels]
)
@option(
    "content",
    description="note contents"
)
async def note_create(ctx, content):
    #Ensure first line of file is auto added
    #NOTE_NUM: 00000000 -- CREATED BY: USERNAME
    contEdit = content.split("\\n")
    content = "\n".join(contEdit)
    await ctx.respond(content=f"### Note: long/right click for Message ID   --   Created By: {str(ctx.user.name)}\n{content}")

    ###### OK, SO APPARENTLY EDITED MESSAGES (IN PYCORD) CREATE A NEW ID
    ###### I CANNOT FIND ANY WAY TO GET AROUND THIS (EMBED THE ID INTO MESSAGE)
    ###### LUCKY, YOU CAN COPY A MESSAGES ID BY LONG/RIGHT CLICK
    ###### BUT NOBODY KNOWS THIS SO WILL NEED TO FIND A WAY TO INFOM WHEN EDIT COMMAND PRESSED (OR CREATE "HELP" COMMAND... :( ))
    # # # # # message = await ctx.respond("CREATING, PLEASE WAIT...")
    # # # # # print(message.id)
    # # # # # #edit the created message and add the message ID
    # # # # # d = await ctx.edit(content=f"### Note: {message.id}   --   Created By: {str(ctx.user.name)}\n{content}")
    # # # # # print(d.id)

@bot.slash_command(
    name="note_edit",
    description="Edit an existing note",
    guild_ids=[channels]
)
@option(
    "message_id",
    description="message_id (first line of message)"
)
@option(
    "content",
    description="new note contents"
)
async def note_edit(ctx):
    grabMessage = await ctx.fetch_message(1325799365343973468)
    grabMessage.edit(content="OKOKOKOKO")
    # await ctx.respond("note should be edited")


@bot.slash_command(
    name="note_append",
    description="Append to an existing note",
    guild_ids=[channels]
)
@option(
    "message_id",
    description="message_id (first line of message)"
)
@option(
    "content",
    description="content to append"
)
async def note_append(ctx):
    await ctx.respond("note should be appended")
    print(ctx)


##COMMAND TO BE IMPLEMENTED LATER
# @bot.slash_command(
#     name="note_delete_lines",
#     description="Delete lines of a note",
#     guild_ids=[channels]
# )
# @option(
#     "message_id",
#     description="message_id (first line of message)"
# )
# @option(
#     "line_number",
#     description="line number to delete"
# )
# async def note_delete_lines(ctx):
#     message = await ctx.respond("note should have lines deleted")
#     print(f"message sent as {message.id}")


@bot.slash_command(
    name="note_delete",
    description="Delete a note",
    guild_ids=[channels]
)
@option(
    "message_id",
    description="message_id (first line of message)"
)
async def note_delete(ctx):
    ## CHECK HERE RUNNING COMMAND USER IS SAME AS OWNER USER (OR ADMIN IF THAT CAN BE DETERMINED)
    await ctx.respond("note should be deleted")

#MAIN
if __name__ == "__main__":
    print("The bot is running...")
    bot.run(token)
    
