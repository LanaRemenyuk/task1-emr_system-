FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-root --no-cache

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "python", "code_dir/manage.py", "runserver"]