import sqlite3

def init_db():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    
    # Tabela de reservas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_usuario TEXT NOT NULL,
            laboratorio TEXT NOT NULL,
            data TEXT NOT NULL,
            horario_inicio TEXT NOT NULL,
            horario_fim TEXT NOT NULL
        )
    ''')

    # Tabela de usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    init_db()
