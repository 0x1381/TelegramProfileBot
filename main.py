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


string = '1BJWap1sBu0htPkSduoEDiuoFIKfdmXuhVxnYn-ZOyTnY5TUwlcs-pbvlb65o8CHOg9EmyhDVTgmQYlK3TweAJtxbMix7kvuojavvnOx7gkBB4LEtRCir6A_5o-u49XQgDXWLATrFOFYSE6h8vzxWYcnqnjb9Dhuy3zXP-i4PUGfgcdD9nvU-XJGT43rIWF69McJ4G-jy43A_WPL666T8zd1Idhr8nXX4n3XUcLuDzz-JvBZZEoP3ScPyRbz20CrMOrvCE589LffnX68u6pNUK8wQ-XsS2XzRjarfPEbvua1gZHgvj6t_fQrHgS4EDx7Iumzf1nftSuveibMF30ayKnP_SVxP2Og='
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
