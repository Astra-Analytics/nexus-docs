.. meta::
    :description: Learn how to insert data to |product|
    :twitter:description: Learn how to insert data to |product|

Insert method
=============

The `insert` method behaves as you'd expect - it simply adds new data without
affecting existing information.

Let's take a look at an example, then walk through and explain each piece:

.. tab-set-code::
    .. code-block:: python 

        from nexus_python.nexusdb import NexusDB

        nexus_db = NexusDB(api_key="your_api_key")

        # Insert data into the relation
        fields = ["id", "name"]
        values = [[1, "Item 1"], [2, "Item 2"]]
        response = nexus_db.insert(relation_name, fields, values)
        print("Insert data response:", response)

    .. code-block:: shell

        NEXUSDB_API_KEY = "YOUR_API_KEY"

        curl -X POST https://api.nexusdb.io/query \
        -H "Content-Type: application/json" \
        -H "API-Key: $NEXUSDB_API_KEY" \
        -d '{
        "query_type": "Insert",
        "relation_name": "example_relation",
        "fields": ["id", "name"],
        "values": [
            [1, "Item 1"],
            [2, "Item 2"]
        ]
        }'