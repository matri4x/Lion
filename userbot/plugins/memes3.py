import asyncio

from telethon import events

from userbot.utils import admin_cmd, register

# ================= CONSTANT =================


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

# ===========================================


A = (
    "`▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `\n"
    "`████▌▄▌▄▐▐▌█████ `\n"
    "`████▌▄▌▄▐▐▌▀████ `\n"
    "`▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `\n"
)

B = (
    "`╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `\n"
    "`╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `\n"
    "`╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `\n"
    "`╱┗━━━┛╰━━━╯┗━━━┛╱ `\n"
)

C = (
    "\n......................................../´¯/) "
    "\n......................................,/¯../ "
    "\n...................................../..../ "
    "\n..................................../´.¯/"
    "\n..................................../´¯/"
    "\n..................................,/¯../ "
    "\n................................../..../ "
    "\n................................./´¯./"
    "\n................................/´¯./"
    "\n..............................,/¯../ "
    "\n............................./..../ "
    "\n............................/´¯/"
    "\n........................../´¯./"
    "\n........................,/¯../ "
    "\n......................./..../ "
    "\n....................../´¯/"
    "\n....................,/¯../ "
    "\n.................../..../ "
    "\n............./´¯/'...'/´¯¯`·¸ "
    "\n........../'/.../..../......./¨¯\ "
    "\n........('(...´...´.... ¯~/'...') "
    "\n.........\.................'...../ "
    "\n..........''...\.......... _.·´ "
    "\n............\..............( "
    "\n..............\.............\..."
)

D = (
    "`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
    "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
    "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `"
)

E = (
    "`\n(\_/)`"
    "`\n(•_•)`"
    "`\n >🌹 *`"
    "`\n                    `"
    "`\n(\_/)`"
    "`\n(•_•)`"
    "`\n🌹<\ *`"
)

F = (
    "`\n█████████`"
    "`\n█▄█████▄█`"
    "`\n█▼▼▼▼▼`"
    "`\n█  Hello Man`"
    "`\n█▲▲▲▲▲`"
    "`\n█████████`"
    "`\n ██   ██`"
)


@borg.on(admin_cmd(pattern="ml (.*)"))
async def kakashi(jisan):
    message = jisan.pattern_match.group(1)
    await jisan.edit(
        "`\n█████████`"
        "`\n█▄█████▄█`"
        "`\n█▼▼▼▼▼`"
        f"`\n█  {message}`"
        "`\n█▲▲▲▲▲`"
        "`\n█████████`"
        "`\n ██   ██`"
    )


@borg.on(admin_cmd(pattern=r"paw$"))
async def kakashi(jisan):
    await jisan.edit("`(=ↀωↀ=)`")


@borg.on(admin_cmd(pattern=r"tf$"))
async def kakashi(jisan):
    await jisan.edit("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")


@borg.on(admin_cmd(pattern=r"gay$"))
async def kakashi(jisan):
    await jisan.edit(
        "`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
        "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
        "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈U GAY`"
        "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈"
    )


@borg.on(admin_cmd(pattern=r"bot$"))
async def kakashi(jisan):
    await jisan.edit(
        "` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
        "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `"
    )


@borg.on(admin_cmd(pattern=r"hai$"))
async def kakashi(jisan):
    await jisan.edit(
        "\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HELLO!┊😀`"
        "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HELLO!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
        "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`"
    )


@borg.on(admin_cmd(pattern=r"nou$"))
async def kakashi(jisan):
    await jisan.edit(
        "`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
        "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
        "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
        "`\n┗━━┻━┛`"
    )


@borg.on(admin_cmd(pattern=r"sayhi$"))
async def kakashi(jisan):
    await jisan.edit(
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛🔷🔷🔷🔷️🔷🔷🔷💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷💛💛️💛💛💛🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷️🔷💛"
        "\n💛🔷💛💛💛💛️💛🔷💛"
        "\n💛💛💛💛💛💛💛💛💛"
    )


@register(outgoing=True, pattern=r"^\.(?:penis|dick)\s?(.)?")
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace("🍆", emoji)
    await e.edit(titid)


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "muth":

        await event.edit(input_str)

        animation_chars = [
            "8✊️===D",
            "8=✊️==D",
            "8==✊️=D",
            "8===✊️D",
            "8==✊️=D",
            "8=✊️==D",
            "8✊️===D",
            "8===✊️D💦",
            "8==✊️=D💦💦",
            "8=✊️==D💦💦💦",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 8])


@borg.on(admin_cmd(pattern=r"fail$"))
async def kakashi(fail):
    await fail.edit(A)


@borg.on(admin_cmd(pattern=r"lol$"))
async def kakashi(lol):
    await lol.edit(B)


@borg.on(admin_cmd(pattern=r"mf$"))
async def kakashi(mf):
    await mf.edit(C)


@borg.on(admin_cmd(pattern=r"lool$"))
async def kakashi(loal):
    await loal.edit(D)


@borg.on(admin_cmd(pattern=r"nih$"))
async def kakashi(shit):
    await shit.edit(E)


@borg.on(admin_cmd(pattern=r"hallo$"))
async def kakashi(hello):
    await hello.edit(E)
