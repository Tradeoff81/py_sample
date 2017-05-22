import sqlite3

conn = sqlite3.connect('test.db');

query = '''
    CREATE TABLE book
    (
        name text,
        pub text,
        isbn text,
        price integer
    )
    ''';

c = conn.cursor();
c.execute(query);
c.close();
