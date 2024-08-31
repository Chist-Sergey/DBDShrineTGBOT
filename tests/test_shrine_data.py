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
    app.stop()

    response_from_bot: str = requests.get(
        'https://api.telegram.org/{}/getUpdates'.format(
            os.getenv('TOKEN'))).text
    response_from_site: str = requests.get(
        'https://api.nightlight.gg/v1/shrine?pretty=true').text

    print(response_from_bot)

    assert response_from_bot == response_from_site
