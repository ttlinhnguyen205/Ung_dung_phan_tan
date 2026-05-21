import pika


def fib(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="localhost")
)

channel = connection.channel()
channel.queue_declare(queue="rpc_queue")


def on_request(ch, method, props, body):
    n = int(body)

    print(f"Received RPC request: fib({n})")

    response = fib(n)

    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(
            correlation_id=props.correlation_id
        ),
        body=str(response)
    )

    ch.basic_ack(delivery_tag=method.delivery_tag)

    print(f"Sent RPC response: {response}")


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

print("RabbitMQ RPC Server is waiting for requests...")
channel.start_consuming()