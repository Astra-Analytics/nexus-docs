.. meta::
    :description: Learn how to upsert data to |product|
    :twitter:description: Learn how to upsert data to |product|

Upsert method
=============

The `upsert` method works exactly like the `insert` method, but it will update the data if the primary key already exists in the relation. If the primary key does not exist, it will insert the data.

.. tab-set-code::
    .. code-block:: python 

        from nexus_python.nexusdb import NexusDB

        nexus_db = NexusDB(api_key="your_api_key")

        # Upsert data into the relation
        fields = ["id", "name"]
        values = [[1, "Item 1"], [2, "Item 2"]]
        response = nexus_db.upsert(relation_name, fields, values)
        print("upsert data response:", response)

    .. code-block:: shell

        NEXUSDB_API_KEY = "YOUR_API_KEY"

        curl -X POST https://api.nexusdb.io/query \
        -H "Content-Type: application/json" \
        -H "API-Key: $NEXUSDB_API_KEY" \
        -d '{
        "query_type": "Upsert",
        "relation_name": "example_relation",
        "fields": ["id", "name"],
        "values": [
            [1, "Item 1"],
            [2, "Item 2"]
        ]
        }'