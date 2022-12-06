#!/bin/bash

xset s noblank
xset s off
xset -dpms

unclutter -idle 0.5 -root &

sed -i 's/"exited_cleanly":false/"exited_cleanly":true/' /home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type":"Crashed"/"exit_type":"Normal"/' /home/pi/.config/chromium/Default/Preferences


npm --prefix /home/pi/OBD2/frontend/OBD2 run dev &
flask --app /home/pi/OBD2/backend/api.py run &

/usr/bin/chromium-browser --noerrdialogs --disable-infobars --kiosk http://127.0.0.1:5173 &

while true; do
   xdotool keydown ctrl+Tab; xdotool keyup ctrl+Tab;
   sleep 10
done
