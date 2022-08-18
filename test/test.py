from formant.sdk.agent.v1 import Client as FormantClient
fclient = FormantClient()

def handle_teleop_controls(datapoint):
    print("DATA!")
    # print(datapoint)
    print(datapoint.twist)
    import pdb
    pdb.set_trace()
    if datapoint.stream == "Buttons":
        handle_button(datapoint.bitset)
    elif datapoint.stream == "Joystick":
        print(datapoint.twist)
        handle_joystick(datapoint.twist)

fclient.register_teleop_callback(handle_teleop_controls)

print(fclient.get_teleop_info())

while(True):
    pass