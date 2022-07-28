import pika

#Initialitation connection in rabbitmq use pika
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

#channel() here is showing the connection is localhost
channel = connection.channel()

#declaration of queue name, here is 'myBowl'
channel.queue_declare(queue='myBowl')

#give message from Publish message exchange to queue later
message = "Hello this is my first message in my bowl"

#Initialitation exchange, routing key and the contents of the body, namely the message itself
channel.basic_publish(exchange='', routing_key='myBowl', body=message)

print(f"Sent Message: {message}")

#every time you make a connection using the pika library, you must close the connection
connection.close()