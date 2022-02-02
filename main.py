from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.functions.account import UpdateProfileRequest
import time
from telethon import functions , types
from utils import generate_image, delete_image, get_current_time
import config
import cute_numbers
from telethon.sessions import StringSession



#with TelegramClient(StringSession(), config.api_id, config.api_hash) as client:
#    print(client.session.save())


string = ''
client = TelegramClient(StringSession(string), config.api_id, config.api_hash)
client.start()


def main():
    previous_time = ''
    while True:
        if not previous_time == get_current_time():
            current_time = get_current_time()
            previous_time = current_time
            generate_image(current_time)
            image = client.upload_file(config.image_filename)
            client(UploadProfilePhotoRequest(image))
            client(DeletePhotosRequest([client.get_profile_photos('me')[-1]]))
            delete_image()
            time.sleep(1)



if __name__ == '__main__':
    main()
