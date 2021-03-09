from learncrypto import db,create_app

app = db.create_all(create_app())
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=False)