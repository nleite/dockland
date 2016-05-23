FROM python:2.7.11
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD app.py /code/

CMD "python" "app.py" "mongodb://repl1:27000,repl2:27000,repl3:27000"
