"""
Headline: Quickcall library handset ADB control
Description:
	Quickcall library for handset ADB control.
"""

from iTestCommon import *

class library_Handset_Control_QC(object):

    def main(self):
        """
        Headline: The entry point to the test case
        """
        session = iTestCommon()._getSession()
        response = session.main()
        return iTestCommon()._formResponse(response)

    def Activate_BAIC(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Activate_BAIC(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Activate_BAOC(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Activate_BAOC(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Activate_BAIC_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Activate_BAIC_S7(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Activate_BAOC_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Activate_BAOC_S7(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Activate_CFU_S7(self, Handset_Id, Forwarded_Number):
        session = iTestCommon()._getSession()
        response = session.Activate_CFU_S7(Handset_Id=Handset_Id, Forwarded_Number=Forwarded_Number)
        return iTestCommon()._formResponse(response)

    def APN_Check_Current_Setting(self, Handset_Id, testServer):
        session = iTestCommon()._getSession()
        response = session.APN_Check_Current_Setting(Handset_Id=Handset_Id, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def APN_Config_Exists(self, Handset_Id, Apn_In):
        session = iTestCommon()._getSession()
        response = session.APN_Config_Exists(Handset_Id=Handset_Id, Apn_In=Apn_In)
        return iTestCommon()._formResponse(response)

    def APN_Add_toberemoved(self, Handset_Id, Apn_Auth_Type, New_Apn, New_Name):
        session = iTestCommon()._getSession()
        response = session.APN_Add_toberemoved(Handset_Id=Handset_Id, Apn_Auth_Type=Apn_Auth_Type, New_Apn=New_Apn, New_Name=New_Name)
        return iTestCommon()._formResponse(response)

    def APN_Add_S7(self, Handset_Id, New_Apn, New_Name, New_APN_Type, New_UserName, New_Password, New_MMSC, New_MMS_Proxy, New_MMS_Port, APN_Protocol, APN_Roaming_Protocol, Auth_Type='-1', Sim_Slot):
        session = iTestCommon()._getSession()
        response = session.APN_Add_S7(Handset_Id=Handset_Id, New_Apn=New_Apn, New_Name=New_Name, New_APN_Type=New_APN_Type, New_UserName=New_UserName, New_Password=New_Password, New_MMSC=New_MMSC, New_MMS_Proxy=New_MMS_Proxy, New_MMS_Port=New_MMS_Port, APN_Protocol=APN_Protocol, APN_Roaming_Protocol=APN_Roaming_Protocol, Auth_Type=Auth_Type, Sim_Slot=Sim_Slot)
        return iTestCommon()._formResponse(response)

    def APN_Change_Protocol_Setting_Deprecated(self, Handset_Id, Reboot_flag='0', Apn, Protocol):
        session = iTestCommon()._getSession()
        response = session.APN_Change_Protocol_Setting_Deprecated(Handset_Id=Handset_Id, Reboot_flag=Reboot_flag, Apn=Apn, Protocol=Protocol)
        return iTestCommon()._formResponse(response)

    def APN_Change_Protocol_Setting(self, Handset_Id, Reboot_flag='0', Apn, Protocol):
        session = iTestCommon()._getSession()
        response = session.APN_Change_Protocol_Setting(Handset_Id=Handset_Id, Reboot_flag=Reboot_flag, Apn=Apn, Protocol=Protocol)
        return iTestCommon()._formResponse(response)

    def APN_Change_Protocol_Setting_byId(self, Handset_Id, Reboot_flag='0', apnId, Protocol, testServer):
        session = iTestCommon()._getSession()
        response = session.APN_Change_Protocol_Setting_byId(Handset_Id=Handset_Id, Reboot_flag=Reboot_flag, apnId=apnId, Protocol=Protocol, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def APN_Get_Protocol_Setting_Deprecated(self, Handset_Id, Apn):
        session = iTestCommon()._getSession()
        response = session.APN_Get_Protocol_Setting_Deprecated(Handset_Id=Handset_Id, Apn=Apn)
        return iTestCommon()._formResponse(response)

    def APN_Get_Protocol_Setting(self, Handset_Id, Apn):
        session = iTestCommon()._getSession()
        response = session.APN_Get_Protocol_Setting(Handset_Id=Handset_Id, Apn=Apn)
        return iTestCommon()._formResponse(response)

    def APN_Get_Protocol_Setting_byId(self, Handset_Id, apnId, testServer):
        session = iTestCommon()._getSession()
        response = session.APN_Get_Protocol_Setting_byId(Handset_Id=Handset_Id, apnId=apnId, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def APN_Get_Attribute(self, Handset_Id, Apn_Id, Apn_Attribute):
        session = iTestCommon()._getSession()
        response = session.APN_Get_Attribute(Handset_Id=Handset_Id, Apn_Id=Apn_Id, Apn_Attribute=Apn_Attribute)
        return iTestCommon()._formResponse(response)

    def APN_Update_Attribute(self, Handset_Id, Apn_Id, Apn_Attribute, Attribute_Value):
        session = iTestCommon()._getSession()
        response = session.APN_Update_Attribute(Handset_Id=Handset_Id, Apn_Id=Apn_Id, Apn_Attribute=Apn_Attribute, Attribute_Value=Attribute_Value)
        return iTestCommon()._formResponse(response)

    def APN_Add_IPv6(self, Handset_Id, New_Apn, New_Name):
        session = iTestCommon()._getSession()
        response = session.APN_Add_IPv6(Handset_Id=Handset_Id, New_Apn=New_Apn, New_Name=New_Name)
        return iTestCommon()._formResponse(response)

    def APN_Switch(self, Handset_Id, Apn_Id, Reboot_Flag='0'):
        session = iTestCommon()._getSession()
        response = session.APN_Switch(Handset_Id=Handset_Id, Apn_Id=Apn_Id, Reboot_Flag=Reboot_Flag)
        return iTestCommon()._formResponse(response)

    def APN_Delete(self, Handset_Id, Apn_Id):
        session = iTestCommon()._getSession()
        response = session.APN_Delete(Handset_Id=Handset_Id, Apn_Id=Apn_Id)
        return iTestCommon()._formResponse(response)

    def APN_Get_Max(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.APN_Get_Max(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Answer_CS_Call(self, Handset_Id, unlock_flag='1', testServer):
        session = iTestCommon()._getSession()
        response = session.Answer_CS_Call(Handset_Id=Handset_Id, unlock_flag=unlock_flag, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Answer_CS_Call_Alt(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Answer_CS_Call_Alt(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Attach_User(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Attach_User(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Attach_User_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Attach_User_S7(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Attach_User_Noreboot(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Attach_User_Noreboot(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Attach_User_Noreboot_S7_toberemoved(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Attach_User_Noreboot_S7_toberemoved(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def UnAttach_User_Noreboot_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.UnAttach_User_Noreboot_S7(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def ReAttach_User_Noreboot_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.ReAttach_User_Noreboot_S7(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Attenuation_LTE(self, Atten_Level, Directory='c:\\\\temp\\\\', Command):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_LTE(Atten_Level=Atten_Level, Directory=Directory, Command=Command)
        return iTestCommon()._formResponse(response)

    def Attenuation_Channel(self, Channel_Number, Atten_Level, Directory='c:\\\\temp\\\\', Command):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_Channel(Channel_Number=Channel_Number, Atten_Level=Atten_Level, Directory=Directory, Command=Command)
        return iTestCommon()._formResponse(response)

    def Attenuation_Channel_ShowStatus(self, File):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_Channel_ShowStatus(File=File)
        return iTestCommon()._formResponse(response)

    def Attenuation_Initialize_All_Channels(self, Atten_Level='0'):
        session = iTestCommon()._getSession()
        response = session.Attenuation_Initialize_All_Channels(Atten_Level=Atten_Level)
        return iTestCommon()._formResponse(response)

    def Attenuation_Lanes_Connectivity(self, Directory='c:\\\\temp\\\\', ComName):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_Lanes_Connectivity(Directory=Directory, ComName=ComName)
        return iTestCommon()._formResponse(response)

    def Attenuation_SetBlockLevel(self, File, Block_No='c:\\\\temp\\\\', Atten_Val):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_SetBlockLevel(File=File, Block_No=Block_No, Atten_Val=Atten_Val)
        return iTestCommon()._formResponse(response)

    def Attenuation_SetAllBlockLevel(self, File, Atten_Val):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_SetAllBlockLevel(File=File, Atten_Val=Atten_Val)
        return iTestCommon()._formResponse(response)

    def Attenuation_GetBlockLevel(self, File, Block_No='c:\\\\temp\\\\'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_GetBlockLevel(File=File, Block_No=Block_No)
        return iTestCommon()._formResponse(response)

    def Attenuation_FadeBlockLevel(self, File, Block_No='c:\\\\temp\\\\', Start_Atten_Val, End_Atten_Val, Int_Time):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_FadeBlockLevel(File=File, Block_No=Block_No, Start_Atten_Val=Start_Atten_Val, End_Atten_Val=End_Atten_Val, Int_Time=Int_Time)
        return iTestCommon()._formResponse(response)

    def Attenuation_Handover(self, File, vBlock_No, wBlock_No, Start_Atten_Val, End_Atten_Val, Int_Time):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_Handover(File=File, vBlock_No=vBlock_No, wBlock_No=wBlock_No, Start_Atten_Val=Start_Atten_Val, End_Atten_Val=End_Atten_Val, Int_Time=Int_Time)
        return iTestCommon()._formResponse(response)

    def Browser_Close(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Browser_Close(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Browse_Internet(self, Handset_Id, Url='http://www.spirent.com', Use_Chrome='0'):
        session = iTestCommon()._getSession()
        response = session.Browse_Internet(Handset_Id=Handset_Id, Url=Url, Use_Chrome=Use_Chrome)
        return iTestCommon()._formResponse(response)

    def Check_IMEI_by_Id(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Check_IMEI_by_Id(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Check_BAIC(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Check_BAIC(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Check_BAIC_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Check_BAIC_S7(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Change_Handset_Network_Type_OLD(self, Handset_Id, New_Network_Type):
        session = iTestCommon()._getSession()
        response = session.Change_Handset_Network_Type_OLD(Handset_Id=Handset_Id, New_Network_Type=New_Network_Type)
        return iTestCommon()._formResponse(response)

    def Change_Handset_Network_Type_Android5(self, Handset_Id, New_Network_Type):
        session = iTestCommon()._getSession()
        response = session.Change_Handset_Network_Type_Android5(Handset_Id=Handset_Id, New_Network_Type=New_Network_Type)
        return iTestCommon()._formResponse(response)

    def Change_Handset_Network_Type(self, Handset_Id, New_Network_Type):
        session = iTestCommon()._getSession()
        response = session.Change_Handset_Network_Type(Handset_Id=Handset_Id, New_Network_Type=New_Network_Type)
        return iTestCommon()._formResponse(response)

    def Check_Handset_Userplane_Ip(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Check_Handset_Userplane_Ip(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Check_Handset_Network_Type(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Check_Handset_Network_Type(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Check_Handset_Screen_Lock(self, Handset_Id, Return_State_As_Boolean='0'):
        session = iTestCommon()._getSession()
        response = session.Check_Handset_Screen_Lock(Handset_Id=Handset_Id, Return_State_As_Boolean=Return_State_As_Boolean)
        return iTestCommon()._formResponse(response)

    def Check_In_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Check_In_Handset(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Check_Network_Connectivity(self, ip):
        session = iTestCommon()._getSession()
        response = session.Check_Network_Connectivity(ip=ip)
        return iTestCommon()._formResponse(response)

    def Check_CS_Call_Status(self, Handset_Id, testServer):
        session = iTestCommon()._getSession()
        response = session.Check_CS_Call_Status(Handset_Id=Handset_Id, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Check_CS_Call_Status_to_be_removed(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Check_CS_Call_Status_to_be_removed(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Check_CS_Calling_Number_Display(self, Handset_Id, testServer):
        session = iTestCommon()._getSession()
        response = session.Check_CS_Calling_Number_Display(Handset_Id=Handset_Id, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Check_MMS_Max_Id(self, Handset_Id, M_Type):
        session = iTestCommon()._getSession()
        response = session.Check_MMS_Max_Id(Handset_Id=Handset_Id, M_Type=M_Type)
        return iTestCommon()._formResponse(response)

    def Check_MMS_Max_Id_New(self, Handset_Id, Type, testServer):
        session = iTestCommon()._getSession()
        response = session.Check_MMS_Max_Id_New(Handset_Id=Handset_Id, Type=Type, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Check_Out_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Check_Out_Handset(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Check_SMS_Max_Id(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Check_SMS_Max_Id(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Check_SMS_Max_Id_New(self, Handset_Id, Type, testServer):
        session = iTestCommon()._getSession()
        response = session.Check_SMS_Max_Id_New(Handset_Id=Handset_Id, Type=Type, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Check_Receive_MMS_Body_Deprecated(self, Handset_Id, Received_MMS_Id):
        session = iTestCommon()._getSession()
        response = session.Check_Receive_MMS_Body_Deprecated(Handset_Id=Handset_Id, Received_MMS_Id=Received_MMS_Id)
        return iTestCommon()._formResponse(response)

    def Check_Receive_MMS_Body(self, Handset_Id, Received_MMS_Id, testServer):
        session = iTestCommon()._getSession()
        response = session.Check_Receive_MMS_Body(Handset_Id=Handset_Id, Received_MMS_Id=Received_MMS_Id, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Check_Receive_MMS_Subject_Deprecated(self, Handset_Id, Received_MMS_Id):
        session = iTestCommon()._getSession()
        response = session.Check_Receive_MMS_Subject_Deprecated(Handset_Id=Handset_Id, Received_MMS_Id=Received_MMS_Id)
        return iTestCommon()._formResponse(response)

    def Check_Receive_MMS_Subject(self, Handset_Id, Received_MMS_Id, testServer):
        session = iTestCommon()._getSession()
        response = session.Check_Receive_MMS_Subject(Handset_Id=Handset_Id, Received_MMS_Id=Received_MMS_Id, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Check_Receive_SMS(self, Handset_Id, SMS_Max_Id, testServer):
        session = iTestCommon()._getSession()
        response = session.Check_Receive_SMS(Handset_Id=Handset_Id, SMS_Max_Id=SMS_Max_Id, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Check_Receive_SMS_Body_original(self, Handset_Id, SMS_Max_Id):
        session = iTestCommon()._getSession()
        response = session.Check_Receive_SMS_Body_original(Handset_Id=Handset_Id, SMS_Max_Id=SMS_Max_Id)
        return iTestCommon()._formResponse(response)

    def Check_Receive_SMS_Body(self, Handset_Id, SMS_Max_Id, testServer):
        session = iTestCommon()._getSession()
        response = session.Check_Receive_SMS_Body(Handset_Id=Handset_Id, SMS_Max_Id=SMS_Max_Id, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Check_Sent_SMS_Body(self, Handset_Id, SMS_Max_Id, B_Number, Select_Items):
        session = iTestCommon()._getSession()
        response = session.Check_Sent_SMS_Body(Handset_Id=Handset_Id, SMS_Max_Id=SMS_Max_Id, B_Number=B_Number, Select_Items=Select_Items)
        return iTestCommon()._formResponse(response)

    def Check_Sent_SMS(self, Handset_Id, SMS_Max_Id):
        session = iTestCommon()._getSession()
        response = session.Check_Sent_SMS(Handset_Id=Handset_Id, SMS_Max_Id=SMS_Max_Id)
        return iTestCommon()._formResponse(response)

    def Clean_Handset_Cache(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Clean_Handset_Cache(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Clear_Handset_XML_Files(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Clear_Handset_XML_Files(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Clean_Handset_SMS_Database(self):
        session = iTestCommon()._getSession()
        response = session.Clean_Handset_SMS_Database()
        return iTestCommon()._formResponse(response)

    def Close_Netcat_Session(self):
        session = iTestCommon()._getSession()
        response = session.Close_Netcat_Session()
        return iTestCommon()._formResponse(response)

    def De_Activate_BAIC(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.De_Activate_BAIC(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def De_Activate_BAOC(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.De_Activate_BAOC(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def De_Activate_BAIC_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.De_Activate_BAIC_S7(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def De_Activate_BAOC_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.De_Activate_BAOC_S7(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def De_Activate_CFU_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.De_Activate_CFU_S7(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Decode_HTTP_Pcap_By_Keyword(self, Pcap_Path, Pcap_Name, Host):
        session = iTestCommon()._getSession()
        response = session.Decode_HTTP_Pcap_By_Keyword(Pcap_Path=Pcap_Path, Pcap_Name=Pcap_Name, Host=Host)
        return iTestCommon()._formResponse(response)

    def Decode_HTTP_Pcap_Redirect(self, Pcap_Path, Pcap_Name, Host):
        session = iTestCommon()._getSession()
        response = session.Decode_HTTP_Pcap_Redirect(Pcap_Path=Pcap_Path, Pcap_Name=Pcap_Name, Host=Host)
        return iTestCommon()._formResponse(response)

    def Delete_Handset_XML(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Delete_Handset_XML(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Delete_SMS(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Delete_SMS(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Detach_User(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Detach_User(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def End_CS_Call(self, Handset_Id, unlock_flag='1', testServer):
        session = iTestCommon()._getSession()
        response = session.End_CS_Call(Handset_Id=Handset_Id, unlock_flag=unlock_flag, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def File_Download(self, Server_Address='10.32.51.15', User, Pwd, DL_Filename, Handset_Id, Local_Folder='/sdcard/Download'):
        session = iTestCommon()._getSession()
        response = session.File_Download(Server_Address=Server_Address, User=User, Pwd=Pwd, DL_Filename=DL_Filename, Handset_Id=Handset_Id, Local_Folder=Local_Folder)
        return iTestCommon()._formResponse(response)

    def FTP_Download(self, Handset_Id, Remote_Folder='/export/home/support/iTest/DL/', Server_Ip, User, Password, File_Get, File_Size, Timeout='1800', testServer):
        session = iTestCommon()._getSession()
        response = session.FTP_Download(Handset_Id=Handset_Id, Remote_Folder=Remote_Folder, Server_Ip=Server_Ip, User=User, Password=Password, File_Get=File_Get, File_Size=File_Size, Timeout=Timeout, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def FTP_Download_OLD(self, Handset_Id, Server_Ip, User, Password, File_Name, File_Size, Timeout='1800'):
        session = iTestCommon()._getSession()
        response = session.FTP_Download_OLD(Handset_Id=Handset_Id, Server_Ip=Server_Ip, User=User, Password=Password, File_Name=File_Name, File_Size=File_Size, Timeout=Timeout)
        return iTestCommon()._formResponse(response)

    def FTP_Upload_OLD(self, Handset_Id, Server_Ip, User, Password, File_Name, File_Size, Timeout='1800'):
        session = iTestCommon()._getSession()
        response = session.FTP_Upload_OLD(Handset_Id=Handset_Id, Server_Ip=Server_Ip, User=User, Password=Password, File_Name=File_Name, File_Size=File_Size, Timeout=Timeout)
        return iTestCommon()._formResponse(response)

    def FTP_Upload(self, Handset_Id, testServer, Remote_Folder='/export/home/support/iTest/UL/', Server_Ip, User, Password, File_Put, File_Size, Timeout='1800'):
        session = iTestCommon()._getSession()
        response = session.FTP_Upload(Handset_Id=Handset_Id, testServer=testServer, Remote_Folder=Remote_Folder, Server_Ip=Server_Ip, User=User, Password=Password, File_Put=File_Put, File_Size=File_Size, Timeout=Timeout)
        return iTestCommon()._formResponse(response)

    def Interrogate_Supplementary_Service(self, UE_ID, Service_User_Number, Interrogate_Number, Service_Name):
        session = iTestCommon()._getSession()
        response = session.Interrogate_Supplementary_Service(UE_ID=UE_ID, Service_User_Number=Service_User_Number, Interrogate_Number=Interrogate_Number, Service_Name=Service_Name)
        return iTestCommon()._formResponse(response)

    def Get_Adb_Handler_For_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_Adb_Handler_For_Handset(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_APN_List(self):
        session = iTestCommon()._getSession()
        response = session.Get_APN_List()
        return iTestCommon()._formResponse(response)

    def Get_APN_Id(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_APN_Id(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_CurrentAPN_Id(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_CurrentAPN_Id(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_APN_UserName(self, Handset_Id, APN):
        session = iTestCommon()._getSession()
        response = session.Get_APN_UserName(Handset_Id=Handset_Id, APN=APN)
        return iTestCommon()._formResponse(response)

    def Get_4G_3G_Id(self, id_List):
        session = iTestCommon()._getSession()
        response = session.Get_4G_3G_Id(id_List=id_List)
        return iTestCommon()._formResponse(response)

    def Get_Device_Index(self):
        session = iTestCommon()._getSession()
        response = session.Get_Device_Index()
        return iTestCommon()._formResponse(response)

    def Get_Date_From_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_Date_From_Handset(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_Element_From_List(self, list_input, i):
        session = iTestCommon()._getSession()
        response = session.Get_Element_From_List(list_input=list_input, i=i)
        return iTestCommon()._formResponse(response)

    def Get_Handset_Software_Version(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_Handset_Software_Version(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_Imsi_From_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_Imsi_From_Handset(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_IMEI_From_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_IMEI_From_Handset(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_First_8_Digit_of__IMEI_From_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_First_8_Digit_of__IMEI_From_Handset(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_Mobile_Number_by_Imsi(self, Imsi):
        session = iTestCommon()._getSession()
        response = session.Get_Mobile_Number_by_Imsi(Imsi=Imsi)
        return iTestCommon()._formResponse(response)

    def Get_MMS_Time(self, Handset_Id, MMS_Id):
        session = iTestCommon()._getSession()
        response = session.Get_MMS_Time(Handset_Id=Handset_Id, MMS_Id=MMS_Id)
        return iTestCommon()._formResponse(response)

    def Get_MMS_Time_New(self):
        session = iTestCommon()._getSession()
        response = session.Get_MMS_Time_New()
        return iTestCommon()._formResponse(response)

    def Get_Ping_RTT(self, testServer, ip, Handset_Id, send_count, packet_size):
        session = iTestCommon()._getSession()
        response = session.Get_Ping_RTT(testServer=testServer, ip=ip, Handset_Id=Handset_Id, send_count=send_count, packet_size=packet_size)
        return iTestCommon()._formResponse(response)

    def Get_Session_IP(self, Handset_Id, Protocol='ipv4'):
        session = iTestCommon()._getSession()
        response = session.Get_Session_IP(Handset_Id=Handset_Id, Protocol=Protocol)
        return iTestCommon()._formResponse(response)

    def Get_SMS_Database_Info(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_SMS_Database_Info(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_MMS_Database_Info(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_MMS_Database_Info(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_Screen_Resolution(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_Screen_Resolution(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Generate_DL_Traffic(self):
        session = iTestCommon()._getSession()
        response = session.Generate_DL_Traffic()
        return iTestCommon()._formResponse(response)

    def Generate_iPerf_Traffic(self, Ip, Ret_Data, Format, Interval, BW, Time, Server_Port, Protocol):
        session = iTestCommon()._getSession()
        response = session.Generate_iPerf_Traffic(Ip=Ip, Ret_Data=Ret_Data, Format=Format, Interval=Interval, BW=BW, Time=Time, Server_Port=Server_Port, Protocol=Protocol)
        return iTestCommon()._formResponse(response)

    def Generate_Ping_Traffic(self, Handset_Id, ip, send_count, packet_size, testServer):
        session = iTestCommon()._getSession()
        response = session.Generate_Ping_Traffic(Handset_Id=Handset_Id, ip=ip, send_count=send_count, packet_size=packet_size, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Generate_Ping_From_Server(self, Dest_Ip):
        session = iTestCommon()._getSession()
        response = session.Generate_Ping_From_Server(Dest_Ip=Dest_Ip)
        return iTestCommon()._formResponse(response)

    def Generate_Ping_From_Ftp_Server_To_IP(self, Dest_Ip, Packets_Num, Packets_Size):
        session = iTestCommon()._getSession()
        response = session.Generate_Ping_From_Ftp_Server_To_IP(Dest_Ip=Dest_Ip, Packets_Num=Packets_Num, Packets_Size=Packets_Size)
        return iTestCommon()._formResponse(response)

    def Generate_User_Plane_Traffic(self, Handset_Id, test_time, test_interval, ip_iperf_server):
        session = iTestCommon()._getSession()
        response = session.Generate_User_Plane_Traffic(Handset_Id=Handset_Id, test_time=test_time, test_interval=test_interval, ip_iperf_server=ip_iperf_server)
        return iTestCommon()._formResponse(response)

    def Get_Total_SMS_MMS(self, Handset_Id, Message_Type):
        session = iTestCommon()._getSession()
        response = session.Get_Total_SMS_MMS(Handset_Id=Handset_Id, Message_Type=Message_Type)
        return iTestCommon()._formResponse(response)

    def Handset_Signal_Strength(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Handset_Signal_Strength(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Handover_From_4G_To_3G(self, Handset_Id, testServer, att_start_level='10', incrBy='1'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Handover_From_4G_To_3G(Handset_Id=Handset_Id, testServer=testServer, att_start_level=att_start_level, incrBy=incrBy)
        return iTestCommon()._formResponse(response)

    def Handover_From_3G_To_4G(self, Handset_Id, testServer, att_start_level='20', decrBy='-1'):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Handover_From_3G_To_4G(Handset_Id=Handset_Id, testServer=testServer, att_start_level=att_start_level, decrBy=decrBy)
        return iTestCommon()._formResponse(response)

    def Handover_From_4G_To_4G(self, Handset_Id, Source_4G_Channel_Id, Destination_4G_Channel_Id, testServer):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Handover_From_4G_To_4G(Handset_Id=Handset_Id, Source_4G_Channel_Id=Source_4G_Channel_Id, Destination_4G_Channel_Id=Destination_4G_Channel_Id, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Http_Get_Wget_Or_Curl(self, Handset_Id, Url, Output_File='output.html'):
        session = iTestCommon()._getSession()
        response = session.Http_Get_Wget_Or_Curl(Handset_Id=Handset_Id, Url=Url, Output_File=Output_File)
        return iTestCommon()._formResponse(response)

    def Intialize_Handset_ADB(self):
        session = iTestCommon()._getSession()
        response = session.Intialize_Handset_ADB()
        return iTestCommon()._formResponse(response)

    def Locate_G_NetTrack_Log(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Locate_G_NetTrack_Log(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Lock_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Lock_Handset(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Network_Traffic_Statistics(self):
        session = iTestCommon()._getSession()
        response = session.Network_Traffic_Statistics()
        return iTestCommon()._formResponse(response)

    def Output_G_NetTrack_Log(self, Handset_Id, Log_Folder_Name):
        session = iTestCommon()._getSession()
        response = session.Output_G_NetTrack_Log(Handset_Id=Handset_Id, Log_Folder_Name=Log_Folder_Name)
        return iTestCommon()._formResponse(response)

    def Power_Off_Handset(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Power_Off_Handset(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Place_CS_Call(self, Handset_Id, Phone_Number, unlock_flag='1', testServer):
        session = iTestCommon()._getSession()
        response = session.Place_CS_Call(Handset_Id=Handset_Id, Phone_Number=Phone_Number, unlock_flag=unlock_flag, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Place_Emergency_Call(self, Handset_Id, Phone_Number, testServer, endCallFlag='1'):
        session = iTestCommon()._getSession()
        response = session.Place_Emergency_Call(Handset_Id=Handset_Id, Phone_Number=Phone_Number, testServer=testServer, endCallFlag=endCallFlag)
        return iTestCommon()._formResponse(response)

    def Query_AIRPLANE_Mode(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Query_AIRPLANE_Mode(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Restart_Adb_Server(self):
        session = iTestCommon()._getSession()
        response = session.Restart_Adb_Server()
        return iTestCommon()._formResponse(response)

    def Restart_Handset(self, Handset_Id, Wait_handset_reboot='0'):
        session = iTestCommon()._getSession()
        response = session.Restart_Handset(Handset_Id=Handset_Id, Wait_handset_reboot=Wait_handset_reboot)
        return iTestCommon()._formResponse(response)

    def Screen_Capture(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Screen_Capture(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Send_SMS(self, Handset_Id, Phone_Number, Sms_Body, Sms_Subject, testServer):
        session = iTestCommon()._getSession()
        response = session.Send_SMS(Handset_Id=Handset_Id, Phone_Number=Phone_Number, Sms_Body=Sms_Body, Sms_Subject=Sms_Subject, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Send_MMS(self, Handset_Id, testServer, Phone_Number, Mms_Body, Mms_Subject):
        session = iTestCommon()._getSession()
        response = session.Send_MMS(Handset_Id=Handset_Id, testServer=testServer, Phone_Number=Phone_Number, Mms_Body=Mms_Body, Mms_Subject=Mms_Subject)
        return iTestCommon()._formResponse(response)

    def Set_Network_Mode(self, Handset_Id, Network_Mode, testServer):
        session = iTestCommon()._getSession()
        response = session.Set_Network_Mode(Handset_Id=Handset_Id, Network_Mode=Network_Mode, testServer=testServer)
        return iTestCommon()._formResponse(response)

    def Set_Network_Mode_Through_GUI(self, Handset_Id, Network_Mode, testServer, turnOffFlag='1'):
        session = iTestCommon()._getSession()
        response = session.Set_Network_Mode_Through_GUI(Handset_Id=Handset_Id, Network_Mode=Network_Mode, testServer=testServer, turnOffFlag=turnOffFlag)
        return iTestCommon()._formResponse(response)

    def SSH_To_Server(self, CustNet_Server, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.SSH_To_Server(CustNet_Server=CustNet_Server, Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def S7_SSH_To_Server(self, Server_Id, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.S7_SSH_To_Server(Server_Id=Server_Id, Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def S7_Generate_iPerf_Traffic(self, Handset_Id, Ip, Ret_Data, Format, Interval, BW, Time, Server_Port, Protocol):
        session = iTestCommon()._getSession()
        response = session.S7_Generate_iPerf_Traffic(Handset_Id=Handset_Id, Ip=Ip, Ret_Data=Ret_Data, Format=Format, Interval=Interval, BW=BW, Time=Time, Server_Port=Server_Port, Protocol=Protocol)
        return iTestCommon()._formResponse(response)

    def S7_Start_iPerf_Server(self, Handset_Id, Port, W_Size, Interval, Format):
        session = iTestCommon()._getSession()
        response = session.S7_Start_iPerf_Server(Handset_Id=Handset_Id, Port=Port, W_Size=W_Size, Interval=Interval, Format=Format)
        return iTestCommon()._formResponse(response)

    def Start_Android_Application(self, Handset_Id, Activity_Name, Application_Name):
        session = iTestCommon()._getSession()
        response = session.Start_Android_Application(Handset_Id=Handset_Id, Activity_Name=Activity_Name, Application_Name=Application_Name)
        return iTestCommon()._formResponse(response)

    def Start_Application(self, Handset_Id, App_Path='com.metricowireless.datumandroid/com.metricowireless.datumandroid.datumui.DatumAndroidFragmentActivity  '):
        session = iTestCommon()._getSession()
        response = session.Start_Application(Handset_Id=Handset_Id, App_Path=App_Path)
        return iTestCommon()._formResponse(response)

    def Start_Netcat_Session(self, Nc_Port, Nc_Host):
        session = iTestCommon()._getSession()
        response = session.Start_Netcat_Session(Nc_Port=Nc_Port, Nc_Host=Nc_Host)
        return iTestCommon()._formResponse(response)

    def Start_iPerf_Server(self, Port, W_Size, Interval, Format):
        session = iTestCommon()._getSession()
        response = session.Start_iPerf_Server(Port=Port, W_Size=W_Size, Interval=Interval, Format=Format)
        return iTestCommon()._formResponse(response)

    def Stop_Android_Application(self, Handset_Id, Application_Name):
        session = iTestCommon()._getSession()
        response = session.Stop_Android_Application(Handset_Id=Handset_Id, Application_Name=Application_Name)
        return iTestCommon()._formResponse(response)

    def Switch_On_Mobile_Data(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Switch_On_Mobile_Data(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Switch_off_Mobile_Data(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Switch_off_Mobile_Data(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Switch_AIRPLANE_Mode_S4(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Switch_AIRPLANE_Mode_S4(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Switch_On_AIRPLANE_Mode_toremove(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Switch_On_AIRPLANE_Mode_toremove(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Switch_On_AIRPLANE_Mode(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Switch_On_AIRPLANE_Mode(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Switch_Off_AIRPLANE_Mode(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Switch_Off_AIRPLANE_Mode(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Switch_Off_AIRPLANE_Mode_toremove(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Switch_Off_AIRPLANE_Mode_toremove(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Tcp_Dump_old(self, Handset_Id, Time):
        session = iTestCommon()._getSession()
        response = session.Tcp_Dump_old(Handset_Id=Handset_Id, Time=Time)
        return iTestCommon()._formResponse(response)

    def Tcp_Dump_HTTP(self, Handset_Id, Time, Url):
        session = iTestCommon()._getSession()
        response = session.Tcp_Dump_HTTP(Handset_Id=Handset_Id, Time=Time, Url=Url)
        return iTestCommon()._formResponse(response)

    def Tcp_Dump(self, Handset_Id, Packets_Number, Name_Index):
        session = iTestCommon()._getSession()
        response = session.Tcp_Dump(Handset_Id=Handset_Id, Packets_Number=Packets_Number, Name_Index=Name_Index)
        return iTestCommon()._formResponse(response)

    def Ui_Check_If_Screen_Element_Is_Present(self, Element_Xpath, Refresh_Screen_XML='1', Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Ui_Check_If_Screen_Element_Is_Present(Element_Xpath=Element_Xpath, Refresh_Screen_XML=Refresh_Screen_XML, Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Ui_Get_Element_Tap_Coordinates(self, Input_XML, Element_Xpath):
        session = iTestCommon()._getSession()
        response = session.Ui_Get_Element_Tap_Coordinates(Input_XML=Input_XML, Element_Xpath=Element_Xpath)
        return iTestCommon()._formResponse(response)

    def Ui_Get_Screen_Layout(self, Handset_Id, Refresh_Screen_XML='1'):
        session = iTestCommon()._getSession()
        response = session.Ui_Get_Screen_Layout(Handset_Id=Handset_Id, Refresh_Screen_XML=Refresh_Screen_XML)
        return iTestCommon()._formResponse(response)

    def Ui_Tap_On_Screen_Element_By_Xpath(self, Element_Xpath, Refresh_Screen_XML='1', Handset_Id, Duration='50', Bypass_MTP_Prompt='1'):
        session = iTestCommon()._getSession()
        response = session.Ui_Tap_On_Screen_Element_By_Xpath(Element_Xpath=Element_Xpath, Refresh_Screen_XML=Refresh_Screen_XML, Handset_Id=Handset_Id, Duration=Duration, Bypass_MTP_Prompt=Bypass_MTP_Prompt)
        return iTestCommon()._formResponse(response)

    def Unlock_Handset(self, Handset_Id, timeOut='600000'):
        session = iTestCommon()._getSession()
        response = session.Unlock_Handset(Handset_Id=Handset_Id, timeOut=timeOut)
        return iTestCommon()._formResponse(response)

    def Unlock_Handset_Simple(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Unlock_Handset_Simple(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Unlock_Handset_S7(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Unlock_Handset_S7(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Unlock_Handset_Non_Reboot(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Unlock_Handset_Non_Reboot(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Attenuation_Channel_Connectivity(self, Directory='c:\\\\temp\\\\', ComName):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_Channel_Connectivity(Directory=Directory, ComName=ComName)
        return iTestCommon()._formResponse(response)

    def Attenuation_SetChannel_Atten(self, File, Block_No='c:\\\\temp\\\\', Atten_Val):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_SetChannel_Atten(File=File, Block_No=Block_No, Atten_Val=Atten_Val)
        return iTestCommon()._formResponse(response)

    def Attenuation_ShowStatus(self, File):
        """
        Headline: LTE Attenuator
        Author: Scott Tuohy
        Description:
			This Quick Call allows you to control the programable attenuator (attenuating the LTE band).
			You can set the attenuation level; as well as, read the current status of the attenuator.
        """
        session = iTestCommon()._getSession()
        response = session.Attenuation_ShowStatus(File=File)
        return iTestCommon()._formResponse(response)

