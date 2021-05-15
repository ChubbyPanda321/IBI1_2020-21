import xml.sax
import matplotlib.pyplot as plt
# build the tree 
class BuildTreeHandler(xml.sax.ContentHandler):
    def __init__(self) -> None:
        self.CurrentData = ""
        self.child_id = ""
        self.father_id_buffer = ""
        self.father_id_list = []
        self.tree_dict = {}
        self.isterm = False
    def startElement(self, name, attrs):
        self.CurrentData = name
        if name == "term":
            self.isterm = True
    def characters(self, content):
        if self.isterm:
            if self.CurrentData == "id":
                self.child_id += content
            elif self.CurrentData == "is_a":
                self.father_id_buffer += content
    def endElement(self, name):
        self.CurrentData = ""
        if name == "is_a":
            self.father_id_list.append(self.father_id_buffer)
            self.father_id_buffer = ""
        if name == "term":
            for father_id in self.father_id_list:
                if self.tree_dict.__contains__(father_id):
                    self.tree_dict[father_id].append(self.child_id)
                else:
                    self.tree_dict[father_id] = [self.child_id]
            # initialize varabiles
            self.isterm = False
            self.child_id = ""
            self.father_id_list = []
# build match list
class BuildMatchHandler(xml.sax.ContentHandler):
    def __init__(self,macromolecules_name) -> None:
        self.CurrentData = ""
        self.match_list = []
        self.id = ""
        self.defstr = ""
        self.isterm = False
        self.macromolecules_name = judgename(macromolecules_name)
    def startElement(self, name, attrs):
        self.CurrentData = name
        if name == "term":
            self.isterm = True
    def characters(self, content):
        if self.isterm:
            if self.CurrentData == "id":
                self.id += content
            elif self.CurrentData == "defstr":
                self.defstr += content
    def endElement(self, name):
        self.CurrentData = "" # i think this is not necessary because startelement will reset it before any operation. but once i delete this, the code doesnt work at all
        if name == "term":
            for molecule_name in self.macromolecules_name:
                if molecule_name in self.defstr:
                    self.match_list.append(self.id)
                    break
            self.defstr = ""
            self.id = ""
            self.isterm = False
# protein and Protein but dont want to use regex
def judgename(name):
    if name.isupper():
        return (name,)
    else:
        return (name,name.capitalize())

def get_match_list(filepath,molecules_name):
    matcher = xml.sax.make_parser()
    matcher.setContentHandler(BuildMatchHandler(molecules_name))
    matcher.setFeature(xml.sax.handler.feature_namespaces,0)
    matcher.parse(filepath)
    return matcher.getContentHandler().match_list

def get_tree_dict(filepath):
    parser = xml.sax.make_parser()
    parser.setContentHandler(BuildTreeHandler())
    parser.setFeature(xml.sax.handler.feature_namespaces,0)
    parser.parse(filepath)
    return parser.getContentHandler().tree_dict

def count_total_childnodes_of_match(filepath,molecules_name,tree_dict):
    match_list = get_match_list(filepath,molecules_name)
    all_childnode_list = get_childnode_id(match_list,tree_dict)
    return len(set(all_childnode_list))       

def get_childnode_id(id_list,tree_dict):
    all_vertex_id_list = []
    for id in id_list:
        if tree_dict.__contains__(id):
            child_id_list = tree_dict[id]
            all_vertex_id_list += child_id_list
            all_vertex_id_list += get_childnode_id(child_id_list,tree_dict)
    return all_vertex_id_list
# this function is 
def make_pie_plot(title,legend_title,**case): 
    plt.pie(
        case.values(),
        labels = case.keys(),
        autopct = '%1.1f%%',
        shadow = True,
        startangle = 90,
    )
    plt.legend(
        title = legend_title,
        loc = 'center left',
        bbox_to_anchor = (-0.3,-0.4,0.6,1)
    )
    plt.title(title)
    plt.show()

XMLfile = r"D:\ZJU\IBI\python\IBI1_2020-21\Practical14\go_obo.xml"
tree_dict = get_tree_dict(XMLfile)

DNA_childnode_num = count_total_childnodes_of_match(XMLfile,"DNA",tree_dict)
RNA_childnode_num = count_total_childnodes_of_match(XMLfile,"RNA",tree_dict)
Protein_childnode_num = count_total_childnodes_of_match(XMLfile,"protein",tree_dict)
# I choose oligosaccharide as my fourth macromolecule
Oligosaccharide_childnode_num = count_total_childnodes_of_match(XMLfile,"oligosaccharide",tree_dict)

print("The number of childNodes associated with DNA is %s."%DNA_childnode_num)
print("The number of childNodes associated with RNA is %s."%RNA_childnode_num)
print("The number of childNodes associated with Protein is %s."%Protein_childnode_num)
print("The number of childNodes associated with oligosaccharide is %s."%Oligosaccharide_childnode_num)

make_pie_plot(
    "The percentages of childNodes associated with macromolecules",
    "Molecule Names",
    DNA = DNA_childnode_num,
    RNA = RNA_childnode_num,
    Protein = Protein_childnode_num,
    Oligosaccharide = Oligosaccharide_childnode_num
)