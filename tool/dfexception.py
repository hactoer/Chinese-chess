class NotSimplfiedException(Exception):
    def __init__(self,message,data):
        self.message=message
        self.d=data
    def __str__(self):
        return f'NotSimplfiedException:{self.message},Data:{[t for t in self.d]})'
class OutSideTheLimit(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return f'OutSideTheLimit:{self.message}'