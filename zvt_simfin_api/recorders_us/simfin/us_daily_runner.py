# -*- coding: utf-8 -*-
import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler

from zvt import init_log
from zvt.recorders_us.simfin.us_stock_1d_kdata_recorder import USStock1dKdata
from zvt.recorders_us.simfin.us_stock_valuation_recorder import USStockValuationRecorder

logger = logging.getLogger(__name__)

sched = BackgroundScheduler()


@sched.scheduled_job('cron', hour=10, minute=00)
def run():
    while True:
        try:
            USStock1dKdata.run()
            USStockValuationRecorder.run()
            break
        except Exception as e:
            logger.exception('sina runner error:{}'.format(e))
            time.sleep(60)


if __name__ == '__main__':
    init_log('simfin_runner.log')

    run()

    sched.start()

    sched._thread.join()