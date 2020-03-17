from flask import Flask , render_template
app = Flask(__name__,template_folder='template')

posts = [
{ 'Rollno' : '001',
  'Dept' : 'CSE',
  'College' : 'ABC'
},
{
  'Rollno' : '001',
  'Dept' : 'CSE',
  'College' : 'ABC'
}
]

@app.route("/")
def home():
    return render_template('Home.html' , posts=posts)

@app.route("/Second")
def Next():
    return render_template('About.html',title='About Page')

if __name__ == "__main__":
    app.run(debug=True)
