# tool-to-create-digital-identities
Automatic tool to create complete digital identities.

## Requirements

- Have python3 installed ```sudo apt install python3```
- Have pip installed     ```python3 get-pip.py```

## Set up

Run the following command

```
pip install -r requirements.txt
```

## Start up

Run the following command

```
python main.py
```

## Configure crontab

Give execution permissions

```
chmod ugo+x tasks.sh
```

Add tasks.sh to crontab

```
crontab tasks.sh
```

**Note:** change the username in tasks.sh before run the file

## Built with :hammer_and_wrench:

- [VSC](https://code.visualstudio.com/) - Code editor
- [GitHub Copilot](https://github.com/features/copilot) -  AI pair programmer
- [Mastodon.py](https://github.com/halcy/Mastodon.py) - Python wrapper for the [Mastodon](https://github.com/tootsuite/mastodon/) API.
- [instagrapi](https://github.com/adw0rd/instagrapi) - Python library for Instagram Private API
- [Tweepy](https://www.tweepy.org/) - Python library for accessing the Twitter API
- [Unsplash Image API](https://unsplash.com/developers) - API to get images
- [Mail.gw](https://docs.mail.gw/) - Free anonymous temporary email

## Authors :black_nib:


* **Raúl Varandela Marra** -  [raulvarandela](https://github.com/raulvarandela)
