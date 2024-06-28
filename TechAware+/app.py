from flask import Flask, render_template, request, url_for
import random
import string

app = Flask(__name__)

facts_list = [
    "Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.",
    "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.",
    "Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.",
    "2019'da yapılan bir araştırmaya göre, insanların %60'ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.",
    "Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.",
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
    "Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.",
    "Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız."
]

@app.route('/')
def index():
    fact = random.choice(facts_list)
    return render_template('index.html', fact=fact)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/resource1')
def resource1():
    return render_template('resource1.html')

@app.route('/resource2')
def resource2():
    return render_template('resource2.html')

@app.route('/resource3')
def resource3():
    return render_template('resource3.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return render_template('contact.html', success=True, name=name)
    return render_template('contact.html')

@app.route('/yazi-tura')
def yazi_tura():
    result = random.choice(['Yazı', 'Tura'])
    return render_template('yazi-tura.html', result=result)

@app.route('/sifre-olustur')
def sifre_olustur():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(12))
    return render_template('sifre-olustur.html', password=password)

@app.route('/rastgele-resim')
def rastgele_resim():
    image_urls = [
        url_for('static', filename='images/teknoloji-bagimliligi.jfif'),
        'https://via.placeholder.com/300.png/09f/fff', 
        'https://via.placeholder.com/300.png/0bf/fff', 
        'https://via.placeholder.com/300.png/0cf/fff'
    ]
    image_url = random.choice(image_urls)
    return render_template('rastgele-resim.html', image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
