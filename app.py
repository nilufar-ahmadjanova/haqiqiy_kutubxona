from flask import Flask, render_template

app = Flask(__name__)

# Kutubxonadagi kitoblar ro'yxati (namuna)
kitoblar_royxati = [
    {"nomi": "O'tkan kunlar", "muallif": "Abdulla Qodiriy", "yil": 1925},
    {"nomi": "Shaytanat", "muallif": "Tohir Malik", "yil": 1992},
    {"nomi": "Alkimyogar", "muallif": "Paulo Koelyo", "yil": 1988}
]

@app.route('/')
def asosiy_sahifa():
    # HTML faylga kitoblar ro'yxatini yuboramiz
    return render_template('index.html', kitoblar=kitoblar_royxati)

if __name__ == '__main__':
    app.run(debug=True)