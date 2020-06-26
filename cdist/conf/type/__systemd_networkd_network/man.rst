cdist-type__systemd_networkd_network(7)
=======================================

NAME
----
cdist-type__systemd_networkd_network - Manage network configuration using
systemd-networkd.


DESCRIPTION
-----------
This space intentionally left blank.


REQUIRED PARAMETERS
-------------------
None.


OPTIONAL PARAMETERS
-------------------
match
    Match directives can be used to filter the interfaces to which this
    configuration applies. This paramter can be used multiple times.
    The value will be copied to the [Match] section of the config file verbatim.
    Defaults to: "Name={interface name}"
name
    The name of the interface to configure.
option
    ...
priority
    The "priority" of this configuration. It is used as a prefix to the
    configuration file name.
    Defaults to 10.
state
    Either ``present`` or ``absent``. Defaults to ``present``.


BOOLEAN PARAMETERS
------------------
auto-reload
    Automatically apply new config after changes have been written.


EXAMPLES
--------

.. code-block:: sh

    # TODO
    __systemd_networkd_network


SEE ALSO
--------
:strong:`systemd.network`\ (5)


AUTHORS
-------
Dennis Camera <dennis.camera at ssrq-sds-fds.ch>


COPYING
-------
Copyright \(C) 2020 Dennis Camera. You can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
