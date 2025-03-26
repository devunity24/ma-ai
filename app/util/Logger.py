import os
import logging
from logging.handlers import TimedRotatingFileHandler
from inspect import getframeinfo, stack
from app.util.TimeUtil import TimeUtil


class Logger:
    loggers = {}
    LOG_DIRECTORY = "logs"
    LOGGING_LEVEL = logging.INFO

    def __init__(self):
        print("Initializing Logger Instance...")
        logging.getLogger("urllib3").setLevel(logging.INFO)
        if not os.path.exists(Logger.LOG_DIRECTORY):
            print("Log directory created")
            os.makedirs(Logger.LOG_DIRECTORY)
        else:
            print("Log directory already exists")

        Logger.createLogFile("master")

    @staticmethod
    def createLogFile(childId):
        print(childId)
        filename = f"{Logger.LOG_DIRECTORY}/AI_{childId}_Output.log"

        logger_info = logging.getLogger(childId)
        logger_info.setLevel(Logger.LOGGING_LEVEL)

        # Create a handler for the info log file
        info_handler = TimedRotatingFileHandler(
            filename=filename, when='midnight')

        # Create a formatter for info log entries
        info_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        info_handler.setFormatter(info_formatter)

        # Add the handler to the info logger
        logger_info.addHandler(info_handler)

        # Create a handler for the console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(info_formatter)

        # Add the console handler to the info logger
        logger_info.addHandler(console_handler)

        Logger.loggers[childId] = logger_info
        return logger_info

    @staticmethod
    def info(message, childId='master'):
        caller = getframeinfo(stack()[1][0])
        formattedMessage = f'{TimeUtil.getFormattedTime()}, [{caller.filename}:{str(caller.lineno)}]: {message}'
        if childId in Logger.loggers:
            logger = Logger.loggers[childId]
        else:
            logger = Logger.createLogFile(childId=childId)
        logger.info(formattedMessage)

    @staticmethod
    def warn(message, childId='master'):
        caller = getframeinfo(stack()[1][0])
        formattedMessage = f'{TimeUtil.getFormattedTime()}, [{caller.filename}:{str(caller.lineno)}]: {message}'
        if childId in Logger.loggers:
            logger = Logger.loggers[childId]
        else:
            logger = Logger.createLogFile(childId=childId)
        logger.warn(formattedMessage)

    @staticmethod
    def error(message, childId='master'):
        caller = getframeinfo(stack()[1][0])
        formattedMessage = f'{TimeUtil.getFormattedTime()}, [{caller.filename}:{str(caller.lineno)}]: {message}'
        if childId in Logger.loggers:
            logger = Logger.loggers[childId]
        else:
            logger = Logger.createLogFile(childId=childId)
        logger.error(formattedMessage)

    @staticmethod
    def debug(message, childId='master'):
        caller = getframeinfo(stack()[1][0])
        formattedMessage = f'{TimeUtil.getFormattedTime()}, [{caller.filename}:{str(caller.lineno)}]: {message}'
        if childId in Logger.loggers:
            logger = Logger.loggers[childId]
        else:
            logger = Logger.createLogFile(childId=childId)
        logger.debug(formattedMessage)
