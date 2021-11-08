Vagrant.configure("2") do |config|



config.vm.box = "ubuntu/xenial64"
# creating a virtual machine ubuntu

# assign private ip to our VM
config.vm.network "private_network", ip: "192.168.10.100"

# alias for private ip
# ensure to install hostsupdater before rerunning vagrant
config.hostsupdater.aliases = ["development.local"]

# Sync folder from OS to Vm
config.vm.synced_folder ".", "/home/vagrant/app"


# automate execution of provision.sh
config.vm.provision "shell", path: "./Vagrant/provision.sh", run: 'always'

end
