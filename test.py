from db import create_connection


def get_room_avaibility(room_id, start_time, end_time):
    """Get information about room avaibility to reserve.

    Keyword arguments:
    room_id: -> int(1)
    start_time: -> str(10:00)
    end_time: -> strt(18:00)
    """
    request_ = get_request_to_databse(room_id, start_time, end_time)

    if request_.fetchone():
        request_.close()
        return get_reserved_person(room_id, start_time, end_time)
    else:
        return f'You can reserve office {room_id} \
                \nfrom {start_time} to {end_time}'


def __check_giving_argumetns(room_id, start_time, end_time):
    if isinstance(room_id, int) and \
            isinstance(start_time, str) and isinstance(end_time, str):
        return True
    else:
        return False


def get_request_to_databse(room_id, start_time, end_time):
    conn = create_connection()
    cursor = conn.cursor()
    if __check_giving_argumetns(room_id, start_time, end_time):
        room_id_query = cursor.execute("SELECT number FROM office \
                                        WHERE number = ? and \
                                        (start_time = ? or end_time = ?);",
                                        (room_id, start_time, end_time, ))
        return room_id_query
    else:
        return 'Please be sure that you \
                \ngiving room_id as int and \
                \nstart_time and end_time as str.'


def get_reserved_person(room_id, start_time, end_time):

    conn = create_connection()
    cursor = conn.cursor()
    if_busy_query = cursor.execute("SELECT name, start_time, end_time \
                                    FROM person INNER JOIN office \
                                    ON person.id = office.person_id \
                                    WHERE office.number = ? and \
                                         (office.start_time = ? or \
                                             office.end_time =?)",
                                             (room_id, start_time, end_time,))
    if_busy_response = if_busy_query.fetchall()
    if if_busy_response:
        for busy in if_busy_response:
            response = f"Sorry, you can't reserve office {room_id}. \
                    \nBecause office reserved by {busy[0]} \
                    \nfrom {busy[1]} to {busy[2]}"
        return response

    conn.commit()
    conn.close()
