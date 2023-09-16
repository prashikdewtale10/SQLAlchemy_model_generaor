import json

file_name = 'test01.py'
class_name = 'Testpy'

# Reading json file
with open('db_base.json', 'r') as json_file:
    json_data = json.load(json_file)

for model in json_data:
    with open(f"{model.get('table')}.py", 'w') as f:
        f.write('from pydantic import BaseModel, Field \
                \nimport json\
                \nimport datetime\
                \nfrom sqlalchemy.ext.declarative import declarative_base\
                \nfrom sqlalchemy import Column, Integer, String, BIGINT, UniqueConstraint, BOOLEAN, DATETIME, DateTime, ForeignKey')
        if model.get('table'):
            f.write('\nBase = declarative_base()')
            f.write('\nclass {}(Base):'.format(model.get('table').capitalize()))
            f.write('\n\t"""\n\t\tWrite model description\n\t"""')
            f.write(f"\n\t__tablename__ = '{str(model.get('table').lower())}'")
            for field in model.get('fields'):
                line = ''
                if field.get('name'):
                    line = f"{field.get('name')} = "
                if field.get('type'):
                    if field.get('max_length'):
                        line = line + f"Column({field.get('type')}({field.get('max_length')})"
                    else:
                        line = line + f"Column({field.get('type')}"
                if field.get('primary_key'):
                    line = line + ", primary_key = True"
                if field.get('nullable'):
                    line = line + f", nullable = {field.get('nullable')}"
                if field.get('autoincrement'):
                    line = line + f", autoincrement = {field.get('autoincrement')}"
                if field.get('unique'):
                    line = line + f", unique = {field.get('unique')}"
                if field.get('default'):
                    line = line + f", default = {field.get('default')}"
                
                line = line + f")"
                f.write(f'\n\t{line}')
                f.write(f'\n\t""" \n\t\tWrite field description \n\t"""')
                f.write("\n")
                


