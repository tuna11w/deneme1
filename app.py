from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def giris():
    hata = ""
    if request.method == "POST":
        kullanici = request.form.get("kullanici")
        sifre    = request.form.get("sifre")

        if kullanici == "admin" and sifre == "1234":
            # Giriş başarılı → /surprise sayfasına yönlendir
            return redirect(url_for("surprise"))
        else:
            hata = "Hatalı kullanıcı adı veya şifre"

    return render_template("index.html", hata=hata)

# Yeni rota: sürpriz sayfası
@app.route("/surprise")
def surprise():
    # surprise.html'ini render et
    return render_template("surprise.html")

if __name__ == "__main__":
    app.run(debug=True)