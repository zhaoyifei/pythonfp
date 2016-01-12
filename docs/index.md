
db.getCollection('orders').ensureIndex({"createdAt": -1})
db.getCollection('orders').ensureIndex({"statisticsUpdatedAt": -1})

db.getCollection('doctors').ensureIndex({"createdAt": -1})
db.getCollection('doctors').ensureIndex({"statisticsUpdatedAt": -1})

db.getCollection('users').ensureIndex({"createdAt": -1})
db.getCollection('users').ensureIndex({"statisticsUpdatedAt": -1})

db.getCollection('reports').ensureIndex({"createdAt": -1})
db.getCollection('reports').ensureIndex({"statisticsUpdatedAt": -1})

python setup.py install