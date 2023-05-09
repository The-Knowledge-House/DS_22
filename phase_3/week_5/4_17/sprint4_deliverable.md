## Sprint 4 Deliverables

### Conceptual Database

Answer the following questions as a group. 

* Purpose: what would be the purpose of our database?
* Information: what information do I have already?
* Identify Objects (aka entities): 
    * Out of the information that I already have, what columns do I want to keep?   
    * Do subsets of these columns represent different objects?      
    * ex: Product, Customer, Store  
    * ex: Company, Job  
* Do these objects relate to one another at all?

You do not have to submit these self-reflections in google classroom, but we still recommend you write down the answers to these questions in some shared document that all group members can look back to.

### Logical Database 

Formalize these observations via an entity relationship diagram. You will be using [draw.io](draw.io). 

Design an erd diagram using the following [symbols](https://github.com/The-Knowledge-House/DS_22/blob/main/phase_2/week_8/1_24/intermediate_sql_I_notes.ipynb) we've discussed before.

For a more in-depth exploration of ERD diagrams, check out the following link: https://vertabelo.com/blog/chen-erd-notation/

Once you've sufficiently described your database using an ERD diagram, you will download it as jpg or png from draw.io and save it to a shared google drive folder that staff can access. 

You will be submitting a link to this diagram as part of your deliverables.

### Choose a Primary Key

Once you've designed your logical database, choose an attribute as a primary key. 

Keep in mind that a key is a unique identifier of a specific set of information. That is, if we know the primary key, we should be able to use it to access any other subsequential and unique information.

For example, let's say you have a table of retirees that are looking to access their pension. Their primary key would be their social security number, which will be used to determine their names, pension fund, and address. We could express this as `Social Security --> (First Name, Last Name, Fund, Address)` in terms of functional dependency.

Multiple people that are accessing their pension can live in the same address, so we cannot use address as a primary key. Similarily, multiple people can share the same first name or last name. Your key must be a unique identifier that has no chance of being `null` or a duplicate.

We usually recommend using an existing attribute to model a key, but in this case, you will develop an attribute such as `company_id` or `comment_id` for your data model.

Your primary key will be expressed in specific notation, as expressed in the [chen-erd](https://vertabelo.com/blog/chen-erd-notation/) documentation above.

### Choose a Foreign key

You will represent any relationships within your tables as foreign keys. For example, if many jobs belong to 1 company, you will have a `company_id` foreign key for each tuple in your `job` table. If a bootcamp contains many bootcamp sessions (2020, 2019, etc), each bootcamp "semester" tuple will have a `bootcamp_id` foreign key. 

When brainstorming foreign keys, consider the following question: which foreign key will allow me to make reliable joins across my tables (if relevant).

Note that some tables (or perhaps even entire databases) will not have foreign keys!