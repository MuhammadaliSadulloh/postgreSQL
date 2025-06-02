import sqlite3

def create_tables():

    conn = sqlite3.connect('factory.db')
    cursor = conn.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Korpuslar (
        ID INTEGER PRIMARY KEY,
        Korpus TEXT NOT NULL
    )
    ''')


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Qurilmalar (
        ID INTEGER PRIMARY KEY,
        Korpuslar_ID INTEGER,
        Qurilma TEXT NOT NULL,
        FOREIGN KEY (Korpuslar_ID) REFERENCES Korpuslar(ID)
    )
    ''')


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Maxsulot (
        ID INTEGER PRIMARY KEY,
        Qurilma_ID INTEGER,
        Korpus_ID INTEGER,
        Maxsulot TEXT NOT NULL,
        FOREIGN KEY (Qurilma_ID) REFERENCES Qurilmalar(ID),
        FOREIGN KEY (Korpus_ID) REFERENCES Korpuslar(ID)
    )
    ''')


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS MXKB (
        ID INTEGER PRIMARY KEY,
        Maxsulot_ID INTEGER,
        MXKB TEXT NOT NULL,
        FOREIGN KEY (Maxsulot_ID) REFERENCES Maxsulot(ID)
    )
    ''')


    korpuslar_data = [
        (1, 'Maydalash korpusi'),
        (2, 'Yanchish korpusi'),
        (3, 'Flotatsiya korpusi'),
        (4, "Quritish va quyish korpusi")
    ]
    cursor.executemany('INSERT OR REPLACE INTO Korpuslar VALUES (?,?)', korpuslar_data)


    qurilmalar_data = [
        (1, 1, "Jag'li maydalagich"),
        (2, 1, 'Konusli maydalagich'),
        (3, 1, 'galvir'),
        (4, 2, 'Sharli tegirmon'),
        (5, 2, 'Barabanli tegirmon'),
        (6, 3, 'Flotatsion mashina'),
        (7, 4, 'Pech')
    ]
    cursor.executemany('INSERT OR REPLACE INTO Qurilmalar VALUES (?,?,?)', qurilmalar_data)


    maxsulot_data = [
        (1, 7, 4, 'Oltin'),
        (2, 6, 3, 'Kumush kukuni'),
        (3, 6, 3, 'Boshqalar'),
        (4, 6, 3, 'Mis kukuni')
    ]
    cursor.executemany('INSERT OR REPLACE INTO Maxsulot VALUES (?,?,?,?)', maxsulot_data)


    mxkb_data = [
        (1, 1, 'Marjonbuloq ochiq koni'),
        (2, 2, 'Marjonbuloq ochiq koni'),
        (3, 3, 'Marjonbuloq ochiq koni'),
        (4, 4, 'Marjonbuloq ochiq koni')
    ]
    cursor.executemany('INSERT OR REPLACE INTO MXKB VALUES (?,?,?)', mxkb_data)


    conn.commit()


    def show_table(table_name):
        print(f"\n{table_name} jadvali:")
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        for row in rows:
            print(row)


    show_table("Korpuslar")
    show_table("Qurilmalar")
    show_table("Maxsulot")
    show_table("MXKB")

    # Bog'lanishni yopish
    conn.close()

if __name__ == "__main__":
    create_tables()