#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack.
"""
from fabric.api import local
from datetime import datetime
# from pathlib import Path
import os

def do_pack():
    """
    do_method method
    """
    local("mkdir -p versions")
    current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    my_file = "web_static_{}.tgz".format(current_time)
    local("tar -cvzf versions/web_static_'{}' web_static".format(my_file))
    my_path = "versions/{}".format(my_file)
    os.path.normpath(my_path)
    if os.path.exists(my_path):
        return my_path
    else:
        return None
