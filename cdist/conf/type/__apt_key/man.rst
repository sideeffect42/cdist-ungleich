cdist-type__apt_key(7)
======================

NAME
----
cdist-type__apt_key - Manage the list of keys used by apt


DESCRIPTION
-----------
Manages the list of keys used by apt to authenticate packages.


REQUIRED PARAMETERS
-------------------
None.


OPTIONAL PARAMETERS
-------------------
state
   'present' or 'absent'. Defaults to 'present'

keyid
   the id of the key to add. Defaults to __object_id

keyserver
   the keyserver from which to fetch the key. If omitted the default set
   in ./parameter/default/keyserver is used.

keydir
   key save location, defaults to ``/etc/apt/trusted.pgp.d``

uri
   the URI from which to download the key


EXAMPLES
--------

.. code-block:: sh

    # Add Ubuntu Archive Automatic Signing Key
    __apt_key 437D05B5
    # Same thing
    __apt_key 437D05B5 --state present
    # Get rid of it
    __apt_key 437D05B5 --state absent

    # same thing with human readable name and explicit keyid
    __apt_key UbuntuArchiveKey --keyid 437D05B5

    # same thing with other keyserver
    __apt_key UbuntuArchiveKey --keyid 437D05B5 --keyserver keyserver.ubuntu.com

    # download key from the internet
    __apt_key rabbitmq \
       --uri http://www.rabbitmq.com/rabbitmq-signing-key-public.asc


AUTHORS
-------
Steven Armstrong <steven-cdist--@--armstrong.cc>
Ander Punnar <ander-at-kvlt-dot-ee>


COPYING
-------
Copyright \(C) 2011-2019 Steven Armstrong and Ander Punnar. You can
redistribute it and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
