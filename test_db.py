import psycopg2

url = None
with open(".env") as f:
    for line in f:
        if line.startswith("DATABASE_URL="):
            url = line.split("=", 1)[1].strip()

conn = psycopg2.connect(url, connect_timeout=5)
print("Connected. Server version:", conn.server_version)
conn.close()