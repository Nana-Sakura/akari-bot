from core.elements import MessageSession


class Template:
    @staticmethod
    async def sendMessage(msg: MessageSession, msgchain, quote=True): ...
    @staticmethod
    async def waitConfirm(msg: MessageSession): ...
    @staticmethod
    def asDisplay(msg: MessageSession): ...
    @staticmethod
    async def revokeMessage(send_msg): ...
    @staticmethod
    def checkPermission(msg: MessageSession): ...
    class Typing:
        def __init__(self, msg: MessageSession): ...
    @classmethod
    def bind_template(cls, BotTemplate):...
