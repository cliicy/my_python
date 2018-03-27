from pymongo import MongoClient
import confInfo
import pprint

uri="mongodb://"+confInfo.server+':'+confInfo.port+'/'+confInfo.db_name

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

cities={
    '台北':20140918,
    '台南': 20140921,
    '台中': 20140924,
    '花莲': 20140927
}

places = {
    '台北动物园': '捷运',
    '清静农场': '大巴',
    '野柳地质公园': '包车',
    '九份': '包车'
}

TaiWan={
    'cities': ['台北', '台中', '台南', '花莲'],
    'expenditures': '12000rmb',
    'travelers': ['罗', '礼礼', '郭敏', '敉敉'],
}

if __name__ == '__main__':
    client=MongoClient(uri)
    dbname=client.travel

    print("Do you want to delete the old traveldb? Please input Y|N?")
    aIn=input()
    if (aIn.lower()== 'y'):
        print("The old traveldb will be deleted! And the new traveldb will be created later")
        client.drop_database(dbname)

    country=dbname.contries
    resort=dbname.resort

    country_id = country.insert(TaiWan)
    resort_id = resort.insert(places)

    print('This is my first step to start travel aboard!')
    print('country_id= ', country_id, '\n')
    print('resort_id= ', resort_id, '\n' )

    counters=country.find()
#    finders=country.find({'expenditures': '{$regex:/rmb$/}'})
#    ct=country.find_one({'expenditures': '12000rmb'})
#    ct=country.find_one()
    for count in country.find():
        pprint.pprint(count)
#    pprint.pprint(ct)
#    print("去过的国家：", ct,'\n')
#    print("去过的景点：", resort)

