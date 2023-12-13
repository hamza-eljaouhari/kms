from flask import Flask, render_template, request, redirect, url_for, flash
from simple_kms import SimpleKMS  # Import your SimpleKMS class

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for message flashing
kms = SimpleKMS()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text_to_encrypt = request.form['text_to_encrypt']
    if text_to_encrypt:
        encrypted_text = kms.encrypt(text_to_encrypt)
        flash(f'Encrypted text: {encrypted_text}')
    else:
        flash('Please enter some text to encrypt.')
    return redirect(url_for('index'))

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text_to_decrypt = request.form['text_to_decrypt']
    if text_to_decrypt:
        try:
            decrypted_text = kms.decrypt(text_to_decrypt)
            flash(f'Decrypted text: {decrypted_text}')
        except Exception as e:
            flash('Failed to decrypt. Please check the encrypted text.')
    else:
        flash('Please enter some encrypted text to decrypt.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
