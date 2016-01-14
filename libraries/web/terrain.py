from lettuce import *
import pdb
import os
import shutil
import csv

@before.all
def setup():
    _file = "index.csv"
    if not os.path.exists(_file):
        index_file = open(_file, "a")
        header = "id,directory,pass,failure,error,total\r\n"
        index_file.writelines(header)
        index_file.close()

    with open(_file, 'rb') as csvFile:
        csv_reader = csv.DictReader(csvFile, delimiter=',', quotechar='|')
        _size = 0
        _next = 0

        for row in csv_reader:
            _size += 1
            _next = int(row['id'])+1

        world.result_dict = {
            'id': _next,
            'directory': _next,
            'pass': 0,
            'failure': 0,
            'error': 0,
            'total': 0
        }

        world.dir_root = os.path.join("logs", str(world.result_dict['directory']))
        createOrEmptyDirectory(world.dir_root)

    try:
        index_file = open(os.path.join(world.dir_root, "index.xml"), "a")
        index_file.writelines("<testplan>\r\n")
    finally:
        index_file.close()

    print "before.all"


def createOrEmptyDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        for the_file in os.listdir(directory):
            file_path = os.path.join(directory, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception, e:
                print e


@before.each_feature
def before_each_feature(feature):
    directory = os.path.join(world.dir_root, feature.__dict__.get('name'))
    # if the directory is not exist, create one
    # if the directory exist but not empty, empty it
    createOrEmptyDirectory(directory)

    world.feature_root = directory
    try:
        index_file = open(os.path.join(world.dir_root, "index.xml"), "a")
        index_file.writelines("<feature name=\""+feature.__dict__.get('name')+"\">\r\n")
    finally:
        index_file.close()
    print "before.each_feature"


@before.each_scenario
def before_each_scenario(scenario):
    if world.feature_root is not None:
        directory = os.path.join(world.feature_root, scenario.__dict__.get('name'))
        os.listdir(world.feature_root)
        createOrEmptyDirectory(directory)
        world.scenario_root = directory
        try:
            index_file = open(os.path.join(world.dir_root, "index.xml"), "a")
            index_file.writelines("<scenario name=\""+scenario.__dict__.get('name')+"\" path=\"" + directory + "\">\r\n")
        finally:
            index_file.close()

    print "before.each_scenario"
    print world.scenario_root


@after.each_scenario
def after_each_scenario(scenario):
    try:
        index_file = open(os.path.join(world.dir_root, "index.xml"), "a")
        index_file.writelines("</scenario>\r\n")
    finally:
        index_file.close()


@after.each_feature
def after_each_feature(feature):
    try:
        index_file = open(os.path.join(world.dir_root, "index.xml"), "a")
        index_file.writelines("</feature>\r\n")
    finally:
        index_file.close()
    world.feature_root = None

    print "after.each_feature"


@after.all
def teardown(total):
    pdb.set_trace()
    _file = "index.csv"
    _fieldnames = ["id", "directory", "pass", "failure", "error", "total"]

    _dict = world.result_dict

    _dict['total'] = total.features_ran
    _dict['pass'] = total.features_passed
    _dict['failure'] = total.features_ran - total.features_passed

    with open(_file, 'a') as csvFile:
        csv_writer = csv.DictWriter(csvFile, fieldnames=_fieldnames)
        csv_writer.writerow(_dict)

    try:
        index_file = open(os.path.join(world.dir_root, "index.xml"), "a")
        index_file.writelines("</testplan>\r\n")
    finally:
        index_file.close()

    print "after.all"

