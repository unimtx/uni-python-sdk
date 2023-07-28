from uni.client import UniClient
from uni.exception import UniException

def example():
  client = UniClient("your access key id", "your access key secret")

  # send a verification code to a recipient
  try:
    res = client.otp.send({
      "to": "your phone number" # in E.164 format
    })
    print(res.data)
  except UniException as e:
    print(e)

  # verify a verification code
  try:
    res = client.otp.verify({
      "to": "your phone number", # in E.164 format
      "code": "the code you received"
    })
    print(res.valid)
  except UniException as e:
    print(e)

if __name__ == '__main__':
    example()
