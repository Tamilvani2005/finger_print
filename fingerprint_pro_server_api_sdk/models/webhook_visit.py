# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import Dict  # noqa: F401
from fingerprint_pro_server_api_sdk.base_model import BaseModel
from fingerprint_pro_server_api_sdk.models.botd_detection_result import BotdDetectionResult
from fingerprint_pro_server_api_sdk.models.ip_info_result import IpInfoResult
from fingerprint_pro_server_api_sdk.models.root_apps_result import RootAppsResult
from fingerprint_pro_server_api_sdk.models.emulator_result import EmulatorResult
from fingerprint_pro_server_api_sdk.models.cloned_app_result import ClonedAppResult
from fingerprint_pro_server_api_sdk.models.factory_reset_result import FactoryResetResult
from fingerprint_pro_server_api_sdk.models.jailbroken_result import JailbrokenResult
from fingerprint_pro_server_api_sdk.models.frida_result import FridaResult
from fingerprint_pro_server_api_sdk.models.ip_block_list_result import IpBlockListResult
from fingerprint_pro_server_api_sdk.models.tor_result import TorResult
from fingerprint_pro_server_api_sdk.models.privacy_settings_result import PrivacySettingsResult
from fingerprint_pro_server_api_sdk.models.virtual_machine_result import VirtualMachineResult
from fingerprint_pro_server_api_sdk.models.vpn_result import VpnResult
from fingerprint_pro_server_api_sdk.models.proxy_result import ProxyResult
from fingerprint_pro_server_api_sdk.models.tampering_result import TamperingResult
from fingerprint_pro_server_api_sdk.models.raw_device_attributes_result import RawDeviceAttributesResult
from fingerprint_pro_server_api_sdk.models.high_activity_result import HighActivityResult
from fingerprint_pro_server_api_sdk.models.location_spoofing_result import LocationSpoofingResult
from fingerprint_pro_server_api_sdk.models.suspect_score_result import SuspectScoreResult
from fingerprint_pro_server_api_sdk.models.remote_control_result import RemoteControlResult
from fingerprint_pro_server_api_sdk.models.velocity_result import VelocityResult
from fingerprint_pro_server_api_sdk.models.browser_details import BrowserDetails
from fingerprint_pro_server_api_sdk.models.deprecated_ip_location import DeprecatedIPLocation
from datetime import datetime
from fingerprint_pro_server_api_sdk.models.confidence import Confidence
from fingerprint_pro_server_api_sdk.models.seen_at import SeenAt
from fingerprint_pro_server_api_sdk.models.seen_at import SeenAt


