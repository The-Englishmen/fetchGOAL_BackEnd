-- settings.sql
CREATE DATABASE app;
CREATE USER appuser WITH PASSWORD 'app';
GRANT ALL PRIVILEGES ON DATABASE app TO appuser;
