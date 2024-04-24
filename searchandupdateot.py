import time
import pyautogui
from time import sleep
import pyperclip
import pendulum
from storagefunctions import (pressingKey,make_window_visible)
from Proces import (Proces_Cancel)

def searchOTHControl(incidentId, cheklist):
    
    crm_dashboard = KICKOFF_NOVEDADES = OTH_Planear_Cliente = crm_warning_message = crm_ot_blocked_message = mod_consulta_popup = None 
    crmAttempts = 0  

    make_window_visible('Sistema Avanzado')
    #/////////////////////////////////// CRM DASHBOARD ///////////////////////////////////////////    

    while crm_dashboard is None:
        crm_dashboard = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/crm_dashboard.png', grayscale = True,confidence=0.85)
        sleep(0.5)
        if crmAttempts == 5:
            pyautogui.getWindowsWithTitle("Sistema Avanzado de Administración de Clientes [Versión 4.2.2.3]")[0].minimize()
            pyautogui.getWindowsWithTitle("Sistema Avanzado de Administración de Clientes [Versión 4.2.2.3]")[0].maximize()
            print("Estoy dentro de los 5 intentos para ver el Dashboard del CRM")
            crmAttempts = 0
        crmAttempts = crmAttempts + 1
                
    print("CRM Dashboard GUI is present!")   
    pyautogui.click(pyautogui.center(crm_dashboard))    
    
    sleep(0.5)
    pressingKey('f2')
    while mod_consulta_popup is None:        
        mod_consulta_popup = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/mod_consulta_popup.png', grayscale = True,confidence=0.85)            
        pressingKey('f2')
    print("mod_consulta_popup field is present and detected on GUI screen!")
    sleep(0.5)
    pyautogui.write(incidentId)
    sleep(0.5)
    pressingKey('enter')
    pressingKey('enter')
    
    #/////////////////////////////////// FASE DE INGRESO ///////////////////////////////////////////
    
    while crm_ot_blocked_message is None and crm_warning_message is None and crmAttempts < 10:
        crm_warning_message = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/mensaje_advertencia.png', grayscale = True,confidence=0.9)   
        crm_ot_blocked_message = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/crm_ot_blocked_message.png', grayscale = True,confidence=0.9)   
        sleep(0.5)
        if crmAttempts == 8:
            print("Estoy dentro de los 8 intentos de medio seg para esperar algun pop up de OT bloqueada inesperado en el CRM")                        
        crmAttempts += 1
        print(crmAttempts)            

    # Close Edit Incident View 
    pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].maximize()      
    sleep(1.5)
    
    #//////////////////////////////////// INGRESE A LA OTH //////////////////////////////////
    time.sleep(1)
    pyautogui.doubleClick(1218,469) 
    crmAttempts = 0
    time.sleep(0.5)
    pyautogui.doubleClick(681,519)
    pyautogui.moveTo(1218,469)
    time.sleep(1)
    while OTH_Planear_Cliente is None or KICKOFF_NOVEDADES is None:
        print("buscando OTH_Control_Cambio in screen")
        OTH_Planear_Cliente = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/OTHPLANEARCLIENTE.png', grayscale = True,confidence=0.95)
        KICKOFF_NOVEDADES = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/KICKOFF_NOVEDADES.png', grayscale = True,confidence=0.95)
        if OTH_Planear_Cliente is not None :
            print("OTH_Control_Cambio is present!")
            pyautogui.moveTo(pyautogui.center(OTH_Planear_Cliente))
            sleep(0.5)            
            pyautogui.doubleClick()
            sleep(1)
            Proces_Cancel(cheklist)
            sleep(1)
            return 0
        if  KICKOFF_NOVEDADES is not None:
            print("OTH_Control_Cambio is present!")
            pyautogui.moveTo(pyautogui.center(KICKOFF_NOVEDADES))
            sleep(0.5)            
            pyautogui.doubleClick()
            sleep(1)
            Proces_Cancel(cheklist)
            sleep(1)
            return 0
        else:
            print("OTH_Control_Cambio no present!")
            # Close Edit Incident View 
            pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].close()        
            sleep(1)
            return 7
        