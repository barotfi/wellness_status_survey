from sqlalchemy.dialects import registry

# Check if the dialect is registered
print(registry.load("sqlite.pysqlitecloud"))
