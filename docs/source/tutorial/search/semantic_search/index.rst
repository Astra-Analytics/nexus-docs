.. meta::
    :description: Learn how to find information within |product|
    :twitter:description: Learn how to find information within |product|

Semantic Search
===============

Searching using semantic similarity with vector embeddings is easy with |product|.
Below is a simple example to get you started.

.. tab-set-code::
    .. code-block:: python 

        from nexus_python.nexusdb import NexusDB
        from openai import OpenAI

        # Initialize NexusDB
        nexus_db = NexusDB(api_key="your_nexusdb_api_key")

        # Initialize OpenAI
        client = OpenAI(api_key="your_openai_api_key")

        # Search for similar vectors
        search_query = "What is the best database?"
        response = client.embeddings.create(input=search_query, model="text-embedding-ada-002")
        query_vector = response.data[0].embedding

        # Perform the search using the vector
        # This assumes the vector_search in NexusDB can handle raw query vectors
        search_response = nexus_db.vector_search(
            query_vector=query_vector,  # Adjust parameters as needed
            number_of_results=5,  # Example parameter
        )
        print("Search Response:", search_response)

Additional parameters like search radius, filter statements, and access keys will be coverd in the "advanced" section, coming soon!

