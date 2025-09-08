from flask import Flask, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'lykzellemaepadasas@gmail.com'      
app.config['MAIL_PASSWORD'] = 'mwbn xtti gqqk mwew'         
app.config['MAIL_DEFAULT_SENDER'] = 'lykzellemaepadasas@gmail.com'

mail = Mail(app)

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    message = data.get('message')
    rating = data.get('rating')

    if not message:
        return jsonify({"error": "Feedback message required"}), 400

    try:
        # Send email
        msg = Message("New Feedback Received", recipients=["lykzellemaepadasas@gmail.com"])
        msg.body = f"Message: {message}\nRating: {rating}"
        mail.send(msg)

        return jsonify({"status": "success", "message": "Feedback sent!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
