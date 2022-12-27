#!/bin/sh

repos=$1

[ -n "$repos" ] || {
	echo "Usage: $0 <repos dir>"
	exit 1
}

for repo in `ls $repos`;
do
	echo "Update $repo ..."
	cd $repos/$repo
	git pull --rebase origin master
	cd -
done
