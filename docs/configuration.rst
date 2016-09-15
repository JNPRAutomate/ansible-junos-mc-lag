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
