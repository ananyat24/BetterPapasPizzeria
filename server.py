import socket
from _thread import *
from constants import Constants
import json
      
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c = Constants()

HOST_IP = c.HOST_IP
HOST_PORT = c.HOST_PORT
ENCODER = c.ENCODER

try:
    server_socket.bind((HOST_IP, HOST_PORT))
except socket.error as e:
    str(e)

server_socket.listen()
print("Waiting for a connection, Server Started")

role = ["chef", "waiter"]
stored_data = {"to_send_to_chef": None, "to_send_to_waiter": None}

def threaded_client(conn, player):
    # conn.send(str.encode(make_pos(pos[player])))
    reply = " "
    while True:
        print("server has been accessed")
        try:
            data = json.loads(conn.recv(2048).decode(ENCODER))

            # print(data["data"]["color"])

            if not data:
                print("Disconnected")
                break

            else:
                print("checking stages")
                
                if data["stage"] == "selection":

                    if data["key"] == "left":
                        data["role"] = "waiter"
                        if "waiter" in data["remaining_roles"]:
                            data["remaining_roles"].remove("waiter")
                        # data["key"] = None
                    
                    if data["key"] == "right":
                        data["role"] = "chef"
                        # print('MAKING ROLE CHEF')
                        if "chef" in data["remaining_roles"]:
                            data["remaining_roles"].remove("chef")
                        # data["key"] = None

                    if data["key"] == "continue":
                        # print("in continue")
                        if data["role"] == "waiter":
                            data["stage"] = "waiter1"
                            data["key"] = None

                        if data["role"] == "chef":
                            data["stage"] = "chef1"
                            data["key"] = None
                           #  print("chef stage beginning")

                    reply = json.dumps(data)
                
                    conn.send(reply.encode(ENCODER))
                        
                else:
                    print("in the right place!")
                    if(data["to_send_to_chef"]):
                        stored_data["to_send_to_chef"] = data["to_send_to_chef"]
                    if(data["to_send_to_waiter"]):
                        stored_data["to_send_to_waiter"] = data["to_send_to_waiter"]
                    
                    data = {"stage": "in_level", "to_send_to_chef": stored_data["to_send_to_chef"], "to_send_to_waiter": stored_data["to_send_to_waiter"]}
                    reply = json.dumps(data)

                    print(data)

                    conn.sendall(reply.encode(ENCODER))

                # if data["key"] == "left":
                #     data["role"] = "waiter"
                #     data["remaining_roles"].remove("waiter")
                #     data["stage"] = "waiter1"
                
                # if data["key"] == "right":
                #     data["role"] = "chef"
                #     data["remaining_roles"].remove("chef")
                #     data["stage"] = "chef1"

                        

                # if data["key"] == "left":
                #     data["role"] = "waiter"
                #     data["remaining_roles"].remove("waiter")
                #     data["stage"] = "waiter1"
                
                # if data["key"] == "right":
                #     data["role"] = "chef"
                #     data["remaining_roles"].remove("chef")
                #     data["stage"] = "chef1"

                        

                # print(data["data"]["color"])
 
                # reply = role[player]

                # print ("Recieved: ", data)
                # print("Sending: ", reply)

                

        except:
            break
 
    print("Lost connection")
    conn.close()

currentPlayer = 0

while True:
    conn, addr = server_socket.accept()
    print("Connected to:", addr)
    # conn.send(role[currentPlayer].encode(ENCODER))
    # print(role[currentPlayer])
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1



    



# while True:
#     conn, addr = server_socket.accept()


    
#     try:
#         data = json.loads(conn.recv(2048).decode(ENCODER))


#         if not data:
#             print("Disconnected")
#             break

#         else:
                
#             if data["data"]["key"] == "left":
#                 data["data"]["color"] = "red"
                    
#             if data["data"]["key"] == "right":
#                 data["data"]["color"] = "blue"

#             print(data["data"]["color"])
    
#                     # reply = role[player]

#                     # print ("Recieved: ", data)
#                     # print("Sending: ", reply)

#             reply = json.dumps(data)
                    
#             conn.send(reply.encode(ENCODER))

#     except:
#         break
 
#     print("Lost connection")
#     conn.close()