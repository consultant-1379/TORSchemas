#!/usr/bin/python

import os
import sys
#sys.path.append("../../../target/deps/opt/ericsson/nms/litp/lib/")

baseroot = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + "/../../")
sys.path.append(baseroot + "/TORSchemas/python/")
sys.path.append(baseroot + "/ERICcommon/ERICcommon_CXP9021401/src/main/python")
sys.path.append(baseroot + "/ERIClandscapeapi/ERIClandscapeapi_CXP9022204/src/main/python")
sys.path.append(baseroot + "/usr/lib/python2.6/site-packages")
sys.path.append(baseroot + "/usr/lib64/python2.6/site-packages")

from xsdgenerate.xsdgenerator import ClassSpecLoader

loader = ClassSpecLoader()

loader.load(baseroot + "/TORSchemas/etc/solution_set.conf")

for key, classspec in loader.classspecs.items():
    f = open(baseroot + "/TORSchemas/solution-set-xsd/src/main/resources/solution_set/" + key + ".xsd", "w")
    f.write(classspec.create_xsd())
    f.close()

f = open(baseroot + "/TORSchemas/solution-set-xsd/src/main/resources/solution_set.xsd", "w")
f.writelines(['<?xml version="1.0" encoding="UTF-8"?>\n',
    '<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"\n',
    'targetNamespace="http://www.ericsson.com/litp" xmlns:litp="http://www.ericsson.com/litp">\n'])

for key, classspec in loader.classspecs.items():
    f.writelines("    <xs:include schemaLocation=\"solution_set/%s.xsd\" />\n" % (key,))
f.writelines("</xs:schema>\n")
f.close()
