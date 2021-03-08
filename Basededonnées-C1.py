# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="student",
  password="pswd",
  database="agence_location"

)

mycursor = mydb.cursor()

sql = "DELETE FROM Commune WHERE distance_de_agence= 150"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

"""mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE agence_location")

mycursor.execute("CREATE TABLE Sexe (sexe VARCHAR(40) PRIMARY KEY, civilite VARCHAR(40) NOT NULL)")

mycursor.execute("CREATE TABLE Client (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(40) NOT NULL, nombre_contrat INT, prenom VARCHAR(40) NOT NULL, sexe VARCHAR(40), FOREIGN KEY(sexe) REFERENCES Sexe(sexe))") 

mycursor.execute("CREATE TABLE Telephone (telephone VARCHAR(20) NOT NULL PRIMARY KEY, client_id INT, FOREIGN KEY(client_id) REFERENCES Client(id))")

mycursor.execute("CREATE TABLE Commune (id INT AUTO_INCREMENT PRIMARY KEY,  nom VARCHAR(40) NOT NULL, nombre_habitant INT NOT NULL, distance_de_agence INT)")

mycursor.execute("CREATE TABLE Logement (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, type_de_logement VARCHAR(40) NOT NULL, loyer INT, superficie INT, quartier VARCHAR(40) NOT NULL, adresse VARCHAR(100), commune_id INT, FOREIGN KEY(commune_id) REFERENCES Commune(id))") 

mycursor.execute("CREATE TABLE Contrat (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, debut_contrat DATE NOT NULL, fin_contrat DATE, client_id INT, logement_id INT, FOREIGN KEY(logement_id) REFERENCES Logement(id), FOREIGN KEY(client_id) REFERENCES Client(id))") 


sql = "INSERT INTO Sexe (sexe, civilite) VALUES (%s, %s)"
val = [('M', 'Monsieur'), ('F', 'Madame')]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


sql = "INSERT INTO Client(nom, prenom, sexe, nombre_de_contrat) VALUES (%s, %s, %s, %s)"
val = [('Sauer', 'Camille', 'F', 1), ('Devic', 'John', 'M', 2), ('Stokowic', 'Fred', 'M', 1),('Dupontel', 'Albert', 'M', 2),('Rubic', 'Ana', 'F', 3)]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


sql = "INSERT INTO Telephone (telephone, client_id) VALUES (%s, %s)"
val = [('0640975449', 1), ('0679458361', 2), ('0654875452', 3), ('0698764479', 4), ('0640974199', 5)]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")



sql = "INSERT INTO  Logement (type_de_logement, loyer, superficie, quartier, adresse) VALUES (%s, %s, %s, %s, %s)"
val=[('appartement', 480, 28, 'Lambersart', '38 rue de la paix'), ('Villa', 2800, 250, 'Saint-john', '454 street stefan zweig'), ('Cabane', 10, 120, 'République', '3 rue de la feria'), ('Studio', 23, 358, 'Mitterie-centre', '25 issue de la contrebande'), ('appartement', 48, 590, 'Bonne-nouvelle', '48 rue de la pace')]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO  Commune (nom, nombre_habitant, distance_de_agence) VALUES (%s, %s, %s)"
val=('Deauville', 7899, 200), ('Mitterie', 2403, 25), ('Roubaix', 11123, 65), ('Bruxelles', 38759, 384);

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO  Commune (nom, nombre_habitant, distance_de_agence) VALUES (%s, %s, %s)"
val=[('Beffroy', 7893, 150)]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

sql = "INSERT INTO  Contrat(logement_id, client_id, debut_contrat, fin_contrat) VALUES (%s, %s, %s, %s)"
val=[(2, 1, '2003/01/22', '2004/01/24'), (3, 3, '2003/01/22', '2006/01/17'), (4, 1, '2000/03/12', '2003/01/22'), (2, 4, '2001/01/02', '2003/01/22'), (1, 1, '2002/05/19', '2003/01/22')]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")



sql = "UPDATE Client SET nom = 'Strassey' WHERE nom = 'Rubic'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 



sql = "UPDATE Contrat SET fin_contrat = '2004/01/10' WHERE fin_contrat = '2004/01/24'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 



sql = "UPDATE Commune SET nom = 'Beffroy' WHERE nom = 'Westminster'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 


sql = "UPDATE Logement SET type_de_logement = 'Cabane' WHERE type_de_logement = 'Bengalow'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 


sql = "UPDATE Telephone SET Telephone = '0607163069' WHERE telephone = '0640975449'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 


sql = "DELETE FROM Commune WHERE distance_de_agence= 150"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

"""
