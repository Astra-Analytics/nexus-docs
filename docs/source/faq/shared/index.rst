How does shared data work?
==========================

In NexusDB, we have a set of relations that are shared between all users of the database. 
This means that if one user changes a relation, all other users will see the change. This is a 
very powerful feature, but it also means that there are some things to consider when using them.

.. note::
    Any relations created by users are not queryable by other users. Relations created by
    users are tied to their API key and are only accessible with that key.

Access keys
-----------

When you add data to a shared relation, you have the option to include a `access_keys`.
This key can be used to share data with other users. If you do not provide a `access_keys`,
your data is not queryable by other users, despite being in a shared relation.

This can be useful if you want to share data with a specific user, but not with everyone.

If you want to share data with everyone, use the key 'public_4', which is the default key for
sharing data, or simply publish any `access_keys` you want to share.

.. hint::
    - If you want to share data with everyone, use the key 'public_4'.
    - If you want to share data with a specific user or group of users, create an `access_keys` value and share it with them.
    - If you do not want to share data at all, either omit `access_keys` or use a private relation.