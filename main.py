from flask import Flask, request, jsonify

app = Flask(__name__)

data = []


@app.route("/")
def entry_point():
    welcome_message = (
        "<div style='font-family: Arial, sans-serif; text-align: center;'>"
        "<h1>Technical Assignment 1 - SIC Batch 5</h1>"
        "<hr>"
        "<h2>Selamat Datang di API Kelompok 24 SIC Batch 5</h2>"
        "<p>Anggota Kelompok 24:</p>"
        "<ul style='list-style-type: none;'>"
        "<li>1. Ginanjar Aditiya Prianata</li>"
        "<li>2. Indri Windriasari</li>"
        "<li>3. Ali Astra Mikail</li>"
        "<li>4. Prayoga Setiawan</li>"
        "</ul>"
        "<p>API ini dirancang untuk menyimpan dan mengakses data suhu dan kelembapan yang dikirimkan oleh sensor DHT22.</p>"
        "<h3>Instruksi Penggunaan:</h3>"
        "<ol style='text-align: left; display: inline-block; margin: 0 auto;'>"
        "<li>Clone atau download kode dari repository ke lokal Anda.</li>"
        "<li>Jalankan <code>app.py</code> menggunakan VSCode atau editor pilihan Anda.</li>"
        "<li>Buka Repl.it dan upload kode <code>app.py</code> untuk menjalankan Flask server secara online.</li>"
        "<li>Catat URL server yang muncul di terminal Repl.it setelah server berjalan.</li>"
        "<li>Buka Wokwi, buat proyek baru untuk ESP32, dan tambahkan kode <code>sic_ta1.ino</code>.</li>"
        "<li>Setel variabel <code>server_url</code> pada file <code>sic_ta1.ino</code> ke URL server yang muncul di Repl.it.</li>"
        "<li>Jalankan simulasi Wokwi untuk ESP32 dan pastikan perangkat terhubung ke jaringan.</li>"
        "<li>Cek serial monitor di Wokwi untuk memastikan tidak ada error dan semuanya telah terkoneksi dengan baik.</li>"
        "<li>Untuk melihat hasil, gunakan endpoint <code>'your-server-url:port/sensor/data'</code> pada browser atau Postman.</li>"
        "</ol>"
        "<p>Technical Assignment 1 - SIC Batch 5 ini menggunakan Wokwi sebagai simulator kit ESP32, Flask sebagai backend, dan Repl.it sebagai hosting.</p>"
        "</div>"
        "<hr>"
        "<footer style='font-family: Arial, sans-serif; text-align: center;'>"
        "API dan .ino file ini adalah versi saya Ginanjar Aditiya Prianata"
        "</footer>")
    return welcome_message


@app.route("/sensor/data", methods=["POST"])
def post_data():
    json_data = request.get_json()
    temperature = json_data.get("temperature")
    humidity = json_data.get("humidity")

    subData = {"temperature": temperature, "humidity": humidity}
    data.append(subData)
    return 'berhasil disimpan ke server', 201


@app.route("/sensor/data", methods=["GET"])
def get_data():
    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
