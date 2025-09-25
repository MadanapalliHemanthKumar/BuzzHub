LOGIN FORM:
Imports  System.Data.SqlCl  ent flubl  c  Class  Form1
D  m  con  As  New  SqlConnect  on D  m  cmd  As  New  SqlCommand
D  m  Username  As  Str  ng D  m  flass  As  Str  ng
D  m  loc  As  flo  nt

flr  vate  Sub  Form1_Load(sender  As  Object,  e  As  EventArgs)  Handles  MyBase.Load flrogressBar1.V  s  ble  =  False
con.Connect  onStr  ng  =  My.Sett  ngs.WWDBConnStr  ng flasswordResetflanel.V  s  ble  =  False
ToolT  p1.SetToolT  p(CloseButton,  "Cl  ck  to  Close")      ToolT  p1.SetToolT  p(M  n  Button,  "Cl  ck  to  M  n  m  ze")   ToolT  p1.SetToolT  p(flINInfo,  "It's  a  4  d  g  t  Number") ToolT  p1.SetToolT  p(flassInfo,  "The  max  character	s  16")
 



End Sub


flr  vate  Sub  ButtOn1_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles LOg  nButtOn.Cl  ck
CursOr  =  CursOrs.Wa  tCursOr UseWa  tCursOr  =  True
Thread  ng.Thread.Sleep(1000)

'LOg  n
If  CheckLOg  nCredent  als()  Then L  nkLabel1.V  s  ble  =  False Thread  ng.Thread.Sleep(50) flrOgressBar1.V  s  ble  =  True D  m  a  As  Integer
FOr  a  =  5  TO  100
flrOgressBar1.Value  =  a Thread  ng.Thread.Sleep(5)
Next
Thread  ng.Thread.Sleep(100)
MessageBOx.ShOw(TextBOxUsername.Text  +  ",  yOu  have  lOg  ned	n successfully",  "WelcOme  :)",  MessageBOxButtOns.OK,  MessageBOxIcOn.InfOrmat  On)
flrOgressBar1.V  s  ble  =  False Thread  ng.Thread.Sleep(100) FOrm2.ShOw()
Me.H  de() TextBOxUsername.Clear() TextBOxflasswOrd.Clear()

