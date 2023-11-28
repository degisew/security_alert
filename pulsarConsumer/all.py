# from pulsar import Client, schema

# client = Client('pulsar://localhost:6650')
# consumer = client.subscribe('negative_acks','test',schema=schema.StringSchema())
# producer = client.create_producer('negative_acks',schema=schema.StringSchema())
# for i in range(10):
#     print('send msg "hello-%d"' % i)
#     producer.send_async('hello-%d' % i, callback=None)
# producer.flush()
# for i in range(10):
#     msg = consumer.receive()
#     consumer.negative_acknowledge(msg)
#     print('receive and nack msg "%s"' % msg.data())
# for i in range(10):
#     msg = consumer.receive()
#     consumer.acknowledge(msg)
#     print('receive and ack msg "%s"' % msg.data())
# try:
#     # No more messages expected
#     msg = consumer.receive(100)
# except:
#     print("no more msg")
#     pass