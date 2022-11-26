[amount, sender], receiver = map(int, input().split()), []
for _ in range(amount): receiver.append(int(input()))
received = {sender-1}
while (receiver[sender-1] and receiver[sender-1]-1 not in received):
    received.add(receiver[sender-1]-1)
    sender = receiver[sender-1]
print(len(received))
# Passed