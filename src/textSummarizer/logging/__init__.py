import os
import sys
import logging

#this will display logging string: time, type of log(like info), module name(from where is the file running) and the message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)


#logic to store and display logs in a file (running_logs.log) and on console
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")