import os
from uuid import uuid4

def rename_imagefile_to_uuid(instance, filename):
        upload_to = f'filter/'
        ext = filename.split('.')[-1]
        uuid = uuid4().hex

        if instance:
            filename = '{}.{}'.format(uuid, ext)
        else:
            filename = '{}.{}'.format(uuid, ext)
        
        return os.path.join(upload_to, filename)