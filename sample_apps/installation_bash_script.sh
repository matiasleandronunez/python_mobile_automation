#!/bin/bash

echo "Waiting until the device is ready"
adb wait-for-device

while [ "`adb shell getprop sys.boot_completed | tr -d '\r' `" != "1" ] ;
do
  echo "Still waiting for boot.."
  sleep 1;
done

adb install /root/tmp/WikipediaSample.apk
