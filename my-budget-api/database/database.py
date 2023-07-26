import sqlite3

# try:
#     conn = sqlite3.connect('my_budget.db')
#     cur = conn.cursor()
#     print('la base de données est connecté a SQLite')
#     sql = 'SELECT sqlite_version()'
#     cur.execute(sql)
#     res = cur.fetchall()
#     print('la version de SQLite est : ', res)
#     cur.close()
#     conn.close()
#     print('la connexion est fermée')
# except sqlite3.Error as error:
#     print('erreur lors de la connextion', error)

# ~~~~~~~~~~ nouvelle table ~~~~~~~~~~~~

# try:
#     conn = sqlite3.connect('my_budget.db')
#     cur = conn.cursor()
#     print('la base de données est connecté a SQLite')
#     sql = '''
#         CREATE TABLE mon_compte(
#         id INTEGER PRIMARY KEY,
#         revenu DOUBLE,
#         depenses_fixes DOUBLE,
#         imprevue DOUBLE,
#         reste DOUBLE
#         )
#     '''
#     cur.execute(sql)
#     conn.commit()
#     print('table crée')
#     cur.close()
#     conn.close()
#     print('la connexion est fermée')
# except sqlite3.Error as error:
#     print('erreur', error)

# try:
#     conn = sqlite3.connect('my_budget.db')
#     cur = conn.cursor()
#     print('la base de données est connecté a SQLite')
#     sql = '''
#         CREATE TABLE mon_epargne(
#         id INTEGER PRIMARY KEY,
#         loisir DOUBLE,
#         vacances DOUBLE,
#         travaux DOUBLE
#         )
#     '''
#     cur.execute(sql)
#     conn.commit()
#     print('table crée')
#     cur.close()
#     conn.close()
#     print('la connexion est fermée')
# except sqlite3.Error as error:
#     print('erreur', error)


# try:
#     conn = sqlite3.connect('my_budget.db')
#     cur = conn.cursor()
#     print('la base de données est connecté a SQLite')
#     sql = '''
#         CREATE TABLE bonus(
#         id INTEGER PRIMARY KEY,
#         bonus DOUBLE
#         )
#     '''
#     cur.execute(sql)
#     conn.commit()
#     print('table crée')
#     cur.close()
#     conn.close()
#     print('la connexion est fermée')
# except sqlite3.Error as error:
#     print('erreur', error)

# ~~~~~~~~~ Insert ~~~~~~~~~~

# try:
#     conn = sqlite3.connect('my_budget.db')
#     cur = conn.cursor()
#     print('la base de données est connecté a SQLite')
#     sql = '''
#         INSERT INTO mon_compte(
#         revenu,
#         depenses_fixes,
#         imprevue,
#         reste)
#         VALUES(
#         2260.36,
#         975.66,
#         150.00,
#         1134.70
#         )
#     '''
#     cur.execute(sql)
#     conn.commit()
#     print('valeurs ajoutées')
#     cur.close()
#     conn.close()
#     print('la connexion est fermée')
# except sqlite3.Error as error:
#     print('erreur', error)

# ~~~~~~~~~~~SELECT ~~~~~~~~~~

try:
    conn = sqlite3.connect('my_budget.db')
    cur = conn.cursor()
    print('la base de données est connecté a SQLite')
    sql = '''SELECT * FROM mon_compte'''
    cur.execute(sql)
    res = cur.fetchall()
    for row in res: 
        print('id: ', row[0])
        print('revenu: ', row[1])
        print('depenses fixes: ', row[2])
        print('imprévus: ', row[3])
        print('reste: ', row[4])
    conn.commit()
    cur.close()
    conn.close()
    print('la connexion est fermée')
except sqlite3.Error as error:
    print('erreur', error)


    # res = cur.fetchall()
    # for row in res:
    #     print("id:",row[0])
    #     print("artist:",row[1])
    #     print("album_name:",row[2])
    #     print("published_year:",row[3])