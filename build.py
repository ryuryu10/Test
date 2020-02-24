import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'r!')

@client.event
async def on_ready():
    print('Ready!')
    

@client.command()
async def dmall(ctx, global_guildid : int,*, message):
    master = [391425164123963394,600471112140324864]
    login_status = 0
    test = ctx.author.id
    for a in master:
        if test == a:
            login_status = login_status + 1
    if login_status == 1:
        guild = client.get_guild(int(global_guildid))
        msg = await ctx.channel.send('> 메시지 전송 작업이 시작되었습니다.')
        su = 0
        fa = 0
        sul = 0
        user = []
        for channelz in guild.members:
            print(channelz)
            user.append(channelz.name)
        print(user)
        for channelz in guild.members:
                
            try:
                channel2 = await channelz.create_dm()
                await channel2.send(message)
                su = su + 1
            except:
                fa = fa + 1
                pass
            try:
                sul = sul + 1
                sui = user[sul]
                print(sui)
                msg1 = '> 메시지를 전송중입니다. \n > 전송중인 유저 : {0} \n > {1}명에게 메시지가 전송되었습니다\n > {2}명에게 메시지가 전송되지 않았습니다.'.format(sui,su,fa)
                await msg.edit(content=msg1)
            except:
                pass
        msg2 = '> 메시지 전송이 완료되었습니다. \n > 총 {0}명에게 메시지가 전송되었으며\n > {1}명에게 메시지가 전송되지 않았습니다.'.format(su,fa)
        await msg.edit(content=msg2)
    else:
        await ctx.channel.send('[Error] 등록된 사용자가 아닙니다.')

client.run('NjgxMzA2NjI4NzY2OTU3NTc2.XlMikQ.r3Kih17QdR7eC5hAM_DRGOcdFRk')

