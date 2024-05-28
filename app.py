from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from ipfs_api_gateway import move_to_ipfs

app = Flask(__name__)

# Define the path for the uploads directory
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/submit", methods=['POST', 'GET'])
def get_form_data():
    if request.method == "POST":
        pokemon_name = request.form["name"]
        pokemon_type = request.form["type"]
        pokemon_power = request.form["power"]
        uploaded_file = request.files['image']

        if uploaded_file.filename != '':
            filename = secure_filename(uploaded_file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(image_path)
            move_to_ipfs(image_path)

        print(f"This is the upload file {uploaded_file}")
        print(type(uploaded_file))
        print([pokemon_name, pokemon_type, pokemon_power])

    return render_template('index_02.html')


if __name__ == '__main__':
    app.run(debug=True)
