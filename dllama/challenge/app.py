from flask import Flask, render_template, request, redirect, url_for, make_response, send_from_directory
import pickle
import base64
import subprocess, os, shutil, re, io

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/'
app.secret_key = os.urandom(32)

class User:
    def __init__(self, username, authenticated=False):
        self.username = username
        self.authenticated = authenticated

    def __str__(self):
        return f"User({self.username}, authenticated={self.authenticated})"

def generate_pdf(latex_code):
    invalid_chars = re.findall(r'[^a-fA-F0-9^\n\t\r ]', latex_code)
    if invalid_chars:
        return "Error: Blacklisted characters detected"

    filename = "input.tex"
    output_pdf = "input.pdf"
    output_pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], output_pdf)
    
    with open(filename, "w") as f:
        f.write(latex_code)
    
    process = subprocess.Popen(["pdflatex", "-interaction=nonstopmode", filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode == 0 and output_pdf in os.listdir():
        shutil.move(output_pdf, output_pdf_path)  # Move the PDF file to static folder
        return output_pdf_path
    else:
        return "Error: PDF generation failed."

class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "__main__" and name == "User":
            return User
        raise pickle.UnpicklingError("Attempting to unpickle unauthorized class")

def restricted_loads(s):
    return RestrictedUnpickler(io.BytesIO(s)).load()

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = request.args.get('error')
    if request.method == 'POST':
        username = request.form.get('username')
        # Create a user with authenticated set to False by default
        user = User(username, authenticated=False)
        user_cookie = base64.b64encode(pickle.dumps(user)).decode('utf-8')
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('user', user_cookie)
        return resp
    return render_template('login.html', error=error)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_cookie = request.cookies.get('user')
    if user_cookie:
        try:
            user = restricted_loads(base64.b64decode(user_cookie))
        except pickle.UnpicklingError:
            return redirect(url_for('login', error='Invalid cookie data'))
        if not user.authenticated:
            return redirect(url_for('login', error='User is not authenticated'))
        if request.method == 'POST':        
            latex_code = request.form.get("latex_code", "")
            pdf_file = generate_pdf(latex_code)
            if pdf_file.startswith("Error"):
                return render_template("index.html", error=pdf_file, user=user)
            return render_template("index.html", pdf_file=pdf_file, user=user)
        return render_template("index.html", user=user)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('user', '', expires=0)
    return resp

@app.route('/static/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1337)
