import time

def cristians_algorithm(client_request_time, server_response_time, server_time_string):
    """
    Calculates the synchronized time on a client based on Cristian's Algorithm.
    
    :param client_request_time: Time (T0) when the client sent the request
    :param server_response_time: Time (T1) when the client received the server response
    :param server_time_string: The exact time the server sent, as a timestamp
    :return: Synchronized client time
    """
    
    # 1. Calculate Round Trip Time (RTT)
    round_trip_time = server_response_time - client_request_time
    # 10-5=5 
    # 2. Assume network delay is symmetrical, so client-server path took RTT / 2
    estimated_propagation_delay = round_trip_time / 2
    
    # 3. Calculate corrected time
    # Estimated current time = Server time + propagation delay
    estimated_client_time = server_time_string + estimated_propagation_delay
    
    return estimated_client_time

# --- Example Usage ---
# T0: Client sends request at epoch 160000.000 seconds
t0 = 5

# Server receives request and responds with its time (e.g., 160000.010)
server_sent_time = 8.5

# T1: Client gets the response back 
t1 = 10

# Sync the client
corrected_time = cristians_algorithm(t0, t1, server_sent_time)

print(f"Original Server Timestamp: {server_sent_time}")
print(f"Synchronized Client Time:  {corrected_time}")

if __name__ == '__main__':
    # Example usage of the algorithm
    t0 = time.time()  # Client sends request
    time.sleep(0.01)  # Simulate network delay
    server_time = time.time()  # Server sends response
    time.sleep(0.01)  # Simulate network delay
    t1 = time.time()  # Client receives response
    
    corrected_time = cristians_algorithm(t0, t1, server_time)
    
    print(f"Original Server Timestamp: {server_time}")
    print(f"Synchronized Client Time:  {corrected_time}")