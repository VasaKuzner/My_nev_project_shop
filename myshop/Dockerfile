FROM python:3.10.12


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /user/src/sdd_vasa


COPY ./requirements.txt /user/src/requirements.txt


RUN pip install -r /user/src/requirements.txt


COPY . /user/src/sdd_vasa


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]