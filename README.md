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