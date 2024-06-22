FROM python:3.10-slim
ENV TOKEN='My_TOKEN'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "bot.py"]