import traceback
import logging

def run_my(callback):
    try:
        callback()
    except Exception as e:
        logging.error(traceback.format_exc())