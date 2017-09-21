"""
Medium Challenge 1 from Microsoft Competition at WashU (10 min)

Moon Box | 2 point(s)

Sending a message to the moon from Earth incurs a lot of latency. Because of this, we don't want to
do a handshake, yet we still want to ensure the correct message is received. To do that, we'll have
five machines send each message. Each message will be sent to a corresponding machine on the moon.
Those five machines on the moon will receive the messages and come to a consensus agreement on what
the original message was. The consensus will be based on a simple majority.

Input definition

An input file for this problem will contain five lines representing the messages received by the
fives machines. Each line will contain the message received by the machine corresponding to that
line number. For example, if machine 2 received the message 'Hello!', the second line of the input
would read "Hello!" .

Each message will be separated by a newline.

Output definition

Your output should have two lines. The first line should be the correct message that was sent from
Earth. The second line should state the number of machines on the moon that received the correct
message.

Example input

Alpha Bravo Charlie
Alpha Bravo Charlie
Alpha Bravo Charlie
Alppa Bravo Charlie
Alpha Bravo Charlie
Example output

Alpha Bravo Charlie
4
"""

if __name__ == "__main__":
    inp = """Alpha Bravo Charlie
Alpha Bravo Charlie
Alpha Bravo Charlie
Alppa Bravo Charlie
Alpha Bravo Charlie"""

    messages = inp.split("\n")

    ht = {}

    for msg in messages:
        if msg in ht:
            ht[msg] += 1
        else:
            ht[msg] = 1

    most_received_msg = ""
    num_times_msg_received = 0
    for msg in ht:
        if ht[msg] > num_times_msg_received:
            num_times_msg_received = ht[msg]
            most_received_msg = msg

    print(msg)
    print(num_times_msg_received)