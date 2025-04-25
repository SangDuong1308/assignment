### APIs docs
[APIs documentation](https://documenter.getpostman.com/view/30706098/2sB2izDsuL)

## Features

- User registration and authentication using JWT
- Password reset functionality
- Transaction management for users
- Staff-only functionalities for managing transactions

## Tech Stack

- Python 3.9.13
- Flask 2.2.3
- PostgreSQL
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Docker & Docker Compose

### Using Docker Compose (Recommended)

1. Clone the repository
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a `.env` file based on `.env.example`
   ```
   cp .env.example .env
   ```

3. Build and start the containers
   ```
   docker compose up -d
   ```

4. Create database migrations
   ```
   docker compose exec web flask db init
   docker compose exec web flask db migrate -m "Initial migration"
   docker compose exec web flask db upgrade
   ```

5. The API will be available at http://localhost:5000

### Local Development

1. Create and activate a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate
   ```

2. Install requirements
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables
   ```
   export FLASK_APP=app
   export FLASK_ENV=development
   export DATABASE_URL=postgresql://user:password@localhost:5432/bn_db
   ```

4. Run database migrations
   ```
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Run the development server
   ```
   flask run
   ```