db.createUser(
  {
    user: "root",
    pwd: "mongo",
    roles: ["root"]
  }
)

db.createUser(
  {
    user: 'mongo',
    pwd: 'mongo',
    roles: ['readWriteAnyDatabase', 'userAdminAnyDatabase', 'dbAdminAnyDatabase']
  }
)

db.createUser(
  {
    user: 'mongo',
    pwd: 'mongo',
    roles: ['readWrite', 'dbAdmin']
  }
)

db.createUser(
  {
    user: "index",
    pwd: "Index^20204BudsHome",
    roles: [
      {
        role: "dbAdmin",
        db: "budshome-index"
      },
      {
        role: "readWrite",
        db: "budshome-index"
      }
    ]
  }
)
