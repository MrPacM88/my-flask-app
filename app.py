# Імпортуємо потрібні бібліотеки з Flask
from flask import Flask, render_template, request
import requests  # Потрібна для відправки повідомлень у Telegram

# Створюю об'єкт Flask — наш веб-сервер
app = Flask(__name__)
app.secret_key = 'ybrjfkq'  # Секретний ключ для сесій (потрібен, якщо я будеш працювати з логінами, формами тощо)

# 🔑 Telegram токен і chat_id (сюди відправляються замовлення)
TOKEN = '7879788759:AAGYVSvPq-Um0LKZQvUo878D94WtjhObmRw'  # Токен бота Telegram
CHAT_ID = '-4957404305'  # ID чату групи, куди надсилається повідомлення

# 📩 Функція для надсилання повідомлення у Telegram
def send_telegram_message(name, email, message):
    # Формуємо текст повідомлення
    text = f"Нове замовлення:\nІм'я: {name}\nEmail: {email}\nПовідомлення: {message}"
    # Формуємо URL для API-запиту до Telegram
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    # Параметри запиту
    payload = {'chat_id': CHAT_ID, 'text': text}
    # Відправляємо POST-запит
    requests.post(url, data=payload)

# 📄 Маршрут для головної сторінки
@app.route('/')
def home():
    return render_template('index.html')  # Відображає index.html

# 📄 Маршрут для сторінки FAQ (about)
@app.route('/about')
def about():
    return render_template('FAQ.html')  # Відображає FAQ.html

# 📄 Маршрут для сторінки замовлення
@app.route('/order')
def order():
    return render_template('order.html')  # Відображає order.html

#Маршрут на прайс
@app.route('/suma')
def suma():
    return render_template('suma.html')

# Муршрут контакти
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')  # Відображає contacts.html

# 📤 Обробник POST-запиту з форми замовлення
@app.route('/submit-order', methods=['POST'])
def submit_order():
    # Отримуємо дані з форми
    name = request.form.get('name')
    email = request.form.get('email')
    details = request.form.get('details')

    # Викликаємо функцію для надсилання повідомлення в Telegram
    send_telegram_message(name, email, details)

    # Після успішного надсилання, показує сторінку успішного замовлення
    return render_template('success.html')

# 🚀 Запускаємо сервер, якщо цей файл виконується напряму
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False)
