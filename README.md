# logs-analysis
fsnd - an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

## Prepare
1. download [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip and get `newsdata.sql`
2. download [vagrant box](https://vagrantcloud.com/bento/boxes/ubuntu-16.04-i386/versions/2.3.5/providers/virtualbox.box), rename to `ubuntu-16.04-i386.box`
3. move `newsdata.sql` and `ubuntu-16.04-i386.box` to directory `vagrant`
4. start vagrant
```
vagrant up
vagrant ssh
cd /vagrant
```

## Synopsis
1. use postgresql as db and load from newsdata.sql
2. `pip install psycopg2-binary` to use [psycopy2](http://initd.org/psycopg/docs/install.html#binary-install-from-pypi)
3. execute specific sql clauses based on sys.argv
4. `psql -d news` then create views
```
create view article_log_view as
select title, count(log.id) as views
from articles, log
where articles.slug = substring(log.path from 10)
group by title;
create view author_log_view as
select author, count(log.id) as views
from articles, log
where articles.slug = substring(log.path from 10)
group by author;
create view day_total_view as
select to_char(time, 'YYYY-MM-DD') as day, count(log.id) as total
from log
group by day;
create view day_error_view as
select to_char(time, 'YYYY-MM-DD') as day, count(log.id) as error
from log
where status != '200 OK'
group by day;
```

## Usage
```
python run.py [<args>]
```

args:

&emsp;&emsp; article: top 3 articles with most views

&emsp;&emsp; author: authors list sorted by views

&emsp;&emsp; error: days when more than 1% of requests led to errors

e.g.
```
python run.py author article error
```
