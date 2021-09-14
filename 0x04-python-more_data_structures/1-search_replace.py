#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [new_list if new_list != search else replace for new_list in my_list]
