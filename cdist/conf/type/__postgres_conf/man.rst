cdist-type__postgres_conf(7)
============================

NAME
----
cdist-type__postgres_conf - Manage PostgreSQL configuration


DESCRIPTION
-----------
This cdist type allows you to change PostgreSQL configurations.


REQUIRED PARAMETERS
-------------------
value
    The value to setup (can be omitted when state is set to "absent").


OPTIONAL PARAMETERS
-------------------
config_file
    The path of the config file into which the parameter should be written.
    Defaults to auto-detection (using the config_file explorer).
state
    either "present" or "absent". Defaults to "present".


EXAMPLES
--------

.. code-block:: sh

    __postgres_conf timezone --value Europe/Zurich
    __postgres_conf listen_address --state present --value '*'
    __postgres_conf max_connections --state absent


SEE ALSO
--------
none


AUTHOR
-------
Dennis Camera <dennis.camera--@--ssrq-sds-fds.ch>


COPYING
-------
Copyright \(C) 2019 Dennis Camera.
You can redistribute it and/or modify it under the terms of the GNU General
Public License as published by the Free Software Foundation, either version 3 of
the License, or (at your option) any later version.
