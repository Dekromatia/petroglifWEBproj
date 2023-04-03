# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/focal64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  #config.vm.network "private_network", ip: "192.168.50.4"
  
    
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "8192"
    vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
  end  

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
    sudo usermod -aG docker vagrant

    # sudo apt install software-properties-common
    # sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt-get install python 3.7
    # sudo apt install nvidia-cuda-toolkit

    #wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
    #echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
    #apt-get update
    #sudo apt-get install -y mongodb-org
    #sudo systemctl enable mongod --now
    
  SHELL

end

  