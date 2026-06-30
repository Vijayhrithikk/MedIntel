#!/bin/bash

docker run -d \
  --name medintel-postgres \
  -e POSTGRES_USER=medintel \
  -e POSTGRES_PASSWORD=medintel \
  -e POSTGRES_DB=medintel \
  -p 5435:5432 \
  -v medintel-postgres-data:/var/lib/postgresql/data \
  postgres:16