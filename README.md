## Homophone Finder

This is a simple script with takes in a raw text file of Japanese words and finds homophones.

A sample list was included with this repo, a simple frequency list of 1000 words taken from Offbeat Band [here](http://www.offbeatband.com/2010/12/the-most-commonly-used-japanese-words-by-frequency/). You can use any list you like, but the format will need to match the one provided, ie:
```
さく
貰う
真実
ゲーム
団
```
If it is not you will need to do some data cleaning beforehand.

### Notes
In order to reduce ambiguity, words comprised only of kana in the list are removed by the script using a simple character check. Based on the listing [here](http://www.rikai.com/library/kanjitables/kanji_codes.unicode.shtml) the bulk of kanji in everyday use fall between 4e00 and 9faf.