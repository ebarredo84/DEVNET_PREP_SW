#------MODEL--------------------------
#import requests
#from enauto.enauto_rest_functions_ebo import *

#------USER INTERFACE (VIEW)----------
import tkinter as tk
from devnet_gui_functions_ebo import *

#------CONTROLLER--------------------
import json
import base64
from enauto.enauto_functions_interface_ebo import *

#-------------IOS NETCONF OPTIONS-----------
def IOSXE_NETCONF_GET_YANG_INTERFACES(ans1,text_box):
    #identifier=input("Por favor intresar un identifier")
    identifier=ASK_PARAMETER("Por favor introducir un modelo, por ejemplo ietf-interfaces")
    #identifier="ietf-interfaces"
    netconf_reply=GET_SCHEMA_IOS_NETCONF(ans1,identifier=identifier)
    #BORRO LO QUE ESTÁ EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto
#    text_box.config(state="disabled")               #solo lectura
    #IMPRIMO EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.insert(tk.END,netconf_reply['rpc-reply']['data']['#text']+"\n")
    text_box.config(state="disabled")               #solo lectura

    
def IOSXE_NETCONF_GET_INTERFACES(ans1,text_box):
    source="running"
    netconf_filter="""
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface></interface>
    </interfaces>
 </filter>"""
    netconf_reply=GET_IOS_NETCONF(ans1,source,netconf_filter)
    #BORRO LO QUE ESTÁ EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto
#    text_box.config(state="disabled")               #solo lectura
    #IMPRIMO EN EL TEXT BOX
    PRINT_RESPONSE(netconf_reply['rpc-reply']['data']['interfaces'],text_box)

def IOSXE_NETCONF_ADD_INTERFACES(ans1,text_box):
    target="running"
    if_type="ianaift:softwareLoopback"
    status="true"

    loopback_num=ASK_PARAMETER("Por favor introducir el número de loopback, por ejemplo 99")
    name="Loopback"+loopback_num

    ip_address=ASK_PARAMETER("Por favor introducir la IP, por ejemplo 192.168.10.2")
    mask=ASK_PARAMETER("Por favor introducir la máscara, por ejemplo 255.255.255.0")

    netconf_interface_template="""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
        	<name>{name}</name>
        	<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">{if_type}</type>
        	<enabled>{status}</enabled>
        	<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        		<address>
        			<ip>{ip_address}</ip>
        			<netmask>{mask}</netmask>
        		</address>
        	</ipv4>
        </interface>
    </interfaces>
</config>"""
    netconf_data = netconf_interface_template.format(
        name = name,
        if_type = if_type,
        status = status,
        ip_address = ip_address,
        mask = mask
    )
    netconf_reply=EDIT_IOS_NETCONF(ans1,target,netconf_data)

    #BORRO Y ESCRIBO RESPUESTA EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto

    PRINT_RESPONSE(netconf_reply,text_box)

def IOSXE_NETCONF_MERGE_DESCRIPTION(ans1,text_box):
    target="running"
    if_type="ianaift:softwareLoopback"

    loopback_num=ASK_PARAMETER("Por favor introducir el número de loopback, por ejemplo 99")
    name="Loopback"+loopback_num
    desc=ASK_PARAMETER("Por favor introducir la descripción, por ejemplo Testin NETCONF EBO")

    netconf_interface_template="""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="merge">
        	<name>{name}</name>
        	<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">{if_type}</type>
        	<description>{desc}</description>
        </interface>
    </interfaces>
</config>"""
    netconf_data = netconf_interface_template.format(
        name = name,
        if_type=if_type,
        desc=desc
    )
    netconf_reply=EDIT_IOS_NETCONF(ans1,target,netconf_data)

    #BORRO Y ESCRIBO RESPUESTA EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto

    PRINT_RESPONSE(netconf_reply,text_box)

def IOSXE_NETCONF_EDIT_INTERFACES(ans1,text_box):
    target="running"
    if_type="ianaift:softwareLoopback"

    loopback_num=ASK_PARAMETER("Por favor introducir el número de loopback, por ejemplo 99")
    name="Loopback"+loopback_num
    desc=ASK_PARAMETER("Por favor introducir la descripción, por ejemplo Testin NETCONF EBO (change IP ADDRESS)")
    ip_address=ASK_PARAMETER("Por favor introducir la IP, por ejemplo 192.168.10.99")
    mask=ASK_PARAMETER("Por favor introducir la máscara, por ejemplo 255.255.255.128")

    netconf_interface_template="""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="replace">
        	<name>{name}</name>
        	<type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">{if_type}</type>
        	<description>{desc}</description>
        	<ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        		<address>
        			<ip>{ip_address}</ip>
                    <netmask>{mask}</netmask>
        		</address>
        	</ipv4>
        </interface>
    </interfaces>
</config>"""
    netconf_data = netconf_interface_template.format(
        name = name,
        if_type=if_type,
        desc=desc,
        ip_address = ip_address,
        mask = mask
    )
    netconf_reply=EDIT_IOS_NETCONF(ans1,target,netconf_data)

    #BORRO Y ESCRIBO RESPUESTA EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto

    PRINT_RESPONSE(netconf_reply,text_box)

