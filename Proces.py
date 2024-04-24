import time
import pyautogui
from time import sleep
import pyperclip
import pendulum
from storagefunctions import (pressingKey,selectToEnd,formatDate)

def Proces_Cancel (cheklist):
    crm_guardada_OTH = crm_asig_OTH = BOTON_ACCEPTAR = Estado_OTH = crm_assign_user = crm_edit_tarea = crm_assign_user = crm_save_OTH = None 
    intentos = crmAttempts = 0
    # Maximize CRM OTH window 
    pyautogui.getWindowsWithTitle("Tarea hija")[0].maximize()
    print("CRM OTH Edit view Window was maximized!")
    sleep(1)                  
    # Validate edit_incident view is visible and on focus  edita la tarea          
    while crm_edit_tarea is None:
        crm_edit_tarea = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/edit_tarea.png', grayscale = True,confidence=0.9)   
    print("Vista de Detalles is present!")    
    print("CRM OTH Edit tarea button is present!")
    crm_edit_tarea_x,crm_edit_tarea_y = pyautogui.center(crm_edit_tarea)
    pyautogui.click(crm_edit_tarea_x, crm_edit_tarea_y)    
    
    # Validate assign user pop up is visible and on focus
    # crm_assign_user = None  # reset variable   
    crmAttempts = 0
    while crm_assign_user is None and crmAttempts < 5:
        crm_assign_user = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/asignar_ot_usuario_OTH.png', grayscale = True,confidence=0.9)   
        sleep(0.5)
        print("buscando ventana de asignación de usuario")
        crmAttempts +=1      

    if crm_assign_user is not None:
        print("CRM OTH Confirm Assign Pop Up is present!")
        sleep(1)
        pressingKey('n') # No re asignar usuario al momento de editar las OTPs 
        sleep(1)
    
    #/////////////////////////////////// TRASLADO DE COMENTARIOS /////////////////////////////////////
    sleep(1)    
    if cheklist is not None:
        pressingKey('tab')
        sleep(1)
        pyperclip.copy(cheklist)
        pyautogui.hotkey('ctrl','v')    
        sleep(1)
        pyautogui.doubleClick(262,229)
        sleep(0.5)
        pyautogui.write('0') 
        pressingKey('enter')
        sleep(0.5)

        while crm_save_OTH is None:
            crm_save_OTH = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/guardar_tarea_button.png', grayscale = True,confidence=0.9)   
        print("CRM OTH Save Incident button is present!")
        crm_save_OTH_x,crm_save_OTH_y = pyautogui.center(crm_save_OTH)
        pyautogui.click(crm_save_OTH_x, crm_save_OTH_y)   
        sleep(1)

        while BOTON_ACCEPTAR is None:
            BOTON_ACCEPTAR = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/BOTON_ACCEPTA.png', grayscale = True,confidence=0.9)   
            if BOTON_ACCEPTAR is not None:
                print("Mensaje de cambio presente!")
                BOTON_ACCEPTAR_x,BOTON_ACCEPTAR_y = pyautogui.center(BOTON_ACCEPTAR)
                pyautogui.moveTo(BOTON_ACCEPTAR_x, BOTON_ACCEPTAR_y) 
                pyautogui.click(BOTON_ACCEPTAR_x, BOTON_ACCEPTAR_y)   
                sleep(1)
                while crm_save_OTH is None:
                    crm_save_OTH = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/guardar_tarea_button.png', grayscale = True,confidence=0.9)   
                print("CRM OTH Save Incident button is present!")
                crm_save_OTH_x,crm_save_OTH_y = pyautogui.center(crm_save_OTH)
                pyautogui.click(crm_save_OTH_x, crm_save_OTH_y)
                sleep(1)
                break
            if intentos == 10:
                print('La prioridad es la msima')
                sleep(0.5)
                break
            intentos += 1
            print('numero de intento que vamos:', intentos)
        while crm_asig_OTH is None:
            crm_asig_OTH = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/asignar_ot_usuario_OTH.png', grayscale = True,confidence=0.9)   
        print("No asignado OTH")
        pressingKey('enter') 
        sleep(1)

        while crm_guardada_OTH is None:
            crm_guardada_OTH = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/OTH_guardado_exitosamente.png', grayscale = True,confidence=0.9)   
        print("Guardado exitoso")
        pressingKey('enter') 
        sleep(1)
    else:
        pass
    #/////////////////////////////////// Cambi de estado a cancelado ///////////////////////////////
    while Estado_OTH is None:
        Estado_OTH = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/ESTADOOTH.png', grayscale = True,confidence=0.9)   
    print("Vista de Detalles is present!")    
    print("CRM OTH Edit tarea button is present!")
    Estado_OTH_x,Estado_OTH_y = pyautogui.center(Estado_OTH)
    pyautogui.click(Estado_OTH_x,Estado_OTH_y)  
    posicion_actual = pyautogui.position()
    print("Posición actual del cursor:", posicion_actual)
    # Mover el cursor 127 píxeles a la derecha desde su posición actual
    pyautogui.moveRel(127, 0, duration=0.5)
    # Imprimir la nueva posición del cursor
    nueva_posicion = pyautogui.position()
    print("Nueva posición del cursor:", nueva_posicion)
    pyautogui.click(nueva_posicion)
    sleep(1)
    pyautogui.click(nueva_posicion)
    sleep(0.5)
    pyautogui.write('CANCELADA')
    pressingKey('enter')
    pressingKey('tab')
    pressingKey('down')
    pressingKey('enter')
    pressingKey('tab')
    pyautogui.write('0')
    pressingKey('enter')
    sleep(0.5)
    #/////////////////////////////////// GUARDADO COMENTARIOS /////////////////////////////////////    
    while crm_save_OTH is None:
        crm_save_OTH = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/guardar_tarea_button.png', grayscale = True,confidence=0.9)   
    print("CRM OTH Save Incident button is present!")
    crm_save_OTH_x,crm_save_OTH_y = pyautogui.center(crm_save_OTH)
    pyautogui.click(crm_save_OTH_x, crm_save_OTH_y)   

    while crm_asig_OTH is None:
        crm_asig_OTH = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/asignar_ot_usuario_OTH.png', grayscale = True,confidence=0.9)   
    print("No asignado OTH")
    pressingKey('enter') 
    sleep(1)

    while crm_guardada_OTH is None:
        crm_guardada_OTH = pyautogui.locateOnScreen('C:/ProsesoOTHCancel/assets/OTH_guardado_exitosamente.png', grayscale = True,confidence=0.9)   
    print("Guardado exitoso")
    pressingKey('enter') 
    sleep(1)

    # Cierre ventana OTH
    pyautogui.getWindowsWithTitle("Tarea hija")[0].close()        
    sleep(1)
    # Validate if changes must be saved or not and Close the OT Details View On Edition mode  
    # Close Edit Incident View 
    pyautogui.getWindowsWithTitle("Ordenes de Trabajo v8")[0].close()        
    sleep(1)