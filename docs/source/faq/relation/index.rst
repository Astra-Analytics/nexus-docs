What is a Relation?
===================


In database terminology, a `relation <https://en.wikipedia.org/wiki/Relation_(database)>`_ is essentially a table. The term comes from the mathematical concept of a relation in relational algebra, which is used as a foundation for relational databases. A relation is made up of tuples (rows) and attributes (columns). Each tuple represents a single item or instance of the relation, and each attribute represents a property of the item. The term "relation" is used interchangeably with "table" in the context of relational databases, while "tuple" corresponds to "row," and "attribute" corresponds to "column."

Here are some key points about relations in a database:

#. Structure: A relation has a fixed structure defined by its attributes (columns), each of which has a name and a data type. The schema of a relation describes the structure of the table.
#. Uniqueness: Each tuple (row) in a relation is unique. This is often enforced through a primary key, which is a column or set of columns that uniquely identifies each row in the table.
#. Ordering: In pure relational algebra, the tuples (rows) in a relation are not ordered. However, in practical database systems, rows can be ordered based on queries using ORDER BY clauses.
#. Integrity: The database enforces integrity constraints, such as primary keys and foreign keys, to maintain accurate and consistent data across different relations (tables).
#. The concept of a relation is central to the design and operation of relational database management systems (RDBMS), such as MySQL, PostgreSQL, SQLite, Oracle, and SQL Server, which organize data into tables (relations) and support operations based on relational algebra.

.. note::

    For Nexus, we use the term "relation" to refer to the data structures
    in the database because we don't always think of them as tables. We may
    want to think of them as document collections, or as graph nodes and edges.