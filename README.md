# JRMonitor

a monitor script for check site https://weibo.com/warshipgirlsr and notificate you there is new ship will be remodeled by email.

listed activies saved as a json file `save.json`.

maill settings in `settings.py`, and you can write them in `local_settings.py`.

it's running under python 3

## install another python 3 in linux, not update python 2. create virtual env

    wget https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tar.xz

    xz -d Python-3.7.1.tar.xz

    tar -xvf Python-3.7.1.tar

    cd Python-3.7.1

    ./configure --prefix=/usr/local --with-ssl

    make

    make altinstall

    cd <project folder>

    /usr/local/bin/pyvenv-3.7 venv

    source venv/bin/activate

    pip install -r requirements.txt

if there is another python version on your server, you can create virtual env `venv` with blow.

    virtualenv -p <python path> venv

## auto run

add auto task with `crontab -e`

    02 11 * * * <project folder>/venv/bin/python <project folder>/main.py
