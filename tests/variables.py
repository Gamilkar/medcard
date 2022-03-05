from main.models import Animal, Procedure
from main import db

# a = Animal(name="animal",
#            species="dog",
#            breed="borzaYa",
#            birth_date="2011-01-01")
# db.session.add(a)
# db.session.commit()

# create_animals(variables.animals_list)


def create_animals(list):
    for animal in list:
        tmp = Animal(
            name=animal["name"],
            species=animal["species"],
            breed=animal["breed"],
            birth_date=animal["birth_date"],
        )
        db.session.add(tmp)
        db.session.commit()


# b = Procedure(animal=3,
#               date="2013-11-11",
#               type="treatment",
#               drug="some drug")
# db.session.add(b)
# db.session.commit()


def create_procedures(list):
    for procedure in list:
        tmp = Procedure(
            animal=procedure["animal"],
            date=procedure["date"],
            type=procedure["type"],
            drug=procedure["drug"],
        )
        db.session.add(tmp)
        db.session.commit()


# create_procedures(variables.procedures_list)

procedures_list = [
    {
        "animal": "1",
        "date": "2021-11-11",
        "type": "vaccination",
        "drug": "drug_1",
    },
    {
        "animal": "2",
        "date": "2020-10-25",
        "type": "vaccination",
        "drug": "drug_2",
    },
    {
        "animal": "1",
        "date": "2019-09-16",
        "type": "treatment",
        "drug": "drug_3",
    },
    {
        "animal": "3",
        "date": "2018-08-19",
        "type": "treatment",
        "drug": "drug_4",
    },
    {
        "animal": "1",
        "date": "2017-07-22",
        "type": "vaccination",
        "drug": "drug_5",
    },
    {
        "animal": "4",
        "date": "2016-06-27",
        "type": "treatment",
        "drug": "drug_6",
    },
    {
        "animal": "2",
        "date": "2015-01-13",
        "type": "vaccination",
        "drug": "drug_7",
    },
    {
        "animal": "4",
        "date": "2014-02-10",
        "type": "vaccination",
        "drug": "drug_8",
    },
    {
        "animal": "1",
        "date": "2013-03-20",
        "type": "vaccination",
        "drug": "drug_9",
    },
    {
        "animal": "3",
        "date": "2012-04-23",
        "type": "treatment",
        "drug": "drug_10",
    },
    {
        "animal": "1",
        "date": "2011-05-10",
        "type": "treatment",
        "drug": "drug_11",
    },
]
animals_list = [
    {
        "name": "animal_1",
        "species": "dog",
        "breed": "pudel",
        "birth_date": "2011-01-01",
    },
    {
        "name": "animal_2",
        "species": "cat",
        "breed": "pers",
        "birth_date": "2010-05-20",
    },
    {
        "name": "animal_3",
        "species": "dog",
        "breed": "buldog",
        "birth_date": "2007-03-17",
    },
    {
        "name": "animal_4",
        "species": "cat",
        "breed": "dvorniaga",
        "birth_date": "2010-11-01",
    },
]
