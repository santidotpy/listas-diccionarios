FROM python:3

RUN git clone https://github.com/santidotpy/listas-diccionarios.git

WORKDIR /listas-diccionarios

RUN pip install -r requirements.txt

CMD ["python3", "test_listas_diccionarios.py"]