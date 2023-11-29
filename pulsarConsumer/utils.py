from core.models import IpAddress, DeviceInfo, BrowserInfo, LocationInfo
from core.email import send_email


def create_instance_and_connect(model, param_names, values, instance):
    # If values is a list, unpack it; otherwise, use it as is
    args = values if isinstance(values, list) else [values]
    if len(param_names) != len(args):
        raise ValueError(
            "Number of parameter names must match the number of values")
    params = {param: value for param, value in zip(param_names, args)}
    new_instance = model(**params).save()
    instance.connect(new_instance)


def match_and_create(browser_instance, location_instance, device_instance, ip_instance, pulsar_message):
    # Fetching instances
    ip_addresses = ip_instance.ip_address.all()
    browser_infos = browser_instance.browser_info.all()
    device_infos = device_instance.device_info.all()
    location_infos = location_instance.location_info.all()

    # Unpacking pulsar message
    email = pulsar_message.get('email')
    ip = pulsar_message.get('userIP')
    os = pulsar_message.get('deviceInfo').get('os')
    platform = pulsar_message.get('deviceInfo').get('platform')
    source = pulsar_message.get('deviceInfo').get('source')
    browser_name = pulsar_message.get('deviceInfo').get('browser')
    browser_version = pulsar_message.get(
        'deviceInfo').get('browserVersion')
    country = pulsar_message.get('location').get('country')
    city = pulsar_message.get('location').get('city')

    # parameter names
    device_params = ['os', 'platform', 'source']
    ip_params = ['address']
    browser_params = ['name', 'version']
    location_params = ['country', 'city']

    if location_infos and browser_infos and ip_addresses and device_infos:
        # print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&', 'Send')
        # Check and set flags for matching in each loop
        ip_match_found = False
        device_match_found = False
        browser_match_found = False
        location_match_found = False

        for db_ip in ip_addresses:
            if (str(ip) == str(db_ip.address)):
                ip_match_found = True
                break

        for db_device in device_infos:
            if (str(os) == str(db_device.os)):
                device_match_found = True
                break

        for db_browser in browser_infos:
            if (str(browser_name) == str(db_browser.name)):
                browser_match_found = True
                break

        for db_location in location_infos:
            if (str(city) == str(db_location.city)):
                location_match_found = True
                break

        if not ip_match_found or not device_match_found or not browser_match_found or not location_match_found:
            # Create instances and connect them for non-matching data
            if not ip_match_found:
                create_instance_and_connect(
                    IpAddress, ip_params, ip, ip_instance.ip_address)

            if not device_match_found:
                create_instance_and_connect(DeviceInfo, device_params, [
                                            os, platform, source], device_instance.device_info)

            if not browser_match_found:
                create_instance_and_connect(BrowserInfo, browser_params, [
                                            browser_name, browser_version], browser_instance.browser_info)

            if not location_match_found:
                create_instance_and_connect(LocationInfo, location_params, [
                                            country, city], location_instance.location_info)

            # Email Notification Here
            send_email(email, os, city, country)

    else:
        create_instance_and_connect(
            IpAddress, ip_params, ip, ip_instance.ip_address)
        create_instance_and_connect(
            DeviceInfo, device_params, [os, platform, source], device_instance.device_info)
        create_instance_and_connect(
            BrowserInfo, browser_params, [browser_name, browser_version], browser_instance.browser_info)
        create_instance_and_connect(
            LocationInfo, location_params, [country, city], location_instance.location_info)
