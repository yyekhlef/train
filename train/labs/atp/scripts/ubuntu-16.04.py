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

# docker os release
curl -sSL https://get.docker.com/ | sh

# docker cs release
#wget -qO- 'https://pgp.mit.edu/pks/lookup?op=get&search=0xee6d536cf7dc86e2d7d56f59a178ac6c6238f52e' | sudo apt-key add --import
#apt-get update
#apt-get install -y apt-transport-https
#echo "deb https://packages.docker.com/1.9/apt/repo ubuntu-trusty main" | tee /etc/apt/sources.list.d/docker.list
#apt-get update
#apt-get install -y docker-engine

usermod -aG docker ubuntu

# compose
curl -L https://github.com/docker/compose/releases/download/1.7.1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

{dinfo}
'''

def pre_process():
    """Anything added to this function is executed before launching the instances"""
    pass

def post_process():
    """Anything added to this function is executed after launching the instances"""
    pass

