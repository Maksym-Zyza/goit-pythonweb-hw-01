import logging

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)

# Створюємо консольний обробник, рівень Info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Створюємо файловий обробник, рівень ERROR
fh = logging.FileHandler("logger.log")
fh.setLevel(logging.ERROR)
fh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# Додаємо обробники, якщо їх немає
if not logger.handlers:
    logger.addHandler(ch)
    logger.addHandler(fh)
