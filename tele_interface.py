import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import time

pp = telegram.utils.request.Request(proxy_url='socks5://103.216.82.206:6667')

auth_token = '417489646:AAGLf-uoQ_ZoIUBmiBTEa-7yHNmKiRQv44E'
bot = telegram.Bot(token=auth_token, request=pp)
id = '-343921014'

def send_image(img, caption = 'Visitor detected'):
    # img - image in bytes
    bot.send_photo(chat_id=id, photo=img, caption = caption)

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def send_prompt():
    button_list = [
        InlineKeyboardButton("Yes", callback_data='yes'),
        InlineKeyboardButton("No", callback_data='no')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    bot.send_message(id, "Do you want to allow the visitor inside?",
                    reply_markup=reply_markup)

def get_menu_response(last_id):
    updates = bot.get_updates(limit=1, offset=-1, timeout=120)
    
    if updates == []:
        return '', last_id

    recent_update = [update for update in updates if update.update_id is not last_id][0]
    
    if recent_update.update_id != last_id:
        last_id = recent_update.update_id
    else:
        return '', last_id

    message = recent_update.callback_query.data
    return message, last_id

if __name__ == '__main__':
    send_prompt()
    # bot.send_message(id, 'hi')
        
    # last_id = 0
    # while True:        
    #     updates = bot.get_updates(limit=1, offset=-1, timeout=20)
    #     recent_update = [update for update in updates if update.update_id is not last_id][0]
    #     last_id = recent_update.update_id
    #     message = last_id.callback_query.data



    
