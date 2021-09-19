import pytest
from selenium import webdriver
from . import utils, packages
from urllib3.exceptions import HTTPError
from .status_codes import status_codes
from .exceptions import (
    RequestException, Timeout, URLRequired,
    TooManyRedirects, HTTPError, ConnectionError,
    FileModeWarning, ConnectTimeout, ReadTimeout
)
from.sessions import session, Session
from .models import Request, Response, PreparedRequest
from .api import request, get, head, post, patch, delete, options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys