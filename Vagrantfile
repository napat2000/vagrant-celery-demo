# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
    # uncomment next line for debugging if virtualbox has problems booting.
    # vb.gui = true
  end
  config.vm.box = "precise64"  # box name
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"  # if vagrant doesn't find box, it'll download from here
  # forward ports from VM to host machine. If there are collisions, vagrant will attempt auto_correct and output necessary info during vagrant up or reload.
  config.vm.network "forwarded_port", guest: 8000, host: 8080, auto_correct: true, id: "django"
  config.vm.network "forwarded_port", guest: 15672, host: 8081, auto_correct: true, id: "rabbitmq-management"
  config.vm.network "forwarded_port", guest: 5555, host: 8082, auto_correct: true, id: "celery-flower"
  config.vm.synced_folder "app/", "/home/vagrant/code/" # setup synced folder b/w host and VM

  # set up ansible as provisioner, which will 
  config.vm.provision "ansible" do |ansible|
    ansible.limit = "all"
    ansible.playbook = "provisioning/playbook.yml"  # simple playbook that sets up the VM and starts all services
    ansible.inventory_path = "provisioning/ansible_hosts" # only has vagrant as the host; would potentially have other hosts if we were using to deploy
    ansible.verbose = "vvvv"  # set max verbosity when ansible is running. goes from 'v' to 'vvvv'
    ansible.host_key_checking = false  # disable host_key_checking
  end
end
