import coloredlogs
import logging

coloredlogs.install()

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
)

log = logging.getLogger(__name__)
log.info("done")