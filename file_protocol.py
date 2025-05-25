import json
import logging
import shlex

from file_interface import FileInterface

"""
* class FileProtocol bertugas untuk memproses 
data yang masuk, dan menerjemahkannya apakah sesuai dengan
protokol/aturan yang dibuat

* data yang masuk dari client adalah dalam bentuk bytes yang 
pada akhirnya akan diproses dalam bentuk string

* class FileProtocol akan memproses data yang masuk dalam bentuk
string
"""



class FileProtocol:
    def __init__(self):
        self.file = FileInterface()
    def proses_string(self, string_datamasuk=''):
        logging.warning(f"string diproses: {string_datamasuk}")
        try:
            tokens = string_datamasuk.strip().split(' ', 2)
            c_request = tokens[0].lower()
            logging.warning(f"memproses request: {c_request}")
            if c_request == "upload":
                filename = tokens[1]
                encoded_data = tokens[2]
                cl = self.file.upload([filename, encoded_data])
            else:
                params = tokens[1:]
                cl = getattr(self.file, c_request)(params)
            return json.dumps(cl)
        except Exception as e:
            return json.dumps(dict(status='ERROR', data=f'request tidak dikenali: {str(e)}'))

if __name__=='__main__':
    #contoh pemakaian
    fp = FileProtocol()
    print(fp.proses_string("LIST"))
    print(fp.proses_string("GET pokijan.jpg"))