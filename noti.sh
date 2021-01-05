#!/bin/sh
CURL='/usr/bin/curl'
CURLARGS='-f -s -S -k'
url=https://asia-northeast3-r-arques-alphasystem.cloudfunctions.net/slack_noti
channel=%23build
now=$(date +%F_%H:%M:%S)
message="${now}%20build%20success"
request="${url}?channel=${channel}&message=${message}"
# echo $url
# echo $channel
# echo $message
# echo $request
raw="$($CURL $CURLARGS $request)"
exit 0
