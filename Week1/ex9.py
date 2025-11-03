from datetime import datetime
class CurrentDateTime:


    def get_formatted_datetime():
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")
    
print(CurrentDateTime.get_formatted_datetime())