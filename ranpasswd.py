#!/usr/bin/env python
# coding:utf-8
# filename=ranpasswd

from random import sample

import string


#

class create():

    def lens(self, length):
        self.length = length
        dic = string.digits + string.letters
        return "".join(sample(dic, self.length))


if __name__ == "__main__":
    print create.__doc__
