FROM python:3.10-slim
ENV TOKEN='7250466417:AAGmOdZ42RzZvpe1OZZ10mQLN5eFmLIgpr4'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]