#!/bin/sh
container=$1
CURL='/usr/bin/curl'
CURLARGS='-f -s -S -k'
url=https://asia-northeast3-r-arques-alphasystem.cloudfunctions.net/slack_noti
channel=%23build
space=%20
newline=%0A
now=$(date +%F_%H:%M:%S)
if [ $container eq '' ]
then
    message="${now}${newline}All${space}build${space}success"
else
    message="${now}${newline}${container}${space}build${space}success"
request="${url}?channel=${channel}&message=${message}"
# echo $url
# echo $channel
# echo $message
# echo $request
raw="$($CURL $CURLARGS $request)"
exit 0
