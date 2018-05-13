FROM    python:3.6.3

RUN     git clone https://github.com/pbx-gs/gs-risk-jira.git
WORKDIR gs-risk-jira
ADD     config.py config.py
RUN     ls -la
RUN     pip install -r requirements.txt

RUN     python models.py



