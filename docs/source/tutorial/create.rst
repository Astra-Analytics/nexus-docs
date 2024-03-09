Create a relation
=================

Let's take a closer look at the `create` method. This method is used to create a new relation in the database.

.. note::
    When using the API directly, your HTTP request must contain an `Api-Key` header that specifies your NexusDB API key.

.. tab-set-code::
    .. code-block:: python 

        relation_name = "example_relation"
        columns = [
            {"name": "id"},
            {"name": "name"},
        ]
        create_response = nexus_db.create(relation_name, columns)

    .. code-block:: shell

        NEXUSDB_API_KEY = "YOUR_API_KEY"

        curl -X POST https://api.nexusdb.io/query \
        -H "Content-Type: application/json" \
        -H "API-Key: $NEXUSDB_API_KEY" \
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