#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:29:22 2022

@author: peter
"""

import logging

logging.basicConfig(force = True,
                    filename = None,
                    level = logging.FATAL)


logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
logging.critical('BANGGG!')



