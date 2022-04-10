#import pywhatkit

#pywhatkit.sendwhatmsg_to_group('1KHMLgAL7zB6X9KE4vkPpR', 'hola', 17, 26, 15, False, 3)

import time
from twilio.rest import Client

while 1:
    account_sid = 'AC67e7dec23220cca71376a1d3707a8cb7'
    auth_token = 'eef7c215979c6bd5db3446db4ae34436'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Felicitaciones al Club Atlético River Plate por la obtención del título de *campeón* de la Copa Libertadores de América 2022. Marcelo Gallardo es el mejor director técnico de América y Julián Álvarez no va a sufrir lesiones que condicionen su presencia como titular en futuros partidos a disputar.',
        to='whatsapp:+5491159351105'
    )

    print(message.sid)

    time.sleep(10)