user_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        userId SERIAL PRIMARY KEY,
        username VARCHAR(45) UNIQUE NOT NULL,
        email VARCHAR,
        signUpData TIMESTAMP
    );
    '''

tasks_table_query = '''
    CREATE TABLE IF NOT EXISTS tasks (
        taskId SERIAL PRIMARY KEY,
        userId INTEGER UNIQUE NOT NULL,
        dateCreated TIMESTAMP,
        dateModified TIMESTAMP,
        title TEXT,
        parent TEXT,
        isDone BOOLEAN,
        editedCount INTEGER,
        isDeleted BOOLEAN,
        FOREIGN KEY (userId) REFERENCES "users"(userId) ON DELETE CASCADE
);
    '''

archived_tasks_table_query = '''
    CREATE TABLE IF NOT EXISTS archived_tasks (
        taskId SERIAL PRIMARY KEY,
        userId INTEGER UNIQUE NOT NULL,
        dateCreated TIMESTAMP,
        dateModified TIMESTAMP,
        title TEXT,
        parent TEXT,
        isDone BOOLEAN,
        editedCount INTEGER,
        isDeleted BOOLEAN,        
        
        FOREIGN KEY (userId) REFERENCES "users"(userId) ON DELETE CASCADE

);
    '''

create_tables_queries = [user_table_query,
                         tasks_table_query, archived_tasks_table_query]
