from sqlite3 import connect, DatabaseError

import re
from bs4 import BeautifulSoup

# We use these variables to keep the count of entries
# Since AUTOINCREMENT is not used these variables are
# also used while assigning the primary key
WORD_COUNT = 0
DEFINITION_COUNT = 0
EXAMPLE_COUNT = 0


def get_records(connection):
    """Extract record from the database"""
    query = 'SELECT ' \
            'component_main_entry_index_title, ' \
            'component_main_entry_index_result ' \
            'from tbl_component_main_entry_index'
    return connection.execute(query)


def parse_record(record):
    """
    Parse the record and generate dictionary entry

    :param record: Database Queryset
    :return: parsed result
        {
            'word': '',
            'pos': '', # part of speech

            'definitions': [
                {
                    'defn': '',
                    'examples': ['example1', 'example2', ...]
                },
                ...
            ]
        }
        eg. For example refer to docstring of `save_to_db`

    """
    regex = re.compile('[०१२३४५६७८९]\. ')
    word, tag = record[0], record[1]

    # Ensure tag is converted to Unicode string
    tag = tag.decode('utf-8') if isinstance(tag, bytes) else tag

    bs = BeautifulSoup(tag, 'html.parser')
    defns = bs.find_all(class_='defn')
    egs = bs.find_all(class_='grey2')
    pos = bs.find(class_='pos')

    result = {
        'word': word,
        'definitions': [],
        'pos': pos.get_text() if pos else 'N/A'
    }

    for i in range(len(defns)):
        try:
            examples = egs[i].get_text()
            examples = examples.split('\xa0')  # split by &nbsp;

            for l in range(len(examples)):
                examples[l] = regex.sub('', examples[l])

            result['definitions'].append({
                'defn': defns[i].get_text(),
                # first two are not examples actually
                'examples': examples[2::]
            })
        except Exception as e:
            print("Error parsing examples:", e)
    return result


def create_tables_for_destination(connection):
    """ create tables to store refined entries """
    queries = [
        'CREATE TABLE IF NOT EXISTS `word`(\
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,\
        `value` varchar(255) NOT NULL,\
        `part_of_speech` varchar(100)\
        );',

        'CREATE TABLE IF NOT EXISTS `definition`(\
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,\
        `word_id` int(11) NOT NULL,\
        `value` TEXT\
        );',
        'CREATE TABLE IF NOT EXISTS `example`(\
        `id` INTEGER PRIMARY KEY AUTOINCREMENT,\
        `definition_id` int(11) NOT NULL,\
        `value` TEXT\
        );'
    ]
    for query in queries:
        connection.execute(query)


def save_word(word, pos, connection):
    """ save word to the database """
    query = '''
        INSERT INTO `word`
        (value, part_of_speech)
        VALUES (?, ?)
    '''

    try:
        connection.execute(query, (word, pos))
        return connection.lastrowid
    except DatabaseError as e:
        print(e)
        return None


def save_examples(examples, definition_id, connection):
    """ save examples to the database """
    query = '''
        INSERT INTO `example`
        (definition_id, value)
        VALUES (?, ?)
    '''
    for example in examples:
        try:
            connection.execute(query, (definition_id, example))
        except DatabaseError as e:
            print(e)


def save_definitions(definitions, word_id, connection):
    """ save definitions to the database """
    query = '''
        INSERT INTO `definition`
        (word_id, value)
        VALUES (?, ?)
    '''
    for definition in definitions:
        try:
            cursor = connection.cursor()
            cursor.execute(query, (word_id, definition.get('defn')))
            definition_id = cursor.lastrowid
            if definition.get('examples'):
                save_examples(
                    examples=definition.get('examples'),
                    definition_id=definition_id,
                    connection=connection
                )
        except DatabaseError as e:
            print(e)


def save_to_db(result, connection):
    """
    Save parsed result to the database

    :param result: details of word
    :param connection: database connection
    :return: None
    """

    word_id = save_word(
        word=result.get('word', None),
        pos=result.get('pos', None),
        connection=connection
    )

    if word_id:
        save_definitions(
            definitions=result.get('definitions'),
            word_id=word_id,
            connection=connection
        )
    else:
        print("Failed to save word to database")


def main():
    try:
        source_db_name = 'nepali_dictionary.sqlite3'
        destination_db_name = 'nep_dict.sqlite3'

        source_connection = connect(source_db_name)
        records = get_records(source_connection)

        destination_connection = connect(destination_db_name)
        create_tables_for_destination(destination_connection)

        for record in records:
            result = parse_record(record)
            save_to_db(result, destination_connection)

        source_connection.close()
        destination_connection.commit()
        destination_connection.close()

        print(str(WORD_COUNT) + ' words written')
    except Exception as e:
        print("An error occurred:", e)


if __name__ == '__main__':
    main()
