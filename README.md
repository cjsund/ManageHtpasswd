ManageHtpasswd
==============

###First 
		You master install htpasswd from python
		sudo easy_install htpasswd

###Function:
		Manage htpasswd(htpasswd and nginx more)
		Add user and user`s password or use random password. 
		Change user`s password or use random password.
		Delete user.

		Specify a password file path or use default(modify the HTPASSWD_PATH and HTPASSWD_NAME).

###Usage:
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

More fast for manage htpasswd .
