
from urllib import request,error
from os import system,popen
import requests



def url_check(url_input:str):
    """
    Function that checks if the url status is 200
    :param url_imput: The url given by the client
    :return: True is the staus is 200, False if not
    """
    try:
        domain=url_input
        r=requests.post(domain) #Gets the request status
        if r.status_code==200:
            print("Client's URL is ok\nRunning ping now.....")
            return True
        else:
            return False
    except ValueError:
        print("Error: cant analyze client's message!")


def write_to_file(file_path: str, contents_to_write: str):
    """
    Function writes the passed contents into the specific file
    :param file_path: A file to write to
    :param contents_to_write: Contents to write
    :return: None
    """
    try:
        with open(file_path, 'a') as f:
            f.write(str(contents_to_write))  # Casting if the given value is not a string
    except PermissionError:
        raise PermissionError("You don't have the permissions to write to the file")
    except FileNotFoundError:
        raise FileNotFoundError("File not found!")

