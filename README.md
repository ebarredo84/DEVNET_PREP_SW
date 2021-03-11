# DEVNET_PREP_SW
I created this software in order to prepare myself for DEVNET CERTIFICATIONS. Right now it only works for ENAUTO 300-435 but the idea is to write the code for the others DEVNET CERTIFICATION EXAMS also.

This DEVNET PREPARATION SOFTWARE starts by running devnet_prep_sw_ebo.py file. It should open a window which ask for which exam do you wish to practice. For now, its only available ENAUTO 300-435 (option 1):
1) ENAUTO 300-435
2) SPAUTO 300-535
3) DCAUTO 300-635
4) SAUTO  300-735
5) CLAUTO 300-835
You should write "1" and press "Select" button. The others options is not available yet.

Then it should open a new window with 4 options:
1) IOS XE
2) DNA CENTER
3) SD WAN
4) MERAKI

All of them ask for which SANBOX do you want to interact with: 
1) IOS XE
  1) SANDBOX IOS XE 1    (host="ios-xe-mgmt.cisco.com")
2) DNA CENTER
  1) SANDBOX DNAC2     (https://sandboxdnac2.cisco.com)   "USER ESTE MEJOR"
  2) SANDBOX DNAC      (https://sandboxdnac.cisco.com)    "ESTÁ MIGRANDO AL 2"
3) SD WAN
  1) SANDBOX SDWAN1    (https://sandbox-sdwan-1.cisco.com:443/)   "USAR ESTE"
  2) SANDBOX SDWAN     (https://sandboxsdwan.cisco.com:8443/)     "ESTE TIENE PROBLEMAS DE AUTHENTICACIÓN"
4) MERAKI
  1) SANDBOX MERAKI1    (https://api.meraki.com/api/v1/)
  2) SANDBOX MERAKI     (https://api.meraki.com/api/v0/) ***
 
Please select always the first one. The second one its not really working or has some problems. I leave it this way in order to easily implement a second SANDBOX (RESERVED for example) o an equipment at your own if you have one.

Each option has more menus and requests to practice. These 4 options interact directly with CISCO SANDBOXES ALWAYS ON which means that the sofware is loaded with the credentials of these 4 SANDBOXES 
1) IOS XE (ios-xe-mgmt.cisco.com)
2) DNA CENTER (https://sandboxdnac2.cisco.com/dna/intent/api/)
3) SD WAN (https://sandbox-sdwan-1.cisco.com:443/)
4) MERAKI (https://api.meraki.com/api/v1/)

I implemented this sofware with a MCV (model-controller view) pattern. I separeted the software in the following way:

view:
enauto/enauto_gui_dnac_menus_ebo: has only DNA MENUS
enauto/enauto_gui_iosxe_menus_ebo: has only IOS XE MENUS
enauto/enauto_gui_meraki_menus_ebo: has only MERAKI MENUS
enauto/enauto_gui_sdwan_menus_ebo: has only SDWAN MENUS
enauto/enauto_gui_class_ebo: has the window and the methods which interact with the menus and requests (controller part).
devnet_gui_functions_ebo: has a secundary window that is used to ask for parameters and also has PRINTS functions that are used to display the requests.

controller:
enauto/enauto_functions_dnac_ebo: has all the request for dna center
enauto/enauto_functions_iosxe_ebo: has all the request for IOS XE
enauto/enauto_functions_meraki_ebo: has all the request for meraki
enauto/enauto_functions_sdwan_ebo: has all the request for SDWAN
enauto/enauto_functions_interface_ebo: has the "interface" between controller and model part. All the credentials are here.

model:
devnet_model_functions_ebo: has ncclient and requests python functions that are used for all the software.

I made it this way in order to be easy to add a new function for each sandbox. For example, if you want to add the option to create a vlan in IOS XE you have to:
1) add that option in IOS XE MENU (in enauto/enauto_gui_iosxe_menus_ebo)
2) add that option in the method to call the function (in enauto/enauto_gui_class_ebo)
3) create the function to add the vlan (in enauto/enauto_functions_iosxe_ebo).

The sofware has a lot of requests (you can see how much in the enauto_gui_xyz_menus_ebo) but you can call all of them with almost the same logic. I will explain for two of themm.

For example, the steps to ask and print all the interfaces of the CSR1000V using NETCONT are:
1) run devnet_prep_sw_ebo.py
2) write 1 and press "select". It should open a new window.
3) write 1 and press "select" to show IOS XE MENU
4) write 1 and press "select" to show IOS XE MENU for the SANDOX ALWAYS ON
5) write 1 and press "select" to show NETCONF MENU
6) write 3 and press "select" to ask for interfaces (GET INTERFACE LIST).
You should wait for a moment and then the request will be shown in the text box of the GUI.

Another example, the steps to ask and print all the interfaces of the CSR1000V using RESTCONF (instead of NETCONF) are:
1) run devnet_prep_sw_ebo.py
2) write 1 and press "select". It should open a new window.
3) write 1 and press "select" to show IOS XE MENU
4) write 1 and press "select" to show IOS XE MENU for the SANDOX ALWAYS ON
5) write 2 and press "select" to show RESTCONF MENU
6) write 1 and press "select" to create the HEADER. This is needed in order to request the GET for interfaces.
7) press "back" option.
8) write 3 and press "select" to ask for interfaces (GET INTERFACE LIST).
You should wait for a moment and then the request will be shown in the text box of the GUI.

Regards,
