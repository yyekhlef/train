#!/usr/bin/env python

PRIMARY_OS = 'Ubuntu-16.04'
PRIMARY = '''#!/bin/sh
#
FQDN="{fqdn}"

# hostname
hostnamectl set-hostname $FQDN

# Change default passwor to "docker"
echo "ubuntu:docker" | chpasswd

# Allow password authentication
sed -i 's|[#]*ChallengeResponseAuthentication no|ChallengeResponseAuthentication yes|g' /etc/ssh/sshd_config

# Restart SSH service
service ssh restart

{dinfo}
'''

def pre_process():
    """Anything added to this function is executed before launching the instances"""
    pass

def post_process():
    """Anything added to this function is executed after launching the instances"""
    pass

