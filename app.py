from flask import Flask, render_template, request, jsonify
import secrets
import string

app = Flask(__name__)

# Configuración para contraseñas seguras
ALPHABET = string.ascii_letters + string.digits + string.punctuation
MIN_LENGTH = 8
MAX_LENGTH = 50

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    data = request.json
    length = int(data.get('length', 12))
    include_upper = data.get('include_upper', True)
    include_lower = data.get('include_lower', True)
    include_digits = data.get('include_digits', True)
    include_symbols = data.get('include_symbols', True)
    
    # Filtrar alfabeto basado en opciones
    alphabet = ''
    if include_lower:
        alphabet += string.ascii_lowercase
    if include_upper:
        alphabet += string.ascii_uppercase
    if include_digits:
        alphabet += string.digits
    if include_symbols:
        alphabet += string.punctuation
    
    if len(alphabet) == 0:
        return jsonify({'error': 'Selecciona al menos un tipo de carácter.'}), 400
    
    length = max(MIN_LENGTH, min(MAX_LENGTH, length))
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)