# liteTwitch

## Description

A simple GUI app for browsing your followed TwitchTV streams and subsequently launching them using livestreamer.

[screenshot here]()

## Installation

1. Download the [`liteTwitch.py`](liveTwitch.py) file. This is all you need from this repo.
2. Make sure you have [livestreamer](https://github.com/chrippa/livestreamer) installed, as well as python of course.
3. Create a `config.cfg` file in the directory you are storing `liveTwitch.py`.
  * Get your auth token from [this](https://api.twitch.tv/kraken/oauth2/authorize?response_type=token&client_id=i8wca4tvk7hhie7ike8uhzy8i3pzr0n&redirect_uri=http://localhost&scope=user_read) URL. You will be redirected to a page with a URL of the form:
  
    `fdsfsd`

    You want to copy this authorization token into your `config.cfg` file in the following format:
    
    `token YOUR_AUTH_TOKEN`
4. Execute `liteTwitch.py`.
