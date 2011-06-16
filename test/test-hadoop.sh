#!/bin/bash
# add if to test HADOOP_HOME is set or not
hadoop_base=`basename $HADOOP_HOME`
cd $HADOOP_HOME
hadoop fs -rmr output
hadoop fs -mkdir input
hadoop fs -copyFromLocal ./conf/* input
hadoop jar ${hadoop_base}-examples.jar wordcount input output
hadoop fs -cat output/part-r-00000
