
#### Start Service MongoDB

Command:
```
mongod --config=/etc/mongod.conf
```

#### Stop Service MongoDB

Query:
```
use admin
db.shutdownServer();
```

#### Add User MongoDB

Query:
```
use <dbname>
db.createUser({user: "<username>", pwd: "<password>", roles:[{role: "dbAdmin", db:"<dbname>"}]})
```
