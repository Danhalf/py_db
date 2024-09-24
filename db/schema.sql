CREATE TABLE IF NOT EXISTS tech (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    number TEXT,
    owner TEXT,
    status TEXT,
    notes TEXT
);