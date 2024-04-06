import logging

logging.basicConfig(level=logging.ERROR,
                     filename="logfile.log",
                     filemode="w",
                     format="We have next logging message:"
                            "%(asctime) : %(levelname)% - %(message)s")
try:
    print(10/0)
except Exception:
    logging.exception("Exception")