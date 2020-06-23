cdist-type__interface(7)
========================

NAME
----
cdist-type__interface - Manage network interfaces


DESCRIPTION
-----------
This cdist type allows you to manage network interfaces on the target.
It dispatches the actual work to the interface management system specific types.
Only TCP/IP is supported. For other protocol stacks, use the specific types for
your OS.


REQUIRED PARAMETERS
-------------------
None.


OPTIONAL PARAMETERS
-------------------
state
   'present', 'absent', 'exists' or 'pre-exists', defaults to 'present' where:

   present
      the file is exactly the one from source
   absent
      the file does not exist
   exists
      the file from source but only if it doesn't already exist
   pre-exists
      check that the file exists and is a regular file, but do not
      create or modify it
name
    The name of the physical or logical network device to configure.
    Defaults to __object_id.
bootproto
    The boot protocol to use.
    Acceptable values are 'dhcp', 'static', 'manual'.
    Defaults to 'dhcp'.
address
    The IP address to assign to the network interface.
    Can be repeated to assign multiple IP addresses.
gateway
    The default gateway to assign to this interface (optional).
netmask
    The netmask.
comment
    A comment to be stored in the configuration file.
type
    The backend to use to store the interface configuration.
    Default is to auto detect.
extra-config
    Other options to be passed to the implementation type verbatim.
    Using this option makes the configuration non-portable to other backends.
    If this option is used extensively, it is recommended to use the respective
    backend type directly.


BOOLEAN PARAMETERS
------------------
onboot
   Whether to bring the interface up on boot
hotplug
   Allow/disallow hotplug support for this interface
nodns
   Do not configure nameservers in /etc/resolv.conf.
noroute
   Do not set default route.


EXAMPLES
--------

.. code-block:: sh

    # TODO
    __interface


AUTHORS
-------
Dennis Camera <dennis.camera@ssrq-sds-fds.ch>


COPYING
-------
Copyright \(C) 2020 Dennis Camera. You can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
