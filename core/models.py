from neomodel import (StringProperty, StructuredNode, IntegerProperty,
                      DateTimeProperty, BooleanProperty, UniqueIdProperty, JSONProperty, EmailProperty, RelationshipTo)


# class Device(StructuredNode):
#     uid = UniqueIdProperty()
#     device_type = StringProperty(max_length=255)
#     device_ip = StringProperty(max_length=255)
#     system_version = StringProperty(max_length=255)


# class LoginEvent(StructuredNode):
#     uid = UniqueIdProperty()
#     timestamp = StringProperty()
#     # status = StringProperty(choices={'success', 'failure'})
#     ip_address = StringProperty()
#     location = JSONProperty()
#     device_info = JSONProperty()
#     # login_duration = IntegerProperty()

# class User(StructuredNode):
#     uid = UniqueIdProperty()
#     first_name = StringProperty(required=True, max_length=255)
#     last_name = StringProperty(required=True, max_length=255)
#     email = EmailProperty(unique_index=True, required=True)
#     position = StringProperty(default='staff')
#     profile_picture = StringProperty(default='')
#     password = StringProperty(max_length=255)
#     phone = IntegerProperty()
#     party = StringProperty(max_length=255)
#     created_at = StringProperty()
#     attempts = IntegerProperty(default=0)
#     suspendedUntil = DateTimeProperty()
#     Subscription_Plan = StringProperty(default="basic")
#     IsApp = BooleanProperty(default=True)
#     device = RelationshipTo(Device, 'USES_DEVICE')
#     login_events = RelationshipTo(LoginEvent, 'LOGGED_IN')




class IpAddress(StructuredNode):
    uid = UniqueIdProperty()
    address = StringProperty(max_length=255)


class Ip(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=255, default='IP')
    ip_address = RelationshipTo(IpAddress, 'HAS_ADDRESS')


class BrowserInfo(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=255)
    version = StringProperty(max_length=255)


class Browser(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=255, default='Browser')
    browser_info = RelationshipTo(BrowserInfo, 'HAS_DETAIL')

class DeviceInfo(StructuredNode):
    uid = UniqueIdProperty()
    os = StringProperty(max_length=255)
    platform = StringProperty(max_length=255)
    source = StringProperty(max_length=255)


class Device(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=255, default='Device')
    device_info = RelationshipTo(DeviceInfo, 'HAS_DETAIL')

class LocationInfo(StructuredNode):
    uid = UniqueIdProperty()
    country = StringProperty(max_length=255)
    city = StringProperty(max_length=255)


class Location(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(max_length=255, default='Location')
    location_info = RelationshipTo(LocationInfo, 'LOCATED_IN')

class status(StructuredNode):
    uid = UniqueIdProperty()
    status = StringProperty(max_length=255)


class connection(StructuredNode):
    Uid = UniqueIdProperty()
    name = StringProperty()
    ip = RelationshipTo(Ip, 'HAS_IP')
    device = RelationshipTo(Device, 'USES_DEVICE')
    location = RelationshipTo(Location, 'ARE_FROM')
    browser = RelationshipTo(Browser, 'USES_BROWSER')

