db.createUser(
{
    user: "teluser",
    pwd: "tel123",
    roles: [
      { role: "readWrite", db: "telegram" }
    ]
});
