import webbrowser
from time import sleep

import pyautogui
from discord.ext import commands


class Zoom(commands.Cog):

    def __init__(self, client):
        self.client = client

    # help command for class
    @commands.command()
    async def helpclass(self, ctx):
        await ctx.send(
            f'.joinclass - To enter the class \n .leavemeeting - to leave the meeting \n .raisehand - Hand raise'
            f'\n .lowerhand - to lower the hand \n .present- to mark the present in chat {ctx.author.mention}')

    # meeting join harsha
    @commands.command()
    async def joinclass(self, ctx):
        url = 'https://zoom.us/j/4013344534?pwd=aDJtdGdCd281MFRoVTZZcmt2U0V5UT09'
        webbrowser.open(url)
        sleep(7)
        pyautogui.write('JIMSBCA')
        pyautogui.hotkey('enter')
        await ctx.send(f"Joined {ctx.author.mention}")

    # meeting end command
    @commands.command()
    async def leavemeeting(self, ctx):
        pyautogui.hotkey('alt', 'f4')
        await ctx.send(f"Meeting left {ctx.author.mention}")

    # raise hand
    @commands.command()
    async def raisehand(self, ctx):
        pyautogui.hotkey('alt', 'y')
        await ctx.send(f"hand raised {ctx.author.mention}")

    # lower hand
    @commands.command()
    async def lowerhand(self, ctx):
        pyautogui.hotkey('alt', 'y')
        await ctx.send(f"hand lowered {ctx.author.mention}")

    # present in chat
    @commands.command()
    async def present(self, ctx):
        pyautogui.hotkey('alt', 'h')
        text = "rahul pahwa 0511420219 present"
        pyautogui.write(text)
        pyautogui.press('enter')
        pyautogui.hotkey('alt', 'f4')
        await ctx.send(f"present sent {ctx.author.mention}")

    # chat
    @commands.command()
    async def chat(self, ctx):
        pyautogui.hotkey('alt', 'h')
        await ctx.send("What do you want to say in chat?")

        def checks(m):
            return m.author.id == ctx.author.id

        #msg = await self.client.wait_for('message', check=checks, timeout=30)
        msg = "hello"
        sleep(2)
        pyautogui.click(x=967, y=30)
        sleep(3)
        pyautogui.write(msg)
        pyautogui.hotkey('enter')
        await ctx.send(f"Message sent {ctx.author.mention}")


def setup(client):
    client.add_cog(Zoom(client))
