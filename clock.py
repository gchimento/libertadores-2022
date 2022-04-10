from apscheduler.scheduler import Scheduler
from wa_automation import river_campeon

if __name__ == '__main__':
    scheduler = Scheduler(standalone=True)
    scheduler.add_interval_job(river_campeon, seconds=3)
    print('Press Ctrl+C to exit')
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass