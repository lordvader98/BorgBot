"""
Available Commands
.muth"""


from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "muth":

        await event.edit(input_str)

        animation_chars = [

            "✊️       ",

            "  ✊️",

            "    ✊️",

            "       ✊️",

            "    ✊️",

            "  ✊️",

            "✊️       ",

            "✊️💦",

            "✊️💦💦",

            "✊️💦💦💦"

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

await event.edit(animation_chars[i % 10])
