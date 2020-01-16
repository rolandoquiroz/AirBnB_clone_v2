#!/usr/bin/python3
"""
Write a Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to your web servers, using
the function deploy
"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ["104.196.104.147", "34.73.38.83"]
env.key_filename = "~/.ssh/holberton"


def do_pack():
    """
    do_method method
    """
    local("mkdir -p versions")
    my_current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    my_file = "web_static_{}.tgz".format(my_current_time)
    local("tar -cvzf versions/'{}' web_static".format(my_file))
    my_path = "versions/{}".format(my_file)
    if (os.path.exists(my_path) and os.path.getsize(my_path)) > 0:
        return my_path
    else:
        return None


def do_deploy(archive_path):
    """ Do deploy """
    if not os.path.exists(archive_path):
        return False
    Upload = put(archive_path, "/tmp/")
    if Upload.failed:
        return False
    archive = archive_path[9:-4]
    Make_dir = run("mkdir -p /data/web_static/releases/'{}'".format(archive))
    if Make_dir.failed:
        return False
    Uncompress = run(
        "tar -xzf '{0}''{1}'.tgz -C /data/web_static/releases/'{1}'".
        format("/tmp/", archive))
    if Uncompress.failed:
        return False
    Delete_compressed = run("rm '{}''{}'.tgz".format("/tmp/", archive))
    if Delete_compressed.failed:
        return False
    Move_uncompressed = run(
        "mv /data/web_static/releases/'{0}'/web_static/* \
        /data/web_static/releases/'{0}'".format(archive))
    if Move_uncompressed.failed:
        return False
    Delete_old = run("rm -rf /data/web_static/releases/'{0}'/web_static".
                     format(archive))
    if Delete_old.failed:
        return False
    Delete_old_sym_link = run("rm -rf /data/web_static/current")
    if Delete_old_sym_link.failed:
        return False
    Create_new_sym_link = run("ln -s /data/web_static/releases/{0} \
    /data/web_static/current".format(archive))
    if Create_new_sym_link.failed:
        return False
    return True


def deploy():
    """
    Deploy method
    """
    pack = do_pack()
    if pack:
        do_deploy(pack)
    else:
    return False
