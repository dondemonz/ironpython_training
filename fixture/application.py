import clr
import sys
import os.path
from fixture.group import GroupHelper

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(project_dir, "..", "TestStack.White.0.13.3\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "..", "Castle.Core.3.3.0\\lib\\net40-client\\"))
clr.AddReferenceByName("TestStack.White")

from TestStack.White.UIItems.Finders import *

clr.AddReferenceByName("UIAutomationTypes, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35")
from System.Windows.Automation import *
from TestStack.White import Application


class My_application:

    def __init__(self):
        # self.app = self
        self.group = GroupHelper(self)



    def open_app(self):
        application = Application.Launch("C:\\devel\\FreeAddressBookPortable\\AddressBook.exe")
        main_window = application.GetWindow("Free Address Book")
        return main_window

    def destroy(self, main_window):
        main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()



