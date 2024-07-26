# coding: utf-8

"""
    Fingerprint Pro Server API

    Fingerprint Pro Server API allows you to get information about visitors and about individual events in a server environment. It can be used for data exports, decision-making, and data analysis scenarios. Server API is intended for server-side usage, it's not intended to be used from the client side, whether it's a browser or a mobile device.   # noqa: E501

    OpenAPI spec version: 3
    Contact: support@fingerprint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from fingerprint_pro_server_api_sdk.base_model import BaseModel


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
    def visitor_id(self):
        """Gets the visitor_id of this WebhookVisit.  # noqa: E501


        :return: The visitor_id of this WebhookVisit.  # noqa: E501
        :rtype: str
        """
        return self._visitor_id

    @visitor_id.setter
    def visitor_id(self, visitor_id):
        """Sets the visitor_id of this WebhookVisit.


        :param visitor_id: The visitor_id of this WebhookVisit.  # noqa: E501
        :type: str
        """
        if visitor_id is None:
            raise ValueError("Invalid value for `visitor_id`, must not be `None`")  # noqa: E501

        self._visitor_id = visitor_id

    @property
    def client_referrer(self):
        """Gets the client_referrer of this WebhookVisit.  # noqa: E501


        :return: The client_referrer of this WebhookVisit.  # noqa: E501
        :rtype: str
        """
        return self._client_referrer

    @client_referrer.setter
    def client_referrer(self, client_referrer):
        """Sets the client_referrer of this WebhookVisit.


        :param client_referrer: The client_referrer of this WebhookVisit.  # noqa: E501
        :type: str
        """

        self._client_referrer = client_referrer

    @property
    def user_agent(self):
        """Gets the user_agent of this WebhookVisit.  # noqa: E501


        :return: The user_agent of this WebhookVisit.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this WebhookVisit.


        :param user_agent: The user_agent of this WebhookVisit.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

    @property
    def bot(self):
        """Gets the bot of this WebhookVisit.  # noqa: E501


        :return: The bot of this WebhookVisit.  # noqa: E501
        :rtype: BotdDetectionResult
        """
        return self._bot

    @bot.setter
    def bot(self, bot):
        """Sets the bot of this WebhookVisit.


        :param bot: The bot of this WebhookVisit.  # noqa: E501
        :type: BotdDetectionResult
        """

        self._bot = bot

    @property
    def ip_info(self):
        """Gets the ip_info of this WebhookVisit.  # noqa: E501


        :return: The ip_info of this WebhookVisit.  # noqa: E501
        :rtype: IpInfoResult
        """
        return self._ip_info

    @ip_info.setter
    def ip_info(self, ip_info):
        """Sets the ip_info of this WebhookVisit.


        :param ip_info: The ip_info of this WebhookVisit.  # noqa: E501
        :type: IpInfoResult
        """

        self._ip_info = ip_info

    @property
    def incognito(self):
        """Gets the incognito of this WebhookVisit.  # noqa: E501

        Flag if user used incognito session.  # noqa: E501

        :return: The incognito of this WebhookVisit.  # noqa: E501
        :rtype: bool
        """
        return self._incognito

    @incognito.setter
    def incognito(self, incognito):
        """Sets the incognito of this WebhookVisit.

        Flag if user used incognito session.  # noqa: E501

        :param incognito: The incognito of this WebhookVisit.  # noqa: E501
        :type: bool
        """
        if incognito is None:
            raise ValueError("Invalid value for `incognito`, must not be `None`")  # noqa: E501

        self._incognito = incognito

    @property
    def root_apps(self):
        """Gets the root_apps of this WebhookVisit.  # noqa: E501


        :return: The root_apps of this WebhookVisit.  # noqa: E501
        :rtype: RootAppsResult
        """
        return self._root_apps

    @root_apps.setter
    def root_apps(self, root_apps):
        """Sets the root_apps of this WebhookVisit.


        :param root_apps: The root_apps of this WebhookVisit.  # noqa: E501
        :type: RootAppsResult
        """

        self._root_apps = root_apps

    @property
    def emulator(self):
        """Gets the emulator of this WebhookVisit.  # noqa: E501


        :return: The emulator of this WebhookVisit.  # noqa: E501
        :rtype: EmulatorResult
        """
        return self._emulator

    @emulator.setter
    def emulator(self, emulator):
        """Sets the emulator of this WebhookVisit.


        :param emulator: The emulator of this WebhookVisit.  # noqa: E501
        :type: EmulatorResult
        """

        self._emulator = emulator

    @property
    def cloned_app(self):
        """Gets the cloned_app of this WebhookVisit.  # noqa: E501


        :return: The cloned_app of this WebhookVisit.  # noqa: E501
        :rtype: ClonedAppResult
        """
        return self._cloned_app

    @cloned_app.setter
    def cloned_app(self, cloned_app):
        """Sets the cloned_app of this WebhookVisit.


        :param cloned_app: The cloned_app of this WebhookVisit.  # noqa: E501
        :type: ClonedAppResult
        """

        self._cloned_app = cloned_app

    @property
    def factory_reset(self):
        """Gets the factory_reset of this WebhookVisit.  # noqa: E501


        :return: The factory_reset of this WebhookVisit.  # noqa: E501
        :rtype: FactoryResetResult
        """
        return self._factory_reset

    @factory_reset.setter
    def factory_reset(self, factory_reset):
        """Sets the factory_reset of this WebhookVisit.


        :param factory_reset: The factory_reset of this WebhookVisit.  # noqa: E501
        :type: FactoryResetResult
        """

        self._factory_reset = factory_reset

    @property
    def jailbroken(self):
        """Gets the jailbroken of this WebhookVisit.  # noqa: E501


        :return: The jailbroken of this WebhookVisit.  # noqa: E501
        :rtype: JailbrokenResult
        """
        return self._jailbroken

    @jailbroken.setter
    def jailbroken(self, jailbroken):
        """Sets the jailbroken of this WebhookVisit.


        :param jailbroken: The jailbroken of this WebhookVisit.  # noqa: E501
        :type: JailbrokenResult
        """

        self._jailbroken = jailbroken

    @property
    def frida(self):
        """Gets the frida of this WebhookVisit.  # noqa: E501


        :return: The frida of this WebhookVisit.  # noqa: E501
        :rtype: FridaResult
        """
        return self._frida

    @frida.setter
    def frida(self, frida):
        """Sets the frida of this WebhookVisit.


        :param frida: The frida of this WebhookVisit.  # noqa: E501
        :type: FridaResult
        """

        self._frida = frida

    @property
    def ip_blocklist(self):
        """Gets the ip_blocklist of this WebhookVisit.  # noqa: E501


        :return: The ip_blocklist of this WebhookVisit.  # noqa: E501
        :rtype: IpBlockListResult
        """
        return self._ip_blocklist

    @ip_blocklist.setter
    def ip_blocklist(self, ip_blocklist):
        """Sets the ip_blocklist of this WebhookVisit.


        :param ip_blocklist: The ip_blocklist of this WebhookVisit.  # noqa: E501
        :type: IpBlockListResult
        """

        self._ip_blocklist = ip_blocklist

    @property
    def tor(self):
        """Gets the tor of this WebhookVisit.  # noqa: E501


        :return: The tor of this WebhookVisit.  # noqa: E501
        :rtype: TorResult
        """
        return self._tor

    @tor.setter
    def tor(self, tor):
        """Sets the tor of this WebhookVisit.


        :param tor: The tor of this WebhookVisit.  # noqa: E501
        :type: TorResult
        """

        self._tor = tor

    @property
    def privacy_settings(self):
        """Gets the privacy_settings of this WebhookVisit.  # noqa: E501


        :return: The privacy_settings of this WebhookVisit.  # noqa: E501
        :rtype: PrivacySettingsResult
        """
        return self._privacy_settings

    @privacy_settings.setter
    def privacy_settings(self, privacy_settings):
        """Sets the privacy_settings of this WebhookVisit.


        :param privacy_settings: The privacy_settings of this WebhookVisit.  # noqa: E501
        :type: PrivacySettingsResult
        """

        self._privacy_settings = privacy_settings

    @property
    def virtual_machine(self):
        """Gets the virtual_machine of this WebhookVisit.  # noqa: E501


        :return: The virtual_machine of this WebhookVisit.  # noqa: E501
        :rtype: VirtualMachineResult
        """
        return self._virtual_machine

    @virtual_machine.setter
    def virtual_machine(self, virtual_machine):
        """Sets the virtual_machine of this WebhookVisit.


        :param virtual_machine: The virtual_machine of this WebhookVisit.  # noqa: E501
        :type: VirtualMachineResult
        """

        self._virtual_machine = virtual_machine

    @property
    def vpn(self):
        """Gets the vpn of this WebhookVisit.  # noqa: E501


        :return: The vpn of this WebhookVisit.  # noqa: E501
        :rtype: VpnResult
        """
        return self._vpn

    @vpn.setter
    def vpn(self, vpn):
        """Sets the vpn of this WebhookVisit.


        :param vpn: The vpn of this WebhookVisit.  # noqa: E501
        :type: VpnResult
        """

        self._vpn = vpn

    @property
    def proxy(self):
        """Gets the proxy of this WebhookVisit.  # noqa: E501


        :return: The proxy of this WebhookVisit.  # noqa: E501
        :rtype: ProxyResult
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this WebhookVisit.


        :param proxy: The proxy of this WebhookVisit.  # noqa: E501
        :type: ProxyResult
        """

        self._proxy = proxy

    @property
    def tampering(self):
        """Gets the tampering of this WebhookVisit.  # noqa: E501


        :return: The tampering of this WebhookVisit.  # noqa: E501
        :rtype: TamperingResult
        """
        return self._tampering

    @tampering.setter
    def tampering(self, tampering):
        """Sets the tampering of this WebhookVisit.


        :param tampering: The tampering of this WebhookVisit.  # noqa: E501
        :type: TamperingResult
        """

        self._tampering = tampering

    @property
    def raw_device_attributes(self):
        """Gets the raw_device_attributes of this WebhookVisit.  # noqa: E501


        :return: The raw_device_attributes of this WebhookVisit.  # noqa: E501
        :rtype: RawDeviceAttributesResult
        """
        return self._raw_device_attributes

    @raw_device_attributes.setter
    def raw_device_attributes(self, raw_device_attributes):
        """Sets the raw_device_attributes of this WebhookVisit.


        :param raw_device_attributes: The raw_device_attributes of this WebhookVisit.  # noqa: E501
        :type: RawDeviceAttributesResult
        """

        self._raw_device_attributes = raw_device_attributes

    @property
    def high_activity(self):
        """Gets the high_activity of this WebhookVisit.  # noqa: E501


        :return: The high_activity of this WebhookVisit.  # noqa: E501
        :rtype: HighActivityResult
        """
        return self._high_activity

    @high_activity.setter
    def high_activity(self, high_activity):
        """Sets the high_activity of this WebhookVisit.


        :param high_activity: The high_activity of this WebhookVisit.  # noqa: E501
        :type: HighActivityResult
        """

        self._high_activity = high_activity

    @property
    def location_spoofing(self):
        """Gets the location_spoofing of this WebhookVisit.  # noqa: E501


        :return: The location_spoofing of this WebhookVisit.  # noqa: E501
        :rtype: LocationSpoofingResult
        """
        return self._location_spoofing

    @location_spoofing.setter
    def location_spoofing(self, location_spoofing):
        """Sets the location_spoofing of this WebhookVisit.


        :param location_spoofing: The location_spoofing of this WebhookVisit.  # noqa: E501
        :type: LocationSpoofingResult
        """

        self._location_spoofing = location_spoofing

    @property
    def suspect_score(self):
        """Gets the suspect_score of this WebhookVisit.  # noqa: E501


        :return: The suspect_score of this WebhookVisit.  # noqa: E501
        :rtype: SuspectScoreResult
        """
        return self._suspect_score

    @suspect_score.setter
    def suspect_score(self, suspect_score):
        """Sets the suspect_score of this WebhookVisit.


        :param suspect_score: The suspect_score of this WebhookVisit.  # noqa: E501
        :type: SuspectScoreResult
        """

        self._suspect_score = suspect_score

    @property
    def remote_control(self):
        """Gets the remote_control of this WebhookVisit.  # noqa: E501


        :return: The remote_control of this WebhookVisit.  # noqa: E501
        :rtype: RemoteControlResult
        """
        return self._remote_control

    @remote_control.setter
    def remote_control(self, remote_control):
        """Sets the remote_control of this WebhookVisit.


        :param remote_control: The remote_control of this WebhookVisit.  # noqa: E501
        :type: RemoteControlResult
        """

        self._remote_control = remote_control

    @property
    def velocity(self):
        """Gets the velocity of this WebhookVisit.  # noqa: E501


        :return: The velocity of this WebhookVisit.  # noqa: E501
        :rtype: VelocityResult
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        """Sets the velocity of this WebhookVisit.


        :param velocity: The velocity of this WebhookVisit.  # noqa: E501
        :type: VelocityResult
        """

        self._velocity = velocity

    @property
    def request_id(self):
        """Gets the request_id of this WebhookVisit.  # noqa: E501

        Unique identifier of the user's identification request.  # noqa: E501

        :return: The request_id of this WebhookVisit.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this WebhookVisit.

        Unique identifier of the user's identification request.  # noqa: E501

        :param request_id: The request_id of this WebhookVisit.  # noqa: E501
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")  # noqa: E501

        self._request_id = request_id

    @property
    def browser_details(self):
        """Gets the browser_details of this WebhookVisit.  # noqa: E501


        :return: The browser_details of this WebhookVisit.  # noqa: E501
        :rtype: BrowserDetails
        """
        return self._browser_details

    @browser_details.setter
    def browser_details(self, browser_details):
        """Sets the browser_details of this WebhookVisit.


        :param browser_details: The browser_details of this WebhookVisit.  # noqa: E501
        :type: BrowserDetails
        """
        if browser_details is None:
            raise ValueError("Invalid value for `browser_details`, must not be `None`")  # noqa: E501

        self._browser_details = browser_details

    @property
    def ip(self):
        """Gets the ip of this WebhookVisit.  # noqa: E501


        :return: The ip of this WebhookVisit.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this WebhookVisit.


        :param ip: The ip of this WebhookVisit.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

    @property
    def ip_location(self):
        """Gets the ip_location of this WebhookVisit.  # noqa: E501


        :return: The ip_location of this WebhookVisit.  # noqa: E501
        :rtype: DeprecatedIPLocation
        """
        return self._ip_location

    @ip_location.setter
    def ip_location(self, ip_location):
        """Sets the ip_location of this WebhookVisit.


        :param ip_location: The ip_location of this WebhookVisit.  # noqa: E501
        :type: DeprecatedIPLocation
        """

        self._ip_location = ip_location

    @property
    def timestamp(self):
        """Gets the timestamp of this WebhookVisit.  # noqa: E501

        Timestamp of the event with millisecond precision in Unix time.  # noqa: E501

        :return: The timestamp of this WebhookVisit.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WebhookVisit.

        Timestamp of the event with millisecond precision in Unix time.  # noqa: E501

        :param timestamp: The timestamp of this WebhookVisit.  # noqa: E501
        :type: int
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def time(self):
        """Gets the time of this WebhookVisit.  # noqa: E501

        Time expressed according to ISO 8601 in UTC format.  # noqa: E501

        :return: The time of this WebhookVisit.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this WebhookVisit.

        Time expressed according to ISO 8601 in UTC format.  # noqa: E501

        :param time: The time of this WebhookVisit.  # noqa: E501
        :type: datetime
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def url(self):
        """Gets the url of this WebhookVisit.  # noqa: E501

        Page URL from which the identification request was sent.  # noqa: E501

        :return: The url of this WebhookVisit.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookVisit.

        Page URL from which the identification request was sent.  # noqa: E501

        :param url: The url of this WebhookVisit.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def tag(self):
        """Gets the tag of this WebhookVisit.  # noqa: E501

        A customer-provided value or an object that was sent with identification request.  # noqa: E501

        :return: The tag of this WebhookVisit.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this WebhookVisit.

        A customer-provided value or an object that was sent with identification request.  # noqa: E501

        :param tag: The tag of this WebhookVisit.  # noqa: E501
        :type: dict(str, object)
        """
        if tag is None:
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501

        self._tag = tag

    @property
    def linked_id(self):
        """Gets the linked_id of this WebhookVisit.  # noqa: E501

        A customer-provided id that was sent with identification request.  # noqa: E501

        :return: The linked_id of this WebhookVisit.  # noqa: E501
        :rtype: str
        """
        return self._linked_id

    @linked_id.setter
    def linked_id(self, linked_id):
        """Sets the linked_id of this WebhookVisit.

        A customer-provided id that was sent with identification request.  # noqa: E501

        :param linked_id: The linked_id of this WebhookVisit.  # noqa: E501
        :type: str
        """

        self._linked_id = linked_id

    @property
    def confidence(self):
        """Gets the confidence of this WebhookVisit.  # noqa: E501


        :return: The confidence of this WebhookVisit.  # noqa: E501
        :rtype: Confidence
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this WebhookVisit.


        :param confidence: The confidence of this WebhookVisit.  # noqa: E501
        :type: Confidence
        """

        self._confidence = confidence

    @property
    def visitor_found(self):
        """Gets the visitor_found of this WebhookVisit.  # noqa: E501

        Attribute represents if a visitor had been identified before.  # noqa: E501

        :return: The visitor_found of this WebhookVisit.  # noqa: E501
        :rtype: bool
        """
        return self._visitor_found

    @visitor_found.setter
    def visitor_found(self, visitor_found):
        """Sets the visitor_found of this WebhookVisit.

        Attribute represents if a visitor had been identified before.  # noqa: E501

        :param visitor_found: The visitor_found of this WebhookVisit.  # noqa: E501
        :type: bool
        """
        if visitor_found is None:
            raise ValueError("Invalid value for `visitor_found`, must not be `None`")  # noqa: E501

        self._visitor_found = visitor_found

    @property
    def first_seen_at(self):
        """Gets the first_seen_at of this WebhookVisit.  # noqa: E501


        :return: The first_seen_at of this WebhookVisit.  # noqa: E501
        :rtype: SeenAt
        """
        return self._first_seen_at

    @first_seen_at.setter
    def first_seen_at(self, first_seen_at):
        """Sets the first_seen_at of this WebhookVisit.


        :param first_seen_at: The first_seen_at of this WebhookVisit.  # noqa: E501
        :type: SeenAt
        """
        if first_seen_at is None:
            raise ValueError("Invalid value for `first_seen_at`, must not be `None`")  # noqa: E501

        self._first_seen_at = first_seen_at

    @property
    def last_seen_at(self):
        """Gets the last_seen_at of this WebhookVisit.  # noqa: E501


        :return: The last_seen_at of this WebhookVisit.  # noqa: E501
        :rtype: SeenAt
        """
        return self._last_seen_at

    @last_seen_at.setter
    def last_seen_at(self, last_seen_at):
        """Sets the last_seen_at of this WebhookVisit.


        :param last_seen_at: The last_seen_at of this WebhookVisit.  # noqa: E501
        :type: SeenAt
        """
        if last_seen_at is None:
            raise ValueError("Invalid value for `last_seen_at`, must not be `None`")  # noqa: E501

        self._last_seen_at = last_seen_at

