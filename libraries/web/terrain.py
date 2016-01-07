from lettuce import *
import pdb
import os
import shutil

@before.all
def setup():
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
    directory = os.path.join("logs",feature.__dict__.get('name'))
    # if the directory is not exist, create one
    # if the directory exist but not empty, empty it
    createOrEmptyDirectory(directory)

    world.feature_root = directory
    try:
        index_file = open(os.path.join(world.feature_root, "index.xml"), "a")
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
            index_file = open(os.path.join(world.feature_root, "index.xml"), "a")
            index_file.writelines("<scenario name=\""+scenario.__dict__.get('name')+"\" path=\"" + directory + "\">\r\n")
        finally:
            index_file.close()

    print "before.each_scenario"
    print world.scenario_root

@after.each_scenario
def after_each_scenario(scenario):
    try:
        index_file = open(os.path.join(world.feature_root, "index.xml"), "a")
        index_file.writelines("</scenario>\r\n")
    finally:
        index_file.close()


@after.each_feature
def after_each_feature(feature):
    try:
        index_file = open(os.path.join(world.feature_root, "index.xml"), "a")
        index_file.writelines("</feature>\r\n")
    finally:
        index_file.close()
    world.feature_root = None

    print "after.each_feature"


@after.all
def teardown(total):
    print "after.all"

