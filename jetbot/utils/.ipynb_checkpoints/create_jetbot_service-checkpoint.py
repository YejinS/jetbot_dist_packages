'''
@Author: Malloy.Yuan
@Wechat: ymlin96546
@Date: 2019-08-26 11:06:33
@LastEditors: Malloy.Yuan
@LastEditTime: 2019-08-26 15:52:11
'''
import argparse
import getpass
import os

STATS_SERVICE_TEMPLATE = """
[Unit]
Description=JetBot start service
After=multi-user.target

[Service]
Type=idle
User=%s
ExecStart=/bin/sh -c "python3 /home/jetbot/yahboom-jetbot/yahboom-jetbot.pyc"
WorkingDirectory=%s

[Install]
WantedBy=multi-user.target
"""

STATS_SERVICE_NAME = 'jetbot_start'


def get_jetbot_service():
    return STATS_SERVICE_TEMPLATE % (getpass.getuser(), os.environ['HOME'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='jetbot_start.service')
    args = parser.parse_args()

    with open(args.output, 'w') as f:
        f.write(get_jetbot_service())
