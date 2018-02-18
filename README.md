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

## Synopsis
1. use postgresql as db and load from newsdata.sql
2. `pip install psycopg2-binary` to use [psycopy2](http://initd.org/psycopg/docs/install.html#binary-install-from-pypi)
3. execute specific sql clauses based on sys.argv
4. `psql -d news` then create postgresql views

## Views
1. article_log_view
```
CREATE OR REPLACE VIEW article_log_view AS
SELECT title, COUNT(log.id) AS views
FROM articles, log
WHERE articles.slug = SUBSTRING(log.path FROM 10)
GROUP BY title;
```

2. author_log_view
```
CREATE OR REPLACE VIEW author_log_view AS
SELECT author, COUNT(log.id) AS views
FROM articles, log
WHERE articles.slug = SUBSTRING(log.path FROM 10)
GROUP BY author;
```

3. day_total_view
```
CREATE OR REPLACE VIEW day_total_view AS
SELECT TO_CHAR(time, 'YYYY-MM-DD') AS day, COUNT(log.id) AS total
FROM log
GROUP BY day;
```

4. day_error_view
```
CREATE OR REPLACE VIEW day_error_view AS
SELECT TO_CHAR(time, 'YYYY-MM-DD') AS day, COUNT(log.id) AS error
FROM log
WHERE status != '200 OK'
GROUP BY day;
```
