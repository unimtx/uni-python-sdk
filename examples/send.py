from uni.client import UniClient
from uni.exception import UniException

def example():
  client = UniClient("your access key id", "your access key secret")

  try:
    res = client.messages.send({
      "to": "your phone number", # in E.164 format
      "signature": "your sender name",
      "content": "Your verification code is 2048."
    })
    print(res.data)
  except UniException as e:
    print(e)

if __name__ == '__main__':
    example()
