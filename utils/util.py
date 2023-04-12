from datetime import datetime

class Util:

    
    def formata_data(self, data:str):
        date_format = '%d/%m/%Y'
        return datetime.strptime(data,'%d/%m/%Y')

