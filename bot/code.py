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
        text="Choose The Crf Below",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('23', callback_data="i23"), InlineKeyboardButton('24', callback_data="i24"), InlineKeyboardButton('25', callback_data="i25")],
                [InlineKeyboardButton('26', callback_data="i26"), InlineKeyboardButton('27', callback_data="i27"), InlineKeyboardButton('28', callback_data="i28")],
                [InlineKeyboardButton('29', callback_data="i29"), InlineKeyboardButton('30', callback_data="i30"), InlineKeyboardButton('31', callback_data="i31")],
                [InlineKeyboardButton('32', callback_data="i32"), InlineKeyboardButton('33', callback_data="i33"), InlineKeyboardButton('34', callback_data="i34")],
                [InlineKeyboardButton('Save this and turn back', callback_data="turnback")]
                ],
            ),
        quote=True,
        )
  elif "23" in event.data:
    crf.insert(0, "23")
  elif "24" in event.data:
    crf.insert(0, "24")
  elif "25" in event.data:
    crf.insert(0, "25")
  elif "26" in event.data:
    crf.insert(0, "26")
  elif "27" in event.data:
    crf.insert(0, "27")
  elif "28" in event.data:
    crf.insert(0, "28")
  elif "29" in event.data:
    crf.insert(0, "29")
  elif "30" in event.data:
    crf.insert(0, "30")
  elif "31" in event.data:
    crf.insert(0, "31")
  elif "32" in event.data:
    crf.insert(0, "32")
  elif "33" in event.data:
    crf.insert(0, "33")
  elif "34" in event.data:
    crf.insert(0, "34")
  # man I am tired of this fffmpeg thing👍
  elif "turnback" in event.data:
        text="You can choose the settings below 👍",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton('Crf', callback_data="icrf"), InlineKeyboardButton('Codec', callback_data="icodec")],
                [InlineKeyboardButton('Preset', callback_data="ipreset"), InlineKeyboardButton('resolution', callback_data="iroc")],
                [InlineKeyboardButton('Save it', callback_data="finalcode")]
                ],
            ),
        quote=True,
        )
          
  elif "icodec" in event.data:
        await event.message.edit_text(
            text="Choose Your Codec",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('Libx265', callback_data="ihevc"), InlineKeyboardButton('Libx264', callback_data="iavc")],
                    [InlineKeyboardButton('Save this and turn back', callback_data="turnback")]
                    ],
                ),
            quote=True,
            )
 elif "ipreset" in event.data:
    await event.message.edit_text(
        text="Bruh! This module isnt set now!",
        quote=True,
        )
 elif "iroc" in event.data:
    await event.message.edit_text(
        text="Bruh! I didn't edit this",
        quote=True,
        )
    
 elif "ihevc" in event.data:
    codec.insert(0, "libx265")
 
elif "iavc" in event.data:
    codec.insert(0, "iavc")
    
    
# still some left 🤮
    
   
 
               
            
        
      
        
      
    
    
 

       
      
        
        
         
    
  
  
  
  
  
  
  
  
  
  


  
