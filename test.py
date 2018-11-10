import clr
import sys
import os.path

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_dir, "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName("TestStack.White")

from TestStack.White import Application
from TestStack.White.InputDevices import Keyboard
from TestStack.White.WindowsAPI import KeyboardInput
from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName("UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")
from System.Windows.Automation import *

"""
TreeNode treeNode = tree.Node("Root", "Child1");
treeNode.Select();


def get_group_list(modal):
    group_list = []
    for element in modal.Get(SearchCriteria.ByControlType(ControlType.TreeItem))
        TreeNode treeNode = tree.Node("Root", "Child1");
        text = element.name
        id = element.find_element_by_name("selected[]").get_attribute("value")
    return list


    # tree = modal.Get < Tree > ("New group");
    # tree.Click();
    # MessageBox.Show(tree.Nodes.Count.ToString());



    # treeNode = modal.Node("Root", "Child1");
    # treeNode.Select()

def get_group_list(modal):
    for element in modal.find_elements_by_css_selector("span.group"):
        text = element.text
        id = element.find_element_by_name("selected[]").get_attribute("value")
        self.group_cache.append(Group(name=text, id=id))

"""