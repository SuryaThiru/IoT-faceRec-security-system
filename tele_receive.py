import tele_interface as tele
import telegram

last_id = 0
res = None
print('listening...')
while True:
    try:
        res, last_id = tele.get_menu_response(last_id)
    except telegram.error.NetworkError:
        print('Network error')

    if res == 'yes':
        print('Lock open')
    elif res == 'no':
        print('Lock close')
