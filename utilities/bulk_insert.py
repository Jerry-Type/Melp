import psycopg2
import pandas as pd
from urllib.parse import urlparse


username = ""
password = ""
database = ""
hostname = ""

connection = psycopg2.connect(
    database = database,
    user = username,
    password = password,
    host = hostname
)

cursor = connection.cursor()

#final_row = "('edb50561-46f9-4541-9c04-8de82401cc13',4,'Pedraza - Niño','http://josé eduardo.gob.mx','Irene_Rojas95@nearbpo.com','537 531 201','207 Chavarría Lado','Franciscohaven','Baja California Norte',19.4426838205224,-99.1250245928884,'(-99.1250245928884,19.4426838205224)')"

data = pd.read_csv("raw_data/restaurantes.csv")
names_columns = ['id', 'rating', 'name', 'site', 'email', 'phone', 'street', 'city', 'state', 'lat', 'lng']
name_colums_no_edit = ['rating','lat', 'lng']
for index, row in data.iterrows():
	val_row_insert= []
	for name_col in names_columns:
		if name_col not in name_colums_no_edit:
			val_row_insert.append("'"+row[name_col]+"'")
		else:
			val_row_insert.append(str(row[name_col]))
	row_to_insert = "("+','.join(val_row_insert)+")"
	cursor.execute("INSERT INTO melp.restaurants VALUES " + row_to_insert) 

print("Completed")

connection.commit()
cursor.close()
