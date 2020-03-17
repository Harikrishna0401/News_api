from flask import Flask , render_template , url_for , flash , redirect , request , session , logging
from flask_mysqldb import MySQL
from passlib.hash import sha256_crypt
from forms import RegistrationForm , LoginForm
from newsapi import NewsApiClient
from flask_paginate import Pagination, get_page_args

app = Flask(__name__,template_folder='template')
users = list(range(100))

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'app'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

def get_users(offset=0 , per_page=4):
    return users[offset: offset + per_page]

mysql = MySQL(app)

@app.route("/")
def first():
    return render_template('first.html')

@app.route("/layout")
def lay():
    return render_template('layout.html')

@app.route("/result")
def result():
    return render_template('result.html')

@app.route("/Logout")
def logout():
    session.clear()
    return redirect(url_for('log'))

@app.route("/SignUp" , methods = ['GET' , 'POST'])
def sign():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        Firstname = form.firstname.data
        Lastname = form.lastname.data
        Email = form.email.data
        Password = sha256_crypt.encrypt(str(form.password.data))
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Signin(FirstName,LastName,Email,Password) VALUES(%s,%s,%s,%s)" , (Firstname,Lastname,Email,Password))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('first'))
    return render_template('sign.html' , form = form)

@app.route("/LogIn" , methods = ['GET' , 'POST'])
def log():
    form = LoginForm()
    if request.method == 'POST':
        Email = request.form['email']
        userpassword = request.form['password']
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM Signin WHERE Email = %s" , [Email])

        if result > 0:
            data = cur.fetchone()
            password = data['Password']

            if sha256_crypt.verify(userpassword,password):
                session['logged_in'] = True
                return redirect(url_for('desktop'))


    return render_template('login.html' , form = form)

@app.route("/desktop" , methods = ['GET' , 'POST'])
def desktop():
    return render_template('desktop.html')

@app.route('/business')
def business():
    newsapi = NewsApiClient(api_key='b92cb162f8064f81964d4268970377c1')
    
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    pagination_users = get_users(offset=offset, per_page=per_page)
    total = len(users)
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap4')

    top_headlines = newsapi.get_top_headlines(category='business',language='en' , country='in' , page=page , page_size = 4)

    articles = top_headlines['articles']
    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticle = articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])
        link.append(myarticle['url'])

        mylist = zip(news, desc, img, link)


    return render_template('business.html', context=mylist, users=pagination_users, page=page,
                        per_page=per_page, pagination=pagination)
    


@app.route('/sport')
def sport():
    newsapi = NewsApiClient(api_key='b92cb162f8064f81964d4268970377c1')
    
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    pagination_users = get_users(offset=offset, per_page=per_page)
    total = len(users)
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap4')

    top_headlines = newsapi.get_top_headlines(category='sports',language='en' , country='in' , page=page , page_size = 4)

    articles = top_headlines['articles']
    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticle = articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])
        link.append(myarticle['url'])

        mylist = zip(news, desc, img, link)


    return render_template('sports.html', context=mylist, users=pagination_users, page=page,
                        per_page=per_page, pagination=pagination)

@app.route('/entertainment')
def entertainment():
    newsapi = NewsApiClient(api_key='b92cb162f8064f81964d4268970377c1')
    
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    pagination_users = get_users(offset=offset, per_page=per_page)
    total = len(users)
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap4')

    top_headlines = newsapi.get_top_headlines(category='entertainment',language='en' , country='in' , page=page , page_size = 4)

    articles = top_headlines['articles']
    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticle = articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])
        link.append(myarticle['url'])

        mylist = zip(news, desc, img, link)


    return render_template('entertainment.html', context=mylist, users=pagination_users, page=page,
                        per_page=per_page, pagination=pagination)

@app.route('/technology')
def technology():
    newsapi = NewsApiClient(api_key='b92cb162f8064f81964d4268970377c1')
    
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    pagination_users = get_users(offset=offset, per_page=per_page)
    total = len(users)
    pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap4')

    top_headlines = newsapi.get_top_headlines(category='technology',language='en' , country='in' , page=page , page_size = 4)

    articles = top_headlines['articles']
    desc = []
    news = []
    img = []
    link = []

    for i in range(len(articles)):
        myarticle = articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])
        link.append(myarticle['url'])

        mylist = zip(news, desc, img, link)


    return render_template('technology.html', context=mylist, users=pagination_users, page=page,
                        per_page=per_page, pagination=pagination)

@app.route('/search' , methods=['GET' , 'POST'])
def search():
    if request.method == 'GET':
        req = request.args.get('srch')
        
        # if len(req) > 0:
        #     newsapi = NewsApiClient(api_key='b92cb162f8064f81964d4268970377c1')
            
        #     top_headlines = newsapi.get_top_headlines(language='en')

        #     articles = top_headlines['articles']

        #     desc = []
        #     news = []
        #     img = []
        #     link = []

        #     n = 0

        #     for i in range(len(articles)):
        #         myarticle = articles[i]
        #         content = myarticle['description']
        #         if req in content:
        #             print(content)
        #             news.append(myarticle['title'])
        #             desc.append(myarticle['description'])
        #             img.append(myarticle['urlToImage'])
        #             link.append(myarticle['url'])


        #         else:
        #             continue

        #     mycontent = zip(news,desc,img,link)
        #     return render_template('search.html' , context = mycontent)

        if len(req) > 0:
            newsapi = NewsApiClient(api_key='b92cb162f8064f81964d4268970377c1')

            page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
            pagination_users = get_users(offset=offset, per_page=per_page)
            total = len(users)
            pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap4')
            
            all_articles = newsapi.get_everything(q = req ,
                                      from_param='2020-03-09',
                                      to='2020-03-11',
                                      language='en',
                                      sort_by='relevancy',page=page,page_size=4)
            articles = all_articles['articles']

            news = []
            desc = []
            img = []
            link = []

            n=0

            for i in range(len(articles)):
                myarticle = articles[i]
                content = myarticle['description']
                print(content)
                if req in content:
                    n+=1
                    print(content)
                    news.append(myarticle['title'])
                    desc.append(myarticle['description'])
                    img.append(myarticle['urlToImage'])
                    link.append(myarticle['url'])
                
                else:
                    continue

            if n < 1:
                return render_template('error.html')

            mycontent = zip(news,desc,img,link)
            return render_template('search.html' , context = mycontent,page=page,per_page=per_page,pagination=pagination)
        
        return render_template('search.html')

if __name__ == "__main__":
    app.secret_key = 'secret123'
    app.run(debug=True)