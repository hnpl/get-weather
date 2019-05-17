#!/bin/bash

#https://stackoverflow.com/questions/4774054/reliable-way-for-a-bash-script-to-get-the-full-path-to-itself
SCRIPT_PATH="$( cd "$(dirname $0)" ; pwd -P )"

TEMPERATURE_FILE="temperature"
PYTHON_FILE="get-weather.py"

TEMPERATURE_PATH="$SCRIPT_PATH/$TEMPERATURE_FILE"
PYTHON_PATH="$SCRIPT_PATH/$PYTHON_FILE"

if [ ! -f "$TEMPERATURE_PATH" ];
then
  $PYTHON_PATH
else
  CURRENT_TIME=`date +%s`
  TEMPERATURE_TIME=`stat -c%Y $TEMPERATURE_PATH`
  if [ $(($CURRENT_TIME - $TEMPERATURE_TIME)) -ge 601 ];
  then
    $PYTHON_PATH
  fi
fi

TEMPERATURE=`sed -n "2p" "$TEMPERATURE_PATH"`
printf "%s%s" "$TEMPERATURE" "°C"
