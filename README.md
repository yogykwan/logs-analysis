# logs-analysis
fsnd - an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Prepare
1. download [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip and get `newdata.sql`
2. download [vagrant box](https://vagrantcloud.com/bento/boxes/ubuntu-16.04-i386/versions/2.3.5/providers/virtualbox.box), rename to `ubuntu-16.04-i386.box`
3. move `newdata.sql` and `ubuntu-16.04-i386.box` to directory `vagrant`
4. start vagrant by `vagrant up` and `vagrant ssh`

## Synopsis
1. use postgresql as db and load from newsdata.sql
2. use python module psycopg2 to `connect|cursor|execute|fetchall|commit` db
3. output results in well-format

## Usage
```
python run.py [<args>]
```

Args:

&emsp;&emsp; article: the most 3 popular articles with the most popular one at the top

&emsp;&emsp; author: a sorted list of authors with the most popular one at the top

&emsp;&emsp; error: on which days more than 1% of requests led to errors
