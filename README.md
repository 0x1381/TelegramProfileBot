# 

<p align="center">

  <h1 align="center">Clock profile telegram</h1>

</p>



<br>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" height="50">
</p>
<br>

## 🛠 Installation & Set Up

```bash
git clone https://github.com/0x1381/Clock-profile-telegram/
cd Clock-profile-telegram
pip install -r requirements.txt

```

Go to <code>my.telegram.org</code> then <code>click API development tools</code> and receive api_id and api_hash

- Open <code>config.py</code>, and change <code>api_id</code> and <code>api_hash</code>.
```python 
  api_id = 1205106
  api_hash = '40e24db52fa79aff3a9aa308fc3e6727'
  session_name = '0x1381'
```

- Then open <code>main.py</code>, remove this line from the hashtag.
```python 
   #with TelegramClient(StringSession(), config.api_id, config.api_hash) as client:
       #print(client.session.save())

   to
 
   with TelegramClient(StringSession(), config.api_id, config.api_hash) as client:
       print(client.session.save())

   then hashtag line 17 18 19

   #string = ''
   #client = TelegramClient(StringSession(string), config.api_id, config.api_hash)
   #client.start()
    
```

- Then save file and run <code>main.py</code>. 
- Now copy the StringSession and open the <code>main.py</code> again and put it in the string variable.

```python 
   string = 'StringSession'

```

- then reset line 17 18 19 

```python 
 string = 'StringSession'
 client = TelegramClient(StringSession(string), config.api_id, config.api_hash)
 client.start()


 and hashtag line 13 14

 #with TelegramClient(StringSession(), config.api_id, config.api_hash) as client:
       #print(client.session.save())

```

- Everything is ready to run the file
<code>python main.py</code>

# Customization

**Go to the <code>resources</code> path to personalize your profile picture and clock color**
- Open the <code>main.py</code> to change the picture 
```python 
photo_filename = '/resources/YourFileName'
image_text_color = 'greenyellow' #ff0800
```
- And you can go to the <code>utils.py</code> file to change the font
```python
font = ImageFont.truetype(font='resources/YourFont.TTF', size=150)
```


# Screenshot 

<p align="center">
  <img src="https://github.com/0x1381/Clock-profile-telegram/blob/main/IMG_20220203_011218.jpg">
</p>


# Server and Hosting
**You can use Hiroka for hosting and server**

<a href="https://heroku.com/deploy">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>


</br>

# Attention

<p align="center">
  <img src="https://github.com/0x1381/Clock-profile-telegram/blob/main/resources/1643835420947.png">
</p>


```diff
- Please do not copy this
- I have spent hours on this project
- Please FORK this repo don't copy 
- داوش بخای اسکی بری مامانت صلوات ختم میکنم
```

# Manufacturer

```diff
+ Afshin Ataei
```

**Contact us :**


<a href="https://t.me/IR_localhost">
  <img src="https://img.shields.io/badge/My-Telegram-blue?color=f20a0a " alt="Telegram" />
</a>
<br>
<a href="https://instagram.com/afshin___ataei">
  <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" alt="Instagram" />
</a>




