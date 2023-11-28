from django.http import HttpResponse
import recordlinkage as rl
from decouple import config
import pandas as pd
import json
import requests
import re  # regx
from rest_framework.generics import CreateAPIView
from core.models import connection, status, Ip, Device, Browser, Location
# from core.models import Device, User
from core.serializers import EntitySerializer
from pulsarConsumer import consumer, producer, all


def produce(request):
    # pulsar_message = {
    #    'user_device': { 
    #     'platform': 'Linux',
    #     'os': 'Ubuntu',
    #     'source': 'tender client',
    #     'browser': 'Chrome',
    #     'browser_version': '94.0.1'
    # },
    # 'ip': '192.168.0.1',
    # 'location': {
    #     'country': 'Ethiopia',
    #     'city': 'Addis Ababa'
    # }
    # }

    # conn = connection.nodes.get_or_none(name='Addis')

    # ip = pulsar_message.get('userIP')
    # os = pulsar_message.get('user_device').get('os')
    # platform = pulsar_message.get('user_device').get('platform')
    # source = pulsar_message.get('user_device').get('source')
    # browser_name = pulsar_message.get('user_device').get('browser')
    # browser_version = pulsar_message.get('user_device').get('browserVersion')
    # country = pulsar_message.get('location').get('country')
    # city = pulsar_message.get('location').get('city')


    # if conn:
    #     #creating Instances
    #     ip = Ip(ip=ip).save()
    #     user_device = device(os=os, platform=platform, source=source).save()
    #     browser = Browser(name=browser_name, version=browser_version).save()
    #     location = Location(country=country, city=city).save()

    #     # Creating relationship
    #     conn.ip.connect(ip)
    #     conn.device.connect(user_device)
    #     conn.location.connect(location)
    #     conn.browser.connect(browser)


    # else: {
    #     print('connection not found for email: %s', pulsar_message.get('email'))
    # }
    # Status(status="Failed").save()
    # con = connection.nodes.get_or_none(Uid='addissystemsMIKnatmek167148')
    # all.all()
    # producer.produce_message()
    # consumer.consume_message()
    return HttpResponse("con")
# def create(request):
#     URL = 'https://account.qa.addissystems.et/Account'
#     data = requests.get(URL)
#     objs = json.loads(data.text)
#     for obj in objs:
#         user = User(first_name=obj.get('Fname'), last_name=obj.get('Lname'), email=obj.get('email'), position=obj.get('Position', ''), password=obj.get('password'), profile_picture=obj.get('profilePicture'), created_at=obj.get('DateCreated'), phone=obj.get('phone'),
#                     party=obj.get('party'), Subscription_Plan=obj.get('Subscription_Plan'), attempts=obj.get('attempts'), suspendedUntil=obj.get('suspendedUntil'), IsApp=obj.get('IsApp')).save()
#         device = Device(device_ip=obj.get('device', {}).get('deviceIP'), device_type=obj.get(
#             'device', {}).get('deviceType'), system_version=obj.get('device', {}).get('systemVersion')).save()
#         # Establish the relationship
#         user.device.connect(device)

#     devices = Device.nodes.all()
#     return HttpResponse(devices)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# class MatchAPIView(CreateAPIView):
#     serializer_class = EntitySerializer
#     def get_queryset(self):
#         return self.request.data
#     def process_data(self, cleaned_data):
#         first_name = re.sub(
#             r'[\W\d_\\\.@#$%^&*~]+', '', cleaned_data['first_name'].strip().lower())
#         middle_name = re.sub(
#             r'[\W\d_\\\.@#$%^&*~]+', '', cleaned_data['middle_name'].strip().lower())
#         last_name = re.sub(
#             r'[\W\d_\\\.@#$%^&*~]+', '', cleaned_data['last_name'].strip().lower())
#         email = cleaned_data[r'email'].strip().lower()
#         phone = re.sub(r'[\D_]+', '', cleaned_data['phone'].strip())
#         location = re.sub(r'[\W\d_\\\.@#$%^&*~]+', '',
#                             cleaned_data['location'].strip().lower())
#         address = re.sub(r'[\W\d_,[\]./#]+', '',
#                             cleaned_data['address'].strip().lower())
#         birth_date = re.sub(r'[a-zA-Z_\.@#$%^&*~]', '',
#                             str(cleaned_data['birth_date']))
#         gender = re.sub(r'[\d_\\\.@#$%^&*~]+', '',
#                         cleaned_data['gender'].strip().lower())

#         # Pass for matching
#         self.matching_data()

#     def matching_data(self, processed_data):
#         # Getting reference data
#         users = ReferenceData.objects.all().values()

#         # Process data into a DataFrame
#         reference_data = pd.DataFrame.from_dict(users)
#         source_data = pd.DataFrame.from_dict([processed_data])

#         # Indexing Records
#         indexer = rl.Index()
#         indexer.full()
#         pairs = indexer.index(reference_data, source_data)
#         # print(pairs)

#         # Define the comparison step
#         compare = rl.Compare()
#         compare.exact("first_name", "first_name", label="first_name")
#         compare.exact("middle_name", "middle_name", label="middle_name")
#         compare.exact("last_name", "last_name", label="last_name")
#         compare.exact("email", "email", label="email")
#         compare.exact('phone', 'phone', label='phone')
#         compare.string('address', 'address', method='jarowinkler', threshold=0.85, label='address')
#         compare.exact("birth_date", "birth_date", label="birth_date")
#         compare.string("gender", "gender", label="gender")
#         compare.string("location", "location", label="location")
#         features = compare.compute(pairs, reference_data, source_data)

#         # Classification step
#         matches = features[features.sum(axis=1) > 7]
#         print('#################################')
#         print(len(matches))
#         print(features)
#         print('#################################')
#         return len(matches)

#     def perform_create(self, serializer:EntitySerializer):
#         deserialized_data = serializer.validated_data
#         self.process_data(deserialized_data)
#         serializer.save()
