import test46
import psycopg

print(psycopg.apilevel)
print(psycopg.__version__)

con = psycopg.connect(
  user="min", 
  password="12345", 
  host="127.0.0.1", 
  port="5432"
)

print("Database opened successfully")