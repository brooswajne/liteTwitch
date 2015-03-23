# liteTwitch

## Description

A simple GUI app for browsing your followed TwitchTV streams and subsequently launching them using livestreamer.

![screenshot here](screenshot.PNG)

## Installation

1. Download the [`liteTwitch.py`](/liteTwitch.py) file. This is all you need from this repo.
2. Make sure you have [livestreamer](https://github.com/chrippa/livestreamer) installed, as well as python of course.
3. Create a `config.cfg` file in the directory you are storing `liteTwitch.py`.
  * Get your TwitchTV API authorization token for this app from <a id="gettoken" href="https://api.twitch.tv/kraken/oauth2/authorize?response_type=token&client_id=i8wca4tvk7hhie7ike8uhzy8i3pzr0n&redirect_uri=http://localhost&scope=user_read">this</a> link. You will be redirected to a page with a URL of the form:
  
    `http://localhost/#access_token=YOUR_AUTH_TOKEN&scope=user_read`

    You want to copy this authorization token into your `config.cfg` file in the following format:
    
    `token YOUR_AUTH_TOKEN`
4. Execute `liteTwitch.py`.

## Configuration Options

A `config.cfg` file is required. If none is found when the app is first run, a blank one will be created for you.

Lines inside the config file take the form:

```PARAMETER ARGUMENT```

Here is a list of currently possible `config.cfg` parameters and their arguments:

Parameter | Argument(s) | Required? | Default Value
---|---|---|---
token | <a href="#gettoken">Twitch API auth token</a> | Yes | N/A
quality | [Livestreamer quality options](http://docs.livestreamer.io/cli.html#positional-arguments) | No | best
chat | true/false | No | false
