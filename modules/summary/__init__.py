import re
from core.builtins import Bot
from core.component import on_command

s = on_command('summary', developers=['Dianliang233'], desc='生成聊天记录摘要', available_for=['QQ|Group'], required_superuser=True)


@s.handle()
async def _(msg: Bot.MessageSession):
    f_msg = await msg.waitNextMessage('请发送要生成摘要的合并转发消息。')
    await msg.sendMessage(f_msg.asDisplay())
    data = await f_msg.call_api('get_forward_msg', msg_id=re.search(r'\[Ke:forward,id=(.*?)\]', f_msg.asDisplay()).group(1))
    msgs = data['data']['messages']
    text = ''
    for m in msgs:
        text += f'\n{m["sender"]["nickname"]}（ID：{m["sender"]["user_id"]}，Unix时间：{m["time"]}）：{m["content"]}'
    await msg.finish(text)
