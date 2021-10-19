# the following content contains ffmpeg violence 
# kindly only 15+ learn it, else u will not study and open a channel like (c) @Animes_Encoded and waste ur time 
# kindly teens only !!
# (c) No Abhir Hassan allowed ....

import asyncio
import io
import logging
import os
import shutil
import sys
import time
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from pyrogram.types import ChatPermissions, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant, UsernameNotOccupied, ChatAdminRequired, PeerIdInvalid



from bot import (
    AUTH_USERS,
    crf,
    watermark,
    audio_b,
    resolution,
    codec,
    preset,
    app,
    data,
    pid_list
)

# inline buttons with callback query data , using append feature ( god level idea 😎 )
guide_b=[]
guide_b.append([InlineKeyboardButton("CRF", callback_data="icrf")])
guide_b.append([InlineKeyboardButton("CODEC", callback_data="icodec")])
guide_b.append([InlineKeyboardButton("VBR", callback_data="ivbr")])
guide_b.append([InlineKeyboardButton("Save It And Dont Turn Back", callback_data="beck")])






async def final_settings_af(client, message):
  await client.send_message(
    message.chat.id,
    text="You can choose the settings below 👍",
    reply_markup=InlineKeyboardMarkup(
      [
        [InlineKeyboardButton('Crf', callback_data="icrf"), InlineKeyboardButton('Codec', callback_data="icodec")],
        [InlineKeyboardButton('Preset', callback_data="ipreset"), InlineKeyboardButton('resolution', callback_data="icodec")],
        [InlineKeyboardButton('Save it', callback_data="finalcode")]
        ],
      ),
    quote=True
    )
 
@app.on_callback_query()
async def callback_handlers(_, event: CallbackQuery):
  if "icrf" in event.data:
    await event.message.edit_text(
      text="Choose the crf below"
      # rest I will add later ( dont deploy) 
    
    
 

       
      
        
        
         
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
