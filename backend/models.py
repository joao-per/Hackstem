userTable = '''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                avatar_id INTEGER NOT NULL,
                FOREIGN KEY (avatar_id) REFERENCES avatar (id)
            )
        '''

userTokenTable = '''
            CREATE TABLE IF NOT EXISTS user_token (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                token TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user (id)
            )
        '''
avatarTable = '''
            CREATE TABLE IF NOT EXISTS avatar (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hats_id INTEGER NOT NULL,
                shirt_id INTEGER NOT NULL,
                pants_id INTEGER NOT NULL,
                FOREIGN KEY (hats_id) REFERENCES hatsTable (id),
                FOREIGN KEY (shirt_id) REFERENCES shirtTable (id),
                FOREIGN KEY (pants_id) REFERENCES pantsTable (id)
            )
        '''

hatsTable = '''
            CREATE TABLE IF NOT EXISTS hat (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            '''

shirtTable = '''
            CREATE TABLE IF NOT EXISTS shirt (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            '''

pantsTable = '''
            CREATE TABLE IF NOT EXISTS pant (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        '''

