import json
import sys
import webbrowser
from urllib.request import urlopen
from urllib.error import URLError
from tkinter import *
from subprocess import *

version = {'major': 0, 'minor': 9, 'patch': 0}

print('liteTwitch {0[major]}.{0[minor]}.{0[patch]}\n'.format(version))
print('Reading config file...')

# open config file
try: configFile = open('config.cfg', 'r')
except FileNotFoundError:
    input('[ERROR] No config file found.')
    sys.exit()

# default values
_quality = 'best'
_chat = 'false'
_token = None

# reading user specified values from config file
for line in configFile:
    if line.split()[0] == 'token':
        _token   = line.split()[1]
        print('\tAuthorization Token set to "{}"'.format(_token))
    if line.split()[0] == 'quality':
        _quality = line.split()[1]
        print('\tStream Quality set to {}'.format(_quality))
    if line.split()[0] == 'chat':
        _chat    = line.split()[1]
        print('\tOpen Chat with streams set to {}'.format(_chat))
        
# user did not specify a value for authorization token
if _token == None:
    input('[ERROR] No authorization token specified in config file.')
    sys.exit()
    
print('[DONE]')

class App:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)
        print('[DONE]')
        # load the streams list straight from the beginning
        self.refresh()
        
    # fetches the list of followed streams from the twitch API
    def fetchStreams(self):
        print('\tFetching followed streams list...')
        try:
            self.streams = json.loads(urlopen(url, timeout=15).read().decode('utf-8'))
            print('\t[DONE]')
        except URLError as e:
            # print error, stop fetching streams
            print('\t[ERROR] {}'.format(e.reason));
        
    # draw a followed stream's name, game and status message to a specified row
    def drawStream(self, STREAM, ROW):
        print('\tAdding stream #{}...'.format(ROW+1))
        if 'name' in STREAM['channel']:   Label(self.frame, text=STREAM['channel']['name']).grid(row=ROW,column=0)
        else: print('\t\tWarning: No stream name found')
        if 'game' in STREAM['channel']:   Label(self.frame, text=STREAM['channel']['game']).grid(row=ROW,column=1)
        else: print('\t\tWarning: No stream game found')
        if 'status' in STREAM['channel']: Label(self.frame, text=STREAM['channel']['status']).grid(row=ROW,column=2)
        else: print('\t\tWarning: No stream status found')
        Button(self.frame, text='Watch', command=lambda:self.openStream(STREAM)).grid(row=ROW,column=3)
    
    # open a specified stream using livestreamer
    def openStream(self, STREAM):
        print('Opening livestreamer...')
        
        if 'name' not in STREAM['channel']:
            print('[ERROR] Stream has no name - operation aborted')
        else:
            if _chat == 'true':
                print('\tOpening chat...')
                try:
                    webbrowser.open_new("http://www.twitch.tv/{}/chat?popout=".format(STREAM['channel']['name']))
                    print('\t[DONE]')
                except Error as e:
                    print('\t[ERROR] {}'.format(e.reason))
            
            command = ['livestreamer','twitch.tv/'+STREAM['channel']['name'],_quality]
            # run livestreamer in new terminal window using subprocess module
            Popen(command, creationflags=CREATE_NEW_CONSOLE)
            
            print('[DONE]')
        
    # refresh the list of followed streams and draw them to the app window
    def refresh(self):
        print('Refreshing...')
        self.frame.destroy()
        
        self.frame = Frame(self.master)
        self.fetchStreams()
        
        r = 0
        for stream in self.streams['streams']:
            self.drawStream(stream, r)
            r = r+1
        Label(self.frame, text='Online: {} | Quality: {} | Chat: {}'.format(self.streams['_total'],_quality,_chat), relief=SUNKEN).grid(row=r,columnspan=3,sticky=W+E)
        Button(self.frame, text="Refresh", command=self.refresh).grid(row=r,column=3)
        self.frame.pack()
        
        print('[DONE]')

# api url containing followed streams
url = 'https://api.twitch.tv/kraken/streams/followed?oauth_token=' + _token

# open main window
print('Opening main app window...')
root = Tk()
root.wm_title('liteTwitch {0[major]}.{0[minor]}.{0[patch]}'.format(version))
app = App(root)
root.mainloop()