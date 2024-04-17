.. meta::
    :description: Learn how to update your data in |product|
    :twitter:description: Learn how to update your data in |product|

Updating existing data
======================

.. rst-class:: lead
    This section explains how to update data in |product|

The `update` method works is structured like the `insert` method, but it will 
update the data if the primary key already exists in the relation. If the primary key does not exist,
it will retrun an error.

.. tab-set-code::
    .. code-block:: python 

        from nexus_python.nexusdb import NexusDB

        nexus_db = NexusDB(api_key="your_api_key")

        # Update data in the relation
        fields = ["id", "name"]
        values = [[1, "Item 1"], [2, "Item 2"]]
        response = nexus_db.update(relation_name, fields, values)
        print("update data response:", response)

    .. code-block:: shell

        NEXUSDB_API_KEY = "YOUR_API_KEY"

        curl -X POST https://api.nexusdb.io/query \
        -H "Content-Type: application/json" \
        -H "API-Key: $NEXUSDB_API_KEY" \
        -d '{
        "query_type": "Update",
        "relation_name": "example_relation",
        "fields": ["id", "name"],
        "values": [
            [1, "Item 1"],
            [2, "Item 2"]
        ]
        }'