class WebhookVisit(BaseModel):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'visitor_id': 'str',
        'client_referrer': 'str',
        'user_agent': 'str',
        'bot': 'BotdDetectionResult',
        'ip_info': 'IpInfoResult',
        'incognito': 'bool',
        'root_apps': 'RootAppsResult',
        'emulator': 'EmulatorResult',
        'cloned_app': 'ClonedAppResult',
        'factory_reset': 'FactoryResetResult',
        'jailbroken': 'JailbrokenResult',
        'frida': 'FridaResult',
        'ip_blocklist': 'IpBlockListResult',
        'tor': 'TorResult',
        'privacy_settings': 'PrivacySettingsResult',
        'virtual_machine': 'VirtualMachineResult',
        'vpn': 'VpnResult',
        'proxy': 'ProxyResult',
        'tampering': 'TamperingResult',
        'raw_device_attributes': 'RawDeviceAttributesResult',
        'high_activity': 'HighActivityResult',
        'location_spoofing': 'LocationSpoofingResult',
        'suspect_score': 'SuspectScoreResult',
        'remote_control': 'RemoteControlResult',
        'velocity': 'VelocityResult',
        'request_id': 'str',
        'browser_details': 'BrowserDetails',
        'ip': 'str',
        'ip_location': 'DeprecatedIPLocation',
        'timestamp': 'int',
        'time': 'datetime',
        'url': 'str',
        'tag': 'dict(str, object)',
        'linked_id': 'str',
        'confidence': 'Confidence',
        'visitor_found': 'bool',
        'first_seen_at': 'SeenAt',
        'last_seen_at': 'SeenAt'
    }

    attribute_map = {
        'visitor_id': 'visitorId',
        'client_referrer': 'clientReferrer',
        'user_agent': 'userAgent',
        'bot': 'bot',
        'ip_info': 'ipInfo',
        'incognito': 'incognito',
        'root_apps': 'rootApps',
        'emulator': 'emulator',
        'cloned_app': 'clonedApp',
        'factory_reset': 'factoryReset',
        'jailbroken': 'jailbroken',
        'frida': 'frida',
        'ip_blocklist': 'ipBlocklist',
        'tor': 'tor',
        'privacy_settings': 'privacySettings',
        'virtual_machine': 'virtualMachine',
        'vpn': 'vpn',
        'proxy': 'proxy',
        'tampering': 'tampering',
        'raw_device_attributes': 'rawDeviceAttributes',
        'high_activity': 'highActivity',
        'location_spoofing': 'locationSpoofing',
        'suspect_score': 'suspectScore',
        'remote_control': 'remoteControl',
        'velocity': 'velocity',
        'request_id': 'requestId',
        'browser_details': 'browserDetails',
        'ip': 'ip',
        'ip_location': 'ipLocation',
        'timestamp': 'timestamp',
        'time': 'time',
        'url': 'url',
        'tag': 'tag',
        'linked_id': 'linkedId',
        'confidence': 'confidence',
        'visitor_found': 'visitorFound',
        'first_seen_at': 'firstSeenAt',
        'last_seen_at': 'lastSeenAt'
    }

    def __init__(self, visitor_id=None, client_referrer=None, user_agent=None, bot=None, ip_info=None, incognito=None, root_apps=None, emulator=None, cloned_app=None, factory_reset=None, jailbroken=None, frida=None, ip_blocklist=None, tor=None, privacy_settings=None, virtual_machine=None, vpn=None, proxy=None, tampering=None, raw_device_attributes=None, high_activity=None, location_spoofing=None, suspect_score=None, remote_control=None, velocity=None, request_id=None, browser_details=None, ip=None, ip_location=None, timestamp=None, time=None, url=None, tag=None, linked_id=None, confidence=None, visitor_found=None, first_seen_at=None, last_seen_at=None):  # noqa: E501
        """WebhookVisit - a model defined in Swagger"""  # noqa: E501
        self._visitor_id = None
        self._client_referrer = None
        self._user_agent = None
        self._bot = None
        self._ip_info = None
        self._incognito = None
        self._root_apps = None
        self._emulator = None
        self._cloned_app = None
        self._factory_reset = None
        self._jailbroken = None
        self._frida = None
        self._ip_blocklist = None
        self._tor = None
        self._privacy_settings = None
        self._virtual_machine = None
        self._vpn = None
        self._proxy = None
        self._tampering = None
        self._raw_device_attributes = None
        self._high_activity = None
        self._location_spoofing = None
        self._suspect_score = None
        self._remote_control = None
        self._velocity = None
        self._request_id = None
        self._browser_details = None
        self._ip = None
        self._ip_location = None
        self._timestamp = None
        self._time = None
        self._url = None
        self._tag = None
        self._linked_id = None
        self._confidence = None
        self._visitor_found = None
        self._first_seen_at = None
        self._last_seen_at = None
        self.discriminator = None
        self.visitor_id = visitor_id
        if client_referrer is not None:
            self.client_referrer = client_referrer
        if user_agent is not None:
            self.user_agent = user_agent
        if bot is not None:
            self.bot = bot
        if ip_info is not None:
            self.ip_info = ip_info
        self.incognito = incognito
        if root_apps is not None:
            self.root_apps = root_apps
        if emulator is not None:
            self.emulator = emulator
        if cloned_app is not None:
            self.cloned_app = cloned_app
        if factory_reset is not None:
            self.factory_reset = factory_reset
        if jailbroken is not None:
            self.jailbroken = jailbroken
        if frida is not None:
            self.frida = frida
        if ip_blocklist is not None:
            self.ip_blocklist = ip_blocklist
        if tor is not None:
            self.tor = tor
        if privacy_settings is not None:
            self.privacy_settings = privacy_settings
        if virtual_machine is not None:
            self.virtual_machine = virtual_machine
        if vpn is not None:
            self.vpn = vpn
        if proxy is not None:
            self.proxy = proxy
        if tampering is not None:
            self.tampering = tampering
        if raw_device_attributes is not None:
            self.raw_device_attributes = raw_device_attributes
        if high_activity is not None:
            self.high_activity = high_activity
        if location_spoofing is not None:
            self.location_spoofing = location_spoofing
        if suspect_score is not None:
            self.suspect_score = suspect_score
        if remote_control is not None:
            self.remote_control = remote_control
        if velocity is not None:
            self.velocity = velocity
        self.request_id = request_id
        self.browser_details = browser_details
        self.ip = ip
        if ip_location is not None:
            self.ip_location = ip_location
        self.timestamp = timestamp
        self.time = time
        self.url = url
        self.tag = tag
        if linked_id is not None:
            self.linked_id = linked_id
        if confidence is not None:
            self.confidence = confidence
        self.visitor_found = visitor_found
        self.first_seen_at = first_seen_at
        self.last_seen_at = last_seen_at

    @property
    def visitor_id(self) -> str:
        """Gets the visitor_id of this WebhookVisit.  # noqa: E501


        :return: The visitor_id of this WebhookVisit.  # noqa: E501
        """
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, visitor_id: str):
        """Sets the visitor_id of this WebhookVisit.


        :param visitor_id: The visitor_id of this WebhookVisit.  # noqa: E501
        """
        if visitor_id is None:
            raise ValueError("Invalid value for `visitor_id`, must not be `None`")  # noqa: E501

        self._visitor_id = visitor_id

    @property
    def client_referrer(self) -> str:
        """Gets the client_referrer of this WebhookVisit.  # noqa: E501


        :return: The client_referrer of this WebhookVisit.  # noqa: E501
        """
        return self._client_referrer

    @client_referrer.setter
    def client_referrer(self, client_referrer: str):
        """Sets the client_referrer of this WebhookVisit.


        :param client_referrer: The client_referrer of this WebhookVisit.  # noqa: E501
        """

        self._client_referrer = client_referrer

    @property
    def user_agent(self) -> str:
        """Gets the user_agent of this WebhookVisit.  # noqa: E501


        :return: The user_agent of this WebhookVisit.  # noqa: E501
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent: str):
        """Sets the user_agent of this WebhookVisit.


        :param user_agent: The user_agent of this WebhookVisit.  # noqa: E501
        """

        self._user_agent = user_agent

    @property
    def bot(self) -> BotdDetectionResult:
        """Gets the bot of this WebhookVisit.  # noqa: E501


        :return: The bot of this WebhookVisit.  # noqa: E501
        """
        return self._bot

    @bot.setter
    def bot(self, bot: BotdDetectionResult):
        """Sets the bot of this WebhookVisit.


        :param bot: The bot of this WebhookVisit.  # noqa: E501
        """

        self._bot = bot

    @property
    def ip_info(self) -> IpInfoResult:
        """Gets the ip_info of this WebhookVisit.  # noqa: E501


        :return: The ip_info of this WebhookVisit.  # noqa: E501
        """
        return self._ip_info

    @ip_info.setter
    def ip_info(self, ip_info: IpInfoResult):
        """Sets the ip_info of this WebhookVisit.


        :param ip_info: The ip_info of this WebhookVisit.  # noqa: E501
        """

        self._ip_info = ip_info

    @property
    def incognito(self) -> bool:
        """Gets the incognito of this WebhookVisit.  # noqa: E501

        Flag if user used incognito session.  # noqa: E501

        :return: The incognito of this WebhookVisit.  # noqa: E501
        """
        return self._incognito

    @incognito.setter
    def incognito(self, incognito: bool):
        """Sets the incognito of this WebhookVisit.

        Flag if user used incognito session.  # noqa: E501

        :param incognito: The incognito of this WebhookVisit.  # noqa: E501
        """
        if incognito is None:
            raise ValueError("Invalid value for `incognito`, must not be `None`")  # noqa: E501

        self._incognito = incognito

    @property
    def root_apps(self) -> RootAppsResult:
        """Gets the root_apps of this WebhookVisit.  # noqa: E501


        :return: The root_apps of this WebhookVisit.  # noqa: E501
        """
        return self._root_apps

    @root_apps.setter
    def root_apps(self, root_apps: RootAppsResult):
        """Sets the root_apps of this WebhookVisit.


        :param root_apps: The root_apps of this WebhookVisit.  # noqa: E501
        """

        self._root_apps = root_apps

    @property
    def emulator(self) -> EmulatorResult:
        """Gets the emulator of this WebhookVisit.  # noqa: E501


        :return: The emulator of this WebhookVisit.  # noqa: E501
        """
        return self._emulator

    @emulator.setter
    def emulator(self, emulator: EmulatorResult):
        """Sets the emulator of this WebhookVisit.


        :param emulator: The emulator of this WebhookVisit.  # noqa: E501
        """

        self._emulator = emulator

    @property
    def cloned_app(self) -> ClonedAppResult:
        """Gets the cloned_app of this WebhookVisit.  # noqa: E501


        :return: The cloned_app of this WebhookVisit.  # noqa: E501
        """
        return self._cloned_app

    @cloned_app.setter
    def cloned_app(self, cloned_app: ClonedAppResult):
        """Sets the cloned_app of this WebhookVisit.


        :param cloned_app: The cloned_app of this WebhookVisit.  # noqa: E501
        """

        self._cloned_app = cloned_app

    @property
    def factory_reset(self) -> FactoryResetResult:
        """Gets the factory_reset of this WebhookVisit.  # noqa: E501


        :return: The factory_reset of this WebhookVisit.  # noqa: E501
        """
        return self._factory_reset

    @factory_reset.setter
    def factory_reset(self, factory_reset: FactoryResetResult):
        """Sets the factory_reset of this WebhookVisit.


        :param factory_reset: The factory_reset of this WebhookVisit.  # noqa: E501
        """

        self._factory_reset = factory_reset

    @property
    def jailbroken(self) -> JailbrokenResult:
        """Gets the jailbroken of this WebhookVisit.  # noqa: E501


        :return: The jailbroken of this WebhookVisit.  # noqa: E501
        """
        return self._jailbroken

    @jailbroken.setter
    def jailbroken(self, jailbroken: JailbrokenResult):
        """Sets the jailbroken of this WebhookVisit.


        :param jailbroken: The jailbroken of this WebhookVisit.  # noqa: E501
        """

        self._jailbroken = jailbroken

    @property
    def frida(self) -> FridaResult:
        """Gets the frida of this WebhookVisit.  # noqa: E501


        :return: The frida of this WebhookVisit.  # noqa: E501
        """
        return self._frida

    @frida.setter
    def frida(self, frida: FridaResult):
        """Sets the frida of this WebhookVisit.


        :param frida: The frida of this WebhookVisit.  # noqa: E501
        """

        self._frida = frida

    @property
    def ip_blocklist(self) -> IpBlockListResult:
        """Gets the ip_blocklist of this WebhookVisit.  # noqa: E501


        :return: The ip_blocklist of this WebhookVisit.  # noqa: E501
        """
        return self._ip_blocklist

    @ip_blocklist.setter
    def ip_blocklist(self, ip_blocklist: IpBlockListResult):
        """Sets the ip_blocklist of this WebhookVisit.


        :param ip_blocklist: The ip_blocklist of this WebhookVisit.  # noqa: E501
        """

        self._ip_blocklist = ip_blocklist

    @property
    def tor(self) -> TorResult:
        """Gets the tor of this WebhookVisit.  # noqa: E501


        :return: The tor of this WebhookVisit.  # noqa: E501
        """
        return self._tor

    @tor.setter
    def tor(self, tor: TorResult):
        """Sets the tor of this WebhookVisit.


        :param tor: The tor of this WebhookVisit.  # noqa: E501
        """

        self._tor = tor

    @property
    def privacy_settings(self) -> PrivacySettingsResult:
        """Gets the privacy_settings of this WebhookVisit.  # noqa: E501


        :return: The privacy_settings of this WebhookVisit.  # noqa: E501
        """
        return self._privacy_settings

    @privacy_settings.setter
    def privacy_settings(self, privacy_settings: PrivacySettingsResult):
        """Sets the privacy_settings of this WebhookVisit.


        :param privacy_settings: The privacy_settings of this WebhookVisit.  # noqa: E501
        """

        self._privacy_settings = privacy_settings

    @property
    def virtual_machine(self) -> VirtualMachineResult:
        """Gets the virtual_machine of this WebhookVisit.  # noqa: E501


        :return: The virtual_machine of this WebhookVisit.  # noqa: E501
        """
        return self._virtual_machine

    @virtual_machine.setter
    def virtual_machine(self, virtual_machine: VirtualMachineResult):
        """Sets the virtual_machine of this WebhookVisit.


        :param virtual_machine: The virtual_machine of this WebhookVisit.  # noqa: E501
        """

        self._virtual_machine = virtual_machine

    @property
    def vpn(self) -> VpnResult:
        """Gets the vpn of this WebhookVisit.  # noqa: E501


        :return: The vpn of this WebhookVisit.  # noqa: E501
        """
        return self._vpn

    @vpn.setter
    def vpn(self, vpn: VpnResult):
        """Sets the vpn of this WebhookVisit.


        :param vpn: The vpn of this WebhookVisit.  # noqa: E501
        """

        self._vpn = vpn

    @property
    def proxy(self) -> ProxyResult:
        """Gets the proxy of this WebhookVisit.  # noqa: E501


        :return: The proxy of this WebhookVisit.  # noqa: E501
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy: ProxyResult):
        """Sets the proxy of this WebhookVisit.


        :param proxy: The proxy of this WebhookVisit.  # noqa: E501
        """

        self._proxy = proxy

    @property
    def tampering(self) -> TamperingResult:
        """Gets the tampering of this WebhookVisit.  # noqa: E501


        :return: The tampering of this WebhookVisit.  # noqa: E501
        """
        return self._tampering

    @tampering.setter
    def tampering(self, tampering: TamperingResult):
        """Sets the tampering of this WebhookVisit.


        :param tampering: The tampering of this WebhookVisit.  # noqa: E501
        """

        self._tampering = tampering

    @property
    def raw_device_attributes(self) -> RawDeviceAttributesResult:
        """Gets the raw_device_attributes of this WebhookVisit.  # noqa: E501


        :return: The raw_device_attributes of this WebhookVisit.  # noqa: E501
        """
        return self._raw_device_attributes

    @raw_device_attributes.setter
    def raw_device_attributes(self, raw_device_attributes: RawDeviceAttributesResult):
        """Sets the raw_device_attributes of this WebhookVisit.


        :param raw_device_attributes: The raw_device_attributes of this WebhookVisit.  # noqa: E501
        """

        self._raw_device_attributes = raw_device_attributes

    @property
    def high_activity(self) -> HighActivityResult:
        """Gets the high_activity of this WebhookVisit.  # noqa: E501


        :return: The high_activity of this WebhookVisit.  # noqa: E501
        """
        return self._high_activity

    @high_activity.setter
    def high_activity(self, high_activity: HighActivityResult):
        """Sets the high_activity of this WebhookVisit.


        :param high_activity: The high_activity of this WebhookVisit.  # noqa: E501
        """

        self._high_activity = high_activity

    @property
    def location_spoofing(self) -> LocationSpoofingResult:
        """Gets the location_spoofing of this WebhookVisit.  # noqa: E501


        :return: The location_spoofing of this WebhookVisit.  # noqa: E501
        """
        return self._location_spoofing

    @location_spoofing.setter
    def location_spoofing(self, location_spoofing: LocationSpoofingResult):
        """Sets the location_spoofing of this WebhookVisit.


        :param location_spoofing: The location_spoofing of this WebhookVisit.  # noqa: E501
        """

        self._location_spoofing = location_spoofing

    @property
    def suspect_score(self) -> SuspectScoreResult:
        """Gets the suspect_score of this WebhookVisit.  # noqa: E501


        :return: The suspect_score of this WebhookVisit.  # noqa: E501
        """
        return self._suspect_score

    @suspect_score.setter
    def suspect_score(self, suspect_score: SuspectScoreResult):
        """Sets the suspect_score of this WebhookVisit.


        :param suspect_score: The suspect_score of this WebhookVisit.  # noqa: E501
        """

        self._suspect_score = suspect_score

    @property
    def remote_control(self) -> RemoteControlResult:
        """Gets the remote_control of this WebhookVisit.  # noqa: E501


        :return: The remote_control of this WebhookVisit.  # noqa: E501
        """
        return self._remote_control

    @remote_control.setter
    def remote_control(self, remote_control: RemoteControlResult):
        """Sets the remote_control of this WebhookVisit.


        :param remote_control: The remote_control of this WebhookVisit.  # noqa: E501
        """

        self._remote_control = remote_control

    @property
    def velocity(self) -> VelocityResult:
        """Gets the velocity of this WebhookVisit.  # noqa: E501


        :return: The velocity of this WebhookVisit.  # noqa: E501
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity: VelocityResult):
        """Sets the velocity of this WebhookVisit.


        :param velocity: The velocity of this WebhookVisit.  # noqa: E501
        """

        self._velocity = velocity

    @property
    def request_id(self) -> str:
        """Gets the request_id of this WebhookVisit.  # noqa: E501

        Unique identifier of the user's identification request.  # noqa: E501

        :return: The request_id of this WebhookVisit.  # noqa: E501
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id: str):
        """Sets the request_id of this WebhookVisit.

        Unique identifier of the user's identification request.  # noqa: E501

        :param request_id: The request_id of this WebhookVisit.  # noqa: E501
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def browser_details(self) -> BrowserDetails:
        """Gets the browser_details of this WebhookVisit.  # noqa: E501


        :return: The browser_details of this WebhookVisit.  # noqa: E501
        """
        return self._browser_details

    @browser_details.setter
    def browser_details(self, browser_details: BrowserDetails):
        """Sets the browser_details of this WebhookVisit.


        :param browser_details: The browser_details of this WebhookVisit.  # noqa: E501
        """
        if browser_details is None:
            raise ValueError("Invalid value for `browser_details`, must not be `None`")  # noqa: E501

        self._browser_details = browser_details

    @property
    def ip(self) -> str:
        """Gets the ip of this WebhookVisit.  # noqa: E501


        :return: The ip of this WebhookVisit.  # noqa: E501
        """
        return self._ip

    @ip.setter
    def ip(self, ip: str):
        """Sets the ip of this WebhookVisit.


        :param ip: The ip of this WebhookVisit.  # noqa: E501
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def ip_location(self) -> DeprecatedIPLocation:
        """Gets the ip_location of this WebhookVisit.  # noqa: E501


        :return: The ip_location of this WebhookVisit.  # noqa: E501
        """
        return self._ip_location

    @ip_location.setter
    def ip_location(self, ip_location: DeprecatedIPLocation):
        """Sets the ip_location of this WebhookVisit.


        :param ip_location: The ip_location of this WebhookVisit.  # noqa: E501
        """

        self._ip_location = ip_location

    @property
    def timestamp(self) -> int:
        """Gets the timestamp of this WebhookVisit.  # noqa: E501

        Timestamp of the event with millisecond precision in Unix time.  # noqa: E501

        :return: The timestamp of this WebhookVisit.  # noqa: E501
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: int):
        """Sets the timestamp of this WebhookVisit.

        Timestamp of the event with millisecond precision in Unix time.  # noqa: E501

        :param timestamp: The timestamp of this WebhookVisit.  # noqa: E501
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def time(self) -> datetime:
        """Gets the time of this WebhookVisit.  # noqa: E501

        Time expressed according to ISO 8601 in UTC format.  # noqa: E501

        :return: The time of this WebhookVisit.  # noqa: E501
        """
        return self._time

    @time.setter
    def time(self, time: datetime):
        """Sets the time of this WebhookVisit.

        Time expressed according to ISO 8601 in UTC format.  # noqa: E501

        :param time: The time of this WebhookVisit.  # noqa: E501
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def url(self) -> str:
        """Gets the url of this WebhookVisit.  # noqa: E501

        Page URL from which the identification request was sent.  # noqa: E501

        :return: The url of this WebhookVisit.  # noqa: E501
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this WebhookVisit.

        Page URL from which the identification request was sent.  # noqa: E501

        :param url: The url of this WebhookVisit.  # noqa: E501
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def tag(self) -> Dict[str, object]:
        """Gets the tag of this WebhookVisit.  # noqa: E501

        A customer-provided value or an object that was sent with identification request.  # noqa: E501

        :return: The tag of this WebhookVisit.  # noqa: E501
        """
        return self._tag

    @tag.setter
    def tag(self, tag: Dict[str, object]):
        """Sets the tag of this WebhookVisit.

        A customer-provided value or an object that was sent with identification request.  # noqa: E501

        :param tag: The tag of this WebhookVisit.  # noqa: E501
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def linked_id(self) -> str:
        """Gets the linked_id of this WebhookVisit.  # noqa: E501

        A customer-provided id that was sent with identification request.  # noqa: E501

        :return: The linked_id of this WebhookVisit.  # noqa: E501
        """
        return self._linked_id

    @linked_id.setter
    def linked_id(self, linked_id: str):
        """Sets the linked_id of this WebhookVisit.

        A customer-provided id that was sent with identification request.  # noqa: E501

        :param linked_id: The linked_id of this WebhookVisit.  # noqa: E501
        """

        self._linked_id = linked_id

    @property
    def confidence(self) -> Confidence:
        """Gets the confidence of this WebhookVisit.  # noqa: E501


        :return: The confidence of this WebhookVisit.  # noqa: E501
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence: Confidence):
        """Sets the confidence of this WebhookVisit.


        :param confidence: The confidence of this WebhookVisit.  # noqa: E501
        """

        self._confidence = confidence

    @property
    def visitor_found(self) -> bool:
        """Gets the visitor_found of this WebhookVisit.  # noqa: E501

        Attribute represents if a visitor had been identified before.  # noqa: E501

        :return: The visitor_found of this WebhookVisit.  # noqa: E501
        """
        return self._visitor_found

    @visitor_found.setter
    def visitor_found(self, visitor_found: bool):
        """Sets the visitor_found of this WebhookVisit.

        Attribute represents if a visitor had been identified before.  # noqa: E501

        :param visitor_found: The visitor_found of this WebhookVisit.  # noqa: E501
        """
        if visitor_found is None:
            raise ValueError("Invalid value for `visitor_found`, must not be `None`")  # noqa: E501

        self._visitor_found = visitor_found

    @property
    def first_seen_at(self) -> SeenAt:
        """Gets the first_seen_at of this WebhookVisit.  # noqa: E501


        :return: The first_seen_at of this WebhookVisit.  # noqa: E501
        """
        return self._first_seen_at

    @first_seen_at.setter
    def first_seen_at(self, first_seen_at: SeenAt):
        """Sets the first_seen_at of this WebhookVisit.


        :param first_seen_at: The first_seen_at of this WebhookVisit.  # noqa: E501
        """
        if first_seen_at is None:
            raise ValueError("Invalid value for `first_seen_at`, must not be `None`")  # noqa: E501

        self._first_seen_at = first_seen_at

    @property
    def last_seen_at(self) -> SeenAt:
        """Gets the last_seen_at of this WebhookVisit.  # noqa: E501


        :return: The last_seen_at of this WebhookVisit.  # noqa: E501
        """
        return self._last_seen_at

    @last_seen_at.setter
    def last_seen_at(self, last_seen_at: SeenAt):
        """Sets the last_seen_at of this WebhookVisit.


        :param last_seen_at: The last_seen_at of this WebhookVisit.  # noqa: E501
        """
        if last_seen_at is None:
            raise ValueError("Invalid value for `last_seen_at`, must not be `None`")  # noqa: E501

        self._last_seen_at = last_seen_at

