# -*- coding: utf-8 -*-
import logging
import time

from apscheduler.schedulers.background import BackgroundScheduler

from zvt import init_log
from zvt.recorders_us.simfin.us_stock_balance_sheet_recorder import USStockBalanceSheetRecorder
from zvt.recorders_us.simfin.us_stock_cash_flow_recorder import USStockCashFlowRecorder
from zvt.recorders_us.simfin.us_stock_income_statement_recorder import USStockIncomeStatementRecorder
from zvt.recorders_us.simfin.us_stock_finance_factor_recorder import USStockFinanceFactorRecorder


logger = logging.getLogger(__name__)

sched = BackgroundScheduler()


@sched.scheduled_job('cron', hour=3, minute=00)
def run():
    while True:
        try:

            USStockBalanceSheetRecorder.run()
            USStockIncomeStatementRecorder.run()
            USStockCashFlowRecorder.run()
            USStockFinanceFactorRecorder.run()
            break
        except Exception as e:
            logger.exception('sina runner error:{}'.format(e))
            time.sleep(60)


if __name__ == '__main__':
    init_log('sina_runner.log')

    run()

    sched.start()

    sched._thread.join()