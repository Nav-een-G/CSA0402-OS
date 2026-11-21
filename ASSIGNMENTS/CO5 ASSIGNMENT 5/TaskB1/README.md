# Task B1 – Linux Administration
Run `cat /etc/os-release`, `uname -r`, `ps aux`, `top`, `free -h`, `vmstat 1 5`, `df -h`, `ss -tulnp`; if available run `iostat -xz 1 3`.
Run scripts using `chmod +x *.sh`, `./log_analysis.sh`, `./disk_alert.sh 80`.
Expected log output: status 200=4, 302=1, 403=1, 404=1; busiest client 10.0.0.5 with 4 requests; total bytes 43200.
Cron hourly (replace with absolute path): `0 * * * * /bin/bash /absolute/path/log_analysis.sh >> /absolute/path/log-analysis.log 2>&1`.
The systemd template assumes a `portal` user, app at `/opt/result-portal`, venv at `/opt/result-portal/.venv`, and env file `/etc/result-portal/result-portal.env`. Adapt before use. Then `sudo systemctl daemon-reload`, `sudo systemctl enable --now result-portal`, `sudo systemctl status result-portal`.
For Nginx: install adapted site config, run `sudo nginx -t`, then `sudo systemctl reload nginx`.
UFW example: `sudo ufw allow OpenSSH`, `sudo ufw allow 'Nginx Full'`, `sudo ufw enable`, `sudo ufw status`. Verify SSH access before enabling firewall remotely.
