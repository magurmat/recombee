from feed_parser import create_app

from feed_parser.controller import api

app = create_app()

app.register_blueprint(api, url_prefix='/')

if __name__ == '__main__':
    app.run()
