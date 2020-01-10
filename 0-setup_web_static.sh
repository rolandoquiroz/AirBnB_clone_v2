#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo service nginx stop
sudo apt-get update && sudo apt-get upgrade
sudo apt-get -y nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Holberton School rules!" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '/^\tlocation \/ {$/i\\tlocation /hbnb_static/ {\n\talias /data/web_static/current/;\n\t}\n' etc/nginx/sites-available/default
sudo service nginx restart
