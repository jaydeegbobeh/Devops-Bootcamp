# Vagrant
-
## Commands
- vagrant up: reads Vagrantfile and sets up a virtual machine (VM) according to information in file (e.g Ubuntu version 16.04.7 VM)
- vagrant halt: shuts down VM forcefully
- vagrant suspend: suspend VM
- vagrant stop:
- vagrant reload:
- vagrant ssh: 
- sudo apt-get install nginx
	- NGINX: free, open-source, high-performance HTTP server and reverse proxy
- systemctl status nginx
- sudo sytemctl start nginx
- sudo systemctl stop nginx
- vagrant plugin install vagrant-hostsupdater: pluging adds an entry to /etc/hosts file on host system, need the hostname and :private network with fixed IP address
## Advantages of vagrant

- There are numerous benefits to using Vagrant to set up our development environment.

	- Vagrant makes resetting our development environment v. easy. This makes it easy to set up a new computer/ recover if something is broken.
	- Reduces “it works on my computer” excuses for bugs. Using a common setup => can be sure we’re using the same versions of packages
	- Provides the “glue” that makes it easier to develop our code such as setting up a shared directory between the host and the guest VM. 
		- Allows us to use GUI applications without having to jump through extra hoops.
