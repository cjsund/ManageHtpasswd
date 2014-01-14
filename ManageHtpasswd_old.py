#!/usr/bin/env python
# coding:utf-8
# filename:ManageHtpasswd

import os
import sys
import datetime
import htpasswd
import ranpasswd


from shutil import copy

HTPASSWD_PATH = os.getcwd()
HTPASSWD_NAME = "htpassword"
HTPASSWD_FILE = os.path.join(HTPASSWD_PATH, HTPASSWD_NAME)
passwd = ranpasswd.create()


class backupfile(object):

    def __init__(self, path=HTPASSWD_PATH, name=HTPASSWD_NAME):
        self.path = path
        self.name = name
        from_file = os.path.join(self.path, self.name)
        backup_file = from_file + \
            datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        copy(from_file, backup_file)


class Usehtpasswd(object):

    def __init__(self, name, htpasswd_file=HTPASSWD_FILE):
        self.name = name
        try:
            if self.name is None:
                raise Exception
        except Exception:
            print "You need a name!"
            sys.exit(1)
        self.htpasswd_file = htpasswd_file

    def add(self, password=passwd.lens(10)):

        self.password = password
        with htpasswd.Basic(self.htpasswd_file) as useradd:
            try:
                useradd.add(self.name, self.password)
                print "name:%s password:%s" % (self.name, self.password)
            except htpasswd.basic.UserExists, e:
                print e

    def change(self, new_password=passwd.lens(10)):

        self.new_password = new_password
        with htpasswd.Basic(self.htpasswd_file) as userchange:
            try:
                userchange.change_password(self.name, self.new_password)
                print "name:%s password:%s" % (self.name, self.new_password)
            except htpasswd.basic.UserNotExists, e:
                print e

    def delete(self):

        backupfile(path=os.path.dirname(self.htpasswd_file),
                   name=os.path.basename(self.htpasswd_file))
        with htpasswd.Basic(self.htpasswd_file) as userdel:
            try:
                userdel.pop(self.name)
                print "Delete %s " % self.name
            except htpasswd.basic.UserNotExists, e:
                print e


if __name__ == "__main__":

    from optparse import OptionParser

    usage = u'''usage: Manage htpasswd 
    add user:
        python %prog -n san.zhang -a  #use random password
        python %prog -n san.zhang -a -p q1w2e3
        python %prog -n san.zhang -a -f /data/http/htpasswd
    change password:
        python %prog -n san.zhang -c  #use random password
        python %prog -n san.zhang -c -p q1w2e3
        python %prog -n sna.zhang -c -f /data/http/htpasswd
    delete user:
        python %prog -n san.zhang -d
        python %prog -n sna.zhang -d -f /data/http/htpasswd
        '''

    parser = OptionParser(usage=usage)

    parser.add_option('-n', '--name', action='store',
                      dest='name', default=None, help="user`s name")
    parser.add_option('-a', '--add', action='store_true',
                      dest='add', default=False, help="add user")
    parser.add_option('-d', '--delete', action='store_true',
                      dest='delete', default=False, help="delete user")
    parser.add_option('-c', '--change', action='store_true',
                      dest='change', default=False, help="change user password")
    parser.add_option('-f', '--file', action='store',
                      dest='file', default=None, help="file`s path")
    parser.add_option('-p', '--password', action='store',
                      dest='password', default=None, help="use`s password, default random")

    (ops, args) = parser.parse_args()

    if ops.file is None:
        use = Usehtpasswd(name=ops.name)
    else:
        use = Usehtpasswd(htpasswd_file=ops.file, name=ops.name)

    if ops.add + ops.change + ops.delete >= 2:
        sys.exit("Check your Option")

    if ops.add:
        arg = "add"
    elif ops.change:
        arg = "change"
    elif ops.delete:
        arg = "delete"
        getattr(use, arg)()
        sys.exit(0)

    if ops.password is None:
        getattr(use, arg)()
    else:
        getattr(use, arg)(ops.password)