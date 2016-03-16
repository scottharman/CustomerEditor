# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provision "shell", path: "pg_config.sh"
  # config.vm.box = "hashicorp/precise32"
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider 'virtualbox' do |v|
      v.customize ['modifyvm', :id, '--nictrace1', 'off']
      v.customize ['modifyvm', :id, '--nictracefile1', 'e:\temp\trace1.pcap']
  end
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.network "forwarded_port", guest: 5432, host: 5432
  #config.vm.network "forwarded_port", guest: 3306, host: 3306

end
