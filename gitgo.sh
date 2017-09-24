#!/bin/sh
# Quick commits to master branch
git pull
git add -A
git commit -m "$1"
git push
git pull
