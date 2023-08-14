#! /usr/bin/env sh
cd ..
while true; do nc -vz 0.0.0.0 5432 && break; done
alembic current
alembic history
alembic upgrade head