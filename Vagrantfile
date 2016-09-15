# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

## Generate a unique ID for this project
UUID = "IREMSFQ"

## Define ports mapping to create a Full Mesh between all 4 vqfx
vqfx_map = {  'spine-01'  => [1,2,3,4,5,6],
              'spine-02'  => [1,2,7,8,9,10],
              'leaf-01'   => [3,7,11,12,15],
              'leaf-02'   => [4,8,11,12,16],
              'leaf-03'   => [5,9,13,14,17],
              'leaf-04'   => [6,10,13,14,18]
            }

srv_map = {
            'srv-01'    => [15,16],
            'srv-02'    => [17,18]
          }

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.ssh.insert_key = false

    vqfx_map.keys.each do |vm|
        re_name  = vm
        pfe_name = ( vm.to_s + "-pfe" ).to_sym

        # ##############################
        # ## Packet Forwarding Engine ##
        # ##############################
        config.vm.define pfe_name do |vqfxpfe|
            vqfxpfe.ssh.insert_key = false
            vqfxpfe.vm.box = 'juniper/vqfx10k-pfe'

            # DO NOT REMOVE / NO VMtools installed
            vqfxpfe.vm.synced_folder '.', '/vagrant', disabled: true
            vqfxpfe.vm.network 'private_network', auto_config: false, nic_type: '82540EM', virtualbox__intnet: "#{UUID}_vqfx_internal_#{vm}"

        end

        ##########################
        ## Routing Engine  #######
        ##########################
        config.vm.define re_name do |vqfx|
            vqfx.vm.hostname = vm
            vqfx.vm.box = 'juniper/vqfx10k-re'

            # DO NOT REMOVE / NO VMtools installed
            vqfx.vm.synced_folder '.', '/vagrant', disabled: true

            # Management port
            vqfx.vm.network 'private_network', auto_config: false, nic_type: '82540EM', virtualbox__intnet: "#{UUID}_vqfx_internal_#{vm}"
            vqfx.vm.network 'private_network', auto_config: false, nic_type: '82540EM', virtualbox__intnet: "#{UUID}_reserved_bridge"

            # count how many interfaces are needed
            nbr_int = vqfx_map[vm].length

            # Dataplane ports
            (0..nbr_int).each do |seg_id|
               vqfx.vm.network 'private_network', auto_config: false, nic_type: '82540EM', virtualbox__intnet: "#{UUID}_seg#{vqfx_map[vm][seg_id]}"
            end
        end
    end

    ##############################
    ## Box provisioning        ###
    ## exclude Windows host    ###
    ##############################
    if !Vagrant::Util::Platform.windows?
        config.vm.provision "ansible" do |ansible|
            ansible.groups = {
                "spine" => ["spine-01", "spine-02" ],
                "leaf:children" => ["access-01", "access-02"],
                "access-01" => ["leaf-01", "leaf-02" ],
                "access-02" => ["leaf-03", "leaf-04" ],
                "spine-pfe"  => ["spine-01-pfe", "spine-02-pfe"],
                "leaf-pfe"  => [ "leaf-01-pfe", "leaf-02-pfe", "leaf-03-pfe", "leaf-04-pfe" ],
                "junos:children" => ["spine", "leaf"],
                "vqfx10k-pfe:children" => ["spine-pfe", "leaf-pfe"],
                "all:children" => ["junos", "vqfx10k-pfe"],
                "all:vars" => ["topology_file=vagrant-topology.yaml"]
            }
            ansible.host_vars = {
              "spine-01"  =>  {"id" => "11"},
              "spine-02"  =>  {"id" => "12"},
              "leaf-01"   =>  {"id" => "21"},
              "leaf-02"   =>  {"id" => "22"},
              "leaf-03"   =>  {"id" => "23"},
              "leaf-04"   =>  {"id" => "24"},
            }
            ansible.extra_vars = {
                   "topology_file" => "vagrant-topology.yaml",
            }
            ansible.playbook = "pb.show_version.yaml"
        end
    end
end
