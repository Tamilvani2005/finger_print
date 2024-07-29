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
from fingerprint_pro_server_api_sdk.models.products_response_identification import ProductsResponseIdentification
from fingerprint_pro_server_api_sdk.models.products_response_botd import ProductsResponseBotd
from fingerprint_pro_server_api_sdk.models.signal_response_ip_info import SignalResponseIpInfo
from fingerprint_pro_server_api_sdk.models.signal_response_incognito import SignalResponseIncognito
from fingerprint_pro_server_api_sdk.models.signal_response_root_apps import SignalResponseRootApps
from fingerprint_pro_server_api_sdk.models.signal_response_emulator import SignalResponseEmulator
from fingerprint_pro_server_api_sdk.models.signal_response_cloned_app import SignalResponseClonedApp
from fingerprint_pro_server_api_sdk.models.signal_response_factory_reset import SignalResponseFactoryReset
from fingerprint_pro_server_api_sdk.models.signal_response_jailbroken import SignalResponseJailbroken
from fingerprint_pro_server_api_sdk.models.signal_response_frida import SignalResponseFrida
from fingerprint_pro_server_api_sdk.models.signal_response_ip_blocklist import SignalResponseIpBlocklist
from fingerprint_pro_server_api_sdk.models.signal_response_tor import SignalResponseTor
from fingerprint_pro_server_api_sdk.models.signal_response_privacy_settings import SignalResponsePrivacySettings
from fingerprint_pro_server_api_sdk.models.signal_response_virtual_machine import SignalResponseVirtualMachine
from fingerprint_pro_server_api_sdk.models.signal_response_vpn import SignalResponseVpn
from fingerprint_pro_server_api_sdk.models.signal_response_proxy import SignalResponseProxy
from fingerprint_pro_server_api_sdk.models.signal_response_tampering import SignalResponseTampering
from fingerprint_pro_server_api_sdk.models.signal_response_high_activity import SignalResponseHighActivity
from fingerprint_pro_server_api_sdk.models.signal_response_location_spoofing import SignalResponseLocationSpoofing
from fingerprint_pro_server_api_sdk.models.signal_response_suspect_score import SignalResponseSuspectScore
from fingerprint_pro_server_api_sdk.models.signal_response_raw_device_attributes import SignalResponseRawDeviceAttributes
from fingerprint_pro_server_api_sdk.models.signal_response_remote_control import SignalResponseRemoteControl
from fingerprint_pro_server_api_sdk.models.signal_response_velocity import SignalResponseVelocity


