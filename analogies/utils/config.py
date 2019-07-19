"""
    Configuration class for analogies application
"""

import getpass


class Config:
    """App configuration"""
    USERNAME = getpass.getuser() or "anonymous-user"

    def __init__(self):
        pass
