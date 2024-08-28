import pyrogram
import requests
import os
import dotenv
dotenv.load_dotenv()

app = pyrogram.Client(
    'my_account',
    os.getenv('API_ID'),
    os.getenv('API_HASH')
)


def test_return_data():
    app.start()
    app.send_message(
        chat_id='dbdshrine_bot',
        text='/start',
        disable_notification=True,
    )
    response: str = requests.get(
        'https://api.telegram.org/{}/getUpdates'.format(
            os.getenv('TOKEN'))).text
    print(response)
    app.stop()
