# PostgreSQL Schema

Open a PR for your change, once a PR is merged, CI will automatically apply these changes to database.

## schema.sql

Defines the tables and triggers relevant to the database. Before creating each table, if it already exists it is deleted.

## put-data.sql

Inserts example data into the tables of the database. Can be utilised for testing. For proper operation, it is assumed that no records currently exist in the database (i.e. within any table).

## delete-data.sql

Delete all data from every table in the database. This process also resets the id sequences to 1 so that the behaviour is as if no data had ever existed in the database.

## [PR \#9](https://github.com/cs261-2022-group22/postgresql-schema/pull/9)

> ⚠️ Please help review these changes carefully :)
> 
> ## Once this PR is merged, the following data will be written into DB:
> * 20 Randomly generated mentors
> * 60 Randomly generated mentees (None of them has a dual profile, i.e. they're either a mentor or a mentee)
> * 5 Default Skills
> * 40 Randomly generated workshops, (**both in the past and in the future**)
> * 40 Randomly generated meetings. (**both in the past and in the future**)
> * 68 Randomly generated mentor messages
> * 92 Randomly generated mentee messages
> * 55 Randomly generated mentor skills
> * 121 Randomly generated mentee skills
> * 60 Assignments (that's for all existing mentees), with:
>   
>   * one mentor, `Timothy Figueroa <johnsonmichaela@hotmail.com>`, is fully assigned, and
>   * one mentor, `James Johnson <briansnyder@gmail.com>`, has zero assignments
> 
> ## Emails and Passwords
> The **emails are the passwords**, except:
> 
> * A "Test Mentor Account" `test@gmail.com` has its original password `test`
> * A "Test Mentee Account" `test-mentee@gmail.com` has its password `test` (as well...)
> 
> ## How to use the generator
> ```shell
> # To store generated SQL into `data.sql`
> python -m data_generator > data.sql
> ```
