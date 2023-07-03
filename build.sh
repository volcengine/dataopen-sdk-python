#!/bin/sh

rm -rf release/dataopen-sdk-python*
mkdir release/dataopen-sdk-python

cp -rf LICENSE release/dataopen-sdk-python/
cp -rf README.md release/dataopen-sdk-python/
cp -rf main.py release/dataopen-sdk-python/
cp -rf requirements.txt release/dataopen-sdk-python/

cd release
zip -r dataopen-sdk-python.zip dataopen-sdk-python/*

rm -rf dataopen-sdk-python

cd ../