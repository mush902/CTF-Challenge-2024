#FROM python:3.12-slim-bookworm

#RUN apt-get update

#WORKDIR /app

#EXPOSE 5000

# Enable a py env
#RUN python3 -m venv .venv
#ENV PATH="./ollamavenv/venv/bin:$PATH"

#COPY ./ai .
#COPY ./static .
#COPY ./templates .
#COPY ./utils .
#COPY ./app.py /
#COPY ./flag.txt /
#COPY ./requirements.txt /
#COPY . .


#ADD ollamavenv   /

#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install ollama

#RUN ollama run codellama
#RUN flask --app app run

#CMD ["sh", "-c", "ollama run codellama & python app.py"]

# FROM python:3.12-slim-bookworm


# RUN apt-get update

# ################################
# #FIXME: drop user to non root

# WORKDIR /app


# # EXPOSE 5000


# RUN python3 -m venv .venv
# ENV PATH="./.venv/bin:$PATH"


# COPY . /app


# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt


# RUN pip install ollama
# ENV PATH="/app/.venv/lib/python3.12/site-packages/ollama:${PATH}"


# CMD ["sh", "-c", "python app.py"]

FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]