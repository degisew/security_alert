from core.models import IpAddress, DeviceInfo, BrowserInfo, LocationInfo


def create_instance_and_connect(model, param_names, values, instance, connector_attribute):
    # If values is a list, unpack it; otherwise, use it as is
    args = values if isinstance(values, list) else [values]
    # connector = getattr(instance, connector_attribute, None)[0]
    # print('#####################################################################################################', connector)
    # Ensure the lengths of param_names and values match
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
    ip = pulsar_message.get('userIP')
    os = pulsar_message.get('deviceInfo').get('os')
    platform = pulsar_message.get('deviceInfo').get('platform')
    source = pulsar_message.get('deviceInfo').get('source')
    browser_name = pulsar_message.get('deviceInfo').get('browser')
    browser_version = pulsar_message.get(
        'deviceInfo').get('browserVersion')
    country = pulsar_message.get('location').get('country')
    city = pulsar_message.get('location').get('city')

    # relationship_attributes
    ip_connector = 'ip_address'
    device_connector = 'device_info'
    browser_connector = 'browser_info'
    location_connector = 'location_info'

    # parameter names
    device_params = ['os', 'platform', 'source']
    ip_params = ['address']
    browser_params = ['name', 'version']
    location_params = ['country', 'city']


    if location_infos and browser_infos and ip_addresses and device_infos:
        # Check and set flags for matching in each loop
        ip_match_found = False
        device_match_found = False
        browser_match_found = False
        location_match_found = False

        for db_ip in ip_addresses:
            if (str(ip) == str(db_ip.address)):
                ip_match_found = True
                break
        # Check if a matching IP was not found
        if not ip_match_found:
            create_instance_and_connect(
                IpAddress, ip_params, ip, ip_instance.ip_address, ip_connector)
            # ip_add = IpAddress(address=ip).save()
            # ip_instance.ip_address.connect(ip_add)

        for db_device in device_infos:
            if (str(os) == str(db_device.os)):
                device_match_found = True
                break

        if not device_match_found:
            create_instance_and_connect(
                DeviceInfo, device_params, [os, platform, source], device_instance.device_info, device_connector)
            # device = DeviceInfo(
            #     os=os, platform=platform, source=source).save()
            # device_instance.device_info.connect(device)

        for db_browser in browser_infos:
            if (str(browser_name) == str(db_browser.name)):
                browser_match_found = True
                break

        if not browser_match_found:
            create_instance_and_connect(
                BrowserInfo, browser_params, [browser_name, browser_version], browser_instance.browser_info, browser_connector)
            # browser = BrowserInfo(
            #     name=browser_name, version=browser_version).save()
            # browser_instance.browser_info.connect(browser)

        for db_location in location_infos:
            if (str(city) == str(db_location.city)):
                location_match_found = True
        if not location_match_found:
            create_instance_and_connect(
                LocationInfo, location_params, [country, city], location_instance.location_info, location_connector)
            # location = LocationInfo(country=country, city=city).save()
            # location_instance.location_info.connect(location)
    else:
        create_instance_and_connect(IpAddress, ip_params, ip, ip_instance.ip_address, ip_connector)
        create_instance_and_connect(
            DeviceInfo, device_params, [os, platform, source], device_instance.device_info, device_connector)
        create_instance_and_connect(
            BrowserInfo, browser_params, [browser_name, browser_version], browser_instance.browser_info, browser_connector)
        create_instance_and_connect(
            LocationInfo, location_params, [country, city], location_instance.location_info, location_connector)
        # ip_add = IpAddress(address=ip).save()
        # ip_instance.ip_address.connect(ip_add)
        # device = DeviceInfo(
        #             os=os, platform=platform, source=source).save()
        # device_instance.device_info.connect(device)
        # browser = BrowserInfo(
        #         name=browser_name, version=browser_version).save()
        # browser_instance.browser_info.connect(browser)
        # browser = BrowserInfo(
        #         name=browser_name, version=browser_version).save()
        # browser_instance.browser_info.connect(browser)
