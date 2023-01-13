# univ_michigan_hurricane_research
A working shared code repository for research projects between Patterson and the University of Michigan

# Conda

This covers the basics around using Conda

## Managing Environments

The "requirements.txt" file was created with the command:
```
conda list -e > requirements.txt
```
## Building a new virtual environment with Conda

You can be used to create a conda virtual environment with
```
conda create --name <env> --file requirements.txt
```


# DBT

Basic concepts for installing and using DBT

## Installing DBT

```
conda install -c conda-forge dbt
```

## dbt-duckdb connector site

Source:
https://github.com/jwills/dbt-duckdb

### Installation of DuckDB Connector for DBT

This project is hosted on PyPI, so you should be able to install it and the necessary dependencies via:

```
pip3 install dbt-duckdb

```

The latest supported version targets dbt-core 1.1.x and duckdb 0.3.2.


## Quick Overvview of DBT

* stuff here

What is the general workflow?

* `dbt init <project-name>`
* set db path in profile
* configure schema and models in project
* `dbt run`


## Using DBT Profiles

[todo]

### What is a DBT Profile?

[ TODO ]

### Where Does the DBT Profile Live?

(OSX) ~/.dbt/profiles.yml

### Example DBT Profile Contents

```
dbt_duckdb_test:
  target: dev
  outputs:
    dev:
      type: duckdb
      path: '...../workspaces/snowpark_demos/duckdb/fips_test_db'
      #optional fields
      #schema: schema_name 
```

### Confirm DBT Profile Connection Works

```
dbt debug
20:04:52  Running with dbt=1.1.1
dbt version: 1.1.1
python version: 3.8.13
python path: /Users/josh/opt/anaconda3/envs/hurricane_analytics/bin/python
os info: macOS-10.16-x86_64-i386-64bit
Using profiles.yml file at /Users/josh/.dbt/profiles.yml
Using dbt_project.yml file at /Users/josh/Documents/PattersonConsulting/workspaces/snowpark_demos/dbt/dbt_duckdb_test/dbt_project.yml

Configuration:
  profiles.yml file [OK found and valid]
  dbt_project.yml file [OK found and valid]

Required dependencies:
 - git [OK found]

Connection:
  database: main
  schema: main
  path: /Users/josh/Documents/PattersonConsulting/workspaces/snowpark_demos/duckdb/fips_test_db
  Connection test: [OK connection ok]

All checks passed!
```
