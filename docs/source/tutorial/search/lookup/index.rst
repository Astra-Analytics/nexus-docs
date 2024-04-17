.. meta::
    :description: Learn how to search for items by key in |product|
    :twitter:description: Learn how to search for items by key in |product|

Lookup
======

The `lookup` method is used to search for items by key in |product|. 
The key is the unique identifier of the item. 

.. tab-set-code::
    .. code-block:: python 

        from nexus_python.nexusdb import NexusDB

        nexus_db = NexusDB(api_key="your_api_key")

        # Lookup and return entire relation
        lookup_response = nexus_db.lookup(relation_name, tabulate=True)
        print("Lookup after deletion:\n", lookup_response)

    .. code-block:: shell

        NEXUSDB_API_KEY = "YOUR_API_KEY"

        curl -X POST https://api.nexusdb.io/query \
        -H "Content-Type: application/json" \
        -H "API-Key: $NEXUSDB_API_KEY" \
        -d '{
            "query_type": "Lookup",
            "relation_name": "Test_Relation2",
            "columns": [],
            "condition": ""
        }'

In this example, we omitted the "fields" and "condition" parameters ("fields" is called "columns" in shell currently but is being updated to "fields" to match the Python SDK). This will return the entire relation.

To return just a handful of fields, you can specify the "fields" parameter. For example, to return just the "name" field where "id" is equal to 1, you can use the following code:

.. tab-set-code::
    .. code-block:: python 

        from nexus_python.nexusdb import NexusDB

        nexus_db = NexusDB(api_key="your_api_key")

        relation_name = "example_relation"
        fields = ["name"]
        condition = "id=1"

        # Lookup and return entire relation
        lookup_response = nexus_db.lookup(relation_name, tabulate=True)
        print("Lookup after deletion:\n", lookup_response)

    .. code-block:: shell

        NEXUSDB_API_KEY = "YOUR_API_KEY"

        curl -X POST https://api.nexusdb.io/query \
        -H "Content-Type: application/json" \
        -H "API-Key: $NEXUSDB_API_KEY" \
        -d '{
            "query_type": "Lookup",
            "relation_name": "Test_Relation2",
            "columns": ["name"],
            "condition": "id=1"
        }'

The condition parameter allows you to filter the results. Simply list them as a string, such as "id=1, name='John'". The condition parameter is optional, and if omitted, all items will be returned.