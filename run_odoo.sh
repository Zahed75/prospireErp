#!/bin/bash
# Run Odoo locally for development
# Usage: ./run_odoo.sh [PORT] [CONFIG_FILE]
#   PORT          defaults to 8069
#   CONFIG_FILE   defaults to odoo.local.conf

set -e

PORT="${1:-8069}"
CONFIG="${2:-odoo.local.conf}"

DB_USER="${DB_USER:-odoo}"
DB_PASSWORD="${DB_PASSWORD:-prospire@2@26}"
DB_NAME="${DB_NAME:-prospire_hq}"

echo "=================================="
echo "Odoo Local Runner"
echo "Port: $PORT"
echo "Config: $CONFIG"
echo "Database: $DB_NAME"
echo "=================================="

# Check PostgreSQL is reachable
if ! command -v pg_isready >/dev/null 2>&1; then
    echo "ERROR: pg_isready not found. Install PostgreSQL first:"
    echo "  brew install postgresql@15"
    exit 1
fi

if ! pg_isready -q; then
    echo "ERROR: PostgreSQL is not running. Start it with:"
    echo "  brew services start postgresql@15"
    echo "or:"
    echo "  pg_ctl -D /usr/local/var/postgres start"
    exit 1
fi

echo "PostgreSQL is ready."

# Ensure the database role exists
if ! psql postgres -tAc "SELECT 1 FROM pg_roles WHERE rolname='$DB_USER'" | grep -q 1; then
    echo "Creating PostgreSQL role '$DB_USER'..."
    psql postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD' CREATEDB;"
else
    echo "PostgreSQL role '$DB_USER' already exists."
fi

# Ensure the target database exists
if ! psql postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'" | grep -q 1; then
    echo "Creating database '$DB_NAME'..."
    psql postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
else
    echo "Database '$DB_NAME' already exists."
fi

# Setup Python virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment (.venv)..."
    python3 -m venv .venv
fi

source .venv/bin/activate

# Install or update requirements when they change
if [ ! -f ".venv/.requirements-installed" ] || [ "requirements.txt" -nt ".venv/.requirements-installed" ]; then
    echo "Installing Python requirements..."
    pip install --upgrade pip
    pip install -r requirements.txt
    touch .venv/.requirements-installed
fi

echo "=================================="
echo "Starting Odoo on http://localhost:$PORT"
echo "=================================="

./odoo-bin -c "$CONFIG" --http-port="$PORT"
