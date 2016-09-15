Ansible Roles
==============

There are severals roles provided as part of this project.
Most are used to generate configurations.

config template - junos-mclag-icl
-----------------------------------

Generate the configuration for the ICL/ICCP link.

Default variables
^^^^^^^^^^^^^^^^^

.. code-block:: yaml

    mclag_shared:
      iccp:
        vlan_id: 10
        vlan_name: ICCP_VLAN
      mode: active-active

    # Automatically calculate an ID (0 or 1) for each device based on the variable "ID"
    mclag_id: "{{ id - ((id//2)*2) }}"

    mclag:
      icl_interface: ae0
      chassis_id: "{{ mclag_id }}"
      status_control: "{{ 'active' if mclag_id == '0' else 'standby' }}"
      iccp:
        local_ip: "{{ '1.1.1.2' if mclag_id == '0' else '1.1.1.1' }}"
        peer_ip: "{{ '1.1.1.1' if mclag_id == '0' else '1.1.1.2' }}"
      icl:
        description: ICL interface


config template - junos-mclag-qfx10k
-------------------------------------

Generate configuration for all MC-AE interfaces.

Default variables
^^^^^^^^^^^^^^^^^


config template - junos-system
--------------------------------

Generate configuration for all base junos configuration:
- ntp
- dns
- login
- etc

generate_vlans
---------------
