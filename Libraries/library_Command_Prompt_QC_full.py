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

    def Cai3G_Create_XML_File_Create(self, Cai3G_Session_Id, Test_Case_Id, Type, Sub_Imsi, Sub_Msisdn, Sub_Id):
        session = iTestCommon()._getSession()
        response = session.Cai3G_Create_XML_File_Create(Cai3G_Session_Id=Cai3G_Session_Id, Test_Case_Id=Test_Case_Id, Type=Type, Sub_Imsi=Sub_Imsi, Sub_Msisdn=Sub_Msisdn, Sub_Id=Sub_Id)
        return iTestCommon()._formResponse(response)

    def Cai3G_Create_XML_File_Create_HSS_ESM(self):
        session = iTestCommon()._getSession()
        response = session.Cai3G_Create_XML_File_Create_HSS_ESM()
        return iTestCommon()._formResponse(response)

    def Cai3G_Create_XML_File_Delete(self, Cai3G_Session_Id, Sub_Imsi, Test_Case_Id, Type, Sub_Id):
        session = iTestCommon()._getSession()
        response = session.Cai3G_Create_XML_File_Delete(Cai3G_Session_Id=Cai3G_Session_Id, Sub_Imsi=Sub_Imsi, Test_Case_Id=Test_Case_Id, Type=Type, Sub_Id=Sub_Id)
        return iTestCommon()._formResponse(response)

    def Cai3G_Create_XML_File_Delete_HSS_ESM(self):
        session = iTestCommon()._getSession()
        response = session.Cai3G_Create_XML_File_Delete_HSS_ESM()
        return iTestCommon()._formResponse(response)

    def Cai3G_Create_XML_File_Set(self, Cai3G_Session_Id, Append_String, Test_Case_Id, Sub_Id, Type, Input_Val):
        session = iTestCommon()._getSession()
        response = session.Cai3G_Create_XML_File_Set(Cai3G_Session_Id=Cai3G_Session_Id, Append_String=Append_String, Test_Case_Id=Test_Case_Id, Sub_Id=Sub_Id, Type=Type, Input_Val=Input_Val)
        return iTestCommon()._formResponse(response)

    def Cai3G_Get_Apn_Type(self, Apn_Id_List):
        session = iTestCommon()._getSession()
        response = session.Cai3G_Get_Apn_Type(Apn_Id_List=Apn_Id_List)
        return iTestCommon()._formResponse(response)

    def Construct_MOAttributes_List(self, MO_Attr_List, MO_Attr_Name):
        session = iTestCommon()._getSession()
        response = session.Construct_MOAttributes_List(MO_Attr_List=MO_Attr_List, MO_Attr_Name=MO_Attr_Name)
        return iTestCommon()._formResponse(response)

    def Construct_MOAttributes_List_2(self, MO_Attr_List, MO_Attr_Name_List):
        session = iTestCommon()._getSession()
        response = session.Construct_MOAttributes_List_2(MO_Attr_List=MO_Attr_List, MO_Attr_Name_List=MO_Attr_Name_List)
        return iTestCommon()._formResponse(response)

    def Compare_WS_CDR_Volumes(self, Cdr_Volumes, Ws_Volumes):
        session = iTestCommon()._getSession()
        response = session.Compare_WS_CDR_Volumes(Cdr_Volumes=Cdr_Volumes, Ws_Volumes=Ws_Volumes)
        return iTestCommon()._formResponse(response)

    def Compare_Two_Lists(self, List1, List2):
        session = iTestCommon()._getSession()
        response = session.Compare_Two_Lists(List1=List1, List2=List2)
        return iTestCommon()._formResponse(response)

    def Condition_Seconds_Minutes(self, Start_Time, Stop_Time):
        session = iTestCommon()._getSession()
        response = session.Condition_Seconds_Minutes(Start_Time=Start_Time, Stop_Time=Stop_Time)
        return iTestCommon()._formResponse(response)

    def Convert_Double_From_Time_String(self, String_Input):
        """
        Description:
			Input is of format:
			String: 33,784
			Output is of format:
			Double number: 33,784
        """
        session = iTestCommon()._getSession()
        response = session.Convert_Double_From_Time_String(String_Input=String_Input)
        return iTestCommon()._formResponse(response)

    def Convert_Frame_Time_MinSec_Gtp(self):
        session = iTestCommon()._getSession()
        response = session.Convert_Frame_Time_MinSec_Gtp()
        return iTestCommon()._formResponse(response)

    def Convert_Wireshark_Id_String(self, In):
        session = iTestCommon()._getSession()
        response = session.Convert_Wireshark_Id_String(In=In)
        return iTestCommon()._formResponse(response)

    def Copy_File_Replace_Content(self, File_To_Change, TC_Id, Res_File_Name, New_Value, Old_Value):
        session = iTestCommon()._getSession()
        response = session.Copy_File_Replace_Content(File_To_Change=File_To_Change, TC_Id=TC_Id, Res_File_Name=Res_File_Name, New_Value=New_Value, Old_Value=Old_Value)
        return iTestCommon()._formResponse(response)

    def Create_SOAPUI_CheckBalance_template(self, File_To_Change, TC_Id, New_Value, Old_Value):
        session = iTestCommon()._getSession()
        response = session.Create_SOAPUI_CheckBalance_template(File_To_Change=File_To_Change, TC_Id=TC_Id, New_Value=New_Value, Old_Value=Old_Value)
        return iTestCommon()._formResponse(response)

    def Create_SOAPUI_AdjustBalance_template(self, File_To_Change, New_Value_1, New_Value_2, Old_Value_1, Old_Value_2, TC_Id):
        session = iTestCommon()._getSession()
        response = session.Create_SOAPUI_AdjustBalance_template(File_To_Change=File_To_Change, New_Value_1=New_Value_1, New_Value_2=New_Value_2, Old_Value_1=Old_Value_1, Old_Value_2=Old_Value_2, TC_Id=TC_Id)
        return iTestCommon()._formResponse(response)

    def Extract_MME_Hostname(self, Input_Name):
        """
        Description:
			Return mme host name in UPPER case.
        """
        session = iTestCommon()._getSession()
        response = session.Extract_MME_Hostname(Input_Name=Input_Name)
        return iTestCommon()._formResponse(response)

    def Extract_Pgw_Apn_Data(self, Pgw_Sub_Data, Data):
        session = iTestCommon()._getSession()
        response = session.Extract_Pgw_Apn_Data(Pgw_Sub_Data=Pgw_Sub_Data, Data=Data)
        return iTestCommon()._formResponse(response)

    def Extract_Sgw_Apn_Data(self, Sgw_Sub_Data, Data):
        session = iTestCommon()._getSession()
        response = session.Extract_Sgw_Apn_Data(Sgw_Sub_Data=Sgw_Sub_Data, Data=Data)
        return iTestCommon()._formResponse(response)

    def Extract_Time_Seconds(self, String_Input):
        session = iTestCommon()._getSession()
        response = session.Extract_Time_Seconds(String_Input=String_Input)
        return iTestCommon()._formResponse(response)

    def Extract_IP_Len(self, List_To_Extract):
        session = iTestCommon()._getSession()
        response = session.Extract_IP_Len(List_To_Extract=List_To_Extract)
        return iTestCommon()._formResponse(response)

    def Extract_IP_Len_FrameNumber(self, List_To_Extract):
        session = iTestCommon()._getSession()
        response = session.Extract_IP_Len_FrameNumber(List_To_Extract=List_To_Extract)
        return iTestCommon()._formResponse(response)

    def Extract_IP_Len_FrameNumber_withFrameNum(self, List_To_Extract):
        session = iTestCommon()._getSession()
        response = session.Extract_IP_Len_FrameNumber_withFrameNum(List_To_Extract=List_To_Extract)
        return iTestCommon()._formResponse(response)

    def Filter_Pcap_File(self, Pcap_File, Pcap_Display_Filter):
        session = iTestCommon()._getSession()
        response = session.Filter_Pcap_File(Pcap_File=Pcap_File, Pcap_Display_Filter=Pcap_Display_Filter)
        return iTestCommon()._formResponse(response)

    def Find_Diameter_Response(self, Pcap_Req_List, Test_Id, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.Find_Diameter_Response(Pcap_Req_List=Pcap_Req_List, Test_Id=Test_Id, Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def Find_Gsm_Map_Response(self, Pcap_Req_List, Test_Id, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.Find_Gsm_Map_Response(Pcap_Req_List=Pcap_Req_List, Test_Id=Test_Id, Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def Find_Gsm_Map_Response_New(self, Pcap_Req_List, Test_Id, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.Find_Gsm_Map_Response_New(Pcap_Req_List=Pcap_Req_List, Test_Id=Test_Id, Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def Find_Http_Response(self, Pcap_Req_List, Test_Id, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.Find_Http_Response(Pcap_Req_List=Pcap_Req_List, Test_Id=Test_Id, Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def Find_Ldap_Response(self, Frame_List, Op, Test_Id, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.Find_Ldap_Response(Frame_List=Frame_List, Op=Op, Test_Id=Test_Id, Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def Find_MME_Subscription(self, MME_Port, MME_User, MME_Pass, IMSI, MME_Nodes):
        """
        Description:
			Return the subscription data and the mme host name
        """
        session = iTestCommon()._getSession()
        response = session.Find_MME_Subscription(MME_Port=MME_Port, MME_User=MME_User, MME_Pass=MME_Pass, IMSI=IMSI, MME_Nodes=MME_Nodes)
        return iTestCommon()._formResponse(response)

    def Find_SAPC_Subscription_tbc(self, SAPC_Port, SAPC_User, SAPC_Pass, IMSI, SAPC_Fqdns, SAPC_Nodes):
        """
        Description:
			Return the subscription data and the SAPC host name
        """
        session = iTestCommon()._getSession()
        response = session.Find_SAPC_Subscription_tbc(SAPC_Port=SAPC_Port, SAPC_User=SAPC_User, SAPC_Pass=SAPC_Pass, IMSI=IMSI, SAPC_Fqdns=SAPC_Fqdns, SAPC_Nodes=SAPC_Nodes)
        return iTestCommon()._formResponse(response)

    def Find_MME_Host(self, MME_Port, MME_User, MME_Pass, IMSI, MME_Nodes):
        """
        Description:
			Return only the MME hostname (in UPPER case)
        """
        session = iTestCommon()._getSession()
        response = session.Find_MME_Host(MME_Port=MME_Port, MME_User=MME_User, MME_Pass=MME_Pass, IMSI=IMSI, MME_Nodes=MME_Nodes)
        return iTestCommon()._formResponse(response)

    def Get_All_Child_Nodes(self, Parent='Network_Configuration'):
        session = iTestCommon()._getSession()
        response = session.Get_All_Child_Nodes(Parent=Parent)
        return iTestCommon()._formResponse(response)

    def Get_All_MME_Fqdn(self, MME_List):
        session = iTestCommon()._getSession()
        response = session.Get_All_MME_Fqdn(MME_List=MME_List)
        return iTestCommon()._formResponse(response)

    def Get_All_MME_Nodes(self, MME_List):
        session = iTestCommon()._getSession()
        response = session.Get_All_MME_Nodes(MME_List=MME_List)
        return iTestCommon()._formResponse(response)

    def Get_All_Nodes(self, Param_Base, Node_Type):
        session = iTestCommon()._getSession()
        response = session.Get_All_Nodes(Param_Base=Param_Base, Node_Type=Node_Type)
        return iTestCommon()._formResponse(response)

    def Get_All_Nodes_Fqdn(self, Nodes_List, Node_Base, Node_Type):
        session = iTestCommon()._getSession()
        response = session.Get_All_Nodes_Fqdn(Nodes_List=Nodes_List, Node_Base=Node_Base, Node_Type=Node_Type)
        return iTestCommon()._formResponse(response)

    def Get_All_SAPC_Nodes(self, SAPC_List):
        session = iTestCommon()._getSession()
        response = session.Get_All_SAPC_Nodes(SAPC_List=SAPC_List)
        return iTestCommon()._formResponse(response)

    def Get_MME_S1Addresses(self, MME_Name):
        session = iTestCommon()._getSession()
        response = session.Get_MME_S1Addresses(MME_Name=MME_Name)
        return iTestCommon()._formResponse(response)

    def Get_All_EPG_Nodes_tbc(self, EPG_List):
        session = iTestCommon()._getSession()
        response = session.Get_All_EPG_Nodes_tbc(EPG_List=EPG_List)
        return iTestCommon()._formResponse(response)

    def Get_All_TCP_Streams(self, Pcap_File, winscp_path):
        session = iTestCommon()._getSession()
        response = session.Get_All_TCP_Streams(Pcap_File=Pcap_File, winscp_path=winscp_path)
        return iTestCommon()._formResponse(response)

    def Get_Attach_Request_S1AP(self):
        session = iTestCommon()._getSession()
        response = session.Get_Attach_Request_S1AP()
        return iTestCommon()._formResponse(response)

    def Get_Date_Time(self):
        session = iTestCommon()._getSession()
        response = session.Get_Date_Time()
        return iTestCommon()._formResponse(response)

    def Get_Frame_Time_Gtp(self):
        session = iTestCommon()._getSession()
        response = session.Get_Frame_Time_Gtp()
        return iTestCommon()._formResponse(response)

    def Get_First_Usable_Address(self, Address_Range):
        session = iTestCommon()._getSession()
        response = session.Get_First_Usable_Address(Address_Range=Address_Range)
        return iTestCommon()._formResponse(response)

    def Get_List_Average(self, In_List):
        session = iTestCommon()._getSession()
        response = session.Get_List_Average(In_List=In_List)
        return iTestCommon()._formResponse(response)

    def Get_List_Largest(self, List_In):
        session = iTestCommon()._getSession()
        response = session.Get_List_Largest(List_In=List_In)
        return iTestCommon()._formResponse(response)

    def Get_Mobile_Number(self, Imsi):
        session = iTestCommon()._getSession()
        response = session.Get_Mobile_Number(Imsi=Imsi)
        return iTestCommon()._formResponse(response)

    def Get_Pcap_Filter(self, Input_Data):
        session = iTestCommon()._getSession()
        response = session.Get_Pcap_Filter(Input_Data=Input_Data)
        return iTestCommon()._formResponse(response)

    def Get_Previous_Day(self, Day, Month, Year):
        session = iTestCommon()._getSession()
        response = session.Get_Previous_Day(Day=Day, Month=Month, Year=Year)
        return iTestCommon()._formResponse(response)

    def Get_Previous_Hour(self, Hour):
        session = iTestCommon()._getSession()
        response = session.Get_Previous_Hour(Hour=Hour)
        return iTestCommon()._formResponse(response)

    def Get_Previous_Month(self, This_Month):
        session = iTestCommon()._getSession()
        response = session.Get_Previous_Month(This_Month=This_Month)
        return iTestCommon()._formResponse(response)

    def Get_Radius_AVP(self, Pcap_File, Frame_Num, AVP_Name):
        session = iTestCommon()._getSession()
        response = session.Get_Radius_AVP(Pcap_File=Pcap_File, Frame_Num=Frame_Num, AVP_Name=AVP_Name)
        return iTestCommon()._formResponse(response)

    def Get_Radius_Request(self, Calling_Id, Pcap_File, Type, Acct_Type):
        session = iTestCommon()._getSession()
        response = session.Get_Radius_Request(Calling_Id=Calling_Id, Pcap_File=Pcap_File, Type=Type, Acct_Type=Acct_Type)
        return iTestCommon()._formResponse(response)

    def Get_Request_Frame_Num_Gtp(self):
        session = iTestCommon()._getSession()
        response = session.Get_Request_Frame_Num_Gtp()
        return iTestCommon()._formResponse(response)

    def Get_Response_Frame_Num_Gtp(self):
        session = iTestCommon()._getSession()
        response = session.Get_Response_Frame_Num_Gtp()
        return iTestCommon()._formResponse(response)

    def Get_Test_PC_Id(self, Handset_Id):
        session = iTestCommon()._getSession()
        response = session.Get_Test_PC_Id(Handset_Id=Handset_Id)
        return iTestCommon()._formResponse(response)

    def Get_Test_PC_Site(self, PC_Fqdn):
        session = iTestCommon()._getSession()
        response = session.Get_Test_PC_Site(PC_Fqdn=PC_Fqdn)
        return iTestCommon()._formResponse(response)

    def Get_TSHARK_Request_HTTP(self, URL, Pcap_File, Packet_Fields, Filter_Str):
        session = iTestCommon()._getSession()
        response = session.Get_TSHARK_Request_HTTP(URL=URL, Pcap_File=Pcap_File, Packet_Fields=Packet_Fields, Filter_Str=Filter_Str)
        return iTestCommon()._formResponse(response)

    def Get_Tshark_Capture_Interface(self, Node):
        session = iTestCommon()._getSession()
        response = session.Get_Tshark_Capture_Interface(Node=Node)
        return iTestCommon()._formResponse(response)

    def Get_Tshark_Details(self, Pcap_File, Filter_Str, Return_Data):
        session = iTestCommon()._getSession()
        response = session.Get_Tshark_Details(Pcap_File=Pcap_File, Filter_Str=Filter_Str, Return_Data=Return_Data)
        return iTestCommon()._formResponse(response)

    def Get_Tshark_Diameter(self, Pcap_File, Packet_Fields, Return_Data, Filter_Str):
        session = iTestCommon()._getSession()
        response = session.Get_Tshark_Diameter(Pcap_File=Pcap_File, Packet_Fields=Packet_Fields, Return_Data=Return_Data, Filter_Str=Filter_Str)
        return iTestCommon()._formResponse(response)

    def Get_Tshark_Request(self, Pcap_File, Packet_Fields, Return_Data, Filter_Str):
        session = iTestCommon()._getSession()
        response = session.Get_Tshark_Request(Pcap_File=Pcap_File, Packet_Fields=Packet_Fields, Return_Data=Return_Data, Filter_Str=Filter_Str)
        return iTestCommon()._formResponse(response)

    def Get_Tshark_Request_New_Version(self, Pcap_File, Packet_Fields, Return_Data, Filter_Str):
        session = iTestCommon()._getSession()
        response = session.Get_Tshark_Request_New_Version(Pcap_File=Pcap_File, Packet_Fields=Packet_Fields, Return_Data=Return_Data, Filter_Str=Filter_Str)
        return iTestCommon()._formResponse(response)

    def Get_Tshark_Ldap(self, Pcap_File, Packet_Fields, Return_Data, Filter_Str):
        session = iTestCommon()._getSession()
        response = session.Get_Tshark_Ldap(Pcap_File=Pcap_File, Packet_Fields=Packet_Fields, Return_Data=Return_Data, Filter_Str=Filter_Str)
        return iTestCommon()._formResponse(response)

    def Get_Tshark_Gsm_Map(self, Pcap_File, Message_Type, Packet_Fields, Return_Data, Filter_Str):
        session = iTestCommon()._getSession()
        response = session.Get_Tshark_Gsm_Map(Pcap_File=Pcap_File, Message_Type=Message_Type, Packet_Fields=Packet_Fields, Return_Data=Return_Data, Filter_Str=Filter_Str)
        return iTestCommon()._formResponse(response)

    def Get_TSHARK_Request_LDAP(self, URL, Pcap_File, Packet_Fields, Filter_Str):
        session = iTestCommon()._getSession()
        response = session.Get_TSHARK_Request_LDAP(URL=URL, Pcap_File=Pcap_File, Packet_Fields=Packet_Fields, Filter_Str=Filter_Str)
        return iTestCommon()._formResponse(response)

    def Get_TSHARK_Request_HTTP_vlanid(self, URL, Pcap_File, Packet_Fields, Filter_Str):
        session = iTestCommon()._getSession()
        response = session.Get_TSHARK_Request_HTTP_vlanid(URL=URL, Pcap_File=Pcap_File, Packet_Fields=Packet_Fields, Filter_Str=Filter_Str)
        return iTestCommon()._formResponse(response)

    def Get_TSHARK_Response_HTTP(self, ACK, Pcap_File, Packet_Fields, Filter_Str):
        session = iTestCommon()._getSession()
        response = session.Get_TSHARK_Response_HTTP(ACK=ACK, Pcap_File=Pcap_File, Packet_Fields=Packet_Fields, Filter_Str=Filter_Str)
        return iTestCommon()._formResponse(response)

    def Insert_Array_Values(self, Array_Id, Value, Name):
        session = iTestCommon()._getSession()
        response = session.Insert_Array_Values(Array_Id=Array_Id, Value=Value, Name=Name)
        return iTestCommon()._formResponse(response)

    def Is_Exit_Test(self, Exit_Status='0', Exit_Message='Exiting Test.'):
        session = iTestCommon()._getSession()
        response = session.Is_Exit_Test(Exit_Status=Exit_Status, Exit_Message=Exit_Message)
        return iTestCommon()._formResponse(response)

    def Is_In_IPv4_Subnet(self, IP, Subnet):
        session = iTestCommon()._getSession()
        response = session.Is_In_IPv4_Subnet(IP=IP, Subnet=Subnet)
        return iTestCommon()._formResponse(response)

    def Is_Leap_Year(self, This_Year):
        session = iTestCommon()._getSession()
        response = session.Is_Leap_Year(This_Year=This_Year)
        return iTestCommon()._formResponse(response)

    def List_Remove_Empty(self, List_In):
        session = iTestCommon()._getSession()
        response = session.List_Remove_Empty(List_In=List_In)
        return iTestCommon()._formResponse(response)

    def L2TP_Find_Tunnel_Session_SmallFile(self, Pcap_File, Calling_Number):
        session = iTestCommon()._getSession()
        response = session.L2TP_Find_Tunnel_Session_SmallFile(Pcap_File=Pcap_File, Calling_Number=Calling_Number)
        return iTestCommon()._formResponse(response)

    def L2TP_Find_Tunnel_Session(self, Pcap_File, Calling_Number):
        session = iTestCommon()._getSession()
        response = session.L2TP_Find_Tunnel_Session(Pcap_File=Pcap_File, Calling_Number=Calling_Number)
        return iTestCommon()._formResponse(response)

    def L2TP_Get_Message_Type(self, Pcap_File, Calling_Number, Type):
        session = iTestCommon()._getSession()
        response = session.L2TP_Get_Message_Type(Pcap_File=Pcap_File, Calling_Number=Calling_Number, Type=Type)
        return iTestCommon()._formResponse(response)

    def L2TP_PPP_Setup_Check(self, Lns_Id, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.L2TP_PPP_Setup_Check(Lns_Id=Lns_Id, Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def L2TP_PPP_TearDown_Check(self, Lac_Id, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.L2TP_PPP_TearDown_Check(Lac_Id=Lac_Id, Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def L2TP_KeepAlive_Check(self, Lac_Id, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.L2TP_KeepAlive_Check(Lac_Id=Lac_Id, Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def L2TP_Session_Setup_Check(self, Pcap_File, Lac_Tunnel, Lns_Tunnel, Calling_Msisdn):
        session = iTestCommon()._getSession()
        response = session.L2TP_Session_Setup_Check(Pcap_File=Pcap_File, Lac_Tunnel=Lac_Tunnel, Lns_Tunnel=Lns_Tunnel, Calling_Msisdn=Calling_Msisdn)
        return iTestCommon()._formResponse(response)

    def L2TP_Tunnel_TearDown_Check(self, Lac_Id, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.L2TP_Tunnel_TearDown_Check(Lac_Id=Lac_Id, Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def L2TP_Tunnel_Setup_Check(self, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.L2TP_Tunnel_Setup_Check(Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def Normalize_IPv6_Address(self, Pcap_File):
        session = iTestCommon()._getSession()
        response = session.Normalize_IPv6_Address(Pcap_File=Pcap_File)
        return iTestCommon()._formResponse(response)

    def PAC0678_Get_Latest(self, User_Id, User_Pass, File_Location='http://func3.collab.in.telstra.com.au/rep/func/0001234/refs/PAC0678%20-%20Wireless%20Value%20Based%20Charging%20Services.xls'):
        """
        Headline: PAC0678 Free-to-Browse List
        Author: Scott Tuohy
        """
        session = iTestCommon()._getSession()
        response = session.PAC0678_Get_Latest(User_Id=User_Id, User_Pass=User_Pass, File_Location=File_Location)
        return iTestCommon()._formResponse(response)

    def PAC0678_Spilt_Files(self, Csv_File):
        session = iTestCommon()._getSession()
        response = session.PAC0678_Spilt_Files(Csv_File=Csv_File)
        return iTestCommon()._formResponse(response)

    def PAC0678_Free_to_Browse_Check_Only(self, User_Id, Find_Url='1', Is_Datacard='0', IP_URL, User_Pass, File_Location='http://func3.collab.in.telstra.com.au/rep/func/0000136/refs/PAC0678%20-%20Wireless%20Value%20Based%20Charging%20Services.xls', PostOrPre='Postpaid'):
        """
        Headline: PAC0678 Free-to-Browse List
        Author: Scott Tuohy
        """
        session = iTestCommon()._getSession()
        response = session.PAC0678_Free_to_Browse_Check_Only(User_Id=User_Id, Find_Url=Find_Url, Is_Datacard=Is_Datacard, IP_URL=IP_URL, User_Pass=User_Pass, File_Location=File_Location, PostOrPre=PostOrPre)
        return iTestCommon()._formResponse(response)

    def PAC0678_Lookup_Dns(self, User_Id, Find_Url='1', Is_Datacard='0', IP_URL, User_Pass, File_Location='http://func3.collab.in.telstra.com.au/rep/func/0000136/refs/PAC0678%20-%20Wireless%20Value%20Based%20Charging%20Services.xls', PostOrPre='Postpaid'):
        """
        Headline: PAC0678 Free-to-Browse List
        Author: Scott Tuohy
        """
        session = iTestCommon()._getSession()
        response = session.PAC0678_Lookup_Dns(User_Id=User_Id, Find_Url=Find_Url, Is_Datacard=Is_Datacard, IP_URL=IP_URL, User_Pass=User_Pass, File_Location=File_Location, PostOrPre=PostOrPre)
        return iTestCommon()._formResponse(response)

    def PAC0678_Lookup_HTTP(self, Is_Datacard='0', IP_URL, PostOrPre='Postpaid'):
        """
        Headline: PAC0678 Free-to-Browse List
        Author: Scott Tuohy
        """
        session = iTestCommon()._getSession()
        response = session.PAC0678_Lookup_HTTP(Is_Datacard=Is_Datacard, IP_URL=IP_URL, PostOrPre=PostOrPre)
        return iTestCommon()._formResponse(response)

    def PAC0678_Lookup_IP(self, Is_Datacard='0', IP_URL, PostOrPre='Postpaid'):
        """
        Headline: PAC0678 Free-to-Browse List
        Author: Scott Tuohy
        """
        session = iTestCommon()._getSession()
        response = session.PAC0678_Lookup_IP(Is_Datacard=Is_Datacard, IP_URL=IP_URL, PostOrPre=PostOrPre)
        return iTestCommon()._formResponse(response)

    def PG_Login_SOAP(self):
        session = iTestCommon()._getSession()
        response = session.PG_Login_SOAP()
        return iTestCommon()._formResponse(response)

    def PG_Send_Request_SOAP(self, XML_File, Soap_Action='CAI3G#Get'):
        session = iTestCommon()._getSession()
        response = session.PG_Send_Request_SOAP(XML_File=XML_File, Soap_Action=Soap_Action)
        return iTestCommon()._formResponse(response)

    def Remove_Temp_Files(self):
        session = iTestCommon()._getSession()
        response = session.Remove_Temp_Files()
        return iTestCommon()._formResponse(response)

    def Seconds_Last_Modified(self, File_Name, File_Folder):
        session = iTestCommon()._getSession()
        response = session.Seconds_Last_Modified(File_Name=File_Name, File_Folder=File_Folder)
        return iTestCommon()._formResponse(response)

    def Setup_Test_Parameters_EPG(self):
        session = iTestCommon()._getSession()
        response = session.Setup_Test_Parameters_EPG()
        return iTestCommon()._formResponse(response)

    def SCP_File(self):
        session = iTestCommon()._getSession()
        response = session.SCP_File()
        return iTestCommon()._formResponse(response)

    def SFTP_File(self, File_To_Fetch, Over_Write, Delete_File, Ftp_Server_Name, Ftp_User, Ftp_Pass, Local_File_Path, Winscp_Path, get_put_oper='get', destFilePath):
        session = iTestCommon()._getSession()
        response = session.SFTP_File(File_To_Fetch=File_To_Fetch, Over_Write=Over_Write, Delete_File=Delete_File, Ftp_Server_Name=Ftp_Server_Name, Ftp_User=Ftp_User, Ftp_Pass=Ftp_Pass, Local_File_Path=Local_File_Path, Winscp_Path=Winscp_Path, get_put_oper=get_put_oper, destFilePath=destFilePath)
        return iTestCommon()._formResponse(response)

    def SFTP_File_Put(self, File_To_Put='0', Over_Write='1', Delete_File, Ftp_Server_Name, Ftp_User, Ftp_Pass, Local_File_Path, Source_File_Path, Single_File='Yes'):
        session = iTestCommon()._getSession()
        response = session.SFTP_File_Put(File_To_Put=File_To_Put, Over_Write=Over_Write, Delete_File=Delete_File, Ftp_Server_Name=Ftp_Server_Name, Ftp_User=Ftp_User, Ftp_Pass=Ftp_Pass, Local_File_Path=Local_File_Path, Source_File_Path=Source_File_Path, Single_File=Single_File)
        return iTestCommon()._formResponse(response)

    def SOAPUI_Adjust_Balance(self, path):
        session = iTestCommon()._getSession()
        response = session.SOAPUI_Adjust_Balance(path=path)
        return iTestCommon()._formResponse(response)

    def SOAPUI_Check_Balance(self, templatefile):
        session = iTestCommon()._getSession()
        response = session.SOAPUI_Check_Balance(templatefile=templatefile)
        return iTestCommon()._formResponse(response)

    def Sum_List(self, List_In):
        session = iTestCommon()._getSession()
        response = session.Sum_List(List_In=List_In)
        return iTestCommon()._formResponse(response)

    def Transfer_Ip_Mask_To_Inverse_Mask(self, Ip_Mask):
        """
        Description:
			Transfer IP mask to inverse mask, for example, it can transfer 255.255.255.0 to 0.0.0.15.
        """
        session = iTestCommon()._getSession()
        response = session.Transfer_Ip_Mask_To_Inverse_Mask(Ip_Mask=Ip_Mask)
        return iTestCommon()._formResponse(response)

    def Wireshark_Analysis_EPG_Old(self, Pcap_File, User_Cat='Postpaid', Apn_Use, User_Ip, Use_Datacard, FTB_IP, winscp_path):
        session = iTestCommon()._getSession()
        response = session.Wireshark_Analysis_EPG_Old(Pcap_File=Pcap_File, User_Cat=User_Cat, Apn_Use=Apn_Use, User_Ip=User_Ip, Use_Datacard=Use_Datacard, FTB_IP=FTB_IP, winscp_path=winscp_path)
        return iTestCommon()._formResponse(response)

    def Wireshark_Analysis_EPG_withSingleSession(self, Pcap_File, User_Cat='Postpaid', Apn_Use, User_Ip, Use_Datacard, FTB_IP, winscp_path):
        session = iTestCommon()._getSession()
        response = session.Wireshark_Analysis_EPG_withSingleSession(Pcap_File=Pcap_File, User_Cat=User_Cat, Apn_Use=Apn_Use, User_Ip=User_Ip, Use_Datacard=Use_Datacard, FTB_IP=FTB_IP, winscp_path=winscp_path)
        return iTestCommon()._formResponse(response)

    def Wireshark_Analysis_EPG(self, Pcap_File, User_Cat='Postpaid', Apn_Use, User_Ip, Use_Datacard, FTB_IP, winscp_path):
        session = iTestCommon()._getSession()
        response = session.Wireshark_Analysis_EPG(Pcap_File=Pcap_File, User_Cat=User_Cat, Apn_Use=Apn_Use, User_Ip=User_Ip, Use_Datacard=Use_Datacard, FTB_IP=FTB_IP, winscp_path=winscp_path)
        return iTestCommon()._formResponse(response)

    def WS_Adjust_TCP_Signalling(self, Stream_Ids, Client_Ip, File_Name):
        session = iTestCommon()._getSession()
        response = session.WS_Adjust_TCP_Signalling(Stream_Ids=Stream_Ids, Client_Ip=Client_Ip, File_Name=File_Name)
        return iTestCommon()._formResponse(response)

    def WS_Check_WebBrowsing_Result(self, Pcap_File, Website_Host, Http_type):
        session = iTestCommon()._getSession()
        response = session.WS_Check_WebBrowsing_Result(Pcap_File=Pcap_File, Website_Host=Website_Host, Http_type=Http_type)
        return iTestCommon()._formResponse(response)

    def getTclInterpreter(self):
        session = iTestCommon()._getSession()
        response = session.getTclInterpreter()
        return iTestCommon()._formResponse(response)

