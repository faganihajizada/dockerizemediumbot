from telebot import TeleBot as tb # Telegram API

class poster:
   _token = "632985476:AAFfx7TD5eeKRhgexKBgMERA6zgD7znLFD4"
   _channel_id = "@mongotest"
   _bot = None
   def __init__(self):
      self._bot = tb(self._token)

   def send_message(self,description):
      self.post_text(description)

   def post_text(self, msg):
      status = self._bot.send_message(chat_id=self._channel_id, text=msg)
