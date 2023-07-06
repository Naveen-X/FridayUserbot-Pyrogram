# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from database import db_x

bsdb = db_x["bot_sdb"]

default_text = """<b>Hello, {user_firstname}!
This is the Assistant Of {boss_firstname}.</b>
<i>My Boss is away or busy as of now, You can wait for him to respond.
Do not spam further messages else I may have to block you!</i>

<b>This is an automated message by the assistant.</b>
<b><u>You Have {warns} Of Warns.</b></u>
"""

default_thumb = "https://icon-icons.com/downloadimage.php?id=106660&root=1527/PNG/512/&file=shield_106660.png"


async def add_pm_text(text=default_text):
    ujwal = await bsdb.find_one({"_id": "PM_START_MSG"})
    if ujwal:
        await bsdb.update_one({"_id": "PM_START_MSG"}, {"$set": {"pm_msg": text}})
    else:
        await bsdb.insert_one({"_id": "PM_START_MSG", "pm_msg": text})


async def add_pm_thumb(thumb=default_thumb):
    ujwal = await bsdb.find_one({"_id": "PM_START_THUMB"})
    if ujwal:
        await bsdb.update_one({"_id": "PM_START_THUMB"}, {"$set": {"pm_img": thumb}})
    else:
        await bsdb.insert_one({"_id": "PM_START_THUMB", "pm_img": thumb})


async def get_thumb():
    ujwal = await bsdb.find_one({"_id": "PM_START_THUMB"})
    return ujwal["pm_img"] if ujwal else None 


async def get_pm_text():
    ujwal = await bsdb.find_one({"_id": "PM_START_MSG"})
    return ujwal["pm_msg"] if ujwal else default_text


async def set_pm_spam_limit(psl=3):
    stark = await bsdb.find_one({"_id": "LIMIT_PM"})
    if stark:
        await bsdb.update_one({"_id": "LIMIT_PM"}, {"$set": {"psl": int(psl)}})
    else:
        await bsdb.insert_one({"_id": "LIMIT_PM", "psl": int(psl)})


async def get_pm_spam_limit():
    meisnub = await bsdb.find_one({"_id": "LIMIT_PM"})
    return int(meisnub["psl"]) if meisnub else 3
