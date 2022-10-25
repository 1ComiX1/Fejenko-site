from django.shortcuts import render, redirect
from datetime import datetime as dt


def idx_to_bool(input_list):
    output_list = [False for i in range(6)]
    for elem in input_list:
        output_list[int(elem) - 1] = True

    return output_list


def format_time(time = dt.now()):
    # [17/Oct/2022 12:16:31]
    return time.strftime("[%d/%b/%Y %H:%M:%S]")
