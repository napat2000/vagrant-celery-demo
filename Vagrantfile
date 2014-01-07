# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
    # uncomment next line for debugging if virtualbox has problems booting.
    # vb.gui = true     
  end
  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"
  config.vm.network "forwarded_port", guest: 8000, host: 8080, id: "django"
  config.vm.network "forwarded_port", guest: 15672, host: 8081, id: "rabbitmq-management"
  config.vm.network "forwarded_port", guest: 5555, host: 8082, id: "celery-flower"
  config.vm.synced_folder "app/", "/home/vagrant/code/"
  config.vm.boot_timeout = 600
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
    ansible.inventory_path = "provisioning/ansible_hosts"
    ansible.verbose = "vvvv"
    ansible.host_key_checking = false
  end
end
