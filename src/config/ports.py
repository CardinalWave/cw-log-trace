import configparser
import os


class Config:
    config = configparser.ConfigParser()
    config.read('src/config/config.ini')

    CW_LOG_TRACE = config['CW_LOG_TRACE']['BaseURL']
    CW_LOG_TRACE_IP = config['CW_LOG_TRACE']['IP']
    CW_LOG_TRACE_PORT = config['CW_LOG_TRACE']['PORT']

    CW_LOG_TRACE = os.getenv('CW_LOG_TRACE', CW_LOG_TRACE)
    CW_LOG_TRACE_IP = os.getenv('CW_LOG_TRACE_IP', CW_LOG_TRACE_IP)
    CW_LOG_TRACE_PORT = os.getenv('CW_LOG_TRACE_PORT', CW_LOG_TRACE_PORT)
