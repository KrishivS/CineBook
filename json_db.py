import json
import cruella
import shershaah
import boomika
import mimi
import mask



def write_json(new_data, filename='data.json'):
	with open(filename,'r+') as file:
		file_data = json.load(file)
		file_data["cinema_bookings"].append(new_data)
		file.seek(0)
		json.dump(file_data, file, indent = 4)

y = {
    "cinema_name": "{request}",
	"book_status": False,
	}

write_json(y)