ElseIf  TextBOxUsername.Text  =  ""  Or  TextBOxflasswOrd.Text  =  ""  Then MessageBOx.ShOw("fllease  enter  the  username  &  passwOrd",  "NO  Value
Entered",  MessageBOxButtOns.OK,  MessageBOxIcOn.Warn  ng)

'  ElseIf  TextBOx1.Text  =  Username  And  TextBOx2.Text  <>  flass  Then
'	MessageBOx.ShOw("Try  aga  n,  flasswOrd  yOu  entered	s	ncOrrect", "IncOrrect  flasswOrd  :(",  MessageBOxButtOns.OK,  MessageBOxIcOn.ErrOr)

'  ElseIf  TextBOx1.Text  <>  Username  And  TextBOx2.Text  =  flass  Then
'	MessageBOx.ShOw("Try  aga  n,  Username  yOu  entered	s	ncOrrect", "IncOrrect  Username  :(",  MessageBOxButtOns.OK,  MessageBOxIcOn.ErrOr)

Else
MessageBOx.ShOw("Username  Or  flasswOrd	s	ncOrrect",  "SOrry,Check  the credent  als",  MessageBOxButtOns.OK,  MessageBOxIcOn.ErrOr)
End If
L  nkLabel1.V  s  ble  =  True

UseWa  tCursOr  =  False CursOr  =  CursOrs.Default
End Sub

'clear  buttOn
flr  vate  Sub  ButtOn2_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles ClearButtOn.Cl  ck
TOOlT  p1.SetTOOlT  p(ClearButtOn,  "Cl  ck  here  tO  clear  the  text  fe  ld") If  TextBOxUsername.Text  =  ""  And  TextBOxflasswOrd.Text  =  ""  Then
MessageBOx.ShOw("There	s  nOth  ng  tO  clear,  TextBOxs  are  empty", "TextBOx  Already  Cleared",  MessageBOxButtOns.OK,  MessageBOxIcOn.ErrOr)
Else
flrOgressBar1.V  s  ble  =  False
 



L  nkLabel1.V  s  ble  =  True TextBOxUsername.Text  =  "" TextBOxflasswOrd.Text  =  ""
End If End Sub

'clOse  buttOn
flr  vate  Sub  ButtOn3_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles ClOseButtOn.Cl  ck

Me.ClOse()
End Sub

'm  n  m  ze  buttOn
flr  vate  Sub  ButtOn4_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles M  n  ButtOn.Cl  ck
Me.W  ndOwState  =  FOrmW  ndOwState.M  n  m  zed End Sub

'FOr  drag  ng
flr  vate  Sub  Spl  tCOnta  ner2_flanel1_MOuseDOwn(sender  As  Object,  e  As MOuseEventArgs)  Handles  Spl  tCOnta  ner2.flanel1.MOuseDOwn
If  e.ButtOn  =  MOuseButtOns.Left  Then lOc  =  e.LOcat  On
End If End Sub
flr  vate  Sub  Spl  tCOnta  ner2_flanel1_MOuseMOve(sender  As  Object,  e  As MOuseEventArgs)  Handles  Spl  tCOnta  ner2.flanel1.MOuseMOve
If  e.ButtOn  =  MOuseButtOns.Left  Then Me.LOcat  On  +=  e.LOcat  On  -  lOc
End If End Sub

'LOg  n  funct  On
flr  vate  Funct  On  CheckLOg  nCredent  als()  As  BOOlean

D  m  UnameInput  As  Str  ng  =  TextBOxUsername.Text D  m  flassInput  As  Str  ng  =  TextBOxflasswOrd.Text D  m  Answer  As  BOOlean  =  False
cOn.Open() cmd.COnnect  On  =  cOn
cmd.COmmandText  =  "SELECT  Username,flasswOrd  FROM  [User];"
D  m  dr1  As  SqlDataReader dr1  =  cmd.ExecuteReader Wh  le  dr1.Read()
Username  =  dr1("Username") flass  =  dr1("flasswOrd")
If  Username  =  UnameInput  And  flass  =  flassInput  Then Answer  =  True
End  If End  Wh  le cOn.ClOse() Return  Answer
End  Funct  On

'Rest  ng  passwOrd  l  nk
flr  vate  Sub  flasswOrdrest_L  nkCl  cked(sender  As  Object,  e  As L  nkLabelL  nkCl  ckedEventArgs)  Handles  L  nkLabel1.L  nkCl  cked
LOg  nflanel.V  s  ble  =  False flasswOrdResetflanel.V  s  ble  =  True
 



'D  m  a,  p  n  As  Integer 'p  n  =  "3554"
'a  =  InputBOx("Enter  the  secur  ty  p  n  fOr  resett  ng  the  passwOrd", "flASSWORD  RESET")
'If a = p n Then 'MsgBOx("It's  wOrk  ng") 'End  If
End Sub

'Back  buttOn  fOr  flasswOrd  Reset
flr  vate  Sub  Back_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles BackButtOn.Cl  ck
TOOlT  p1.SetTOOlT  p(BackButtOn,  "Back  tO  LOg  n  flage") UsernameTextBOx.Text  =  ""
flINTextBOx.Text  =  "" COnfflassTextBOx.Text  =  "" NewflassTextBOx.Text  =  ""
LOg  nflanel.V  s  ble  =  True flasswOrdResetflanel.V  s  ble  =  False
End Sub

'Clear  buttOn  fOr  flasswOrd  Reset
flr  vate  Sub  ClearButtOn2_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles ClearButtOn2.Cl  ck
TOOlT  p1.SetTOOlT  p(ClearButtOn2,  "Cl  ck  tO  clear  the  text  fe  ld") If  flINTextBOx.Text  =  ""  And  UsernameTextBOx.Text  =  ""  And
NewflassTextBOx.Text  =  ""  And  COnfflassTextBOx.Text  =  ""  Then MessageBOx.ShOw("There	s  nOth  ng  tO  clear,  TextBOxs  are  empty",
"TextBOx  Already  Cleared",  MessageBOxButtOns.OK,  MessageBOxIcOn.ErrOr)
Else
flINTextBOx.Text  =  "" UsernameTextBOx.Text  =  "" NewflassTextBOx.Text  =  "" COnfflassTextBOx.Text  =  ""
End If End Sub

'rest  buttOn
flr  vate  Sub  ResetButtOn_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles ResetButtOn.Cl  ck
TOOlT  p1.SetTOOlT  p(ResetButtOn,  "Cl  ck  tO  Reset  flasswOrd") If  NOt  CheckResetCredent  als()  Then
MessageBOx.ShOw("CrOsscheck  the  flIN  &  Username",  "WrOng  Credent  als", 0,  MessageBOxIcOn.ErrOr)

ElseIf  UsernameTextBOx.Text  =  ""  Or  flINTextBOx.Text  =  ""  Or NewflassTextBOx.Text  =  ""  Or  COnfflassTextBOx.Text  =  ""  Then
MessageBOx.ShOw("Enter  all  the  deta  ls",  "",  0, MessageBOxIcOn.Warn  ng)

ElseIf  NewflassTextBOx.Text  <>  COnfflassTextBOx.Text  Then MessageBOx.ShOw("The  passwOrds  dOesnt  match",  "",  0,
MessageBOxIcOn.ErrOr)

ElseIf  CheckResetCredent  als()  And  NewflassTextBOx.Text  = COnfflassTextBOx.Text  Then
D  m  dr1  As  SqlDataReader Try
cOn.Open() cmd.COnnect  On  =  cOn
 



cmd.COmmandText  =  "UflDATE  [User]  SET  flasswOrd  ='"  + COnfflassTextBOx.Text  +  "'  WHERE  Username  ='"  +  UsernameTextBOx.Text  +  "'"
dr1  =  cmd.ExecuteReader
MessageBOx.ShOw("flasswOrd  Updated  Sucessfully",  "",  0, MessageBOxIcOn.InfOrmat  On)
UsernameTextBOx.Text  =  "" flINTextBOx.Text  =  "" COnfflassTextBOx.Text  =  "" NewflassTextBOx.Text  =  "" cOn.ClOse()

Catch  ex  As  Except  On MsgBOx(ex.Message)
End Try End If
End Sub

flr  vate  Funct  On  CheckResetCredent  als()  As  BOOlean

D  m  UnameInput  As  Str  ng  =  UsernameTextBOx.Text D  m  flINInput  As  Str  ng  =  flINTextBOx.Text
D  m  Answer  As  BOOlean  =  False Try
cOn.Open() cmd.COnnect  On  =  cOn
cmd.COmmandText  =  "SELECT  Username,UserflIN  FROM  [User];"
D  m  dr1  As  SqlDataReader dr1  =  cmd.ExecuteReader Wh  le  dr1.Read()
Username  =  dr1("Username") flass  =  dr1("UserflIN")
If  Username  =  UnameInput  And  flass  =  flINInput  Then Answer  =  True
End  If End  Wh  le cOn.ClOse() Return  Answer
Catch  ex  As  Except  On MsgBOx("ERROR")
End Try End  Funct  On

flr  vate  Sub  flINTextBOx_keypress(sender  As  Object,  e  As  KeyflressEventArgs) Handles  flINTextBOx.Keyflress
If  Asc(e.KeyChar)  <>  13  AndAlsO  Asc(e.KeyChar)  <>  8  AndAlsO  NOt IsNumer  c(e.KeyChar)  Then
MsgBox(“fllease  enter  numbers  only”,  0,  "Inval  d  Character  ")
e.Handled  =  True End If
End Sub

'flasswOrd  V  s  b  l  ty
flr  vate  Sub  LOck_Cl  ck_1(sender  As  Object,  e  As  EventArgs)  Handles ButtOn1.Cl  ck
TOOlT  p1.SetTOOlT  p(V  s  bl  tyOpen,  "Cl  ck  here  tO  ShOw  the  flasswOrd") NewflassTextBOx.flasswOrdChar  =  "*"
COnfflassTextBOx.flasswOrdChar  =  "*" flINTextBOx.flasswOrdChar  =  "*"
V  s  bl  tyOpen.V  s  ble  =  True
 



ButtOn1.V  s  ble  =  False End Sub
flr  vate  Sub  LOckOpen_Cl  ck_1(sender  As  Object,  e  As  EventArgs)  Handles V  s  bl  tyOpen.Cl  ck
TOOlT  p1.SetTOOlT  p(ButtOn1,  "Cl  ck  here  tO  h  de  the  flasswOrd") NewflassTextBOx.flasswOrdChar  =  ""
COnfflassTextBOx.flasswOrdChar  =  "" flINTextBOx.flasswOrdChar  =  ""
V  s  bl  tyOpen.V  s  ble  =  False ButtOn1.V  s  ble  =  True
End Sub End  Class
FORM 2
ImpOrts  System.Data.SqlCl  ent ImpOrts  WashWOrld.MOdule1 flubl  c  Class  FOrm2
D  m  LOc  As  flO  nt
D  m  cOn  As  New  SqlCOnnect  On D  m  cmd  As  New  SqlCOmmand
D  m  sda  As  New  SqlDataAdapter D  m  dTable  As  New  DataTable   D  m  bs  As  New  B  nd  ngSOurce   D  m  prevBut  As  ButtOn
D  m  dr  As  SqlDataReader

flr  vate  Sub  ChangeButCOlOr(sender  As  Object,  e  As  EventArgs)  Handles CustButtOn.Cl  ck,  Veh  ButtOn.Cl  ck,  WOrkerButtOn.Cl  ck,  Serv  ceButtOn.Cl  ck,
InvO  ceButtOn.Cl  ck,  flayButtOn.Cl  ck
prevBut.BackCOlOr  =  COlOr.FrOmArgb(0,  0,  0,  0) sender.backcOlOr  =  COlOr.Wh  te
prevBut  =  sender End Sub

'**************  FORM  2  LOAD  ************
flr  vate  Sub  FOrm2_LOad(sender  As  Object,  e  As  EventArgs)  Handles  MyBase.LOad cOn.COnnect  OnStr  ng  =  My.Sett  ngs.WWDBCOnnStr  ng
Custflanel.V  s  ble  =  False
TOOlT  p1.SetTOOlT  p(CustIDInfO,  "Enter  the  custOmer  ID  Only  fOr  Updat  On and  Delet  On")
TOOlT  p1.SetTOOlT  p(CustNameInfO,  "Full  name  Of  the  custOmer") TOOlT  p1.SetTOOlT  p(flhOneInfO,  "flhOne  Number  w  thOut  ISD  cOde.")
TOOlT  p1.SetTOOlT  p(WOrkerflhOnInfO,  "flhOne  Number  w  thOut  ISD  cOde.") TOOlT  p1.SetTOOlT  p(WOrkIDInfO,  "Enter  the  WOrker  Ident  f  cat  On  Number") TOOlT  p1.SetTOOlT  p(WOkerNameInfO,  "Enter  the  Full  name  Of  the  WOrker") TOOlT  p1.SetTOOlT  p(Serv  ceID  nfO,  "Enter  the  Serv  ce  ID")
TOOlT  p1.SetTOOlT  p(CustIDInfO2,  "Enter  the  cOustOmer  ID") TOOlT  p1.SetTOOlT  p(RegInfO,  "Example  :  KL  13  J  1234  ") TOOlT  p1.SetTOOlT  p(CarRegInfO,  "Example  :  KL  13  AB  1235")
TOOlT  p1.SetTOOlT  p(CarBrandInfO,  "Example  :  BMW,  Benz,  Hyunda		etc.") TOOlT  p1.SetTOOlT  p(CarMOdelInfO,  "Example  :  Sw  ft,  E-Class,	-10  etc.") TOOlT  p1.SetTOOlT  p(Serv  ceTypeInfO,  "Enter  Or  Select  the  Serv  ce  Type.") TOOlT  p1.SetTOOlT  p(Sev  ceChargeInfO,  "Enter  the  COst  Of  sev  ce")
TOOlT  p1.SetTOOlT  p(flaymentIDInfO,  "It,s  autOmated  Or  enter  the  payment ID  maually")
TOOlT  p1.SetTOOlT  p(flaymentTypeInfO,  "Select  the  payment  Type") TOOlT  p1.SetTOOlT  p(InvO  ceIDInfO,  "Enter  the	nvO  ce  number")
 





prevBut  =  CustButtOn End Sub

'Return  tO  lOg  n  fOrm
flr  vate  Sub  ButtOn1_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles ButtOn1.Cl  ck
FOrm1.ShOw() Me.H  de()
End Sub

'clOse  buttOn
flr  vate  Sub  ButtOn2_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles ClOseButtOn2.Cl  ck
FOrm1.ClOse()

End Sub

'm  n  m  ze  buttOn
flr  vate  Sub  ButtOn9_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles M  n  ButtOn2.Cl  ck
Me.W  ndOwState  =  FOrmW  ndOwState.M  n  m  zed End Sub

'max  m  ze  buttOn
flr  vate  Sub  ButtOn8_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles MaxButtOn.Cl  ck
If  Me.W  ndOwState  =  FOrmW  ndOwState.Max  m  zed  Then Me.W  ndOwState  =  FOrmW  ndOwState.NOrmal
Else
Me.W  ndOwState  =  FOrmW  ndOwState.Max  m  zed End If
End Sub

flr  vate  Sub  ButtOn1_MOuseenter(sender  As  Object,  e  As  EventArgs)  Handles ButtOn1.MOuseEnter
ButtOn1.FOreCOlOr  =  COlOr.BlueV  Olet End Sub
flr  vate  Sub  ButtOn1_MOuseleave(sender  As  Object,  e  As  EventArgs)  Handles ButtOn1.MOuseLeave
ButtOn1.FOreCOlOr  =  COlOr.Black End Sub

'***************  CUSTOMER  flANEL  ****************** 'lOad  table  buttOn
flr  vate  Sub  LOadfOrm_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles LOadCustTableButtOn.Cl  ck
CustTablelOad() ClearCustTB()
End Sub

'lOad  Table  funct  On
flr  vate  Sub  CustTablelOad()
D  m  CustDGV  As  DataGr  dV  ew  =  Me.CustTableDataGr  dV  ew1 Try
cOn.Open()
 



cmd  =  New  SqlCOmmand("select  *  frOm  [Cust]",  cOn)
dr  =  cmd.ExecuteReader(COmmandBehav  Or.ClOseCOnnect  On) CustDGV.ROws.Clear()
DO  Wh  le  dr.Read  =  True
CustDGV.ROws.Add(dr(0),  dr(1),  dr(2),  dr(3))
LOOp
Catch  ex  As  Except  On MsgBOx(ex.Message)
F  nally
cmd.D  spOse() cOn.ClOse()
End Try End Sub

'Save  ButtOn
flr  vate  Sub  CustSaveBUT_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles CustSaveBUT.Cl  ck
Try
If  (CustNameTextBOx.Text  =  ""  Or  CustflhOneTextBOx.Text  =  "")  Then MsgBOx("fllease  enter  the  CustOmer  Deta  ls",
MsgBOxStyle.InfOrmat  On,  "Data  Updat  On  Unsuccessful") Else
cOn.Open() cmd.COnnect  On  =  cOn
cmd.COmmandType  =  COmmandType.Text cmd  =  New  SqlCOmmand("INSERT  INTO
[Cust](CustName,CustflhOne,CustAddress)  Values('"  &  CustNameTextBOx.Text  &  "','"  & CustflhOneTextBOx.Text  &  "','"  &  CustAddressTextBOx.Text  &  "')",  cOn)
cmd.ExecuteNOnǪuery() cOn.ClOse()
MsgBOx("CustOmer  "  +  CustNameTextBOx.Text  +  "	s  Successfully added  tO  CustOmer  Database",  MsgBOxStyle.InfOrmat  On,  "Data  Updat  On  Successful")
ClearCustTB() CustTablelOad()

End If
Catch  ex  As  Except  On MsgBOx(ex.Message)
End Try ' Try
'CustB  nd  ngSOurce.EndEd  t() 'CustTableAdapter.Update(Database1DataSet.Cust) 'MsgBOx("Saved  Successfully")
'Catch  ex  As  Except  On 'MsgBOx(ex,  0,  "Message")

'End  Try End Sub

'Upadte  ButtOn
flr  vate  Sub  CustUpdateButt_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles CustUpdateButt.Cl  ck
CustIDTextBOx.ReadOnly  =  False Try
If  (CustIDTextBOx.Text  =  ""  Or  CustNameTextBOx.Text  =  ""  Or CustflhOneTextBOx.Text  =  "")  Then
MsgBOx("fllease  enter  the  deta  ls  fOr  updat  On")
Else
cOn.Open()
 



cmd  =  New  SqlCOmmand("UflDATE  [Cust]  SET  CustName  =  '"  & CustNameTextBOx.Text  &  "'  ,  CustflhOne=  '"  &  CustflhOneTextBOx.Text  &  "', CustAddress  =  '"  &  CustAddressTextBOx.Text  &  "'	WHERE  CustID  =  '"  & CustIDTextBOx.Text  &  "'",  cOn)
D  m	As  Integer
=  cmd.ExecuteNOnǪuery If	> 0 Then
MsgBOx("Updated  the  Custmer  deat  ls  Successfully", MsgBOxStyle.InfOrmat  On,  "Data  Updat  On  Successful")
Else
MsgBOx("Fa  led	n  Updat  ng  data",  MsgBOxStyle.InfOrmat  On, "Data  Updat  On  Unsuccessful")
End If cOn.ClOse() CustTablelOad() ClearCustTB()

End If
Catch  ex  As  Except  On MsgBOx(ex.Message)
F  nally
cmd.D  spOse() cOn.ClOse()
End Try End Sub

'Delete  ButtOn
flr  vate  Sub  CustDeleteBut_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles CustDeleteBut.Cl  ck
D  m  CustDGV  As  DataGr  dV  ew  =  Me.CustTableDataGr  dV  ew1 CustIDTextBOx.ReadOnly  =  False
Try
If  (CustNameTextBOx.Text  =  ""  Or  CustflhOneTextBOx.Text  =  "")  Then MsgBOx("fllease  enter  the  CustOmer  ID  tO  Delete")
 
Else
 

cOn.Open()
cmd  =  New  SqlCOmmand("DELETE  FROM  [Cust]  WHERE  CustID  =  '"  &
 
CustIDTextBOx.Text  &  "'",  cOn)
dr  =  cmd.ExecuteReader(COmmandBehav  Or.ClOseCOnnect  On) MsgBOx("CustOmer  "  &  CustNameTextBOx.Text  &  "  Deleted
Successfully",  MsgBOxStyle.InfOrmat  On,  "Data  Updat  On") cOn.ClOse()
ClearCustTB() CustTablelOad()

'  DO  Wh  le  dr.Read  =  True 'CustDGV.ROws.Add(dr(0),  dr(1),  dr(2),  dr(3)) 'LOOp
End If
Catch  ex  As  Except  On MsgBOx(ex.Message)
F  nally
cmd.D  spOse() cOn.ClOse()
End Try End Sub
'TextBOx  AutOF  ll
 



flr  vate  Sub  CustIDTextBOx_Keyflress(sender  As  Object,  e  As  KeyflressEventArgs) Handles  CustIDTextBOx.Keyflress
Try
If  e.KeyChar  =  M  crOsOft.V  sualBas  c.ChrW(Keys.Return)  Or  e.KeyChar  =
M  crOsOft.V  sualBas  c.ChrW(Keys.Space)  Then cOn.Open()
sda  =  New  SqlDataAdapter("SELECT  CustID,  CustName,  CustflhOne, CustAddress  FROM  [Cust]  WHERE  CustID  ='"  &  CustIDTextBOx.Text  &  "'",  cOn)
D  m  table  As  New  DataTable() sda.F  ll(table)
CustNameTextBOx.Text  =  table(0)(1) CustflhOneTextBOx.Text  =  table(0)(2) CustAddressTextBOx.Text  =  table(0)(3) cOn.ClOse()

End If
Catch  ex  As  Except  On
MsgBOx("Inval  d  User  ID,  fllease  check  the  User  ID") End Try

End Sub


'Select  frOm  cust  table  test
flr  vate  Sub  dataGr  dV  ew1_CellMOuseCl  ck(sender  As  System.Object,  e  As System.W  ndOws.FOrms.DataGr  dV  ewCellMOuseEventArgs)  Handles CustTableDataGr  dV  ew1.CellMOuseCl  ck
Try
If  e.ROwIndex  >=  0  Then
D  m  rOw  As  DataGr  dV  ewROw  = CustTableDataGr  dV  ew1.ROws(e.ROwIndex)
CustIDTextBOx.Text  =  rOw.Cells(0).Value.TOStr  ng CustNameTextBOx.Text  =  rOw.Cells(1).Value.TOStr  ng CustflhOneTextBOx.Text  =  rOw.Cells(2).Value.TOStr  ng CustAddressTextBOx.Text  =  rOw.Cells(3).Value.TOStr  ng
End If

Catch  ex  As  Except  On MsgBOx(ex.Message)
End Try End Sub


'clear  textbOx
flr  vate  Sub  ClearCustTB() CustIDTextBOx.Text  =  "" CustNameTextBOx.Text  =  "" CustflhOneTextBOx.Text  =  "" CustAddressTextBOx.Text  =  ""
End Sub

'flannel  LayOut  and  cOlOur
flr  vate  Sub  Cust_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles CustButtOn.Cl  ck
CustTablelOad() Custflanel.V  s  ble  =  True
Veh  cleflanel.V  s  ble  =  False WOrkerflanel.V  s  ble  =  False Serv  ceflanel.V  s  ble  =  False InvO  ceflanel.V  s  ble  =  False
 



flaymentflanel.V  s  ble  =  False

CustglOw.BackCOlOr  =  COlOr.FrOmArgb(255,  50,  135,  212)
Veh  glOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
ServglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
WOrkglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
InvOglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
flaymglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)

End Sub




'*********************VEHICLE  flANEL************************* 'lOad  Veh  cle  Table  funct  On
flr  vate  Sub  Veh  TablelOad()
D  m  Veh  DGV  As  DataGr  dV  ew  =  Me.Veh  cleDataGr  dV  ew Try
cOn.Open()
cmd  =  New  SqlCOmmand("SELECT  C.CustID,  C.CustName,  V.CarRegnO, V.CarBrand,  V.CarMOdel,  V.CarType  FROM  Cust  C,  Car  V  WHERE  V.CustID=C.CustID", cOn)
dr  =  cmd.ExecuteReader(COmmandBehav  Or.ClOseCOnnect  On) Veh  DGV.ROws.Clear()
DO  Wh  le  dr.Read  =  True
Veh  DGV.ROws.Add(dr(0),  dr(1),  dr(2),  dr(3),  dr(4),  dr(5))
LOOp
cOn.ClOse()
Catch  ex  As  Except  On MsgBOx(ex.Message)
F  nally
cmd.D  spOse() cOn.ClOse()
End Try End Sub

'LOad  ButtOn
flr  vate  Sub  Veh  LOadButt_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles Veh  LOadButt.Cl  ck
Veh  TablelOad() ClearVeh  TB()
End Sub

'Upadte  ButtOn
flr  vate  Sub  Veh  UpdateButt_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles Veh  UpdateButt.Cl  ck
Try
If  (CustIDTextBOx1.Text  =  ""  Or  CarRegNOTextBOx.Text  =  ""  Or CarBrandTextBOx.Text  =  "")  Then
MsgBOx("fllease  enter  the  deta  ls  fOr  updat  On")
Else
cOn.Open()
cmd  =  New  SqlCOmmand("UflDATE  [Car]  SET  CustID='"  &
CustIDTextBOx1.Text  &  "',  CarRegNO  =  '"  &  CarRegNOTextBOx.Text  &  "'  ,  CarBrand= '"  &  CarBrandTextBOx.Text  &  "',	CarMOdel  =  '"  &  CarMOdelTextBOx.Text  &  "', CarType  ='"  &  CarTypeCOmbOBOx.Text  &  "'	WHERE  CarRegNO  =  '"  & CarRegNOTextBOx.Text  &  "'",  cOn)
 



'Or  CustID  =  '"  &  CustIDTextBOx1.Text  &  "'",  cOn) D  m	As  Integer
=  cmd.ExecuteNOnǪuery If	> 0 Then
MsgBOx("Updated  the  Car  deat  ls  Successfully", MsgBOxStyle.InfOrmat  On,  "Data  Updat  On  Successful")
Else
MsgBOx("Fa  led	n  Updat  ng  data",  MsgBOxStyle.InfOrmat  On, "Data  Updat  On  Unsuccessful")
End If cOn.ClOse()
Veh  TablelOad() ClearVeh  TB()

End If
Catch  ex  As  Except  On MsgBOx(ex.Message)
F  nally
cmd.D  spOse() cOn.ClOse()
End Try End Sub

'Add  ButtOn
flr  vate  Sub  Veh  AddButt_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles Veh  AddButt.Cl  ck
Try
If  (CustIDTextBOx1.Text  =  ""  Or  CarRegNOTextBOx.Text  =  "")  Then MsgBOx("fllease  enter  the  Car  Deta  ls",  MsgBOxStyle.InfOrmat  On,
"Data  Updat  On  Unsuccessful") Else
cOn.Open() cmd.COnnect  On  =  cOn
cmd.COmmandType  =  COmmandType.Text
cmd  =  New  SqlCOmmand("INSERT  INTO  [Car](CustID,  CarRegNO, CarBrand,  CarMOdel,  CarType)  Values('"  &  CustIDTextBOx1.Text  &  "','"  & CarRegNOTextBOx.Text  &  "','"  &  CarBrandTextBOx.Text  &  "',  '"  & CarMOdelTextBOx.Text  &  "',  '"  &  CarTypeCOmbOBOx.Text  &  "')",  cOn)
cmd.ExecuteNOnǪuery() cOn.ClOse()
MsgBOx("CustOmer  "  +  CustNameTextBOx.Text  +  "	s  Successfully added  tO  CustOmer  Databse",  MsgBOxStyle.InfOrmat  On,  "Data  Updat  On  Successful")
ClearVeh  TB() Veh  TablelOad()

End If
Catch  ex  As  Except  On MsgBOx(ex.Message)
End Try End Sub 'Delete  ButtOn
flr  vate  Sub  Veh  DeleteButt_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles Veh  DeleteButt.Cl  ck
Try
If  (CustIDTextBOx1.Text  =  ""  Or  CarRegNOTextBOx.Text  =  ""  Or CarBrandTextBOx.Text  =  "")  Then
MsgBOx("fllease  enter  the  Reg  strat  On  Number  tO  Delete")
Else
cOn.Open()
 



cmd  =  New  SqlCOmmand("DELETE  FROM  [Car]  WHERE  CarRegNO  =  '"  & CarRegNOTextBOx.Text  &  "'",  cOn)
dr  =  cmd.ExecuteReader(COmmandBehav  Or.ClOseCOnnect  On) MsgBOx("Car  Reg  strat  On"  &  CarRegNOTextBOx.Text  &  "  Deleted
Successfully",  MsgBOxStyle.InfOrmat  On,  "Data  Updat  On") cOn.ClOse()
ClearVeh  TB() Veh  TablelOad()

End If
Catch  ex  As  Except  On MsgBOx(ex.Message)
F  nally
cmd.D  spOse() cOn.ClOse()
End Try End Sub

'selct  On  test
flr  vate  Sub  CarTable_CellMOuseCl  ck(sender  As  System.Object,  e  As System.W  ndOws.FOrms.DataGr  dV  ewCellMOuseEventArgs)  Handles
Veh  cleDataGr  dV  ew.CellMOuseCl  ck Try
If  e.ROwIndex  >=  0  Then
D  m  rOw  As  DataGr  dV  ewROw  =  Veh  cleDataGr  dV  ew.ROws(e.ROwIndex) CustIDTextBOx1.Text  =  rOw.Cells(0).Value.TOStr  ng CarRegNOTextBOx.Text  =  rOw.Cells(2).Value.TOStr  ng
End If
Catch  ex  As  Except  On MsgBOx(ex.Message)
End Try
End Sub 'AutO  f  ll
flr  vate  Sub  CarRegNOTextBOx_Keyflress(sender  As  Object,  e  As KeyflressEventArgs)  Handles  CarRegNOTextBOx.Keyflress
Try
If  e.KeyChar  =  M  crOsOft.V  sualBas  c.ChrW(Keys.Return)  Then cOn.Open()
sda  =  New  SqlDataAdapter("SELECT  CustID,  CarRegNO,  CarBrand, CarMOdel,  CarType  FROM  [Car]  WHERE  CarRegNO  ='"  &  CarRegNOTextBOx.Text  &  "'", cOn)
D  m  table  As  New  DataTable() sda.F  ll(table) CustIDTextBOx1.Text  =  table(0)(0)
CarBrandTextBOx.Text  =  table(0)(2) CarMOdelTextBOx.Text  =  table(0)(3) CarTypeCOmbOBOx.SelectedText  =  table(0)(4) cOn.ClOse()
End If
Catch  ex  As  Except  On
MsgBOx("Inval  d  RegNO,  fllease  check  the  Reg  strat  On  Number") End Try
End Sub


'Car  TB  clear
flr  vate  Sub  ClearVeh  TB() CustIDTextBOx1.Text  =  "" CarBrandTextBOx.Text  =  ""
 



CarMOdelTextBOx.Text  =  "" CarRegNOTextBOx.Text  =  "" CarTypeCOmbOBOx.ResetText() CarTypeflB.Image  =  NOth  ng
End Sub

'Veh  cle  flanel  cOlOr
flr  vate  Sub  Veh  _Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles Veh  ButtOn.Cl  ck
Veh  TablelOad() Custflanel.V  s  ble  =  False
Veh  cleflanel.V  s  ble  =  True WOrkerflanel.V  s  ble  =  False Serv  ceflanel.V  s  ble  =  False InvO  ceflanel.V  s  ble  =  False flaymentflanel.V  s  ble  =  False

CustglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
Veh  glOw.BackCOlOr  =  COlOr.FrOmArgb(255,  50,  135,  212)
ServglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
WOrkglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
InvOglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
flaymglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
End Sub
flr  vate  Sub  COmbOBOx1_SelectedIndexChanged(sender  As  Object,  e  As  EventArgs) Handles  CarTypeCOmbOBOx.SelectedIndexChanged

D  m  type  As  Integer
type  =  CarTypeCOmbOBOx.SelectedIndex Select  Case  type
Case 0
CarTypeflB.Image  =  WashWOrld.My.ResOurces.ResOurces.MICRO Case 1
CarTypeflB.Image  =  WashWOrld.My.ResOurces.ResOurces.SEDAN Case 2
CarTypeflB.Image  =  WashWOrld.My.ResOurces.ResOurces.HATCHBACK Case 3
CarTypeflB.Image  =  WashWOrld.My.ResOurces.ResOurces.ROADSTER Case 4
CarTypeflB.Image  =  WashWOrld.My.ResOurces.ResOurces.COUflE Case 5
CarTypeflB.Image  =  WashWOrld.My.ResOurces.ResOurces.CUV Case 6
CarTypeflB.Image  =  WashWOrld.My.ResOurces.ResOurces.SUV Case  Else
CarTypeflB.Image  =  NOth  ng End  Select
End Sub
'****************SERVICE  flANEL******************** 'lOad  serv  ce  Table  funct  On
flr  vate  Sub  Serv  ceTablelOad()
D  m  Serv  DGV  As  DataGr  dV  ew  =  Me.Serv  ceDataGr  dV  ew Try
cOn.Open()
cmd  =  New  SqlCOmmand("SELECT  V.CarRegNO,  S.Serv  ceID,  S.Serv  ceType, S.Serv  ceCharge,  S.WOrkID,  S.Serv  ceDesc  FROM  Serv	S,  Car  V  WHERE S.CarRegNO=V.CarRegNO",  cOn)
dr  =  cmd.ExecuteReader(COmmandBehav  Or.ClOseCOnnect  On) Serv  DGV.ROws.Clear()
 



DO  Wh  le  dr.Read  =  True
Serv  DGV.ROws.Add(dr(0),  dr(1),  dr(2),  dr(3),  dr(4),  dr(5))
LOOp
cOn.ClOse()
Catch  ex  As  Except  On MsgBOx(ex.Message)
F  nally
cmd.D  spOse() cOn.ClOse()
End Try End Sub

'Clear  TextBOx
flr  vate  Sub  ClearServ  TB() RegNOTB.Text  =  "" ServIDTB.Text  =  "" ServTypeCOmbOBOx.ResetText() ServChargeTB.Text  =  "" WOrkerIDTextBOx2.Text  =  "" Serv  ceDesc.Text  =  ""
End Sub

'lOad  ButtOn
flr  vate  Sub  ServTableLOadButtOn_Cl  ck(sender  As  Object,  e  As  EventArgs) Handles  ServTableLOadButtOn.Cl  ck
Serv  ceTablelOad() ClearServ  TB()
End Sub

'Add  ButtOn
flr  vate  Sub  Serv  AddButt_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles Serv  AddButt.Cl  ck
Try
If  (RegNOTB.Text  =  ""  Or  ServChargeTB.Text  =  "")  Then MsgBOx("fllease  enter  the  Serv  ce  Deta  ls",
MsgBOxStyle.InfOrmat  On,  "Data  Updat  On  Unsuccessful") Else
cOn.Open() cmd.COnnect  On  =  cOn
cmd.COmmandType  =  COmmandType.Text
cmd  =  New  SqlCOmmand("INSERT  INTO  [Serv  ](CarRegNO,  Serv  ceType, Serv  ceCharge,  WOrkID,  Serv  ceDesc)  Values('"  &  RegNOTB.Text  &  "','"  & ServTypeCOmbOBOx.Text  &  "',  '"  &  ServChargeTB.Text  &  "',  '"  & WOrkerIDTextBOx2.Text  &  "',	'"  &  Serv  ceDesc.Text  &  "')",  cOn)
cmd.ExecuteNOnǪuery() cOn.ClOse()
MsgBOx("Reg  strat  On  "  +  RegNOTB.Text  +  "	s  Successfully  added tO  Serv  ce  Database",  MsgBOxStyle.InfOrmat  On,  "Data  Updat  On  Successful")
ClearServ  TB() Serv  ceTablelOad()

End If
Catch  ex  As  Except  On MsgBOx(ex.Message)
F  nally
cmd.D  spOse() cOn.ClOse()

End Try End Sub
 




'Update  ButtOn  serv  ce
flr  vate  Sub  Serv  UpdateButt_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles Serv  UpdateButt.Cl  ck
Try
 

"") Then
 
If  (RegNOTB.Text  =  ""  Or  ServChargeTB.Text  =  ""  Or  ServIDTB.Text  =

MsgBOx("fllease  enter  the  serv  ce  deta  ls  fOr  updat  On")
Else
cOn.Open()
cmd  =  New  SqlCOmmand("UflDATE  [Serv  ]  SET	CarRegNO  =  '"  &
 
RegNOTB.Text  &  "'  ,  Serv  ceType=  '"  &  ServTypeCOmbOBOx.Text  &  "',	Serv  ceCharge
=  '"  &  ServChargeTB.Text  &  "',  WOrkID  ='"  &  WOrkerIDTextBOx2.Text  &  "',
Serv  ceDesc='"  &  Serv  ceDesc.Text  &  "'	WHERE  Serv  ceID  =  '"  &  ServIDTB.Text  & "'",  cOn)
'Or  CustID  =  '"  &  CustIDTextBOx1.Text  &  "'",  cOn) D  m	As  Integer
=  cmd.ExecuteNOnǪuery If	> 0 Then
MsgBOx("Serv  ce  deta  ls  updated  Successfully", MsgBOxStyle.InfOrmat  On,  "Data  Updat  On  Successful")
Else
MsgBOx("Fa  led	n  Updat  ng  data",  MsgBOxStyle.InfOrmat  On, "Data  Updat  On  Unsuccessful")
End If cOn.ClOse()
Serv  ceTablelOad() ClearServ  TB()

End If
Catch  ex  As  Except  On MsgBOx(ex.Message)
F  nally
cmd.D  spOse() cOn.ClOse()
End Try End Sub

'selct  On  test
flr  vate  Sub  Serv  ceTable_CellMOuseCl  ck(sender  As  System.Object,  e  As System.W  ndOws.FOrms.DataGr  dV  ewCellMOuseEventArgs)  Handles
Serv  ceDataGr  dV  ew.CellMOuseCl  ck Try
If  e.ROwIndex  >=  0  Then
D  m  rOw  As  DataGr  dV  ewROw  =  Serv  ceDataGr  dV  ew.ROws(e.ROwIndex) RegNOTB.Text  =  rOw.Cells(0).Value.TOStr  ng
ServIDTB.Text  =  rOw.Cells(1).Value.TOStr  ng End If
Catch  ex  As  Except  On MsgBOx(ex.Message)
End Try End Sub
'AutO  f  ll
flr  vate  Sub  RegNOTextBOx_Keyflress(sender  As  Object,  e  As  KeyflressEventArgs) Handles  ServIDTB.Keyflress
Try
If  Asc(e.KeyChar)  <>  13  AndAlsO  Asc(e.KeyChar)  <>  8  AndAlsO  NOt IsNumer  c(e.KeyChar)  Then
MsgBox(“fllease  enter  numbers  only”,  0,  "Inval  d  Character  ")
 



e.Handled  =  True End If
If  e.KeyChar  =  M  crOsOft.V  sualBas  c.ChrW(Keys.Return)  Then cOn.Open()
sda  =  New  SqlDataAdapter("SELECT  CarRegNO,  serv  ceID,
Serv  ceType,  Serv  ceCharge,  WOrkID,  Serv  ceDesc  FROM  [Serv  ]  WHERE  Serv  ceID  ='" &  ServIDTB.Text  &  "'",  cOn)
D  m  table  As  New  DataTable() sda.F  ll(table)
RegNOTB.Text  =  table(0)(0) ServTypeCOmbOBOx.Text  =  table(0)(2) ServChargeTB.Text  =  table(0)(3) WOrkerIDTextBOx2.Text  =  table(0)(4) Serv  ceDesc.Text  =  table(0)(5) cOn.ClOse()
End If
Catch  ex  As  Except  On
MsgBOx("Inval  d  Serv  ce  ID,  fllease  check  the  Serv  ce  ID  and  try
aga n")
End Try
End Sub

'COmbOBOx  AutOF  ll
flr  vate  Sub  ServTypeCOmbOBOx_SelectedIndexChanged(sender  As  Object,  e  As EventArgs)  Handles  ServTypeCOmbOBOx.SelectedIndexChanged
D  m  type  As  Integer
D  m  bkl  =  Env  rOnment.NewL  ne
type  =  ServTypeCOmbOBOx.SelectedIndex Select  Case  type
Case 0
Serv  ceDesc.Text  =  "*  Wheel  Arc	"  &  bkl  &  "*  BOdy  Wash  "  &  bkl  & "*  AutO  Wax  flOl  sh  "  &  bkl  &  "*  UnderChase  Wash  "  &  bkl  &  "*  Inter  rOr  Clean  ng  "
Case 1
Serv  ceDesc.Text  =  "*  Wheel  Arc	"  &  bkl  &  "*  BOdy  Wash  "  &  bkl  & "*  AutO  Wax  "  &  bkl  &  "*  Inter  rOr  Clean  ng  "
Case 2
Serv  ceDesc.Text  =  "*  Vaccum  Clean  ng  " Case 3
Serv  ceDesc.Text  =  "*  Wheel  Arc	"  &  bkl  &  "*  Under  BOdy  Wash  " Case 4
Serv  ceDesc.Text  =  "*  AutO  Wax  " Case  Else
Serv  ceDesc.Text  =  "" End  Select
End Sub
flr  vate  Sub  Serv  ceButtOn_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles Serv  ceButtOn.Cl  ck
Serv  ceTablelOad() Custflanel.V  s  ble  =  False Veh  cleflanel.V  s  ble  =  False WOrkerflanel.V  s  ble  =  False Serv  ceflanel.V  s  ble  =  True InvO  ceflanel.V  s  ble  =  False flaymentflanel.V  s  ble  =  False

CustglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
Veh  glOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
ServglOw.BackCOlOr  =  COlOr.FrOmArgb(255,  50,  135,  212)
WOrkglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
InvOglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
flaymglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
 



End Sub

'***************************WORKER  DETAILS  ********************* 'WOrker  flanel
flr  vate  Sub  LOadWOrkTable_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles LOadWOrkTable.Cl  ck
WOrkerLOadTable()
End Sub

'table  lOad  funct  On
flr  vate  Sub  WOrkerLOadTable()
D  m  WOrkerDGV  As  DataGr  dV  ew  =  Me.WOrkerTableDataGr  dV  ew Try
cOn.Open()
cmd  =  New  SqlCOmmand("SELECT  WOrkID,  WOrkName,  WOrkAddress, WOrkflhOne,  WOrkJObT  tle  FROM  WOrker",  cOn)
dr  =  cmd.ExecuteReader(COmmandBehav  Or.ClOseCOnnect  On) WOrkerDGV.ROws.Clear()
DO  Wh  le  dr.Read  =  True
WOrkerDGV.ROws.Add(dr(0),  dr(1),  dr(2),  dr(3),  dr(4))
LOOp
cOn.ClOse()
Catch  ex  As  Except  On MsgBOx(ex.Message)
F  nally
cmd.D  spOse() cOn.ClOse()
End Try

End Sub
flr  vate  Sub  WOrkerButtOn_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles WOrkerButtOn.Cl  ck
WOrkerLOadTable() Custflanel.V  s  ble  =  False Veh  cleflanel.V  s  ble  =  False WOrkerflanel.V  s  ble  =  True Serv  ceflanel.V  s  ble  =  False InvO  ceflanel.V  s  ble  =  False flaymentflanel.V  s  ble  =  False

CustglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
Veh  glOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
ServglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
WOrkglOw.BackCOlOr  =  COlOr.FrOmArgb(255,  50,  135,  212)
InvOglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
flaymglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
End Sub

'InvO  ce  flannel
flr  vate  Sub  Text_cnter(sender  As  Object,  e  As  EventArgs)  Handles InvO  ceflanel.Enter
Serv  ceInvO.TextAl  gn  =  COntentAl  gnment.M  ddleCenter End Sub
flr  vate  Sub  InvO  ceButtOn_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles InvO  ceButtOn.Cl  ck
ClearF  elds() lOadCB(RegNOInvOCB) Custflanel.V  s  ble  =  False Veh  cleflanel.V  s  ble  =  False WOrkerflanel.V  s  ble  =  False Serv  ceflanel.V  s  ble  =  False
 



InvO  ceflanel.V  s  ble  =  True flaymentflanel.V  s  ble  =  False

CustglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
Veh  glOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
ServglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
WOrkglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
InvOglOw.BackCOlOr  =  COlOr.FrOmArgb(255,  50,  135,  212)
flaymglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
End Sub

'flayment  flannel
flr  vate  Sub  flayButtOn_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles flayButtOn.Cl  ck
Custflanel.V  s  ble  =  False Veh  cleflanel.V  s  ble  =  False WOrkerflanel.V  s  ble  =  False Serv  ceflanel.V  s  ble  =  False InvO  ceflanel.V  s  ble  =  False flaymentflanel.V  s  ble  =  True

CustglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
Veh  glOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
ServglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
WOrkglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
InvOglOw.BackCOlOr  =  COlOr.FrOmArgb(0,  50,  135,  212)
flaymglOw.BackCOlOr  =  COlOr.FrOmArgb(255,  50,  135,  212)
End Sub

'FOr  drag  ng
flr  vate  Sub  flanel1_MOuseDOwn(sender  As  Object,  e  As  MOuseEventArgs)  Handles flanel1.MOuseDOwn
If  e.ButtOn  =  MOuseButtOns.Left  Then LOc  =  e.LOcat  On
End If End Sub
flr  vate  Sub  flanel1_MOuseMOve(sender  As  Object,  e  As  MOuseEventArgs)  Handles flanel1.MOuseMOve
If  e.ButtOn  =  MOuseButtOns.Left  Then Me.LOcat  On  +=  e.LOcat  On  -  LOc
End If End Sub

flr  vate  Sub  CustB  nd  ngNav  gatOrSaveItem_Cl  ck(sender  As  Object,  e  As EventArgs)
Me.Val  date()
'  Me.CustB  nd  ngSOurce.EndEd  t() 'Me.TableAdapterManager.UpdateAll(Me.Database1DataSet)

End Sub

flr  vate  Sub  InvO  ceflanel_fla  nt(sender  As  Object,  e  As  fla  ntEventArgs)  Handles InvO  ceflanel.fla  nt

End Sub

flr  vate  Sub  ServIDTB_Keyflress(sender  As  Object,  e  As  EventArgs)  Handles ServIDTB.TextChanged

End Sub
 



'*********************  TEXTBOX  VALIDATION  ******************************* flr  vate  Sub  flINTextBOx_keypress(sender  As  Object,  e  As  KeyflressEventArgs)
Handles  WOrkerIDTextBOx2.Keyflress,  WOrkerflhOneTextBOx.Keyflress, CustflhOneTextBOx.Keyflress,  CustIDTextBOx.Keyflress,  CustIDTextBOx1.Keyflress
If  Asc(e.KeyChar)  <>  13  AndAlsO  Asc(e.KeyChar)  <>  8  AndAlsO  NOt IsNumer  c(e.KeyChar)  Then
MsgBox(“fllease  enter  numbers  only”,  0,  "Inval  d  Character  ")
e.Handled  =  True End If
End Sub

'*************************  flRINT  flREVIEW  ******************************** flr  vate  Sub  btnpr  nt_Cl  ck(sender  As  Object,  e  As  EventArgs)  Handles
btnpr  nt.Cl  ck
If  Serv  ceDataGr  dV  ew.ROws.COunt  =  0  Then
MsgBOx("fllease  lOad  Items  tO  pr  nt.",  MsgBOxStyle.Exclamat  On,
"RepOrt")
Ex t Sub
End If
flr  ntD  alOg1.DOcument  =  Me.flr  ntDOcument1
D  m  ButtOnflressed  As  D  alOgResult  =  flr  ntD  alOg1.ShOwD  alOg() If  (ButtOnflressed  =  D  alOgResult.OK)  Then
Me.He  ght  =  Me.He  ght flanel1.He  ght  =  flanel1.He  ght flr  ntDOcument1.flr  nt()
End If
Cl  pbOard.SetData("Text",  lblInvO  ce.Text)
End Sub

flr  vate  Sub  RegNOInvOCB_Select  OnChangeCOmm  tted(sender  As  Object,  e  As EventArgs)  Handles  RegNOInvOCB.Select  OnChangeCOmm  tted
ClearF  elds()
InvO  ceIDTB.Text  =  "hahahaha"

D  m  query1,  query2  As  Str  ng
D  m  RegNO1  As  Str  ng  =  RegNOInvOCB.SelectedText
D  m  custID1  As  Str  ng  =  RegNOInvOCB.SelectedValue.TOStr  ng MsgBOx(RegNO1  &  "  "  &  custID1)
'FOr  Name  and  flhOne
query1  =  "SELECT  Cu.CustName,  Cu.CustflhOne  FROM  Cust  Cu  WHERE  Cu.CustID  = "  &  RegNOInvOCB.SelectedValue.TOStr  ng
dTable  =  getDataTable(query1) CustNameInvOTB.Text  =  dTable(0)(0) CustflhOneInvOTB.Text  =  dTable(0)(1) dTable.Reset()

'FOr  Serv  ceID  and  Charge Try
query2  =  "SELECT  Serv  ceID,  Serv  ceCharge  FROM  Serv	WHERE  CarRegNO  = '"  &  RegNOInvOCB.SelectedText  &  "'  ORDER  BY  Serv  ceID  DESC"

dTable  =  getDataTable(query2) InvO  ceIDTB.Text  =  dTable(0)(0)
Serv  ceChargeInvOTB.Text  =  dTable(0)(1) dTable.Reset()
Catch  ex  As  System.NullReferenceExcept  On
MsgBOx("NO  Serv  ce  DOne  fOr  th  s  veh  cle",  0,  "INFO") End Try

End Sub
 



flr  vate  Sub  ClearF  elds() InvO  ceIDTB.Clear() CustNameInvOTB.Clear() CustflhOneInvOTB.Clear()
Serv  ceChargeInvOTB.Clear()

End Sub
flr  vate  Sub  lOadCB(ByRef  CB  As  COmbOBOx) cOn.Open()
D  m  adapter  As  New  SqlDataAdapter("SELECT  CarRegNO,  CustID  FROM  Car  ",
 
cOn)
 

D  m  table  As  New  DataTable() adapter.F  ll(table)
 
CB.DataSOurce  =  table CB.ValueMember  =  "CustID" CB.D  splayMember  =  "CarRegNO" cOn.ClOse()
End Sub
flubl  c  Funct  On  getDataTable(ByVal  SǪL  As  Str  ng)  As  DataTable cOn.Open()
D  m  cmd  As  New  SqlCOmmand(SǪL,  cOn) D  m  dt  As  New  DataTable
D  m  da  As  New  SqlDataAdapter(cmd) da.F  ll(dt)
cOn.ClOse() Return  dt
End  Funct  On End  Class
