# internet_checker
Rudimentary internet service checker

## Setup
- `pip install twitter`
##
This script was created to run continuosly on a raspberry pi with the intention to know if the internet service at home was up while away, by tweeting every 30 minutes.

To run script on raspberry pi start up:

- Add script `python path/to/internet_checker.py &` before line `exit 0` on `/etc/rc.local`
- Change file permissions `chmod 755` for both `/etc/rc.local` and `path/to/internet_checker.py`
- `sudo reboot`
