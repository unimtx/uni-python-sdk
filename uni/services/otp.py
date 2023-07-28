class OtpService(object):

  def __init__(self, client):
    self.client = client

  def send(self, params):
    return self.client.request("otp.send", params)

  def verify(self, params):
    res = self.client.request("otp.verify", params)
    res.valid = res.data != None and res.data["valid"]
    return res
