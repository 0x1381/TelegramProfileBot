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
  ```




```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```


