import  subprocess
import os

os.environ["CLASSPATH"]="/home/reza/eclipse-workspace/lucene-7.7.1/core/lucene-core-7.7.1.jar:/home/reza/eclipse-workspace/lucene-7.7.1/queryparser/lucene-queryparser-7.7.1.jar:/home/reza/eclipse-workspace/lucene-7.7.1/analysis/common/lucene-analyzers-common-7.7.1.jar:/home/reza/eclipse-workspace/lucene-7.7.1/demo/lucene-demo-7.7.1.jar"
os.chdir('/home/reza/eclipse-workspace/lucene-7.7.1')

fileHandler= open("stopword")
listOfLines = fileHandler.readlines()
for line in listOfLines:
    if line.strip()!="":
        ret=subprocess.getoutput("java org.apache.lucene.demo.SearchFiles -query %s"%line.strip())
        if ret.split().pop()=="documents":
            print(line.strip())