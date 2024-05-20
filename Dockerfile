FROM debian:11-slim AS build
RUN apt-get update && \
    apt-get install --yes python3-venv gcc libpython3-dev
RUN python3 -m venv /venv 
RUN /venv/bin/pip install --upgrade pip 
RUN /venv/bin/pip install --upgrade wheel 
RUN /venv/bin/pip install --upgrade setuptools

# Build the virtualenv as a separate step: Only re-execute this step when requirements.txt changes
FROM build AS build-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install -r /requirements.txt

# Copy the virtualenv into a distroless image
FROM gcr.io/distroless/python3-debian11
COPY --from=build-venv /venv /venv
COPY ./src /app
WORKDIR /app
ENTRYPOINT ["/venv/bin/python3", "main.py"]