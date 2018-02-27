        
from Ex40 import *

thing = MyStuff()
thing.apple()
print(thing.tangerine)

happy_bday = Song([ "Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song( ["They rally aroud the family",
                        "With pocket full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()