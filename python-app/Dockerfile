FROM python:3.10
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY main.py /app/main.py
ENTRYPOINT exec python /app/main.py
