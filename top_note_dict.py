def tope_note_dict(dict):
    top_note = {}
    top_note["name"] = dict["name"]
    notes = dict["notes"]
    notes.sort()
    top_note["notes"] = notes[-1]
    print(top_note)

tope_note_dict({ "name": "John", "notes": [3, 5, 4] })