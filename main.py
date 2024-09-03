import telegram
import telegram.ext
import requests
import datetime
import os
import dotenv
dotenv.load_dotenv()


async def main(context: telegram.ext.ContextTypes.DEFAULT_TYPE) -> None:
    current_shrine: str = requests.get(
        'https://api.nightlight.gg/v1/shrine?pretty=true').text
    previous_shrine: str = open('last_shrine.txt', 'r').readline()

    if not current_shrine == previous_shrine:
        previous_shrine = open('last_shrine.txt', 'w').write(current_shrine)
        await context.bot.send_message(
            # "return to sender"
            chat_id=context.job.chat_id,
            text=current_shrine,
        )


async def start(
    update: telegram.Update,
    context: telegram.ext.ContextTypes.DEFAULT_TYPE
) -> None:

    context.job_queue.run_daily(
        main,
        datetime.datetime.now().hour,
        chat_id=update.effective_message.chat_id,
    )


if __name__ == '__main__':
    app = telegram.ext.ApplicationBuilder(
    ).token(os.getenv('TOKEN')).build()

    app.add_handler(telegram.ext.CommandHandler('start', start))

    app.run_polling(poll_interval=36) # 3600
