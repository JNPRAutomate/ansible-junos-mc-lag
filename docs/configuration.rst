Generate and Deploy Configuration
=================================

Multiple topologies are available as part of this project.
- Sample Topology
- Vagrant
- Ravello (in progress)

Sample Topology
---------------

The main benefit of the sample-topology is that you can generate configuration even without devices.
The generate configuration, you need to excute the following command

.. code-block:: text

  ansible-playbook -i sample-topology.yaml pb.conf.all.yaml

Vagrant
-------

To be able to generate and deploy all configurations on Vagrant, you need first to start all VMs in vagrant.

.. code-block:: text

  vagrant up

Once all VMs are up and running, it's possible to use ansible directly without vagrant.

.. code-block:: text

  ansible-playbook -i .vagrant/provisioners/ansible/inventory/vagrant_ansible_inventory pb.conf.all.commit.yaml

Ravello
--------

1. Install the ravello-ansible roles
2. Make sure you have the right images in your Ravello library
3. Create a local `credential` file for Ravello.

Create the tolopogy on Ravello

.. code-block:: text

    ansible-playbook -i ravello-inventory.ini pb.rav.create.yaml --forks=1

Deploy the application and start VMs

.. code-block:: text

    ansible-playbook -i ravello-inventory.ini pb.rav.deplay.yaml --forks=1


Auto-generate Vlans and IRB Ip addresses
-----------------------------------------

.. code-block:: text

  ansible-playbook pb.gen.vlans.yaml
