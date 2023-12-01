from ftplib import FTP

class ftp_get:
    def __init__(self, address):
        if address.startswith('ftp://'):
            address = address[6:]
        if address.count('/') > 0:
            self.address = address[:address.index('/')]
            self.path = address[address.index('/'):]
        else:
            self.address = address
        self.ftp = FTP(self.address)

    def login(self):
        self.ftp.login()

    def navigate(self, path):
        if self.path != '':
            path = self.path + path
        self.ftp.cwd(path)

    def ls(self):
        self.ftp.retrlines('LIST')

    def copy(self, file_name):
        with open(file_name, 'wb') as file:
            self.ftp.retrbinary(f'RETR {file_name}', file.write)

    def quit(self):
        self.ftp.quit()
        print('Stopped')

ftp = ftp_get("ftp://ftp.ncbi.nih.gov/gene/DATA/GENE_INFO/Mammalia/")
ftp.login()
ftp.navigate("")
ftp.ls()
