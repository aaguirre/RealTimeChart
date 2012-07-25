RealTimeChart

Installation:

python setup.py develop
pserve development.ini
python setup.py test

Links:
http://gevent-socketio.readthedocs.org/
http://www.gevent.org

Development Version

http://gevent.googlecode.com/files/gevent-1.0b2.tar.gz

tar -zxvf gevent-1.0b2.tar.gz
cd gevent-1.0b2
python setup.py install


TDD with PyCharm
http://tv.jetbrains.net/videocontent/getting-started-with-pycharm


Socket.IO.js
http://socket.io/

Tweepy
https://github.com/tweepy/tweepy/

Pyramid
http://docs.pylonsproject.org/en/latest/index.html



auth = tweepy.OAuthHandler(self.credentials['consumer_key'], self.credentials['consumer_secret'])
auth.set_access_token(self.credentials['access_token'], self.credentials['access_token_secret'])
api = tweepy.API(auth)

user = tweepy.api.get_user(self.username)
user.timeline():

