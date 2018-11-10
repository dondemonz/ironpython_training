import clr
import sys
import os.path
import time

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


def get_group_list(main_window):
    modal = open_group_editor(main_window)
    tree = modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
    root = tree.Nodes[0]
    # list compehantion
    l = [node.Text for node in root.Nodes]
    close_group_editor(modal)
    return l


def test_add_group():
    application = Application.Launch("C:\\devel\\FreeAddressBookPortable\\AddressBook.exe")
    main_window = application.GetWindow("Free Address Book")
    old_list = get_group_list(main_window)
    add_new_group(main_window, "Test group")
    new_list = get_group_list(main_window)
    old_list.append("Test group")
    assert sorted(old_list) == sorted(new_list)
    main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()


def test_delete_group():
    application = Application.Launch("C:\\devel\\FreeAddressBookPortable\\AddressBook.exe")
    main_window = application.GetWindow("Free Address Book")
    if len(get_group_list(main_window)) == 1:
        add_new_group(main_window, "Test group")
    old_list = get_group_list(main_window)
    delete_first_group(main_window)
    new_list = get_group_list(main_window)
    old_list.remove("Test group")
    assert sorted(old_list) == sorted(new_list)
    main_window.Get(SearchCriteria.ByAutomationId("uxExitAddressButton")).Click()


def delete_first_group(main_window):
    main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
    modal = main_window.ModalWindow("Group editor")
    tree = modal.Get(SearchCriteria.ByAutomationId("uxAddressTreeView"))
    root = tree.Nodes[0]
    item = root.Nodes[0]
    item.Select()
    modal.Get(SearchCriteria.ByAutomationId("uxDeleteAddressButton")).Click()
    delete_window = modal.ModalWindow("Delete group")
    delete_window.Get(SearchCriteria.ByAutomationId("uxOKAddressButton")).Click()
    close_group_editor(modal)

def add_new_group(main_window, name):
    modal = open_group_editor(main_window)
    modal.Get(SearchCriteria.ByAutomationId("uxNewAddressButton")).Click()
    modal.Get(SearchCriteria.ByControlType(ControlType.Edit)).Enter(name)
    Keyboard.Instance.PressSpecialKey(KeyboardInput.SpecialKeys.RETURN)
    close_group_editor(modal)



def close_group_editor(modal):
    modal.Get(SearchCriteria.ByAutomationId("uxCloseAddressButton")).Click()


def open_group_editor(main_window):
    main_window.Get(SearchCriteria.ByAutomationId("groupButton")).Click()
    modal = main_window.ModalWindow("Group editor")
    return modal
