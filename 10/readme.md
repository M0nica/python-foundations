#These are the steps I took to access digital ocean

Navigate to Digital Ocean Droplet in server
- `ssh -i ~/.ssh/do-droplet root@MY_IP`

Transfer file
- `scp -i ~/.ssh/do-droplet forecast.py root@MY_IP:~/`

Edit cron job
- `crontab -e`

- `0 8 * * * python3 forecast.py`
  - runs the forecast.py script once a day
