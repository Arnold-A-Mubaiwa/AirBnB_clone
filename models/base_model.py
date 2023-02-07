#!/usr/bin/python3
import uuid
import datetime


class BaseModel():

    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.datetime().now().isoformat("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.datetime().now().isoformat("%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        return __class__ + self.id +self.__dict__
    
    def save(self):
        self.updated_at = datetime.datetime().now().isoformat("%Y-%m-%dT%H:%M:%S.%f")

    