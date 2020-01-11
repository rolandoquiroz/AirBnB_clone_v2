#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo service nginx stop
sudo apt-get -y update && sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "<html>
  <head>
  </head>
  <body>
    Holberton School rules!
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -ie '/^\tlocation \/ {$/i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
