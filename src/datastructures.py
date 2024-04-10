
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1  #>>>>---- SI QUISIERA CREAR UN ID ASCENDENTE----<<<<
        # example list of members
        self._members = [
            {
                'id': self._generateId(),
                'firt_name': "John",
                'last_name': self.last_name,
                'age': 33,
                'lucky_numbers': [7, 13, 22]
            },
            {
                'id': self._generateId(),
                'first_name':"Jane",
                'last_name': self.last_name,
                'age':35,
                'lucky_numbers': [10, 14, 3]
            },
            {
                'id': self._generateId(),
                'first_name': "Jimmy",
                'last_name': self.last_name,
                'age': 5,
                'lucky_numbers': [1]
            },]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id #---- SI QUISIERA CREAR UN ID ASCENDENTE----
        self._next_id += 1       #-------------------------------------------
        return generated_id      #---- SI QUISIERA CREAR UN ID ASCENDENTE----
    
    # return randint(0, 99999999) #---- SI QUISIERA CREAR UN ID Aleatorio----


    def add_member(self, member):
            for new_member in self._members:
                if new_member['id'] == member['id']:
                    return {'msg': 'El usuario ya existe'}
            self._members.append(member)
            return {'msg': 'Usuario creado correctamente'}, self._members
    
    # def add_member(self, member):    
    #     family_member = {
    #         "id" : self._generateId(),
    #         "first_name" : member.get("first_name"),
    #         "last_name" : self.last_name,
    #         "age" : member.get("age"),
    #         "lucky_numbers" : member.get("lucky_numbers")
    #     }
    #     self._members.append(family_member)
    #     return {'msg': 'Usuario creado correctamente'}

    def delete_member(self, id):
        # fill this method and update the return
        for delete in self._members:
            if delete.get("id") == id:
                self._members.remove(delete)
                return { "done": True }

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if id == member["id"]:
                return member

    # this method is done, it returns a list with all the family mem-bers
    def get_all_members(self):
        return self._members
