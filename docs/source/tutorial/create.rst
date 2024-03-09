Create a relation
=================

.. tab-set-code::
    .. code-block:: python

        relation_name = "example_relation"
        columns = [
            {"name": "id"},
            {"name": "name"},
        ]
        create_response = nexus_db.create(relation_name, columns)

    .. code-block:: bash

        curl -X POST https://api.nexusdb.io/query \
        -H "Content-Type: application/json" \
        -H "API-Key: your-api-key" \
        -d '{
        "query_type": "Create",
        "relation_name": "example_relation",
        "fields": [
            {"name": "id", "type": "Any?", "default": null, "is_primary": true},
            {"name": "name", "type": "Any?", "default": null, "is_primary": false}
        ]
        }'

You may notice that the bash command contains more information than the python one. This is
because the python client has default values for the fields, so you don't need to specify them.