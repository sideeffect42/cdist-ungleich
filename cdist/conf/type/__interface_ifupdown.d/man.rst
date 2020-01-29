cdist-type__interface_ifupdown.d(7)
===================================

NAME
----
cdist-type__interface_ifupdown.d - Manage network interfaces using ifupdown
using the interfaces.d directory


DESCRIPTION
-----------
This space intentionally left blank.

NOTE: Only interfaces declared by cdist are removed when using --state absent.
      Moreover, the interface declaration is identified by the object_id,
      not by the interface's IP address or the like.

REQUIRED PARAMETERS
-------------------
family
   The name of the address family that the interface uses.
   Available options are: 'inet', 'ipx', 'inet6', 'can'.
method
   The name of the method used to configure the interface.
   Available options depend on the address family and are, for
   inet:
      'loopback', 'static', 'manual', 'dhcp', 'bootp', 'tunnel', 'ppp',
      'wvdial', and 'ip4ll'.
   ipx:
      'static', and 'dynamic'.
   inet6:
      'auto', 'loopback', 'static', 'manual', 'dhcp', 'v4tunnel', '6to4'.
   can:
      'static'.


OPTIONAL PARAMETERS
-------------------
name
   The name of the logical interface to configure (usually equivalent to the
   physical interface).
   Defaults to __object_id.
comment
   If supplied, the value will be inserted at the top of the configuration file
   as a comment.
   If comment is '-', what was written to stdin is used as the comment.
rename
   If supplied, the given interface renaming spefication will be added to the
   config file.
   This option can e.g. be used to generate predictable interface names based on
   the interface's MAC address.
state
   Either present or absent. Defaults to present.
option
   Additional option that is added to the generated interface configuration
   verbatim.
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


BOOLEAN PARAMETERS
------------------
auto
   If supplied, the interface will be marked "auto" and brought up during boot.
hotplug
   Allow hotplug support for this interface.
   The interface will be brought up when udev detects it, this can be during
   boot or later.
no-auto-down
   If supplied, the interface will not be brought down by the command
   "ifdown -a".
no-scripts
   If supplied, scripts in '/etc/network/if-*.d/' will not be run when this
   interface is brought up or down.


EXAMPLES
--------

.. code-block:: sh

    # Configure interface eth0 to use DHCP.
    __interface_ifupdown.d eth0 --family inet --method dhcp

    # Rename interface with MAC 00:11:22:33:44:55 to eth1 and use DHCP.
    __interface_ifupdown.d eth1 --rename mac/00:11:22:33:44:55=eth1 \
        --family inet --method dhcp


SEE ALSO
--------
:strong:`interfaces`\ (5)


AUTHORS
-------
Dennis Camera <dennis.camera@ssrq-sds-fds.ch>


COPYING
-------
Copyright \(C) 2020 Dennis Camera. You can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
