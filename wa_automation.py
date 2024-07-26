# import pywhatkit

# pywhatkit.sendwhatmsg_to_group('XXXXXXX', 'hola', 17, 26, 15, False, 3)

import time
from twilio.rest import Client

def river_campeon():
# while 1:
    account_sid = 'XXXXXXX'
    auth_token = 'XXXXXXX'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Felicitaciones al Club Atlético River Plate por la obtención del título de *campeón* de la Copa Libertadores de América 2022. Marcelo Gallardo es el mejor director técnico de América y Julián Álvarez no va a sufrir lesiones que condicionen su presencia como titular en futuros partidos a disputar.',
        to='whatsapp:+XXXXXXX'
    )

    print(message.sid)

#    time.sleep(10)
