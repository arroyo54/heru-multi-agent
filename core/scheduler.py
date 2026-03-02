"""
Scheduler para los reportes del Social Listener de heru.app.

Frecuencias:
  - Reporte semanal:    cada lunes 8:00am CDMX  (Reddit + YouTube + TikTok + Facebook + X)
  - Reporte quincenal:  lunes 1 y 15 de cada mes 8:30am CDMX  (Quora)
"""
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz

MEXICO_TZ = pytz.timezone("America/Mexico_City")


def start_scheduler(weekly_report_fn, quora_report_fn=None) -> BackgroundScheduler:
    """
    Inicia el scheduler con dos jobs:
    - weekly_report_fn:  cada lunes 8:00am CDMX
    - quora_report_fn:   cada lunes en el que el día es 1-15 del mes (quincenal)

    Args:
        weekly_report_fn: Función que genera el reporte semanal completo.
        quora_report_fn:  Función que genera el reporte quincenal de Quora (opcional).

    Returns:
        El scheduler ya corriendo.
    """
    scheduler = BackgroundScheduler(timezone=MEXICO_TZ)

    # Reporte semanal — cada lunes 8:00am
    scheduler.add_job(
        weekly_report_fn,
        CronTrigger(day_of_week="mon", hour=8, minute=0, timezone=MEXICO_TZ),
        id="weekly_social_report",
        name="Reporte Semanal Social Listener heru",
        replace_existing=True,
        misfire_grace_time=3600,
    )

    # Reporte quincenal Quora — lunes donde el día del mes es <= 15
    if quora_report_fn:
        scheduler.add_job(
            quora_report_fn,
            CronTrigger(day_of_week="mon", day="1-15", hour=8, minute=30, timezone=MEXICO_TZ),
            id="biweekly_quora_report",
            name="Reporte Quincenal Quora heru",
            replace_existing=True,
            misfire_grace_time=3600,
        )

    scheduler.start()
    logging.getLogger("apscheduler").setLevel(logging.WARNING)

    jobs = ["lunes 8:00am (semanal)"]
    if quora_report_fn:
        jobs.append("lunes 1-15 del mes 8:30am (Quora quincenal)")
    print(f"⏰ Scheduler activo — {' | '.join(jobs)} | CDMX")

    return scheduler
