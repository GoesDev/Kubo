from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/form_login_user', methods=['POST'])
def form_login_user():
    email = request.form.get('user_email')
    password = request.form.get('user_password')


    print(f"Email: {email}")
    print(f"Senha: {password}")
    
    return (render_template('home.html') + "<h1>Sucess login!</h1>")

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/form_register_user', methods=['POST'])
def form_register_user():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password = request.form.get("user_password")

    print(f"Nome: {name}")
    print(f"Email: {email}")
    print(f"Password: {password}")

    return ("<h1>Sucess register!</h1>" + render_template("login.html") )

@app.route('/home.html')
def home():
    render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
