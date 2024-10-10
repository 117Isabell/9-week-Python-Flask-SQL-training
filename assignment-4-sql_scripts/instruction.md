graph TD;
    config[config.py stores credentials] -->|import the credentials| app[Python App: sql_connection_1];
    app -->|Calls| db[MySQL Database];
    db -->|Returns data| app;
