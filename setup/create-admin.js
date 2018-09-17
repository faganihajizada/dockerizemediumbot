db.createUser(
{
    user: "superadmin",
    pwd: "super123",
    roles: [
       "userAdminAnyDatabase", "readWriteAnyDatabase", "dbAdminAnyDatabase", "clusterAdmin"
    ]
});
