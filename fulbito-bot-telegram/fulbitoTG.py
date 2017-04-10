import sys
import asyncio
import telepot
from telepot.aio.delegate import pave_event_space, per_chat_id, create_open

class MessageCounter(telepot.aio.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(MessageCounter, self).__init__(*args, **kwargs)
        self._count = 0

    async def on_chat_message(self, msg):
        command = msg['text']
        if command == "todas":
            self._count += 1
            todas = futbol.getListOfLeagues()
            await self.sender.sendMessage(todas)
        elif command == "Argentina" or command == "Chile" or command == "Uruguay" or command == "Chile" or command == "Venezuela":
            ligas = futbol.getLeaguesInfo(command)
            await self.sender.sendMessage(ligas)
        elif command == "33424" or command == "37746" or command == "36658" or command == "37744" or command == "33440":
            liga = futbol.getInfoLeague(command)
            await self.sender.sendMessage(liga)
        else:
            await self.sender.sendMessage(" Pone Argentina o Uruguay o Venezuela o Chile, luego el codigo de cada liga, o sino tipea todas")


TOKEN = sys.argv[1]  # get token from command-line

bot = telepot.aio.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, MessageCounter, timeout=10),
])

loop = asyncio.get_event_loop()
loop.create_task(bot.message_loop())
print('Listening ...')

loop.run_forever()
