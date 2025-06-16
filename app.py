from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('calendar.html')

@app.route('/api/reservations', methods=['GET'])
def get_reservations():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT r.id, r.date, r.client, r.commentaire, l.nom AS jeu_nom FROM reservations r JOIN wp_louables l ON r.jeu_id = l.id")
    data = cur.fetchall()
    conn.close()
    return jsonify([dict(row) for row in data])

@app.route('/api/reserve', methods=['POST'])
def reserve():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    for jeu_id in data['jeux']:
        cur.execute("INSERT INTO reservations (date, client, jeu_id, commentaire) VALUES (?, ?, ?, ?)",
                    (data['date'], data['client'], jeu_id, data['commentaire']))
    conn.commit()
    conn.close()
    return jsonify({'status': 'ok'})

@app.route('/api/jeux_disponibles/<date>', methods=['GET'])
def jeux_disponibles(date):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nom, stock FROM wp_louables WHERE disponible = 1")
    jeux = cur.fetchall()

    cur.execute("SELECT jeu_id, COUNT(*) as count FROM reservations WHERE date = ? GROUP BY jeu_id", (date,))
    reserves = {row['jeu_id']: row['count'] for row in cur.fetchall()}
    dispo = []
    for jeu in jeux:
        restant = jeu['stock'] - reserves.get(jeu['id'], 0)
        if restant > 0:
            dispo.append({'id': jeu['id'], 'nom': jeu['nom']})
    conn.close()
    return jsonify(dispo)

if __name__ == '__main__':
    app.run(debug=True)