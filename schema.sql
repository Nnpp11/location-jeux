DROP TABLE IF EXISTS reservations;

CREATE TABLE reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    client TEXT NOT NULL,
    jeu_id INTEGER NOT NULL,
    commentaire TEXT,
    FOREIGN KEY (jeu_id) REFERENCES wp_louables(id)
);