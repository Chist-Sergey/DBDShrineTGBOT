from requests import get;from telegram import Update as U;from telegram.ext import ContextTypes as C,ApplicationBuilder as A,CommandHandler as H
async def f(c:C.DEFAULT_TYPE)->None:await c.bot.send_message(c.job.chat_id,get('https://api.nightlight.gg/v1/shrine?pretty=true').text)
async def b(u:U,c:C.DEFAULT_TYPE)->None:c.job_queue.run_repeating(f,604800,1,chat_id=u.effective_chat.id)
if __name__=='__main__':a=A().token('YOUR_VERY_PERSONAL_BOT_KEY_HERE').build();a.add_handler(H('start',b));a.run_polling(10)