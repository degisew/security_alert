# from pulsar import Client, Message
# from decouple import config


# def produce_message():
#     client = Client(config('PULSAR_URL'))
#     producer = client.create_producer('er-topic')

#     for i in range(10):
#         message= f'Message {i}'.encode('utf-8')  # Convert string to bytes
#         producer.send(message)
#         producer.send("Hello".encode('utf-8'))
    
#     print("Producing Message")
#     client.close()


