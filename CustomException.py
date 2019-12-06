class ErrorInCode(Exception):
    def __init__(self,data):
        self.data=data
try:
    age=118
    if age<18:
        raise ErrorInCode("ur not valid member")
except ErrorInCode as ae:
    print("Received error:", ae.data)



class ErrorInCode(Exception):
    def __init__(self, data):
        self.data = data

    def str(self):
        return repr(self.data)
try:
    raise ErrorInCode(2)
except ErrorInCode as ae:
    print("Received error:", ae.data)
