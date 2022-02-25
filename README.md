# PostgreSQL Schema

Open a PR for your change, once a PR is merged, CI will automatically apply these changes to database.

## schema.sql

Defines the tables and triggers relevant to the database. Before creating each table, if it already exists it is deleted.

## put-data.sql

Inserts example data into the tables of the database. Can be utilised for testing. For proper operation, it is assumed that no records currently exist in the database (i.e. within any table).

## delete-data.sql

Delete all data from every table in the database. This process also resets the id sequences to 1 so that the behaviour is as if no data had ever existed in the database.
