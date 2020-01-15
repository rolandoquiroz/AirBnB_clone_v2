#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    do_method method
    """
    current_time=datetime.utcnow().strftime("%Y%m%d%H%M%S")
    path_and_file_tgz='versions/web_static{}.tgz'.format(current_time)
    local("mkdir -p versions")
    local("tar -cvzf path_and_file_tgz web_static")
    if (os.path.exists(path_and_file_tgz) and os.path.getsize(path_and_file_tgz)) > 0:
        return
    else:
        return None
