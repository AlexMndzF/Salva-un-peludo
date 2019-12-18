import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
cloudinary.config(
                cloud_name = "alexmendezf", 
                api_key = api_key, 
                api_secret = api_secret
                )

def uploadfoto_cloudinary(name,path):
    cloudinary.uploader.upload(path, 
                                folder = "final_database", 
                                public_id = name,
                                overwrite = True, 
                                resource_type = "image")
    print('image upload')