FROM python:3.8

RUN apt-get update && apt-get install -yq \
    xvfb \
    xsel

# set display port to avoid crash
ENV DISPLAY=:99

# xvfb - X server display
#ADD xvfb-chromium /usr/bin/xvfb-chromium
#RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
#    && chmod 777 /usr/bin/xvfb-chromium

# upgrade pip
RUN pip install --upgrade pip

# create folder to copy code
RUN mkdir /code

# project scope
WORKDIR /code

#copy testing code
COPY ./ ./

# install requirements
RUN pip install -r requirements.txt
