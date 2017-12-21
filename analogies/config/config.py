"""
	Configuration class for analogies application
"""

import getpass

class Config(object):
	USERNAME = getpass.getuser() or "anonymous-user"
	TESTING = False