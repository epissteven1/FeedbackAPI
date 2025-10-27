from flask import Flask, request, jsonify
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

app = Flask(__name__)

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL = "stevenepis9@gmail.com" 

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.json
    message = data.get('message')
    rating = data.get('rating')

    if not message:
        return jsonify({"error": "Feedback message required"}), 400

    try:
        email = Mail(
            from_email=SENDER_EMAIL,
            to_emails="lykzellemaepadasas@gmail.com", 
            subject="New Feedback Received",
            plain_text_content=f"Message: {message}\nRating: {rating}"
        )

        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(email)

        return jsonify({"status": "success", "message": "Feedback sent successfully!"}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route('/')
def index():
    return "Flask Feedback API is running! Use POST /feedback to send feedback."


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
