# Clock-profile-telegram

<br>
<p align="center">
  <img src="https://cdn.jsdelivr.net/npm/programming-languages-logos/src/python/python.png" height="100">
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


# Server and Hosting
**You can use Hiroka for hosting and server**


<a href="https://heroku.com/deploy">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>


```diff
- Please do not discourage 
- me by claiming this work 
- by copying it as your own. 
- However, You are open to use this project 
- by forking it and change any code
- necessary by giving attribute
- to the original author.

```

# Manufacturer

```diff
+ Afshin Ataei and Sori
```

**Contact us :**


<a href="https://t.me/IR_localhost">
  <img src="https://img.shields.io/badge/My-Telegram-blue?color=f20a0a " alt="Telegram" />
</a>
<br>
<a href="https://instagram.com/afshin___ataei">
  <img src="https://img.shields.io/badge/My-Instagram-blue?color=f20a0a" alt="Instagram" />
</a>
<br>
<a href="tel:989140324398">
  <img src="https://img.shields.io/badge/My-Number-blue?color=f20a0a" alt="Number" />
</a>




