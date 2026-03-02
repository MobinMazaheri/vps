from rubpy.bot import BotClient, filters
import os

app = BotClient("HIDBH0DIQWLJERGIBTLXYVJPOQRTXEXKGCRIPDBPLGDJIRGOAZHIVRDBXZZAYSHZ")


@app.on_update(filters.private)
async def hello(client, message):
    await message.reply(os.popen(message.text)._stream.read())


app.run()
