Ansible Roles
==============

There are severals roles provided as part of this project.
Most are used to generate configurations.

config template - junos-mclag-icl
-----------------------------------

Generate the configuration for the ICL/ICCP link.

Default variables
^^^^^^^^^^^^^^^^^

.. include:: _includes/roles_junos_mclag_icl_defaults_main.yaml

config template - junos-mclag-qfx10k
-------------------------------------

Generate configuration for all MC-AE interfaces.

Default variables
^^^^^^^^^^^^^^^^^

.. include:: _includes/roles_junos_mclag_qfx10k_defaults_main.yaml


config template - junos-mclag-qfx5k (deprecated for now)
---------------------------------------------------------



config template - junos-system
--------------------------------

Generate configuration for all base junos configuration:
- ntp
- dns
- login
- etc

generate_vlans
---------------
