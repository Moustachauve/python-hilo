"""Define the hilo package."""

from pyhilo.api import API
from pyhilo.devices import Devices
from pyhilo.device import HiloDevice
from pyhilo.event import Event
from pyhilo.exceptions import HiloError, InvalidCredentialsError, WebsocketError
from pyhilo.oauth2 import AuthCodeWithPKCEImplementation
from pyhilo.util import from_utc_timestamp, time_diff
from pyhilo.websocket import WebsocketEvent
from pyhilo.const import UNMONITORED_DEVICES
from pyhilo.device.switch import Switch

__all__ = [
    "API",
    "Devices",
    "HiloDevice",
    "Event",
    "HiloError",
    "InvalidCredentialsError",
    "WebsocketError",
    "AuthCodeWithPKCEImplementation",
    "from_utc_timestamp",
    "time_diff",
    "WebsocketEvent",
    "UNMONITORED_DEVICES",
    "Switch",
]
