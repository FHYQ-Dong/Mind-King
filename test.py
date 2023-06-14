import network.hash

pwd = input().encode('utf-8')
HashObj = network.hash.Hash(pwd)
h = HashObj.encrypt()
print(h)
repwd = input().encode('utf-8')
HashObj = network.hash.Hash(repwd, h[:8], target=h)
print(HashObj.verify())