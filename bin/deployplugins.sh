#!/bin/bash
cp /TORSchemas/etc/solution_set.conf /opt/ericsson/nms/litp/etc/plugins/
cp -R /TORSchemas/python/solution_set /opt/ericsson/nms/litp/lib/solution_set
cp -R /TORSchemas/solution-set-xsd/src/main/resources/ /opt/ericsson/nms/litp/share/xsd
cp /TORSchemas/solution-set-xsd/src/main/resources/solution_set.xsd  /opt/ericsson/nms/litp/share/xsd
service landscaped restart




