# python 2.7
# $java PingServer port
# $python PingClient.py host port (for Python)
from socket import *
import sys
import time
import math

# Get command line argument.
if len(sys.argv) != 3:
    print 'Required arguments: port'
    exit()

serverHost = sys.argv[1]
serverPort = int(sys.argv[2])
#print serverHost
#print serverPort

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(3)

rtt_list = []

# Send 10 pings to the server.
# MESSAGE FORMAT: PING sequence_number time CRLF
for num in range(0, 10):
    try:
        time_send = time.time()
        time_tup = time.localtime(time_send)
        time_fmt = '%Y-%m-%d_%a_%H-%M-%S'
        time_curr = time.strftime(time_fmt, time_tup)

        message = 'PING ' + str(num) + ' ' + time_curr + ' \r\n'
        
        clientSocket.sendto(message, (serverHost, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        time_recv = time.time()
        # Wait two seconds
        time.sleep(2)

    except timeout:
        print 'ping to ' + serverHost +', seq = ' + str(num) + ', rtt = time out'
        
    else:
        rtt_in_ms = round(time_recv - time_send, 3) * 1000
        rtt_list.append(rtt_in_ms)
        print 'ping to ' + serverHost +', seq = ' + str(num) + ', rtt = ' + str(rtt_in_ms) + 'ms'

max_rtt = -1000
min_rtt = 1000
for rtt_num in rtt_list:
    # Compute sum
    sum =+ rtt_num

    # Find the max rtt
    if (rtt_num > max_rtt):
        max_rtt = rtt_num
    
    # Find the min rtt
    if (rtt_num < min_rtt):
        min_rtt = rtt_num

avrg_rtt = float(sum / len(rtt_list))

print '\nAverage RTT: ' + str(avrg_rtt) + 'ms'
print 'Maximum RTT: ' + str(max_rtt) + 'ms'
print 'Minimum RTT: ' + str(min_rtt) + 'ms'



        
