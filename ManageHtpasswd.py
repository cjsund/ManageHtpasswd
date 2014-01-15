#!/usr/bin/env python


import os
import sys
import string

import htpasswd

from random import sample


FILE_NAME = "htpassword"
FILE_PATH = os.getcwd()
FILE = os.path.join(FILE_PATH, FILE_NAME)


class Usehtpasswd(object):

    def __init__(self, user_name, htpasswd_file):
        self.user_name = user_name
        self.htpasswd_file = htpasswd_file

    def show(self, user_name, passwd):
        print "User name: %s Password: %s" % (user_name, passwd)


class Ranpasswd(object):

    def __init__(self, length=12):
        dic = string.digits + string.letters
        self.ranpasswd = "".join(sample(dic, length))
        return self.ranpasswd


class File_name(object):

    def __init__(self, htpasswd_file):
        if htpasswd_file:
            self.htpasswd_file = htpasswd_file            
        else:
            self.htpasswd_file = FILE


class Passwd(Ranpasswd):

    def __init__(self, passwd):
        if passwd:
            self.passwd = passwd
        else:
            Ranpasswd.__init__(self)
            self.passwd = self.ranpasswd


class Add(Usehtpasswd, Passwd, File_name):

    def __init__(self, user_name, htpasswd_file=None, passwd=None):
        Usehtpasswd.__init__(self, user_name, htpasswd_file)
        File_name.__init__(self, htpasswd_file)
        Passwd.__init__(self, passwd)

        with htpasswd.Basic(self.htpasswd_file) as use:
            try:
                use.add(self.user_name, self.passwd)
                Usehtpasswd.show(self, self.user_name, self.passwd)
            except htpasswd.basic.UserExists, e:
                print e


class Change(Usehtpasswd, Passwd, File_name):

    def __init__(self, user_name, htpasswd_file=None, passwd=None):
        Usehtpasswd.__init__(self, user_name, htpasswd_file)
        File_name.__init__(self, htpasswd_file)
        Passwd.__init__(self, passwd)

        with htpasswd.Basic(self.htpasswd_file) as use:
            try:
                use.change_password(self.user_name, self.passwd)
                Usehtpasswd.show(self, self.user_name, self.passwd)
            except htpasswd.basic.UserNotExists, e:
                print e


class Delete(Usehtpasswd, File_name):

    def __init__(self, user_name, htpasswd_file=None):
        Usehtpasswd.__init__(self, user_name, htpasswd_file)
        File_name.__init__(self, htpasswd_file)

        with htpasswd.Basic(self.htpasswd_file) as use:
            try:
                use.pop(self.user_name)
                print "Delete user: %s" % self.user_name
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

    parser.add_option('-n', '--name', dest='name',
                      action='store', default=None, help="user name")
    parser.add_option('-p', '--password', dest='passwd', action='store',
                      default=None, help="password ,default random password")
    parser.add_option('-f', '--file', dest='file',
                      action='store', default=None, help="htpaswd file")
    parser.add_option('-a', '--add', dest='add',
                      action='store_true', default=False, help="add user")
    parser.add_option('-c', '--change', dest='change',
                      action='store_true', default=False, help="change password")
    parser.add_option('-d', '--delete', dest='delete',
                      action='store_true', default=False, help="delete user")

    (ops, args) = parser.parse_args()

    status = ops.add + ops.change + ops.delete
    if status >= 2:
        print "Check your option!"
        sys.exit(1)

    if ops.name is None:
        parser.print_help()
        print "You need -n zhangsan or --name zhangsan"
        sys.exit(1)
    elif status != 1:
        print "Do you want to add user or change password or delete user?"

    if ops.add:
        Add(user_name=ops.name, htpasswd_file=ops.file, passwd=ops.passwd)

    if ops.change:
        Change(user_name=ops.name, htpasswd_file=ops.file, passwd=ops.passwd)

    if ops.delete:
        Delete(user_name=ops.name, htpasswd_file=ops.file)
