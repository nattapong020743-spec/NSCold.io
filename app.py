import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/scenery')
def scenery():
    return render_template('scenery.html')

@app.route('/sustainability')
def sustainability():
    return render_template('sustainability.html')

@app.route('/energy-detail')
def energy_detail():
    return render_template('energy-detail.html')

@app.route('/energy-report')
def energy_report():
    return render_template('energy-report.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')

@app.route('/fanpage')
def fanpage():
    return render_template('fanpage.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/service-freeze')
def service_freeze():
    return render_template('service-freeze.html')

@app.route('/service-finished-goods')
def service_finished_goods():
    return render_template('service-finished-goods.html')

@app.route('/service-raw-materials')
def service_raw_materials():
    return render_template('service-raw-materials.html')

@app.route('/delivery-finished-goods')
def delivery_finished_goods():
    return render_template('delivery-finished-goods.html')

@app.route('/delivery-raw-materials')
def delivery_raw_materials():
    return render_template('delivery-raw-materials.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

if __name__ == '__main__':
    # ดึงค่าพอร์ตจากระบบ (ถ้ามี) หรือใช้ 5000 เป็นค่าเริ่มต้น
    port = int(os.environ.get('PORT', 5000))
    is_debug = os.environ.get('DEBUG', 'FALSE').upper() == 'TRUE'
    
    # เปิดโหมดให้รองรับการเชื่อมต่อผ่านวง Wi-Fi ด้วย (host='0.0.0.0')
    app.run(host='0.0.0.0', port=port, debug=is_debug)