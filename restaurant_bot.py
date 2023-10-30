from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Get the incoming message from the request
    incoming_message = request.values.get("Body", "").lower()
    
    # If the message is a food order, respond with a confirmation message
    if "order" in incoming_message:
        response_message = "Thank you for your order! We'll get it ready as soon as possible."
    else:
        response_message = "Welcome to our restaurant! How can we help you today?"
    
    # Create a new TwiML response object
    twiml_response = MessagingResponse()
    twiml_response.message(response_message)
    
    # Return the TwiML response as a string
    return str(twiml_response)

if __name__ == "__main__":
    app.run(debug=True)
