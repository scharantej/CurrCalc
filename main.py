
# Import required libraries
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def home():
  # Render the convert.html template
  return render_template('convert.html')

# Define the route for converting USD to SGD
@app.route('/convert', methods=['POST'])
def convert():
  # Get the USD amount from the form
  usd_amount = float(request.form['usd_amount'])

  # Perform the conversion to SGD based on the current exchange rate
  sgd_amount = usd_amount * 1.35

  # Return the converted SGD amount to convert.html for display
  return render_template('convert.html', sgd_amount=sgd_amount)

# Run the Flask app
app.run(debug=True)
