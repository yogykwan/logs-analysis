import sys
import psycopg2


def execute(clause):
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(clause)
    res = cursor.fetchall()
    db.close()
    return res


def get_top3_articles():
    res = execute("""
        select * from article_log_view
        order by views desc
        limit 3;
        """)
    print "\n\nTop 3 articles with most views:"
    print '%-35s %9s' % ('article', 'views')
    print '\n'.join(['%-35s %9s' % x for x in res])


def get_sorted_authors():
    res = execute("""
        select name, views from author_log_view, authors
        where author_log_view.author = authors.id
        order by views desc;
        """)
    print "\n\nAuthors list sorted by views:"
    print '%-35s %9s' % ('author', 'views')
    print '\n'.join(['%-35s %9s' % x for x in res])


def get_error_days():
    res = execute("""
        select day_total_view.day,
        round(error::numeric/total::numeric, 2) as error_rate
        from day_total_view, day_error_view
        where (day_total_view.day = day_error_view.day)
        and (error > total * 0.01);
        """)
    print "\n\nDays when more than 1% of requests led to errors:"
    print '%-35s %9s' % ('day', 'error rate')
    print '\n'.join(['%-35s %9s' % x for x in res])


if __name__ == '__main__':
    for type in sys.argv:
        if type == 'article':
            get_top3_articles()
        elif type == 'author':
            get_sorted_authors()
        elif type == 'error':
            get_error_days()
