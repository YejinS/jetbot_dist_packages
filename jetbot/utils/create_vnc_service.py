'''
@Author: LIUSEN
@Date: 2020-04-03 16:29:33
@LastEditors: LIUSEN
@LastEditTime: 2020-04-03 16:29:33
'''
import argparse
import getpass
import os

STATS_SERVICE_TEMPLATE = """
[Unit]
Description=JetBot VNC service
After=network.target multi-user.target 

[Service]
Type=simple
User=%s
ExecStart=/bin/sh -c "/usr/lib/vino/vino-server --display=:0"
WorkingDirectory=%s

[Install]
WantedBy=multi-user.target
"""

STATS_SERVICE_NAME = 'jetbot_vnc'


def get_jetbot_service():
    return STATS_SERVICE_TEMPLATE % (getpass.getuser(), os.environ['HOME'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='jetbot_vnc.service')
    args = parser.parse_args()

    with open(args.output, 'w') as f:
        f.write(get_jetbot_service())
