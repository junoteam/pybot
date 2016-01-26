# PyBot - Bot written in Python
Telegram bot written in Python. 
Targeted to check server load, status and actually to send any commands to server, to control it.

From PyBot you can get next information:
- Load Average of Linux server
- Memory (RAM) information from server
- General information about OS and Kernel

Monitoring:
- Now bot knows to monitor site LinuxSpace.org
- When site LinuxSpace.org down, bot knows to send alert to user 
in Telegram with delay 5 seconds

You can send to PyBot next commands:
- Restart Apache server
- Restart MySQL server
- Get Status of site LinuxSpace.org

Run it in background:
```
nohup python BotApi.py &
```
![ScreenShot](https://pbs.twimg.com/media/CZqX3fTWQAA-GRl.jpg "PyBot Screenshot iPhone6")
