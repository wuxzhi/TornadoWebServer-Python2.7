#!/usr/bin/env Python
# coding=utf-8

from db import *

"""
database=testDB ---- tables=[users,]
+----------+-------------+------+-----+---------+----------------+
| Field    | Type        | Null | Key | Default | Extra          |
+----------+-------------+------+-----+---------+----------------+
| id       | int(2)      | NO   | PRI | NULL    | auto_increment |
| username | varchar(40) | YES  |     | NULL    |                |
| password | text        | YES  |     | NULL    |                |
| email    | text        | YES  |     | NULL    |                |
+----------+-------------+------+-----+---------+----------------+
"""

def select_table(table, column, condition, value):
    sql = 'select ' + column + ' from ' + table + ' where ' + condition + " = '" + value + "'"
    cur.execute(sql)
    lines = cur.fetchall()
    return lines

def select_column(table, column):
    sql = 'select ' + column + ' from ' + table
    cur.execute(sql)
    lines = cur.fetchall()
    return lines