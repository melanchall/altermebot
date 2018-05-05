import telegram.bot
from telegram.ext import messagequeue as mq


class MessageQueueBot(telegram.bot.Bot):
    def __init__(self, *args, is_queued_def=True, message_queue=None, **kwargs):
        super(MessageQueueBot, self).__init__(*args, **kwargs)
        self._is_messages_queued_default = is_queued_def
        self._msg_queue = message_queue or mq.MessageQueue()

    def __del__(self):
        try:
            self._msg_queue.stop()
        except:
            pass
        super(MessageQueueBot, self).__del__()

    @mq.queuedmessage
    def send_message(self, *args, **kwargs):
        return super(MessageQueueBot, self).send_message(*args, **kwargs)
