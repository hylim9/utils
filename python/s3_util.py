import boto3
from django.conf import settings
from botocore.exceptions import ClientError
from dataclasses import dataclass


# @dataclass
class S3Utils:
    # bucket_name: str
    # s3_resource: object = boto3.resource("s3")
    # __s3_bucket: object = s3_resource.Bucket(bucket_name)

    def __init__(self, bucket_name):
        s3_resource = boto3.resource(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_ID,
            aws_secret_access_key=settings.AWS_ACCESS_KEY,
        )
        self.bucket_name = bucket_name
        self.s3_resource = s3_resource
        self.__s3_bucket = s3_resource.Bucket(bucket_name)

    def upload_s3_fileobj(self, s3_path, file):
        try:
            obj = self.__s3_bucket.upload_fileobj(
                file,
                s3_path,
                # ExtraArgs={
                #     "ContentType": content_type,
                # },
            )

            return obj
        except ClientError as exception:
            raise exception("S3 Upload Error")

    def delete_s3_fileobj(self, file_name):
        try:
            obj = self.s3_resource.Object(self.bucket_name, file_name)
            obj.delete()
        except ClientError as exception:
            raise exception("S3 Delete Error")

    def get_s3_fileobj(self, s3_path):
        try:
            objs = self.__s3_bucket.objects.filter(Prefix=s3_path)

            filename = None
            for obj in objs:
                import os

                path, filename = os.path.split(obj.key)

            return filename
        except ClientError as exception:
            raise exception("S3 FILE GET Error")
