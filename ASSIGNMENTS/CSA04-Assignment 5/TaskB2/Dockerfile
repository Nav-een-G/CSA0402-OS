FROM python:3.12-slim
# TODO 1: set working directory
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# TODO 2: copy application files and create non-root user
COPY app.py .
COPY templates ./templates
COPY static ./static
RUN useradd --create-home --shell /usr/sbin/nologin portal && chown -R portal:portal /app
USER portal
# TODO 3: expose port and run Gunicorn on 0.0.0.0:8000
EXPOSE 8000
CMD ["gunicorn","--workers","2","--bind","0.0.0.0:8000","app:app"]
