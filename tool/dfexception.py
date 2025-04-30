class NotSimplfiedException(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return f'NotSimplfiedException:{self.message}'
class OutSideTheLimit(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return f'OutSideTheLimit:{self.message}'