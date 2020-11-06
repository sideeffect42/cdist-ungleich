cdist-type__sshd_config(7)
==========================

NAME
----
cdist-type__sshd_config - TODO


DESCRIPTION
-----------
This space intentionally left blank.


REQUIRED PARAMETERS
-------------------
None.


OPTIONAL PARAMETERS
-------------------
file
    ....
match
    Can be used multiple times.
    All of the attributes on a single Match line are ANDed together
option
    ....
state
    ....
value
    ....


BOOLEAN PARAMETERS
------------------
None.


EXAMPLES
--------

.. code-block:: sh

    # TODO
    __sshd_config


SEE ALSO
--------
:strong:`TODO`\ (7)


BUGS
----
- This type assumes a nicely formatted config file, i.e. only one config option per line (and no config options spanning multiple lines)
- ``Include`` directives are ignored.



AUTHORS
-------
Dennis Camera <dennis.camera--@--ssrq-sds-fds.ch>


COPYING
-------
Copyright \(C) 2020 Dennis Camera. You can redistribute it
and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
