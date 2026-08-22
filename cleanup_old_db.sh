#!/bin/bash
# cleanup_old_db.sh — Remove legacy databases from production PostgreSQL.
# Usage: ./cleanup_old_db.sh

set -e

DB_USER="${DB_USER:-odoo}"
DB_NAME="${DB_NAME:-prospire_hq}"
LEGACY_DB="${LEGACY_DB:-garshoub_hq}"

echo "========================================="
echo "ProspireNext Database Cleanup"
echo "========================================="
echo "Target production DB: $DB_NAME"
echo "Legacy DB to remove: $LEGACY_DB"
echo "========================================="

if [ "$DB_NAME" = "$LEGACY_DB" ]; then
    echo "ERROR: Legacy database name cannot equal the production database name."
    exit 1
fi

# Drop legacy database if it exists
if docker exec prospire_postgres psql -U "$DB_USER" -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$LEGACY_DB'" | grep -q 1; then
    echo "Found legacy database '$LEGACY_DB'. Dropping..."
    docker exec prospire_postgres psql -U "$DB_USER" -d postgres -c "DROP DATABASE \"$LEGACY_DB\";"
    echo "Dropped '$LEGACY_DB'."
else
    echo "Legacy database '$LEGACY_DB' not found. Nothing to do."
fi

# Restart Odoo so the database list refreshes
echo "Restarting Odoo container..."
docker-compose restart odoo

echo "========================================="
echo "Cleanup complete."
echo "========================================="
