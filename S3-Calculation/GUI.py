'''
Created on May 2, 2015

@author: Lei Meng
'''

import wx
import os
import Evaluation

class Frame(wx.Frame):
    #mapping_name = ""
    #true_mapping_name = ""
    #goterm_name1 = ""
    #goterm_name2 = ""
    
    measures = ['P-NC', 'R-NC', 'F-NC', 'NCV', 'GS3', 'NCV-GS3', 'GC', 'P-PF', 'R-PF', 'F-PF']
    result = None
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'LNA vs. GNA evaluation', pos=(100,100),
                size=(600, 1000), style=wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.FRAME_NO_TASKBAR)

        panel = wx.Panel(self, wx.ID_ANY)
        #self.SetMinSize(wx.Size(700, 800))
        
        #select node mapping
        self.labelMapping = wx.StaticText(panel, wx.ID_ANY, 'Aligned node pairs', size=(150, 20), style=wx.ALIGN_RIGHT)
        self.inputTxtMapping = wx.TextCtrl(panel, wx.ID_ANY, '', size=(20, 20))
        self.btnMapping = wx.Button(panel, wx.ID_ANY, '...', size=(30,20))
        self.Bind(wx.EVT_BUTTON, self.OnClick_open, self.btnMapping)
        self.labelMappingRequired = wx.StaticText(panel, wx.ID_ANY, '(Required)', size=(70, 20), style=wx.ALIGN_LEFT)
        
        #select network1
        self.labelNetwork1 = wx.StaticText(panel, wx.ID_ANY , 'Network 1', size=(150, 20), style=wx.ALIGN_RIGHT)
        self.inputTxtNetwork1 = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.btnNetwork1 = wx.Button(panel, wx.ID_ANY, '...', size=(30,20))
        self.Bind(wx.EVT_BUTTON, self.OnClick_open, self.btnNetwork1)        
        self.labelNetwork1Optional = wx.StaticText(panel, wx.ID_ANY, '(Optional)', size=(70, 20), style=wx.ALIGN_LEFT)
        
        #select network2
        self.labelNetwork2 = wx.StaticText(panel, wx.ID_ANY, 'Network 2', size=(150, 20), style=wx.ALIGN_RIGHT)
        self.inputTxtNetwork2 = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.btnNetwork2 = wx.Button(panel, wx.ID_ANY, '...', size=(30,20))
        self.Bind(wx.EVT_BUTTON, self.OnClick_open, self.btnNetwork2)
        self.labelNetwork2Optional = wx.StaticText(panel, wx.ID_ANY, '(Optional)', size=(70, 20), style=wx.ALIGN_LEFT)
     

        #select true node mapping
        self.labelTrueMapping = wx.StaticText(panel, wx.ID_ANY, 'Ground truth node mapping', size=(150, 20), style=wx.ALIGN_RIGHT)
        self.inputTxtTrueMapping = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.btnTrueMapping = wx.Button(panel, wx.ID_ANY, '...', size=(30,20))
        self.Bind(wx.EVT_BUTTON, self.OnClick_open, self.btnTrueMapping)
        self.labelTrueMappingOptional = wx.StaticText(panel, wx.ID_ANY, '(Optional)', size=(70, 20), style=wx.ALIGN_LEFT)
        
        #select go term 1
        self.labelGo1 = wx.StaticText(panel, wx.ID_ANY, 'GO data for Network 1', size=(150, 20), style=wx.ALIGN_RIGHT)
        self.inputTxtGo1 = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.btnGo1 = wx.Button(panel, wx.ID_ANY, '...', size=(30,20))
        self.Bind(wx.EVT_BUTTON, self.OnClick_open, self.btnGo1)
        self.labelGo1Optional = wx.StaticText(panel, wx.ID_ANY, '(Optional)', size=(70, 20), style=wx.ALIGN_LEFT)
        
        #select go term 2        
        self.labelGo2 = wx.StaticText(panel, wx.ID_ANY, 'GO data for Network 2', size=(150, 20), style=wx.ALIGN_RIGHT)
        self.inputTxtGo2 = wx.TextCtrl(panel, wx.ID_ANY, '')
        self.btnGo2 = wx.Button(panel, wx.ID_ANY, '...', size=(30,20))
        self.Bind(wx.EVT_BUTTON, self.OnClick_open, self.btnGo2)
        self.labelGo2Optional = wx.StaticText(panel, wx.ID_ANY, '(Optional)', size=(70, 20), style=wx.ALIGN_LEFT)
        
        #select topological measures        
        self.checkbox_top_all = wx.CheckBox(panel, -1, "All")
        self.checkbox_NC_P = wx.CheckBox(panel, -1, "P-NC")        
        self.checkbox_NC_R = wx.CheckBox(panel, -1, "R-NC")
        self.checkbox_NC_F = wx.CheckBox(panel, -1, "F-NC")        
        self.checkbox_NCV = wx.CheckBox(panel, -1, "NCV")
        self.checkbox_GS3 = wx.CheckBox(panel, -1, "GS3")        
        self.checkbox_NCV_GS3 = wx.CheckBox(panel, -1, "NCV-GS3")                 
        self.checkbox_top_all.SetValue(False)
        self.checkbox_NC_P.SetValue(False)
        self.checkbox_NC_R.SetValue(False)    
        self.checkbox_NC_F.SetValue(False)
        self.checkbox_NCV.SetValue(False)
        self.checkbox_GS3.SetValue(False)
        self.checkbox_NCV_GS3.SetValue(False)                                    
        self.Bind(wx.EVT_CHECKBOX, self.OnClick_top_all, self.checkbox_top_all)

        #select biological measures          
        self.checkbox_bio_all = wx.CheckBox(panel, -1, "All")
        self.checkbox_GC = wx.CheckBox(panel, -1, "GC")
        self.checkbox_PF_P = wx.CheckBox(panel, -1, "P-PF")
        self.checkbox_PF_R = wx.CheckBox(panel, -1, "R-PF")
        self.checkbox_PF_F = wx.CheckBox(panel, -1, "F-PF")
        
        self.checkbox_bio_all.SetValue(False)
        self.checkbox_GC.SetValue(False)
        self.checkbox_PF_P.SetValue(False)
        self.checkbox_PF_R.SetValue(False)
        self.checkbox_PF_F.SetValue(False)
        self.Bind(wx.EVT_CHECKBOX, self.OnClick_bio_all, self.checkbox_bio_all)
        
        #results
        self.list=wx.ListCtrl(panel, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER, size=(40,80))
        self.list.Show(True)
        self.list.InsertColumn(0,"Measure")
        self.list.InsertColumn(1,"Score")
        
        #buttons
        self.btnRun = wx.Button(panel, -1, "Run", pos=(40, 570))
        self.btnSave = wx.Button(panel, -1, "Save", pos=(180, 570))
        self.btnExit = wx.Button(panel, -1, "Exit", pos=(320, 570))
        self.Bind(wx.EVT_BUTTON, self.OnClick_run, self.btnRun)
        self.Bind(wx.EVT_BUTTON, self.OnClick_save, self.btnSave)
        self.Bind(wx.EVT_BUTTON, self.OnClick_exit, self.btnExit)
        if self.result == None:
            self.btnSave.Disable()
        else:
            self.btnSave.Enable()        
        
        boxInput = wx.StaticBox(panel, -1, "Select input files:")               
        boxTopEval = wx.StaticBox(panel, -1, "Select topological measures for evaluation:")
        boxBioEval = wx.StaticBox(panel, -1, "Select biological measures for evaluation:")
        boxResults = wx.StaticBox(panel, -1, "Results (click the 'Save' button below to save the results to a text file)")
                        
        topSizer                = wx.BoxSizer(wx.VERTICAL)
        boxInputSizer           = wx.StaticBoxSizer(boxInput, wx.VERTICAL)
        boxTopEvalSizer           = wx.StaticBoxSizer(boxTopEval, wx.VERTICAL)
        boxBioEvalSizer           = wx.StaticBoxSizer(boxBioEval, wx.VERTICAL)
        boxResultsSizer           = wx.StaticBoxSizer(boxResults, wx.VERTICAL)
        inputTxtNetwork1Sizer      = wx.BoxSizer(wx.HORIZONTAL)
        inputTxtNetwork2Sizer      = wx.BoxSizer(wx.HORIZONTAL)
        inputMappingSizer       = wx.BoxSizer(wx.HORIZONTAL)
        inputTrueMappingSizer   = wx.BoxSizer(wx.HORIZONTAL)
        inputGoOneSizer         = wx.BoxSizer(wx.HORIZONTAL)
        inputGoTwoSizer         = wx.BoxSizer(wx.HORIZONTAL)
        chkTopSizer             = wx.BoxSizer(wx.HORIZONTAL)
        chkBioSizer             = wx.BoxSizer(wx.HORIZONTAL)
        listSizer               = wx.BoxSizer(wx.HORIZONTAL)
        btnSizer                = wx.BoxSizer(wx.HORIZONTAL)
        
        
        inputTxtNetwork1Sizer.Add(self.labelNetwork1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        inputTxtNetwork1Sizer.Add(self.btnNetwork1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL , 5)
        inputTxtNetwork1Sizer.Add(self.inputTxtNetwork1, 1, wx.ALL|wx.EXPAND, 5)
        inputTxtNetwork1Sizer.Add(self.labelNetwork1Optional, 0, wx.ALL|wx.EXPAND, 5)

        inputTxtNetwork2Sizer.Add(self.labelNetwork2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        inputTxtNetwork2Sizer.Add(self.btnNetwork2,  0, wx.ALL|wx.ALIGN_CENTER_VERTICAL , 5)
        inputTxtNetwork2Sizer.Add(self.inputTxtNetwork2, 1, wx.ALL|wx.EXPAND, 5)
        inputTxtNetwork2Sizer.Add(self.labelNetwork2Optional, 0, wx.ALL|wx.EXPAND, 5)
         
        inputMappingSizer.Add(self.labelMapping, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        inputMappingSizer.Add(self.btnMapping, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        inputMappingSizer.Add(self.inputTxtMapping, 1, wx.ALL|wx.EXPAND, 5)
        inputMappingSizer.Add(self.labelMappingRequired, 0, wx.ALL|wx.EXPAND, 5)
        

        inputTrueMappingSizer.Add(self.labelTrueMapping, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        inputTrueMappingSizer.Add(self.btnTrueMapping, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)  
        inputTrueMappingSizer.Add(self.inputTxtTrueMapping, 1, wx.ALL|wx.EXPAND, 5)
        inputTrueMappingSizer.Add(self.labelTrueMappingOptional, 0, wx.ALL|wx.EXPAND, 5)      

        inputGoOneSizer.Add(self.labelGo1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        inputGoOneSizer.Add(self.btnGo1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)  
        inputGoOneSizer.Add(self.inputTxtGo1, 1, wx.ALL|wx.EXPAND, 5)
        inputGoOneSizer.Add(self.labelGo1Optional, 0, wx.ALL|wx.EXPAND, 5)          
        
        inputGoTwoSizer.Add(self.labelGo2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        inputGoTwoSizer.Add(self.btnGo2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)  
        inputGoTwoSizer.Add(self.inputTxtGo2, 1, wx.ALL|wx.EXPAND, 5)
        inputGoTwoSizer.Add(self.labelGo2Optional, 0, wx.ALL|wx.EXPAND, 5)          

        chkTopSizer.Add(self.checkbox_top_all, 0, wx.ALL, 5)
        chkTopSizer.Add(self.checkbox_NC_P, 0, wx.ALL, 5)
        chkTopSizer.Add(self.checkbox_NC_R, 0, wx.ALL, 5)
        chkTopSizer.Add(self.checkbox_NC_F, 0, wx.ALL, 5)
        chkTopSizer.Add(self.checkbox_NCV, 0, wx.ALL, 5)
        chkTopSizer.Add(self.checkbox_GS3, 0, wx.ALL, 5)
        chkTopSizer.Add(self.checkbox_NCV_GS3, 0, wx.ALL, 5)
        
        chkBioSizer.Add(self.checkbox_bio_all, 0, wx.ALL, 5)
        chkBioSizer.Add(self.checkbox_GC, 0, wx.ALL, 5)
        chkBioSizer.Add(self.checkbox_PF_P, 0, wx.ALL, 5)
        chkBioSizer.Add(self.checkbox_PF_R, 0, wx.ALL, 5)
        chkBioSizer.Add(self.checkbox_PF_F, 0, wx.ALL, 5)   
         
        listSizer.Add(self.list, 1, wx.ALL|wx.EXPAND, 5)
        
        btnSizer.Add(self.btnRun, 0, wx.ALL, 1)
        btnSizer.Add(self.btnSave, 0, wx.ALL, 1)
        btnSizer.Add(self.btnExit, 0, wx.ALL, 1)  
        
        boxInputSizer.Add(inputMappingSizer, 0, wx.ALL|wx.EXPAND, 5)
        boxInputSizer.Add(inputTxtNetwork1Sizer, 0, wx.ALL|wx.EXPAND, 5)
        boxInputSizer.Add(inputTxtNetwork2Sizer, 0, wx.ALL|wx.EXPAND, 5)
        boxInputSizer.Add(inputTrueMappingSizer, 0, wx.ALL|wx.EXPAND, 5)
        boxInputSizer.Add(inputGoOneSizer, 0, wx.ALL|wx.EXPAND, 5)
        boxInputSizer.Add(inputGoTwoSizer, 0, wx.ALL|wx.EXPAND, 5)
        
        boxTopEvalSizer.Add(chkTopSizer, 0, wx.ALL|wx.EXPAND, 5)
        
        boxBioEvalSizer.Add(chkBioSizer, 0, wx.ALL|wx.EXPAND, 5)
        
        boxResultsSizer.Add(listSizer, 0, wx.ALL|wx.EXPAND|wx.TOP, 1)
        
        topSizer.Add(boxInputSizer, 0, wx.ALL|wx.EXPAND, 10)
        topSizer.Add(boxTopEvalSizer, 0, wx.ALL|wx.EXPAND, 10)
        topSizer.Add(boxBioEvalSizer, 0, wx.ALL|wx.EXPAND, 10)          
        topSizer.Add(boxResultsSizer, 0, wx.ALL|wx.EXPAND, 10)        
        topSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 10)

        panel.SetSizer(topSizer)
        topSizer.Fit(self)
        
    def OnClick_run(self, event):                    
        graph1 = self.inputTxtNetwork1.GetValue().strip()
        graph2 = self.inputTxtNetwork2.GetValue().strip()
        mapping_name = self.inputTxtMapping.GetValue().strip()
        true_mapping_name = self.inputTxtTrueMapping.GetValue().strip()
        goterm_name1 = self.inputTxtGo1.GetValue().strip()
        goterm_name2 = self.inputTxtGo2.GetValue().strip()
        
        
        eval_NC_P = self.checkbox_NC_P.GetValue()
        eval_NC_R = self.checkbox_NC_R.GetValue()
        eval_NC_F = self.checkbox_NC_F.GetValue()
        eval_NCV = self.checkbox_NCV.GetValue()
        eval_GS3 = self.checkbox_GS3.GetValue()        
        eval_NCV_GS3 = self.checkbox_NCV_GS3.GetValue()
        eval_GC = self.checkbox_GC.GetValue()
        eval_PF_P = self.checkbox_PF_P.GetValue()
        eval_PF_R = self.checkbox_PF_R.GetValue()
        eval_PF_F = self.checkbox_PF_F.GetValue()
        
        if eval_NC_P == True or eval_NC_R == True or eval_NC_F == True:
            if true_mapping_name == "":
                self.MessageBox("Known mapping file must be provided!")
                return
            if os.path.isfile(true_mapping_name)  == False:
                self.MessageBox("Known mapping file '" + true_mapping_name + "' does not exist!")
                return
            
        if eval_GC == True or eval_PF_P == True or eval_PF_R == True or eval_PF_F == True:
            if goterm_name1 == "":
                self.MessageBox("GO terms 1 file must be provided!")
                return

        #print eval_NC_P,eval_NC_R,eval_NC_F, eval_NCV, eval_GS3, eval_NCV_GS3, eval_GC, eval_PF_P, eval_PF_R, eval_PF_F
        quality = Evaluation.AlignmentQuality(graph1, graph2, mapping_name, true_mapping_name, goterm_name1, goterm_name2);
        self.result = quality.evaluate(eval_NC_P, eval_NC_R, eval_NC_F, eval_GS3, eval_NCV, eval_NCV_GS3, eval_GC, eval_PF_P, eval_PF_R, eval_PF_F)
        
        self.list.DeleteAllItems()
        lineIdx = 0
        for key in self.measures:
            if key in self.result:
                value = self.result[key]
                pos = self.list.InsertStringItem(lineIdx,key)
                self.list.SetStringItem(pos,1,str(value))
                lineIdx = lineIdx + 1
        
        if self.result == None:
            self.btnSave.Disable()
        else:
            self.btnSave.Enable()
        
    def OnClick_exit(self, event):
        self.Close()
    
    def OnClick_top_all(self, event):
        eval_top_all = self.checkbox_top_all.GetValue()
        self.checkbox_NC_P.SetValue(eval_top_all)
        self.checkbox_NC_R.SetValue(eval_top_all)
        self.checkbox_NC_F.SetValue(eval_top_all)
        self.checkbox_NCV.SetValue(eval_top_all)
        self.checkbox_GS3.SetValue(eval_top_all)     
        self.checkbox_NCV_GS3.SetValue(eval_top_all)

    def OnClick_bio_all(self, event):
        eval_bio_all = self.checkbox_bio_all.GetValue()
        self.checkbox_GC.SetValue(eval_bio_all)
        self.checkbox_PF_P.SetValue(eval_bio_all)
        self.checkbox_PF_R.SetValue(eval_bio_all)
        self.checkbox_PF_F.SetValue(eval_bio_all)       
                
    def OnClick_open(self, event):
        dlg = wx.FileDialog(self, message="Open a file...", defaultDir=os.getcwd(), 
                            defaultFile="", style=wx.OPEN)
        
        # Call the dialog as a model-dialog so we're required to choose Ok or Cancel
        if dlg.ShowModal() == wx.ID_OK:
            # User has selected something, get the path, set the window's title to the path
            filename = dlg.GetPath()
            
            if(event.GetEventObject() == self.btnMapping):
                self.inputTxtMapping.SetValue(filename)
            elif(event.GetEventObject() == self.btnTrueMapping):
                self.inputTxtTrueMapping.SetValue(filename)
            elif(event.GetEventObject() == self.btnGo1):
                self.inputTxtGo1.SetValue(filename)
            elif(event.GetEventObject() == self.btnGo2):
                self.inputTxtGo2.SetValue(filename)
            elif(event.GetEventObject() == self.btnNetwork1):
                self.inputTxtNetwork1.SetValue(filename)
            elif(event.GetEventObject() == self.btnNetwork2):
                self.inputTxtNetwork2.SetValue(filename)
            elif(event.GetEventObject() == self.btnSave):
                self.inputTxtSave.SetValue(filename)
                        
        dlg.Destroy() # we don't need the dialog any more so we ask it to clean-up
        
    def OnClick_save(self, event):
        dlg = wx.FileDialog(self, message="Save as...", defaultDir=os.getcwd(), 
                defaultFile="", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
        
        if dlg.ShowModal() == wx.ID_OK:
            # User has selected something, get the path, set the window's title to the path
            filename = dlg.GetPath()
            fo = open(filename, 'w')
            
            fo.write("Measure\tScore\n")
            for key in self.measures:
                if key in self.result:
                    value = self.result[key]
                    fo.write(key + "\t" + str(value) + "\n")
            fo.close()
            self.MessageBox("Saved to " + filename)
            
    def MessageBox(self, message, caption = "Warning!"):
        dlg = wx.MessageDialog(self, message, caption, wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
    
    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.SetPen(wx.Pen(wx.BLACK, 4))
        dc.DrawLine(20, 20, 50, 50)
        
if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()
