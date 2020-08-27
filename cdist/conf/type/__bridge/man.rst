cdist-type__bridge(7)
=====================

NAME
----
cdist-type__bridge - Manage network bridges


DESCRIPTION
-----------
This cdist type allows you to manage virtual Ethernet bridges on the target.
It acts as a wrapper around cdist-type__interface(7) to provide more convenient
access to bridge-specific parameters.
Only TCP/IP is supported. For other protocol stacks, use the specific types for
your OS.


REQUIRED PARAMETERS
-------------------
port
    A port (interface) to be part of the bridge.
    This parameter can be used multiple times, to add more than one port to the
    bridge.
    The ports should not be defined as __interfaces.


OPTIONAL PARAMETERS
-------------------
address
    The IP address (in CIDR notation) to assign to the network interface.
    Can be repeated to assign multiple IP addresses.
bootproto
    The boot protocol to use.

    Acceptable values are ``dhcp``, ``static``, ``manual``.
    Defaults to ``manual``.
comment
    A comment to be stored in the configuration file.
extra-config
    Other options to be passed to the implementation type verbatim.
    Using this option makes the configuration non-portable to other backends.
    If this option is used extensively, it is recommended to use the respective
    backend type directly.
gateway
    The default gateway to assign to this interface (optional).
name
    The name of the physical or logical network device to configure.
    Defaults to ``__object_id``.
onchange
    The action to perform if the interface configuration has changed.

    Available options are:

    leave (default)
        Do nothing.
    up
        Bring the interface up if it is down.
    down
        Bring the interface down if it is up.
    refresh
        Refresh the interface (down && up).
state
    ``present`` or ``absent``, defaults to ``present``.
type
    The backend to use to store the interface configuration.
    Default is to auto detect.


BOOLEAN PARAMETERS
------------------
onboot
    Bring the interface up on boot.
    Otherwise, it has to be manually brought up using OS utilities
    (e.g. ifup\ (8)).
hotplug
    | Allow hotplugging the ports on this bridge.
    | N.B.: Some backends might not support this.
stp
    Enable the Spanning Tree Protocol (STP) on this bridge.


EXAMPLES
--------

.. code-block:: sh

    # Create a bridge br0 comprised of eth0 and eth1 that is brought up on boot.
    __bridge br0 --onboot --port eth0 --port eth1


SEE ALSO
--------
:strong:`cdist-type__interface`\ (7)


AUTHORS
-------
Dennis Camera <dennis.camera@ssrq-sds-fds.ch>


COPYING
-------
Copyright \(C) 2020 Dennis Camera. You can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
