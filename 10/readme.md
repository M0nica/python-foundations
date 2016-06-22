This README serves as a guide as to how I transferred this script into my do-droplet and scheduled cron job.

Navigate to Digital Ocean Droplet in server
- `ssh -i ~/.ssh/do-droplet root@MY_IP`

Transfer file
- `scp -i ~/.ssh/do-droplet forecast.py root@MY_IP:~/`

Edit cron job
- `crontab -e`

- `0 8 * * * python3 forecast.py`
  - runs the forecast.py script once a day  at 8 AM.
