#!/usr/bin/env python
#coding:utf-8
#filename=ranpasswd

from random import sample

import string


#

class create():
	"""
	Generate a random password

	#!/usr/bin/evn python
	
	import ranpasswd

	password = ranpasswd.create()
	password.len(10) #len(10) password length is 10


	"""
	def lens(self, length):
		self.length = length
		dic = string.digits + string.letters
		return "".join(sample(dic, self.length))
		

if __name__ == "__main__":
	print create.__doc__