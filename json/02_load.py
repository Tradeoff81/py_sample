import json
import pprint

with open('01_test.json', 'r') as f:
    obj = json.load(f);

    print('load : ', end='');
    pprint.pprint(obj);
