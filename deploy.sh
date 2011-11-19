#!/bin/sh
cp -r public/ ../qinlijing.github.com/

cd ../qinlijing.github.com
git add .
git commit -am "automatic commit"
git push -u origin master
