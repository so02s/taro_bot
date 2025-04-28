FROM python:3.11.2-slim

WORKDIR /usr/src/app/
COPY app /usr/src/app/

RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["python", "main.py"]
