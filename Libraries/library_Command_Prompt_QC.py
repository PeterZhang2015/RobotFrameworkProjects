from iTestCommon import *

class library_Command_Prompt_QC(object):

    def main(self):
        """
        Headline: The entry point to the test case
        """
        session = iTestCommon()._getSession()
        response = session.main()
        return iTestCommon()._formResponse(response)

    def Cai3G_Create_XML_File_Get(self, Cai3G_Session_Id, Test_Case_Id, Type, Sub_Id):
        session = iTestCommon()._getSession()
        response = session.Cai3G_Create_XML_File_Get(Cai3G_Session_Id=Cai3G_Session_Id, Test_Case_Id=Test_Case_Id, Type=Type, Sub_Id=Sub_Id)
        return iTestCommon()._formResponse(response)

    def Get_List_Average(self, In_List):
        session = iTestCommon()._getSession()
        print In_List
        response = session.Get_List_Average(In_List=In_List)
        print response
        return iTestCommon()._formResponse(response)

    def Get_List_Largest(self, List_In, Type='Test'):
        session = iTestCommon()._getSession()
        response = session.Get_List_Largest(Type=Type, List_In=List_In)
        return iTestCommon()._formResponse(response)

