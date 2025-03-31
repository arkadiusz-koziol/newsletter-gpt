from src import create_app, db
from src.scheduler import start_scheduler

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        print('Creating database tables...')
        db.create_all()
        print('Database tables created.')
        start_scheduler(app)
    app.run(host='0.0.0.0', port=5000)
