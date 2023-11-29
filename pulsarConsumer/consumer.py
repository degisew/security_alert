import datetime
from pulsar import Client, ConsumerType
from decouple import config
from avro.io import DatumReader, BinaryDecoder
import io
from core.models import connection, Ip, Device, Location, Browser
from pulsarConsumer.schema import parsed_schema
from .utils import match_and_create
# from core.models import User, LoginEvent
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def pulsar_consumer():
    # Set up your Pulsar client
    # client = Client(config('PULSAR_URL'))
    client = Client(config('PULSAR'))

    consumer = client.subscribe(
        config('PULSAR_TOPIC'), 'entity-subscription', consumer_type=ConsumerType.Shared)
    try:
        while True:
            message = consumer.receive()
            message_bytes = message.data()
            # Deserialize Avro message
            reader = DatumReader(parsed_schema)
            decoder = BinaryDecoder(io.BytesIO(message_bytes))
            pulsar_message = reader.read(decoder)
            # print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$', pulsar_message) # working
            # Log consumer position
            logger.info('Consumer position after processing message: %s',
                        consumer.get_last_message_id())

            # Get data from the graph DB
            # conn = connection.nodes.get_or_none(email='user@example.com')
            uid = pulsar_message.get('uid')
            conn_instance = connection.nodes.get_or_none(Uid=uid)

            if all(getattr(conn_instance, attr) for attr in ['browser', 'location', 'device', 'ip']):
                browser_instance = conn_instance.browser[0]
                location_instance = conn_instance.location[0]
                device_instance = conn_instance.device[0]
                ip_instance = conn_instance.ip[0]
                match_and_create(browser_instance, location_instance, device_instance, ip_instance, pulsar_message)
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                
            else:
                print('######## Else')
                # Creating Instances
                ip_instance = Ip(name='IP').save()
                device_instance = Device(name='Device').save()
                browser_instance = Browser(name='Browser').save()
                location_instance = Location(name='Location').save()

                # Creating relationship
                conn_instance.ip.connect(ip_instance)
                conn_instance.device.connect(device_instance)
                conn_instance.location.connect(location_instance)
                conn_instance.browser.connect(browser_instance)

                match_and_create(browser_instance, location_instance, device_instance, ip_instance, pulsar_message)



            # else: {
            #     logger.warning('connection not found for email: %s', pulsar_message.get('email'))
            # }

            # Process the pulsar message
            # user = User.nodes.get_or_none(email = pulsar_message.get('email'))
            # if user:
            #     login_event_data = {
            #         'timestamp': pulsar_message.get('timestamp', ''),
            #         'ip_address': pulsar_message.get('userIP', ''),
            #         'device_info': pulsar_message.get('deviceInfo', {}),
            #         'location': pulsar_message.get('location', {}),
            #     }
            #     login_event = LoginEvent(**login_event_data).save()
            #     user.login_events.connect(login_event)
            # else: {
            #     logger.warning('User not found for email: %s', pulsar_message.get('email'))
            # }
            print('#######################################################################################')
            print('Received Message:', pulsar_message)
            print('#######################################################################################')
            # Check the number of login events for the user within the current day
            # today = datetime.date.today()
            # login_events_today = user.login_events.filter(timestamp__gte=today)

            # if login_events_today.count() > 3:
            #     print("@@@@@@@@@@@@@@@@@@@@@ Detect")
            # Trigger actions, such as blocking the user or sending a security email
            # Example: user.blocked = True
            # Example: send_security_email(user)

            # Acknowledge the successful processing of the message
            consumer.acknowledge(message)
            logger.info('Consumer position after processing message: %s',
                        consumer.get_last_message_id())
    except Exception as e:
        # Message failed to be processed
        logger.error('############# Error processing Pulsar message: %s', str(e))
        consumer.negative_acknowledge(message)
    # finally:
    #     consumer.close()
    #     client.close()
