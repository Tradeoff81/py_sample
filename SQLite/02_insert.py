import sqlite3

conn = sqlite3.connect('test.db');

querySingleIn = '''
    INSERT INTO
        book
    VALUES
    (
         "book1"
        ,"pub1"
        ,"111-11111-111"
        ,11000
    )
    ''';

queryMultiIn = '''
    INSERT INTO
        book
    VALUES
    (?,?,?,?)
    ''';

c = conn.cursor();

c.execute(querySingleIn);

c.execute(queryMultiIn, ('book2','pub2','222-22222-222', 12000));

bookdata = [
    ('book3','pub3','333-33333-333', 13000),
    ('book4','pub4','444-44444-444', 14000),
    ('book5','pub5','555-55555-555', 15000)
]

c.executemany(queryMultiIn, bookdata);

c.close();
conn.commit();
