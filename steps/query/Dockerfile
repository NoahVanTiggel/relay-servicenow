FROM relaysh/core:latest-python
RUN pip --no-cache-dir install pysnow && apk add libmagic
COPY "./step.py" "/step.py"
ENTRYPOINT []
CMD ["python3", "/step.py"]

LABEL "org.opencontainers.image.title"="Query ServiceNow"
LABEL "org.opencontainers.image.description"="This task queries ServiceNow."
LABEL "sh.relay.sdk.version"="v1"