class ProductsResponse(BaseModel):
    """
    Contains all information about the request identified by `requestId`, depending on the pricing plan (Pro, Pro Plus, Enterprise)

    NOTE: This class is auto generated by the swagger code generator program.

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
        'identification': 'ProductsResponseIdentification',
        'botd': 'ProductsResponseBotd',
        'ip_info': 'SignalResponseIpInfo',
        'incognito': 'SignalResponseIncognito',
        'root_apps': 'SignalResponseRootApps',
        'emulator': 'SignalResponseEmulator',
        'cloned_app': 'SignalResponseClonedApp',
        'factory_reset': 'SignalResponseFactoryReset',
        'jailbroken': 'SignalResponseJailbroken',
        'frida': 'SignalResponseFrida',
        'ip_blocklist': 'SignalResponseIpBlocklist',
        'tor': 'SignalResponseTor',
        'privacy_settings': 'SignalResponsePrivacySettings',
        'virtual_machine': 'SignalResponseVirtualMachine',
        'vpn': 'SignalResponseVpn',
        'proxy': 'SignalResponseProxy',
        'tampering': 'SignalResponseTampering',
        'high_activity': 'SignalResponseHighActivity',
        'location_spoofing': 'SignalResponseLocationSpoofing',
        'suspect_score': 'SignalResponseSuspectScore',
        'raw_device_attributes': 'SignalResponseRawDeviceAttributes',
        'remote_control': 'SignalResponseRemoteControl',
        'velocity': 'SignalResponseVelocity'
    }

    attribute_map = {
        'identification': 'identification',
        'botd': 'botd',
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
        'high_activity': 'highActivity',
        'location_spoofing': 'locationSpoofing',
        'suspect_score': 'suspectScore',
        'raw_device_attributes': 'rawDeviceAttributes',
        'remote_control': 'remoteControl',
        'velocity': 'velocity'
    }

    def __init__(self, identification=None, botd=None, ip_info=None, incognito=None, root_apps=None, emulator=None, cloned_app=None, factory_reset=None, jailbroken=None, frida=None, ip_blocklist=None, tor=None, privacy_settings=None, virtual_machine=None, vpn=None, proxy=None, tampering=None, high_activity=None, location_spoofing=None, suspect_score=None, raw_device_attributes=None, remote_control=None, velocity=None):  # noqa: E501
        """ProductsResponse - a model defined in Swagger"""  # noqa: E501
        self._identification = None
        self._botd = None
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
        self._high_activity = None
        self._location_spoofing = None
        self._suspect_score = None
        self._raw_device_attributes = None
        self._remote_control = None
        self._velocity = None
        self.discriminator = None
        if identification is not None:
            self.identification = identification
        if botd is not None:
            self.botd = botd
        if ip_info is not None:
            self.ip_info = ip_info
        if incognito is not None:
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
        if high_activity is not None:
            self.high_activity = high_activity
        if location_spoofing is not None:
            self.location_spoofing = location_spoofing
        if suspect_score is not None:
            self.suspect_score = suspect_score
        if raw_device_attributes is not None:
            self.raw_device_attributes = raw_device_attributes
        if remote_control is not None:
            self.remote_control = remote_control
        if velocity is not None:
            self.velocity = velocity

    @property
    def identification(self) -> ProductsResponseIdentification:
        """Gets the identification of this ProductsResponse.  # noqa: E501


        :return: The identification of this ProductsResponse.  # noqa: E501
        """
        return self._identification

    @identification.setter
    def identification(self, identification: ProductsResponseIdentification):
        """Sets the identification of this ProductsResponse.


        :param identification: The identification of this ProductsResponse.  # noqa: E501
        """

        self._identification = identification

    @property
    def botd(self) -> ProductsResponseBotd:
        """Gets the botd of this ProductsResponse.  # noqa: E501


        :return: The botd of this ProductsResponse.  # noqa: E501
        """
        return self._botd

    @botd.setter
    def botd(self, botd: ProductsResponseBotd):
        """Sets the botd of this ProductsResponse.


        :param botd: The botd of this ProductsResponse.  # noqa: E501
        """

        self._botd = botd

    @property
    def ip_info(self) -> SignalResponseIpInfo:
        """Gets the ip_info of this ProductsResponse.  # noqa: E501


        :return: The ip_info of this ProductsResponse.  # noqa: E501
        """
        return self._ip_info

    @ip_info.setter
    def ip_info(self, ip_info: SignalResponseIpInfo):
        """Sets the ip_info of this ProductsResponse.


        :param ip_info: The ip_info of this ProductsResponse.  # noqa: E501
        """

        self._ip_info = ip_info

    @property
    def incognito(self) -> SignalResponseIncognito:
        """Gets the incognito of this ProductsResponse.  # noqa: E501


        :return: The incognito of this ProductsResponse.  # noqa: E501
        """
        return self._incognito

    @incognito.setter
    def incognito(self, incognito: SignalResponseIncognito):
        """Sets the incognito of this ProductsResponse.


        :param incognito: The incognito of this ProductsResponse.  # noqa: E501
        """

        self._incognito = incognito

    @property
    def root_apps(self) -> SignalResponseRootApps:
        """Gets the root_apps of this ProductsResponse.  # noqa: E501


        :return: The root_apps of this ProductsResponse.  # noqa: E501
        """
        return self._root_apps

    @root_apps.setter
    def root_apps(self, root_apps: SignalResponseRootApps):
        """Sets the root_apps of this ProductsResponse.


        :param root_apps: The root_apps of this ProductsResponse.  # noqa: E501
        """

        self._root_apps = root_apps

    @property
    def emulator(self) -> SignalResponseEmulator:
        """Gets the emulator of this ProductsResponse.  # noqa: E501


        :return: The emulator of this ProductsResponse.  # noqa: E501
        """
        return self._emulator

    @emulator.setter
    def emulator(self, emulator: SignalResponseEmulator):
        """Sets the emulator of this ProductsResponse.


        :param emulator: The emulator of this ProductsResponse.  # noqa: E501
        """

        self._emulator = emulator

    @property
    def cloned_app(self) -> SignalResponseClonedApp:
        """Gets the cloned_app of this ProductsResponse.  # noqa: E501


        :return: The cloned_app of this ProductsResponse.  # noqa: E501
        """
        return self._cloned_app

    @cloned_app.setter
    def cloned_app(self, cloned_app: SignalResponseClonedApp):
        """Sets the cloned_app of this ProductsResponse.


        :param cloned_app: The cloned_app of this ProductsResponse.  # noqa: E501
        """

        self._cloned_app = cloned_app

    @property
    def factory_reset(self) -> SignalResponseFactoryReset:
        """Gets the factory_reset of this ProductsResponse.  # noqa: E501


        :return: The factory_reset of this ProductsResponse.  # noqa: E501
        """
        return self._factory_reset

    @factory_reset.setter
    def factory_reset(self, factory_reset: SignalResponseFactoryReset):
        """Sets the factory_reset of this ProductsResponse.


        :param factory_reset: The factory_reset of this ProductsResponse.  # noqa: E501
        """

        self._factory_reset = factory_reset

    @property
    def jailbroken(self) -> SignalResponseJailbroken:
        """Gets the jailbroken of this ProductsResponse.  # noqa: E501


        :return: The jailbroken of this ProductsResponse.  # noqa: E501
        """
        return self._jailbroken

    @jailbroken.setter
    def jailbroken(self, jailbroken: SignalResponseJailbroken):
        """Sets the jailbroken of this ProductsResponse.


        :param jailbroken: The jailbroken of this ProductsResponse.  # noqa: E501
        """

        self._jailbroken = jailbroken

    @property
    def frida(self) -> SignalResponseFrida:
        """Gets the frida of this ProductsResponse.  # noqa: E501


        :return: The frida of this ProductsResponse.  # noqa: E501
        """
        return self._frida

    @frida.setter
    def frida(self, frida: SignalResponseFrida):
        """Sets the frida of this ProductsResponse.


        :param frida: The frida of this ProductsResponse.  # noqa: E501
        """

        self._frida = frida

    @property
    def ip_blocklist(self) -> SignalResponseIpBlocklist:
        """Gets the ip_blocklist of this ProductsResponse.  # noqa: E501


        :return: The ip_blocklist of this ProductsResponse.  # noqa: E501
        """
        return self._ip_blocklist

    @ip_blocklist.setter
    def ip_blocklist(self, ip_blocklist: SignalResponseIpBlocklist):
        """Sets the ip_blocklist of this ProductsResponse.


        :param ip_blocklist: The ip_blocklist of this ProductsResponse.  # noqa: E501
        """

        self._ip_blocklist = ip_blocklist

    @property
    def tor(self) -> SignalResponseTor:
        """Gets the tor of this ProductsResponse.  # noqa: E501


        :return: The tor of this ProductsResponse.  # noqa: E501
        """
        return self._tor

    @tor.setter
    def tor(self, tor: SignalResponseTor):
        """Sets the tor of this ProductsResponse.


        :param tor: The tor of this ProductsResponse.  # noqa: E501
        """

        self._tor = tor

    @property
    def privacy_settings(self) -> SignalResponsePrivacySettings:
        """Gets the privacy_settings of this ProductsResponse.  # noqa: E501


        :return: The privacy_settings of this ProductsResponse.  # noqa: E501
        """
        return self._privacy_settings

    @privacy_settings.setter
    def privacy_settings(self, privacy_settings: SignalResponsePrivacySettings):
        """Sets the privacy_settings of this ProductsResponse.


        :param privacy_settings: The privacy_settings of this ProductsResponse.  # noqa: E501
        """

        self._privacy_settings = privacy_settings

    @property
    def virtual_machine(self) -> SignalResponseVirtualMachine:
        """Gets the virtual_machine of this ProductsResponse.  # noqa: E501


        :return: The virtual_machine of this ProductsResponse.  # noqa: E501
        """
        return self._virtual_machine

    @virtual_machine.setter
    def virtual_machine(self, virtual_machine: SignalResponseVirtualMachine):
        """Sets the virtual_machine of this ProductsResponse.


        :param virtual_machine: The virtual_machine of this ProductsResponse.  # noqa: E501
        """

        self._virtual_machine = virtual_machine

    @property
    def vpn(self) -> SignalResponseVpn:
        """Gets the vpn of this ProductsResponse.  # noqa: E501


        :return: The vpn of this ProductsResponse.  # noqa: E501
        """
        return self._vpn

    @vpn.setter
    def vpn(self, vpn: SignalResponseVpn):
        """Sets the vpn of this ProductsResponse.


        :param vpn: The vpn of this ProductsResponse.  # noqa: E501
        """

        self._vpn = vpn

    @property
    def proxy(self) -> SignalResponseProxy:
        """Gets the proxy of this ProductsResponse.  # noqa: E501


        :return: The proxy of this ProductsResponse.  # noqa: E501
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy: SignalResponseProxy):
        """Sets the proxy of this ProductsResponse.


        :param proxy: The proxy of this ProductsResponse.  # noqa: E501
        """

        self._proxy = proxy

    @property
    def tampering(self) -> SignalResponseTampering:
        """Gets the tampering of this ProductsResponse.  # noqa: E501


        :return: The tampering of this ProductsResponse.  # noqa: E501
        """
        return self._tampering

    @tampering.setter
    def tampering(self, tampering: SignalResponseTampering):
        """Sets the tampering of this ProductsResponse.


        :param tampering: The tampering of this ProductsResponse.  # noqa: E501
        """

        self._tampering = tampering

    @property
    def high_activity(self) -> SignalResponseHighActivity:
        """Gets the high_activity of this ProductsResponse.  # noqa: E501


        :return: The high_activity of this ProductsResponse.  # noqa: E501
        """
        return self._high_activity

    @high_activity.setter
    def high_activity(self, high_activity: SignalResponseHighActivity):
        """Sets the high_activity of this ProductsResponse.


        :param high_activity: The high_activity of this ProductsResponse.  # noqa: E501
        """

        self._high_activity = high_activity

    @property
    def location_spoofing(self) -> SignalResponseLocationSpoofing:
        """Gets the location_spoofing of this ProductsResponse.  # noqa: E501


        :return: The location_spoofing of this ProductsResponse.  # noqa: E501
        """
        return self._location_spoofing

    @location_spoofing.setter
    def location_spoofing(self, location_spoofing: SignalResponseLocationSpoofing):
        """Sets the location_spoofing of this ProductsResponse.


        :param location_spoofing: The location_spoofing of this ProductsResponse.  # noqa: E501
        """

        self._location_spoofing = location_spoofing

    @property
    def suspect_score(self) -> SignalResponseSuspectScore:
        """Gets the suspect_score of this ProductsResponse.  # noqa: E501


        :return: The suspect_score of this ProductsResponse.  # noqa: E501
        """
        return self._suspect_score

    @suspect_score.setter
    def suspect_score(self, suspect_score: SignalResponseSuspectScore):
        """Sets the suspect_score of this ProductsResponse.


        :param suspect_score: The suspect_score of this ProductsResponse.  # noqa: E501
        """

        self._suspect_score = suspect_score

    @property
    def raw_device_attributes(self) -> SignalResponseRawDeviceAttributes:
        """Gets the raw_device_attributes of this ProductsResponse.  # noqa: E501


        :return: The raw_device_attributes of this ProductsResponse.  # noqa: E501
        """
        return self._raw_device_attributes

    @raw_device_attributes.setter
    def raw_device_attributes(self, raw_device_attributes: SignalResponseRawDeviceAttributes):
        """Sets the raw_device_attributes of this ProductsResponse.


        :param raw_device_attributes: The raw_device_attributes of this ProductsResponse.  # noqa: E501
        """

        self._raw_device_attributes = raw_device_attributes

    @property
    def remote_control(self) -> SignalResponseRemoteControl:
        """Gets the remote_control of this ProductsResponse.  # noqa: E501


        :return: The remote_control of this ProductsResponse.  # noqa: E501
        """
        return self._remote_control

    @remote_control.setter
    def remote_control(self, remote_control: SignalResponseRemoteControl):
        """Sets the remote_control of this ProductsResponse.


        :param remote_control: The remote_control of this ProductsResponse.  # noqa: E501
        """

        self._remote_control = remote_control

    @property
    def velocity(self) -> SignalResponseVelocity:
        """Gets the velocity of this ProductsResponse.  # noqa: E501


        :return: The velocity of this ProductsResponse.  # noqa: E501
        """
        return self._velocity

    @velocity.setter
    def velocity(self, velocity: SignalResponseVelocity):
        """Sets the velocity of this ProductsResponse.


        :param velocity: The velocity of this ProductsResponse.  # noqa: E501
        """

        self._velocity = velocity

