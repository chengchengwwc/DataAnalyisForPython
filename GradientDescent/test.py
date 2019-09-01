#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys


def get_first_position(tmg_list,one_arg):
    return tmg_list.index(one_arg)


def sort_dict(target_dict:dict,message_list:list):
    tmp_list = reversed(sorted(list(set(target_dict.values()))))
    for one_value in tmp_list:
        one_list = []
        for key,value in target_dict.items():
            if one_value == value:
               one_list.append(key)

        if len(one_list) == 1:
            print("{}={}".format(one_list[0],one_value))
        else:
            tmp_dict = {}
            for one_key in one_list:
                tmp_dict[get_first_position(message_list,one_key)] = one_key
            positionkeys = sorted(tmp_dict.keys())
            for positionkey in positionkeys:
                print("{}={}".format(tmp_dict[positionkey],one_value))


def main(target_arg):
    target_dict = {}
    if len(target_arg) >= 100:
        print(">= 100")
        return
    if len(target_arg) == 0:
        print("=0")
        return

    message_list = list(target_arg)
    mesaage_keys = target_dict.keys()
    for one_message in message_list:
        try:
            int(one_message)
        except Exception as e:
            if one_message in mesaage_keys:
                tmp_value = target_dict[one_message] + 1
                target_dict[one_message] = tmp_value
            else:
                target_dict[one_message] = 1
        else:
            continue
    sort_dict(target_dict,message_list)



if __name__ == "__main__":
    main(sys.argv[1])


