#!/usr/bin/python3
""" test Place model """
import unittest
from models.place import Place


class BasemodelClass(unittest.TestCase):
    """test basemodel"""
    def test_place(self):
        inst = Place()
        self.assertEquals(inst.city_id, '')
        self.assertEquals(inst.user_id, '')
        self.assertEquals(inst.name, '')
        self.assertEquals(inst.description, '')
        self.assertEquals(inst.number_rooms, 0)
        self.assertEquals(inst.number_bathrooms, 0)
        self.assertEquals(inst.max_guest, 0)
        self.assertEquals(inst.price_by_night, 0)
        self.assertEquals(inst.latitude, 0.0)
        self.assertEquals(inst.longitude, 0.0)
        self.assertEquals(inst.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
