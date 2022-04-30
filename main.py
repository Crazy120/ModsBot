from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from pyrogram.errors import UserNotParticipant
from mods import *

bot = Client(
            "yazhi",
            api_id =3769190,
            api_hash = "e125d5abf9dadd0f9b861f774f5aae6a",
            bot_token = "5120333138:AAFd1XvDIWEsu4mGwSSy-WAh7WaPJovFLmI"
)

force_channel = "yazhi_org"
send = "yazhisp"
start_message = "<b>Hello, Welcome To Our Mods Bot</b>"
force_message = "<b>You Must Subscribe Our Channel To Use This Bot</b>"
force_msg_but = [[InlineKeyboardButton("CHANNEL", url="https://t.me/yazhisp")]]
start_msg_but = [[("MODS")], [("ABOUT")], [("REQUEST/FEEDBACK")]]
mods_msg_butt = [[("NETFLIX"), ("HOTSTAR")], [("PRIME VIDEO"), ("VOOT")], [("ZEE5"), ("ULLU")], [("SONY LIV"), ("RESSO")], [("ALT BALAJI"), ("IPL MOD")], [("BACK")]]

@bot.on_message(filters.command("start") & filters.private)
async def start(bot, msg):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, msg.from_user.id)
            if user.status:
                text1 = "<b>Hello, Welcome To Yazhi's Mods Bot\n\n1. You Can Get Mods Here ❤\n\n2. You Will Get Our New Updates ❤\n\n</b>"
                reply_markup1= ReplyKeyboardMarkup(start_msg_but, one_time_keyboard=True, resize_keyboard=True)
                await msg.reply_text(text=text1, reply_markup=reply_markup1)
                await msg.reply_text(text="<b>Use The Buttons To Control Me</b>")

        except UserNotParticipant:
            ReplyKeyboardRemove(True)
            text = force_message
            reply_markup = InlineKeyboardMarkup(force_msg_but)
            await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("ABOUT") & filters.private)
async def abt(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            await msg.reply(text="<b>ABOUT\n\nYAZHI TELEGRAM BOT TO GET MODS AND NEW UPDATES OF @Yazhi_Org\n\nBOT BY : @YAZHI_ORG\n\nDEVLOPER : @Walker_Web</b>")

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("REQUEST/FEEDBACK"))
async def bak(bot, msg):
    await msg.reply(text="<b>Enter Your FeedBack OR Request, I Will Give It To My Boss</b>")

@bot.on_message(filters.document & filters.private)
async def file(bot, msg):
    if msg.from_user.id in [1058482162, 1153912202]:
        await msg.reply(msg.document.file_id)

@bot.on_message(filters.regex("MODS"))
async def mods(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            reply_markup = ReplyKeyboardMarkup(mods_msg_butt, one_time_keyboard=True, resize_keyboard=True)
            ReplyKeyboardRemove(True)
            await msg.reply_text(text="<b>CHOSE ANY MOD</b>", reply_markup=reply_markup)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("NETFLIX"))
async def nef(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            if netflix == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, netflix, caption=caption)
    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("HOTSTAR"))
async def hot(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            if hotstar == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, hotstar, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("PRIME VIDEO"))
async def prm(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            if prime == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, prime, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("VOOT"))
async def vot(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            if voot == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, voot, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("ZEE5"))
async def zee(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            if zee5 == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, zee5, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("ULLU"))
async def ulu(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            if ullu == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, ullu, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("SONLY LIV"))
async def sny(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            if sonyliv == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, sonyliv, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("ALT BALAJI"))
async def alt(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            if alt == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, alt, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("RESSO"))
async def rese(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            if resso == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, resso, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("IPL MOD"))
async def ipl(bot, msg):
    try:
        user = await bot.get_chat_member(force_channel, msg.from_user.id)
        if user.status:
            if ipl == "none":
                await msg.reply(text="<b>Mod Is Not Updated Yet, Please Wait Until We Update</b>")
            else:
                await bot.send_document(msg.chat.id, ipl, caption=caption)

    except UserNotParticipant:
        ReplyKeyboardRemove(True)
        text = force_message
        reply_markup = InlineKeyboardMarkup(force_msg_but)
        await msg.reply_text(text=text, reply_markup=reply_markup)

@bot.on_message(filters.regex("BACK"))
async def baVk(bot, msg):
    ReplyKeyboardRemove(True)
    reply_markup1= ReplyKeyboardMarkup(start_msg_but, one_time_keyboard=True, resize_keyboard=True)
    await msg.reply_text(text="<b>Use The Buttons To Control Me</b>", reply_markup=reply_markup1)

print("*RESPAWNED*, IAM ALIVE")
bot.run()