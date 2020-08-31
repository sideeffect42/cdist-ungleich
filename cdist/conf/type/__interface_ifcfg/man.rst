cdist-type__interface_ifcfg(7)
===============================

NAME
----
cdist-type__interface_ifcfg - Manage network interfaces using ifcfg network
scripts.


DESCRIPTION
-----------
This type allows to configure network interfaces using the ifcfg network scripts
on RedHat and SuSE distributions.


REQUIRED PARAMETERS
-------------------
bootproto
    ...
type
    The type of the interface, e.g. ``Ethernet``, ``Bridge``, ``Dummy``,
    ``Loopback``.
    Defaults to ``Ethernet``.


OPTIONAL PARAMETERS
-------------------
address

comment
    If supplied, the value will be inserted at the top of the configuration file
    as a comment.
option
    ...
    Can be used multiple times.


BOOLEAN PARAMETERS
------------------
onboot

hotplug



EXAMPLES
--------

.. code-block:: sh

    # TODO
    __interface_ifcfg ...


SEE ALSO
--------
:strong:`cdist-type__interface`\ (7)


AUTHORS
-------
Steven Armstrong <steven-cdist at armstrong.cc>
Dennis Camera <dennis.camera at ssrq-sds-fds.ch>


COPYING
-------
Copyright \(C) 2014--2020 Steven Armstrong and Dennis Camera.

You can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.
