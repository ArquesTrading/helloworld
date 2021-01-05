#!/bin/sh
url=https://asia-northeast3-r-arques-alphasystem.cloudfunctions.net/slack_noti
channel=#build
now='date'
message="${now} build success"
echo $url
echo $channel
echo $message
exit 0
