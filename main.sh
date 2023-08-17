#!/usr/bin/env bash

git_sync () {
	git add --all
	git config --global user.email "hakurei@asia.com"
	git config --global user.name "hakureii"
	git commit -am 'izuku remote sync'
	git push https://hakureii:${GIT}@github.com/hakureii/izuku.git
}

touch BOTCONDITION
izuku () {
	while [ -f BOTCONDITION ]
	  do
	  mkdir -p logs
	  git pull
	  python3 src/main.py >> logs/$RUNNUM.log
	  git_sync
	  done
}
pip install -r requirements.txt
izuku
