#!/bin/sh

rm -f main.js
transcrypt -e 8 -n main.py
cp __javascript__/main.js ./main.tmp.js
browserify -e main.tmp.js -o main.js
#browserify -t vueify -e main.tmp.js -o main.js
rm main.tmp.js
