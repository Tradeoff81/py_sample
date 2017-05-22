import sqlite3

conn = sqlite3.connect('test.db');

query = '''
    SELECT * FROM book
    ''';

c = conn.cursor();
c.execute(query);

# 조회 데이터 중 처음 1개
print(c.fetchone());

for s in c.fetchmany(5):
    print(s);

for s in c.fetchall():
    print(s);

c.close();
