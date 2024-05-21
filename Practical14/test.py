import matplotlib.pyplot as plt
import datetime
import xml.dom.minidom
import xml.sax
import os
path=r'C:\Users\giggity\Desktop\2023-24 IBI1 notes\IBI1_2023-24\Practical14\go_obo.xml'
st_time1=datetime.datetime.now() #set the starttime
DOMTree=xml.dom.minidom.parse(path)
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")
count={'molecular_function':0,'cellular_component':0,'biological_process':0}
for each_term in terms:
    if each_term.getElementsByTagName("namespace")[0].firstChild.data == "biological_process":
        count['biological_process']+=1
    if each_term.getElementsByTagName("namespace")[0].firstChild.data == "molecular_function":
        count['molecular_function']+=1
    if each_term.getElementsByTagName("namespace")[0].firstChild.data == "cellular_component":
        count['cellular_component']+=1
end_time1=datetime.datetime.now()
time1=end_time1-st_time1
print(f'The time taken for DOM is: {time1}')
print(f'The number of terms within molecular function: {count['molecular_function']}')
print(f'The number of terms within biological process: {count['biological_process']}')
print(f'The number of terms within cellular components: {count['cellular_component']}')
x=['molecular function','biological process','cellular component'] #ontology
y=[count['molecular_function'],count['biological_process'],count['cellular_component']]   #numbers for ontology
colors=['blue','green','red']
plt.bar(x,y,color=colors)
plt.xlabel('Ontology')
plt.ylabel('Number')
plt.title('The number of terms within three specified ontology')
plt.show()
plt.clf()

st_time2 = datetime.datetime.now()
ontology = []
count2= {}
class myHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentElement = ''
        self.namespace = ''
    
    def startElement(self, tag, attrs):
        self.currentElement = tag
    
    def characters(self, content):
        if self.currentElement == 'namespace':
            self.namespace += content.strip()
    
    def endElement(self, tag):
        if tag == 'namespace':
            if self.namespace:  
                ontology.append(self.namespace)  
                self.namespace = ''  
    
handler = myHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse(path)
    
for name in ontology:
    if name not in count2:
        count2[name] = 1
    else:
        count2[name] += 1
    
end_time2 = datetime.datetime.now()
time2 = end_time2 - st_time2
print('time taken by SAX methods', time2)
print('The number of terms within molecular function:'+str(count2['molecular_function']))
print('The number of terms within biological process:'+str(count2['biological_process']))
print('The number of terms within cellular components:'+str(count['cellular_component']))
color=['blue','green','red']
plt.bar(['molecular_function','biological_process','celluar_component'], [count2['molecular_function'], count2['biological_process'], count2['cellular_component']],color=color)
plt.xlabel('ontology')
plt.ylabel('number')
plt.show()
plt.clf()

#DOM takes 10.6s
#SAX takes  1.6s
#SAX is the quickest!
