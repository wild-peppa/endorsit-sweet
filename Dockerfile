FROM eds-swt-env

WORKDIR /root/endorsit-sweet

COPY ./ ./

    # setup endorsit-sweet 
RUN cd endorsit \
    # && pip3 install -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt \
    && pip3 install -e .

WORKDIR /root/endorsit-sweet/endorsit-sweet/endorsit-sweet

EXPOSE 8001

CMD ["python3", "sweet.py"]
