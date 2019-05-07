from sqlite3 import connect
from contextlib import contextmanager


# class contextmanager(object):
#     def __init__(self, gen):
#         self.gen = gen
#
#     def __call__(self, *args, **kwargs):
#         self.args, self.kwargs = args, kwargs
#         return self
#
#     def __enter__(self):
#         print "__enter__"
#         self.gen_instance = self.gen(*self.args, **self.kwargs)
#         next(self.gen_instance)
#     def __exit__(self, *args):
#         print "__exit__"
#         next(self.gen_instance, None)

@contextmanager
def temptable(cur):
    print "calling temptable 1"
    cur.execute('create table points(x int, y int)')
    yield
    print "calling temptable 2"
    cur.execute("drop table points")


# temptable = context_manager(temptable)

with connect("test.db") as conn:
    curs = conn.cursor()
    with temptable(curs):
        curs.execute('insert into points values(1,1)')
        curs.execute('insert into points values(1,2)')
        curs.execute('insert into points values(2,1)')

        for row in curs.execute('select x,y from points'):
            print row

        for row in curs.execute('select sum(x * y) from points'):
            print row
