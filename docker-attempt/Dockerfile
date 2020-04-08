FROM python:2.7-stretch

RUN apt-get update && apt-get install -yq \
    chromium=73.0.3683.75-1~deb9u1 \
    git=1:2.11.0-3+deb9u5 \ 
    xvfb=2:1.19.2-1+deb9u5 \
    xsel=1.2.0-2+b1 \
    unzip=6.0-21+deb9u2 \
    python-pytest=3.0.6-1 \
    libgconf2-4=3.2.6-4+b1 \
    libncurses5=6.0+20161126-1+deb9u2 \
    libxml2-dev=2.9.4+dfsg1-2.2+deb9u2 \
    libxslt-dev \
    libz-dev \
    xclip=0.12+svn84-4+b1

# chromeDriver v2.35
RUN wget -q "https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip

# xvfb - X server display
ADD ./xvfb-chromium /usr/bin/xvfb-chromium
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome \
    && chmod 777 /usr/bin/xvfb-chromium

RUN easy_install -U setuptools
RUN pip install pytest-dependency
RUN pip install selenium

RUN pwd

RUN mkdir /src

COPY new_test.py ./src
#COPY requirements.txt ./src
#RUN pip install -r /src/requirements.txt

RUN ["pytest", "-v", "/src/new_test.py" ]
CMD tail -f /dev/null

#RUN cp new_test.py /usr
#RUN cd /usr
#RUN python -m pytest /usr/new_test.py

#CMD ["/bin/true"]

