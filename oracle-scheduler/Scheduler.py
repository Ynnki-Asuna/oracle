#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import Oracle
from apscheduler.schedulers.background import BackgroundScheduler

if __name__ == '__main__':
    oracle = Oracle.Oracle()
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 10s
    scheduler.add_job(oracle.update, 'interval', seconds=30)
    # 启动调度任务
    scheduler.start()
    print('the scheduler has started.......')
    while True:
        time.sleep(30)