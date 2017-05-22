import json

book1 = {
    'name' : 'Python Basic',
    'pub' : 'MyHome',
    'isbn' : '111-11111-111',
    'price' : '10000'
};

#바이트 타입으로 화면에 출력
print(json.dumps(book1));

#텍스트 타입으로 파일로 저장
with open('01_test.json', 'w') as f:
    json.dump(book1, f);
