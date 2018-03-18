import pymongo

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}
if __name__ == '__main__':
    #client=pymongo.MongoClient(host='localhost',port=27017)
    client=pymongo.MongoClient('mongodb://localhost:27017/luotest')
#    db=client.mytest
#    collection = db.students
 #   result = collection.insert(student)
    resources = client.luotest.resources
    result = resources.insert(student)
    print(result)

    result = resources.find_one({'name': 'Jordan'})
    print(type(result))
    print(result)

    count = resources.find().count()
    print(count)

    sequence = client.luotest.sequence
    sequence.insert({"_id": "version", "seq": 1})
    seq = sequence.find_one({"_id": "version"})["seq"]
    sequence.update_one({"_id": "version"}, {"$inc": {"seq": 1}})
    post_data = {"_class": "com.gionee.smart.domain.entity.Resources", "version": seq, "path": 'c:\Program',
                 "content": 'z786', "status": "enable", "operation": '+',
                 "createtime": '2018/3/18'}
    resources.insert(post_data)