import os

import boto3

from config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME, IMG_DIR, TIMETABLES_DIR


class FileUtilFactory:

    __instance = None

    @staticmethod
    def getFileUtil():
        if FileUtilFactory.__instance is not None:
            return FileUtilFactory.__instance

        if "HEROKU" in list(os.environ.keys()):
            FileUtilFactory.__instance = S3FileUtil()
        else:
            FileUtilFactory.__instance = DiskFileUtil()

        return FileUtilFactory.__instance


class FileUtil:
    def saveImage(self, file_path, file_content):
        pass

    def getFileDescriptor(self, file_path):
        pass

    def getTimetableImagePath(self, json_path, class_profile, day_of_the_week):
        pass

    def exists(self, file_path):
        pass


class DiskFileUtil(FileUtil):
    def saveImage(self, file_path, file_content):
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(file_content.getbuffer())

    def getFileDescriptor(self, file_path):
        return open(file_path, 'rb')

    def getTimetableImagePath(self, json_path, class_profile, day_of_the_week):
        img_path = json_path.replace(TIMETABLES_DIR, "", 1)
        img_path = img_path.split(".")[0] + "_" + class_profile + "_" + day_of_the_week + ".png"
        return IMG_DIR + img_path

    def exists(self, file_path):
        return os.path.exists(file_path)


class S3FileUtil(FileUtil):
    def saveImage(self, file_path, file_content):
        s3 = self.getS3Resource()
        bucket = s3.Bucket(BUCKET_NAME)
        bucket.put_object(Body=file_content, Key=file_path)

    def getFileDescriptor(self, file_path):
        s3 = self.getS3Resource()
        file_content = s3.Object(BUCKET_NAME, file_path).get()["Body"]
        return file_content

    def getTimetableImagePath(self, json_path, class_profile, day_of_the_week):
        img_path = json_path.replace(".." + os.path.sep, "", 1)
        return img_path.split(".")[0] + "_" + class_profile + "_" + day_of_the_week + ".png"

    def exists(self, file_path):
        return file_path in self.get_bucket_keys()

    def get_bucket_keys(self):
        keys = []
        resp = self.getS3Client().list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' not in resp.keys():
            return keys
        for obj in resp['Contents']:
            keys.append(obj['Key'])
        return keys

    @staticmethod
    def getS3Resource():
        return boto3.resource('s3',
                              aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    @staticmethod
    def getS3Client():
        return boto3.client('s3',
                            aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
