"""
Available Commands
.muth"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 120)

    input_str = event.pattern_match.group(1)

    if input_str == "muth":

        await event.edit(input_str)

        animation_chars = [

            "8鉁婏笍===D",

            "8=鉁婏笍==D",

            "8==鉁婏笍=D",

            "8===鉁婏笍D",

            "8==鉁婏笍=D",

            "8=鉁婏笍==D",

            "8鉁婏笍===D",

            "8===鉁婏笍D馃挦",

            "8==鉁婏笍=D馃挦馃挦",

            "8=鉁婏笍==D馃挦馃挦馃挦"

        ]

        for i in animation_ttl:
        
            await asyncio.sleep(animation_interval)
        
            await event.edit(animation_chars[i % 10])

