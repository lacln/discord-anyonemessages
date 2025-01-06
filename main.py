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

    await ctx.respond("CREATING, PLEASE WAIT...", delete_after=1)
    message = await ctx.send("POPULATING...")
    print(message.id)
    #edit the created message and add the message ID
    await message.edit(content=f"### Note: {message.id}   --   Created By: {str(ctx.user.name)}\n{content}")


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
async def note_edit(ctx, message_id, content):
    try:
        grabMessage = await ctx.fetch_message(message_id.strip())
        await grabMessage.edit(content=f"### Note: {message_id}   --   Created By: {str(ctx.user.name)}\n{content}")
        await ctx.respond("DONE", delete_after=1)
    except discord.errors.NotFound:
        await ctx.respond("ERROR: MESSAGE ID NOT FOUND")
    

## TO BE IMPLEMENTED, ISSUE CURRENTLY MESSAGE ID SHOULD BE UPDATED
# @bot.slash_command(
#     name="note_edit_ping",
#     description="Edit an existing note",
#     guild_ids=[channels]
# )
# @option(
#     "message_id",
#     description="message_id (first line of message)"
# )
# @option(
#     "content",
#     description="new note contents"
# )
# async def note_edit_ping(ctx, message_id, content):
#     grabMessage = await ctx.fetch_message(message_id)
#     await ctx.send(content=f"### Note: {message_id}   --   Created By: {str(ctx.user.name)}\n{content}")
#     await grabMessage.delete()
#     await ctx.respond("DONE", delete_after=1)


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
    description="content to append (maybe add a space at the start)"
)
async def note_append(ctx, message_id, content):
    try:
        grabMessage = await ctx.fetch_message(message_id.strip())
        await grabMessage.edit(f"{grabMessage.content + content}")
        await ctx.respond("DONE", delete_after=1)
    except discord.errors.NotFound:
        await ctx.respond("ERROR: MESSAGE ID NOT FOUND")


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
async def note_delete(ctx, message_id):
    ## CHECK HERE RUNNING COMMAND USER IS SAME AS OWNER USER (OR ADMIN IF THAT CAN BE DETERMINED)
    ## require a "are you sure" IMPLEMENT LATER
    try:
        grabMessage = await ctx.fetch_message(message_id.strip())
        # print(grabMessage.content.split('\n')[0].split('Created By: ')[-1])
        if grabMessage.content.split('\n')[0].split('Created By: ')[-1] == ctx.user.name:
            await grabMessage.delete()
            await ctx.respond(f"MESSAGE {message_id} DELETED")
        else:
            await ctx.respond("ERROR: ONLY THE CREATOR CAN DELETE THIS NOTE")
    except discord.errors.NotFound:
        await ctx.respond("ERROR: MESSAGE ID NOT FOUND")

#MAIN
if __name__ == "__main__":
    print("The bot is running...")
    bot.run(token)
    
