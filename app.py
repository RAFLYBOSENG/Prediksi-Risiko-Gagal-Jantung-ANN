import os
from flask import Flask, render_template

# --- Konfigurasi Flask dengan path absolut ---
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    __name__,
    static_folder=os.path.join(basedir, 'static'),
    template_folder=os.path.join(basedir, 'templates')
)


@app.route('/')
def home():
    """Merender halaman utama yang menampilkan semua visualisasi hasil ANN."""
    return render_template('index.html')


@app.route('/debug')
def debug():
    """Route debug untuk mengecek apakah file gambar dapat diakses."""
    static_path = app.static_folder
    files = os.listdir(static_path) if os.path.exists(static_path) else []
    return f"""
    <h1>Debug Info</h1>
    <p>Static folder path: {static_path}</p>
    <p>Files in static folder: {files}</p>
    """


if __name__ == "__main__":
    print(f"Static folder: {app.static_folder}")
    print(f"Template folder: {app.template_folder}")
    app.run(debug=True, host='127.0.0.1', port=5000)
