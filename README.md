# clientserver-daniel
# Client server
# Flow:

    # Client 
        - gui (Main thread) - (Input)  recive cmd from User
      - (Secound Thread) recive cmd from Gui in english (What is my ip?)
      - send cmd to server

    # Server
        - recive cmd from client
        - Translate cmd to Windows cmd
        - Send cmd to User

    # Client
        - recive cmd from server
        - show cmd to user
        - send cmd to server