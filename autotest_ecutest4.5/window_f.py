# -*- coding: utf-8 -*-
import wx
import os
class test_info(wx.App):

    def select_dir(self,text):
            dialog = wx.DirDialog(None, "Choose <<" + text +">> diractory!",os.getcwd())
            if dialog.ShowModal() == wx.ID_OK: 
                a = dialog.GetPath()  

            dialog.Destroy()
            try:
                print "You choice<<"+text+">> diractory is -->"+a
                
            except:
                print "No Choice,You Need be prepared your <<"+text+">> diractory!"

            return a

    def select_file(self,text,file_type):
            dialog = wx.FileDialog(None, "Choose <<" + text +">> File!",os.getcwd(),wildcard=file_type+"(*."+file_type+")|*."+file_type)
            if dialog.ShowModal() == wx.ID_OK: 
                a = dialog.GetPath()  

            dialog.Destroy()
            try:
                print "You choice<<"+text+">> file is -->"+a
                
            except:
                print "No Choice,You Need be prepared your <<"+text+">> File!"
                
            return a