def IOSXE_NETCONF_DEL_INTERFACES(ans1,text_box):
    target="running"

    loopback_num=ASK_PARAMETER("Por favor introducir el número de loopback, por ejemplo 99")
    name="Loopback"+loopback_num

    netconf_interface_template = """
 <config>
     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
         <interface operation="delete">
             <name>{name}</name>
         </interface>
     </interfaces>
 </config>"""        
    netconf_data = netconf_interface_template.format(
        name = name)
    netconf_reply=EDIT_IOS_NETCONF(ans1,target,netconf_data)

    #BORRO Y ESCRIBO RESPUESTA EN EL TEXT BOX
    text_box.config(state="normal")                 #habilito la escritura
    text_box.delete("1.0", tk.END)                  #para borrar el texto

    PRINT_RESPONSE(netconf_reply,text_box)

#-------------IOS RESTCONF OPTIONS-----------
def IOSXE_RESTCONF_GET_HEADERS(ans1,text_box):
    headers=SANDBOX_AUTHENTICATION(ans1,text_box)
    return headers

def IOSXE_RESTCONF_GET_YANG_INTERFACES(ans1,headers,text_box):
    services="netconf-state/capabilities"
    response=GET_FUNCTION_EBO(ans1,services,headers,text_box)
    PRINT_RESPONSE_JSON(response,text_box)

def IOSXE_RESTCONF_GET_INTERFACES(ans1,headers,text_box):
    services="ietf-interfaces:interfaces"
    response=GET_FUNCTION_EBO(ans1,services,headers,text_box)
    PRINT_RESPONSE_JSON(response,text_box)

def IOSXE_RESTCONF_ADD_INTERFACES(ans1,headers,text_box):
    loopback_num=ASK_PARAMETER("Por favor introducir el número de loopback, por ejemplo 99")
    name="Loopback"+loopback_num
    ip_address=ASK_PARAMETER("Por favor introducir la IP, por ejemplo 192.168.10.2")
    mask=ASK_PARAMETER("Por favor introducir la máscara, por ejemplo 255.255.255.0")

    services="ietf-interfaces:interfaces"

    data = {
        "ietf-interfaces:interface": {
            "name": name,
            "type": "iana-if-type:softwareLoopback",
            "enabled": "true",
            "ietf-ip:ipv4": {
                "address": [
                    {
                    "ip": ip_address,
                    "netmask": mask
                    }
                ]
            },
            "ietf-ip:ipv6": {
            }
        }
    }
    response=POST_FUNCTION_EBO(ans1,services,headers,text_box,json.dumps(data))

    PRINT_STATUS_CODE(response,text_box)

def IOSXE_RESTCONF_MERGE_DESCRIPTION(ans1,headers,text_box):
    loopback_num=ASK_PARAMETER("Por favor introducir el número de loopback, por ejemplo 99")
    name="Loopback"+loopback_num
    desc=ASK_PARAMETER("Por favor introducir la descripción, por ejemplo Testin NETCONF EBO")

    services="ietf-interfaces:interfaces/interface="+name

    data = {
        "ietf-interfaces:interface": {
            "name": name,
            "description": desc,
            "type": "iana-if-type:softwareLoopback",
            "enabled": "true",
        }
    }
    response=PATCH_FUNCTION_EBO(ans1,services,headers,text_box,json.dumps(data))

    PRINT_STATUS_CODE(response,text_box)

def IOSXE_RESTCONF_EDIT_INTERFACES(ans1,headers,text_box):
    loopback_num=ASK_PARAMETER("Por favor introducir el número de loopback, por ejemplo 99")
    name="Loopback"+loopback_num
    desc=ASK_PARAMETER("Por favor introducir la descripción, por ejemplo Testin NETCONF EBO (change IP ADDRESS)")
    ip_address=ASK_PARAMETER("Por favor introducir la IP, por ejemplo 192.168.10.99")
    mask=ASK_PARAMETER("Por favor introducir la máscara, por ejemplo 255.255.255.128")

    services="ietf-interfaces:interfaces/interface="+name

    data = {
        "ietf-interfaces:interface": {
            "name": name,
            "description": desc,
            "type": "iana-if-type:softwareLoopback",
            "enabled": "true",
            "ietf-ip:ipv4": {
                "address": [
                    {
                    "ip": ip_address,
                    "netmask": mask
                    }
                ]
            },
            "ietf-ip:ipv6": {
            }
        }
    }
    response=PUT_FUNCTION_EBO(ans1,services,headers,text_box,json.dumps(data))

    PRINT_STATUS_CODE(response,text_box)

def IOSXE_RESTCONF_DEL_INTERFACES(ans1,headers,text_box):
    loopback_num=ASK_PARAMETER("Por favor introducir el número de loopback, por ejemplo 99")
    name="Loopback"+loopback_num

    services="ietf-interfaces:interfaces/interface="+name

    response=DELETE_FUNCTION_EBO(ans1,services,headers,text_box)
    
    PRINT_STATUS_CODE(response,text_box)