.. meta::
    :description: Learn how to add vector embeddings to your data in |product|
    :twitter:description: Learn how to add vector embeddings to your data in |product|

Inserting data with vectors
===========================

To insert vectors along with your data, you can use the `insert_with_vector` method.
This method allows you to insert data along with the vector embeddings.
The vector embeddings can be generated using any method you choose, but currently only supporting 
1536 dimensions (the same dimensions as OpenAI embedding models for simplicity).

.. tab-set-code::
    .. code-block:: python 

        from nexus_python.nexusdb import NexusDB
        from openai import OpenAI

        # Initialize NexusDB
        nexus_db = NexusDB(api_key="your_nexusdb_api_key")

        # Initialize OpenAI
        client = OpenAI(api_key="your_openai_api_key")

        # Example text to insert
        text_to_insert = "nexusdb is a great database."

        # First, get the vector for the given text
        vector = get_embedding(text_to_insert)

        insert_response = nexus_db.insert_with_vector(
            relation_name="example_relation",
            text=text_to_insert,
            vectors=vector,
        )
        print("Insert Response:", insert_response)
    
    .. code-block:: shell

        NEXUSDB_API_KEY = "YOUR_API_KEY"
        vectors = list_of_vector_embeddings

        curl -X POST https://api.nexusdb.io/query \
        -H "Content-Type: application/json" \
        -H "API-Key: $NEXUSDB_API_KEY" \
        -d '{
        "query_type": "Insert",
        "relation_name": "example_relation",
        "searchable_content": {
                "text": text,
                "vectors": $vectors,
            }
        }'

This code will insert the text "nexusdb is a great database." along with the vector embeddings into the relation "example_relation".
If using the shell script, you might have noticed that this is also the `insert` method, but with an additional `vectors` parameter.
This is because the `insert_with_vector` method is a wrapper around the `insert` method, with the `vectors` parameter added.
You may optionally include the `vectors` parameter when inserting fields and values, but it is not required. Note that doing this
will not automatically link the vectors and other data together, but will link the text and vector embeddings to the specified relation.

Information about referencing other data, metadata filtering, 
and access keys will be discussed in the "advanced" section, 
coming soon. For now, you can reference the source code, `here <https://github.com/Astra-Analytics/nexus-python>`_.