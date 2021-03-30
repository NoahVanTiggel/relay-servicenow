FROM relaysh/core:latest-python
RUN pip --no-cache-dir install pysnow
COPY "./step.py" "/step.py"
ENTRYPOINT []
CMD ["python3", "/step.py"]

LABEL "org.opencontainers.image.title"="Create ServiceNow incident"
LABEL "org.opencontainers.image.description"="This task creates a ServiceNow incident."
LABEL "sh.relay.sdk.version"="v1"
