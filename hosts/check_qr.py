from participants import create
from hosts import Event_entry


def check(code):
    qr = code[5:]

    result = create.find_details(qr)
    entry = Event_entry.find_details(qr)

    if result is None:
        return str(f"Invalid Id: {qr}\nNo result found......")
    elif entry is not None:
        return str(f"The Code has already been Scanned for today.... \n<h1>Date: {entry['date']}</h1>")
    else:
        _id = result['_id']
        name = result['name']
        Event_entry.insert(_id, name)
        return str(f'Access granted\n <h1>{name}</h1>')