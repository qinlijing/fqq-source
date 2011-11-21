#!/bin/sh
cd ../qinlijing.github.com
git reset --hard HEAD
git rm -r .

cp -r ../ebook/public/ .

git add .
git commit -a
git push -u origin master
