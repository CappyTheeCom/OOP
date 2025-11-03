class Note:
    __id_counter = 1

    @classmethod
    def get_next_id(cls):
        id_ = cls.__id_counter
        cls.__id_counter += 1
        return id_

    def __init__(self, tag, memo):
        self.tag = tag 
        self.memo = memo  
        self.id = self.get_next_id()


class NoteBook:
    def __init__(self):
        self.__notebook = []

    def show_note(self):
        for note in self.__notebook:
            print(f"{note.id}: {note.tag}")
            print(note.memo)
    

    def search_note(self):
        search_note = input("Search for: ")
        for note in self.__notebook:

            if search_note in note.tag or search_note in note.memo:
                print(f"{note.id}: {note.tag}")
                print(note.memo)
            else:
                print("Note not found!")


    
    def modify_note(self):
        note_id = int(input("Enter a note id: "))

        for note in self.__notebook:
            
            if  note_id == note.id:
                new_note = input("Enter a tag: ")
                new_memo = input("Enter a new memo:  ")
                
                note.tag = new_note
                note.memo = new_memo

                return print("Note modified")
            else:
                print("page not found!")

                
        



    def add_note(self):
        new_note = input("Enter a tag: ")
        new_memo = input("Enter a new memo: ")

        new_page = Note(new_note,new_memo)

        return self.__notebook.append(new_page)
    
initalise = NoteBook()

initalise.add_note()
initalise.show_note()
initalise.modify_note()
initalise.show_note()