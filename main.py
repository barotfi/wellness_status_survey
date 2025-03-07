import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from functions import *
from titles import *
from PIL import Image
from streamlit.components.v1 import html
import datetime
import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, Date, MetaData
import sqlitecloud



options = [
    ["Kiváló", "Jó", "Elfogadható", "Rossz"],
    ["Naponta", "Hetente néhány alkalommal", "Ritkán"],
    ["Kiváló", "Jó", "Közepes", "Rossz"]
]
c=st.container(height=40, border=False)
img = Image.open("Leadwell_logo_blue.png")

st.markdown(
    """
    <style>
    .centered {
        display: flex;
        justify-content: left;
        align-items: left;
    }
    </style>
    """, unsafe_allow_html=True
)

# Center the image on the page
st.markdown("<div class='centered'>", unsafe_allow_html=True)
c.image(img, width=100)  # Adjust the width as needed
st.markdown("</div>", unsafe_allow_html=True)


if 'ended' not in st.session_state:
    # Initialize step and points in session state if 'step' not in st.session_state:

    sessionstateinit('step')


    #Step1
    sessionstateinit('egeszseg_valasz')
    sessionstateinit('szuletesi_datum')
    sessionstateinit('neme')
    sessionstateinit('testsuly')
    sessionstateinit('testsuly_keteve')
    sessionstateinit('testmagassag')

    #Step2
    sessionstateinit('magasvernyomas')
    sessionstateinit('koleszterin')
    sessionstateinit('vercukor')
    sessionstateinit('kronikusbetegseg')
    sessionstateinit('szures')

    #Step3

    sessionstateinit('taplalkozas_zoldseg')
    sessionstateinit('taplalkozas_gyumolcs')
    sessionstateinit('taplalkozas_hal')
    sessionstateinit('taplalkozas_edesseg')
    sessionstateinit('taplalkozas_udito')
    sessionstateinit('taplalkozas_teljeskiorles')

    #Step4

    sessionstateinit('taplalkozas_husfele')
    sessionstateinit('taplalkozas_nassolas')
    sessionstateinit('taplalkozas_foetkezes')
    sessionstateinit('taplalkozas_folyadek')
    sessionstateinit('taplalkozas_rendszeres')

    #Step5
    sessionstateinit('testmozgas_alkalom')
    sessionstateinit('testmozgas_osszesen')
    sessionstateinit('testmozgas_nyujtas')
    sessionstateinit('testmozgas_kardio')
    sessionstateinit('testmozgas_erosites')

    #Step6
    sessionstateinit('alvas_ido')
    sessionstateinit('alvas_felebredes')
    sessionstateinit('alvas_kipihent')
    sessionstateinit('alvas_altato')

    #Step7
    sessionstateinit('dohanyzas')
    sessionstateinit('alkohol')
    sessionstateinit('karos_szenvedely')

    sessionstateinit("egeszseg_finalscor")
    sessionstateinit("taplalkozas_finalscore")
    sessionstateinit("testmozgas_finalscore")
    sessionstateinit("alvas_finalscore")
    sessionstateinit("karosszenvedely_finalscore")
    sessionstateinit("erzelmi_egeszseg_finalscore")
    sessionstateinit("szellemi_egeszseg_finalscore")
    sessionstateinit("tarsasagi_kapcsolatok_finalscore")

    sessionstateinit("stressz")
    sessionstateinit("jovokep")
    sessionstateinit("stressz_technika")
    sessionstateinit("mentalis_egeszseg")
    sessionstateinit("tanulas")
    sessionstateinit("tarsasagi")
    sessionstateinit("kapcsolat_minoseg")
    sessionstateinit("munkakor")
    sessionstateinit("kitoltes_ideje")
    sessionstateinit("felhasznalonev")

     
    if st.session_state['step'] == 1:

        st.session_state['felhasznalonev'] = st.text_input("Kérem, adjon meg egy felhasználónevet!", value=None)
                      
        st.session_state['szuletesi_datum'] = st.date_input("Kérem, adja meg a születési dátumát!", min_value="1900-01-01", value=None)
        
        st.session_state['neme'] = st.selectbox("Kérem, adja meg a nemét!", ['Nő', 'Férfi'],index= None,placeholder="Válasszon a lehetőségek közül!")

        st.session_state['munkakor'] = st.selectbox("Milyen jellegű munkát végez?",['Felsővezető', 'Középvezető', 'Beosztott', 'Egyéni vállalkozó', 'Egyéb'], index= None,placeholder="Válasszon a lehetőségek közül!")

        if (st.session_state['munkakor'] != None and
            st.session_state['felhasznalonev'] != None and
            st.session_state['szuletesi_datum'] != None and
            st.session_state['neme'] != None):
            
            
            st.button("Tovább", on_click=next_step)
        
        st.progress(7,'7%')
        

    elif st.session_state['step'] == 2:

        st.session_state['egeszseg_valasz'] = st.selectbox("Milyennek értékeli összeségében az egészségi állapotát?", options[0],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['testsuly'] = st.number_input("Mennyi a testsúlya (kg)?", value=None, step=1,placeholder="Írjon be egy számot, majd nyomjon ENTERT")
        
        st.session_state['testsuly_keteve'] = st.number_input("Mennyi volt a testsúlya két évvel ezelőtt (kg)?", value=None, step=1,placeholder="Írjon be egy számot, majd nyomjon ENTERT")

        st.session_state['testmagassag'] = st.number_input("Milyen magas (cm)?", value=None,placeholder="Írjon be egy számot, majd nyomjon ENTERT" ,step=1)

        if (st.session_state['testsuly'] != None and
            st.session_state['testsuly_keteve'] != None and
            st.session_state['egeszseg_valasz'] != None and
            st.session_state['testmagassag'] != None):
            
            st.button("Tovább", on_click=next_step)
        
        st.progress(14, text="14%")

    elif st.session_state['step'] == 3:
          
        st.session_state['magasvernyomas'] = st.selectbox("Van magasvérnyomás betegsége?", ["Van", "Nincs"], index = None, placeholder = "Válasszon a lehetőségek közül!")
        
        st.session_state['koleszterin'] = st.selectbox("Magas a koleszterinszintje?", ["Igen", "Nem"], index = None, placeholder = "Válasszon a lehetőségek közül!")
        
        st.session_state['vercukor'] = st.selectbox("Cukorbeteg?", ["Igen", "Nem"], index = None, placeholder = "Válasszon a lehetőségek közül!")
        
        if (st.session_state['magasvernyomas'] != None and
            st.session_state['koleszterin'] != None and
            st.session_state['vercukor'] != None):
            
            st.button("Tovább", on_click=next_step)     
        
        st.progress(21, text="21%")

    elif st.session_state['step'] == 4:   
        
        st.session_state['kronikusbetegseg'] = st.selectbox("A fentieken kívül hány krónikus (rendszeres gyógyszerszedést igénylő) betegsége van még?", ["Nincs több", "Egy", "Kettő", "Kettőnél több"], index = None, placeholder = "Válasszon a lehetőségek közül!")
        
        st.session_state['szures'] = st.selectbox("Milyen gyakran jár egészségügyi szűrővizsgálatokra?", ["Nem járok", "Ritkábban, mint évente", "Évente, vagy gyakrabban"], index = None, placeholder = "Válasszon a lehetőségek közül!")

        if (st.session_state['kronikusbetegseg'] != None and
            st.session_state['szures'] != None):
            
            st.button("Tovább", on_click=next_step)

        st.progress(27, text="27%")  
            
    elif st.session_state['step'] == 5:

        st.session_state['taplalkozas_zoldseg'] = st.selectbox("Milyen gyakran fogyaszt zöldséget?", options=["Naponta", "Hetente néhány alkalommal", "Ritkán"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['taplalkozas_gyumolcs'] = st.selectbox("Milyen gyakran fogyaszt gyümölcsöt?", options[1],index= None,placeholder="Válasszon a lehetőségek közül!")

        st.session_state['taplalkozas_hal'] = st.selectbox("Milyen gyakran fogyaszt halfélét?", options[1],index= None,placeholder="Válasszon a lehetőségek közül!")

        if (st.session_state['taplalkozas_zoldseg'] != None and
            st.session_state['taplalkozas_gyumolcs'] != None and
            st.session_state['taplalkozas_hal'] != None):
            
            st.button("Tovább", on_click=next_step)
        
        st.progress(34, text="34%")

    elif st.session_state['step'] == 6:  
        
        st.session_state['taplalkozas_edesseg'] = st.selectbox("Milyen gyakran fogyaszt édességet?", options[1],index= None,placeholder="Válasszon a lehetőségek közül!")

        st.session_state['taplalkozas_udito'] = st.selectbox("Milyen gyakran fogyaszt cukros üdítőitalt?", options[1],index= None,placeholder="Válasszon a lehetőségek közül!")

        st.session_state['taplalkozas_teljeskiorles'] = st.selectbox("Milyen gyakran fogyaszt  teljes kiőrlésű gabonából készült ételt?", options[1],index= None,placeholder="Válasszon a lehetőségek közül!")

        if (st.session_state['taplalkozas_edesseg'] != None and
            st.session_state['taplalkozas_udito'] != None and
            st.session_state['taplalkozas_teljeskiorles'] != None):
            
            st.button("Tovább", on_click=next_step)
            
        st.progress(41, text="41%")
            
    elif st.session_state['step'] == 7:

        st.session_state['taplalkozas_husfele'] = st.selectbox("Milyen húsfélét fogyaszt leggyakrabban?", ["szárnyas", "sertés", "marha", "egyéb húsfajta", "nem fogyasztok húst"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['taplalkozas_nassolas'] = st.selectbox("Szokott étkezések között nassolni?", ["előfordul", "rendszeresen","elvétve/soha"],index= None,placeholder="Válasszon a lehetőségek közül!")       
        
        st.session_state['taplalkozas_foetkezes'] = st.selectbox("Általában milyen ételt eszik főétkezésekre?", ["saját magam főzök", "étteremben eszem", "gyorsétteremben eszem", "félkész ételt készítem el"],index= None,placeholder="Válasszon a lehetőségek közül!")
    
        if (st.session_state['taplalkozas_husfele'] != None and
            st.session_state['taplalkozas_nassolas'] != None and
            st.session_state['taplalkozas_foetkezes'] != None):
            
            st.button("Tovább", on_click=next_step)

        st.progress(48, text="48%")

    elif st.session_state['step'] == 8:    
        
        st.session_state['taplalkozas_folyadek'] = st.selectbox("Mennyi folyadékot fogyaszt naponta?", ["1 liternél kevesebbet", "1-2 litert","2 liternél többet"],index= None,placeholder="Válasszon a lehetőségek közül!")       

        st.session_state['taplalkozas_rendszeres'] = st.selectbox("Mennyire étkezik rendszeresen a nap során?", ["rendszeresen", "többnyire rendszeresen","többnyire rendszertelenül"],index= None,placeholder="Válasszon a lehetőségek közül!")       

        if (st.session_state['taplalkozas_folyadek'] != None and
            st.session_state['taplalkozas_rendszeres'] != None):
            
            st.button("Tovább", on_click=next_step)

        st.progress(54, text="54%")

    elif st.session_state['step'] == 9:

        st.session_state['testmozgas_alkalom'] = st.selectbox("Átlagosan heti hány alkalommal végez testmozgást? ?", ["Nem nagyon végzek testmozgást", "Heti 1-2 alkalommal", "Heti 3-4 alkalommal", "Heti 4 alkalomnál többször"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['testmozgas_osszesen'] = st.selectbox("Átlagosan egy héten összesen hány percet tölt aktív testmozgással? ", ["Kevesebb mint 30 percet", "30-60 percet","60-120 percet", "120-180 percet", "180 percnél többet"],index= None,placeholder="Válasszon a lehetőségek közül!")       

        st.session_state['testmozgas_nyujtas'] = st.selectbox("Szokott rendszeresen nyújtani/mobilizáló gyakorlatokat végezni?", ["előfordul", "rendszeresen","elvétve/soha"],index= None,placeholder="Válasszon a lehetőségek közül!")       
        
        if (st.session_state['testmozgas_alkalom'] != None and
            st.session_state['testmozgas_osszesen'] != None and
            st.session_state['testmozgas_nyujtas'] != None):
            
            st.button("Tovább", on_click=next_step)

        st.progress(61, text="61%")

    elif st.session_state['step'] == 10:   
        
        st.session_state['testmozgas_kardio'] = st.selectbox("Szokott rendszeresen kardió (magas pulzuszámmal járó) gyakorlatokat végezni?", ["előfordul", "rendszeresen","elvétve/soha"],index= None,placeholder="Válasszon a lehetőségek közül!")       
        
        st.session_state['testmozgas_erosites'] = st.selectbox("Szokott rendszeresen erősítő gyakorlatokat végezni?", ["előfordul", "rendszeresen","elvétve/soha"],index= None,placeholder="Válasszon a lehetőségek közül!")       
        
        if (st.session_state['testmozgas_kardio'] != None and
            st.session_state['testmozgas_erosites'] != None):
            
            st.button("Tovább", on_click=next_step)

        st.progress(66, text="66%")
        
    elif st.session_state['step'] == 11:
                   
        st.session_state['alvas_ido'] = st.selectbox("Általában hány órát alszik éjjelente?", ["Kevesebb mint 5 órát", "5-6 órát", "7 órát vagy többet"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['alvas_felebredes'] = st.selectbox("Gyakran előfordul, hogy nehezen alszik el vagy éjjel felébred és nem tud visszaaludni? ", ["Igen", "Nem"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['alvas_kipihent'] = st.selectbox("Ébredéskor általában kipihentnek és frissnek érzi magát?", ["Igen", "Nem"],index= None,placeholder="Válasszon a lehetőségek közül!")

        st.session_state['alvas_altato'] = st.selectbox("Szed rendszeresen altatót?", ["Igen", "Nem"],index= None,placeholder="Válasszon a lehetőségek közül!")

        if (st.session_state['alvas_ido'] != None and
            st.session_state['alvas_felebredes'] != None and
            st.session_state['alvas_kipihent'] != None and
            st.session_state['alvas_altato'] != None):
            
            st.button("Tovább", on_click=next_step)

        st.progress(77, text="77%")
    
    elif st.session_state['step'] == 12:
  
        st.session_state['dohanyzas'] = st.selectbox("Dohányzik?", ["Nem dohányzom", "Alkalmanként", "Napi 1 dobozt vagy annál kevesebbet", "Napi 1 doboznál többet"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['alkohol'] = st.selectbox("Milyen gyakorisággal fogyaszt alkoholt? ", ["Soha", "Alkalmanként", "Havonta 1-2 alkalommal", "Hetente 1-2 alkalommal", "Naponta"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['karos_szenvedely'] = st.selectbox("Van egyéb (szerencsejáték, kábítószer, stb) káros szenvedélye?", ["Van", "Nincs"],index= None,placeholder="Válasszon a lehetőségek közül!")

        if (st.session_state['dohanyzas'] != None and
            st.session_state['alkohol'] != None and
            st.session_state['karos_szenvedely'] != None):
            
            st.button("Tovább", on_click=next_step)

        st.progress(84, text="84%")
       
    
    elif st.session_state['step'] == 13:
      
        st.session_state['stressz'] = st.selectbox("Milyen gyakran érzi magát stresszesnek vagy idegesnek?", ["Soha", "Ritkán", "Időnként", "Gyakran"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['jovokep'] = st.selectbox("Milyen a jövőről alkotott képe?", ["Inkább borúlátó", "Inkább bizakodó"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['stressz_technika'] = st.selectbox("Használ valamilyen stresszkezelési technikát??", ["Igen", "Nem"],index= None,placeholder="Válasszon a lehetőségek közül!")

        if (st.session_state['stressz'] != None and
            st.session_state['jovokep'] != None and
            st.session_state['stressz_technika'] != None):
            
            st.button("Tovább", on_click=next_step)

        st.progress(91, text="91%")

    elif st.session_state['step'] == 14:
    
        st.session_state['mentalis_egeszseg'] = st.selectbox("Hogyan értékeli a mentális egészségét (koncentrációkészség, mennyire könnyen megy az új dolgok megtanulása)?", ["Nagyon rossz", "Rossz", "Közepes", "Jó", "Kiváló"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['tanulas'] = st.selectbox("Mennyi időt fordít hetente olyan szellemi tevékenységekre, amelyek révén új dolgokat tanul, vagy új készségeket szerez?", ["Kevesebb mint heti 15 percet", "Heti 15-30 percet", "Heti 30-60 percet", "Heti 60 percnél többet"],index= None,placeholder="Válasszon a lehetőségek közül!")
        
        st.session_state['tarsasagi'] = st.selectbox("Milyen gyakran tud minőségi időt tölteni családtagjaival/barátaival?", ["Naponta", "Hetente", "Időnként", "Ritkán"],index= None,placeholder="Válasszon a lehetőségek közül!")

        st.session_state['kapcsolat_minoseg'] = st.selectbox("Milyennek értékeli a kapcsolatainak minőségét?", ["Rossz", "Elfogadható", "Jó", "Kiváló"],index= None,placeholder="Válasszon a lehetőségek közül!")

        if (st.session_state['mentalis_egeszseg'] != None and
            st.session_state['tanulas'] != None and
            st.session_state['tarsasagi'] != None and
            st.session_state['kapcsolat_minoseg'] != None):
            
            st.button("Tovább", on_click=next_step)

        st.progress(100, text="100%")
    
    elif st.session_state['step'] == 15:


#PONTOK SZÁMOLÁSA

#Egészség------------------------------------------------------------------------------------------
        if not st.session_state["egeszseg_valasz"]:
            egeszsegpont = 0
        else:
        
            egeszsegpont = convert (st.session_state['egeszseg_valasz'])

        if not st.session_state['testsuly'] or not st.session_state['testmagassag']:
            bmi = int(0)
        else:
            bmi = int(st.session_state['testsuly']) / ((int(st.session_state['testmagassag'])/100) * (int(st.session_state['testmagassag'])/100))

        bmipont = convertbmi (bmi)

        if not st.session_state['testsuly'] or not st.session_state['testsuly_keteve']:
            testsulytrendpont = 0
        else:   
            testsulytrendpont = testsulytrend(st.session_state['testsuly'], st.session_state['testsuly_keteve'])
                
        if st.session_state['magasvernyomas'] == "Van":
            magasvernyomaspont = 10
        else:   
            magasvernyomaspont = 100

        if st.session_state['vercukor'] == "Igen":
            cukorbetegpont = 10
        else:   
            cukorbetegpont = 100

        if st.session_state['koleszterin'] == "Igen":
            koleszterinpont = 10
        else:   
            koleszterinpont = 100

        if st.session_state['kronikusbetegseg'] == "Nincs több":
            kronikusbetegsegpont = 100
        elif st.session_state['kronikusbetegseg'] == "Egy":
            kronikusbetegsegpont = 70
        elif st.session_state['kronikusbetegseg'] == "Kettő":
            kronikusbetegsegpont = 40
        elif st.session_state['kronikusbetegseg'] == "Kettőnél több":
            kronikusbetegsegpont = 10
        else:
            kronikusbetegsegpont = 0

        if st.session_state['szures'] == "Nem járok":
            szurespont = 10
        if st.session_state['szures'] == "Ritkábban, mint évente":
            szurespont = 55
        if st.session_state['szures'] == "Évente, vagy gyakrabban":
            szurespont = 100
        else: 
            szurespont = 0

        st.session_state['egeszseg_finalscore'] = round(((egeszsegpont+bmipont+testsulytrendpont+magasvernyomaspont+
                            cukorbetegpont+koleszterinpont+kronikusbetegsegpont+szurespont)/8),ndigits=1)


        #Táplálkozás----------------------------------------------------------------------------------------------------
        
        if not st.session_state['taplalkozas_zoldseg']:
            taplalkozaspont_zoldseg = 0
        else:
            taplalkozaspont_zoldseg = taplalkozaspont(st.session_state['taplalkozas_zoldseg'])

        taplalkozaspont_gyumolcs = taplalkozaspont(st.session_state['taplalkozas_gyumolcs'])

        taplalkozaspont_hal = taplalkozaspont(st.session_state['taplalkozas_hal'])

        
        if st.session_state['taplalkozas_edesseg'] == "Naponta":
            taplalkozaspont_edesseg = 10
        
        elif st.session_state['taplalkozas_edesseg'] == "Hetente néhány alkalommal":
            taplalkozaspont_edesseg = 55
        
        elif st.session_state['taplalkozas_edesseg'] == "Ritkán":
            taplalkozaspont_edesseg = 100
        
        else:
            taplalkozaspont_edesseg = 0
        
        if st.session_state['taplalkozas_udito'] == "Naponta":
            taplalkozaspont_udito = 10
        
        elif st.session_state['taplalkozas_udito'] == "Hetente néhány alkalommal":
            taplalkozaspont_udito = 55
        
        elif st.session_state['taplalkozas_udito'] == "Ritkán":
            taplalkozaspont_udito = 100
        
        else:
            taplalkozaspont_udito = 0
        

        taplalkozaspont_teljeskiorles = taplalkozaspont(st.session_state['taplalkozas_teljeskiorles'])

        if st.session_state['taplalkozas_husfele'] == "szárnyas":
            taplalkozaspont_husfele = 100

        elif st.session_state['taplalkozas_husfele'] == "sertés":
            taplalkozaspont_husfele = 30

        elif st.session_state['taplalkozas_husfele'] == "marha":
            taplalkozaspont_husfele = 10

        elif st.session_state['taplalkozas_husfele'] == "egyeb húsfajta":
            taplalkozaspont_husfele = 50
        
        elif st.session_state['taplalkozas_husfele'] == "nem fogyasztok húst":
            taplalkozaspont_husfele = 100
        
        else:
            taplalkozaspont_husfele = 0


        if st.session_state['taplalkozas_nassolas'] == "előfordul":
            taplalkozaspont_nassolas = 55

        elif st.session_state['taplalkozas_nassolas'] == "rendszeresen":
            taplalkozaspont_nassolas = 10     

        elif st.session_state['taplalkozas_nassolas'] == "elvétve/soha":
            taplalkozaspont_nassolas = 100

        else:
            taplalkozaspont_nassolas = 0    
                
        if st.session_state['taplalkozas_foetkezes'] == "saját magam főzök":
            taplalkozaspont_foetkezes = 100

        elif st.session_state['taplalkozas_foetkezes'] == "étteremben eszem":
            taplalkozaspont_foetkezes =  70

        elif st.session_state['taplalkozas_foetkezes'] == "gyorsétteremben eszem":
            taplalkozaspont_foetkezes =  10

        elif st.session_state['taplalkozas_foetkezes'] == "félkész ételt készítem el":
            taplalkozaspont_foetkezes =  40

        else:
            taplalkozaspont_foetkezes = 0   

        if st.session_state['taplalkozas_folyadek'] == "1 liternél kevesebbet":
            taplalkozaspont_folyadek = 10

        elif st.session_state['taplalkozas_folyadek'] == "1-2 litert":
            taplalkozaspont_folyadek = 55

        elif st.session_state['taplalkozas_folyadek'] == "2 liternél többet":
            taplalkozaspont_folyadek = 100

        else:
            taplalkozaspont_folyadek=0
            
        if st.session_state['taplalkozas_rendszeres'] == "rendszeresen":  
            taplalkozaspont_rendszeres = 100
        
        elif st.session_state['taplalkozas_rendszeres'] == "többnyire rendszeresen":  
            taplalkozaspont_rendszeres = 55
        
        elif st.session_state['taplalkozas_rendszeres'] == "többnyire rendszertelenül":  
            taplalkozaspont_rendszeres = 10

        else:
            taplalkozaspont_rendszeres = 0
        
        tapl_valtozok = [taplalkozaspont_zoldseg,
        taplalkozaspont_gyumolcs,
        taplalkozaspont_hal,
        taplalkozaspont_edesseg,
        taplalkozaspont_udito,
        taplalkozaspont_teljeskiorles,
        taplalkozaspont_husfele,
        taplalkozaspont_nassolas,
        taplalkozaspont_foetkezes,
        taplalkozaspont_folyadek,
        taplalkozaspont_rendszeres]

        st.session_state['taplalkozas_finalscore'] = atlag (tapl_valtozok)

        #Testmozgás----------------------------------------------------------------------------------------------------

        testmozgas_alkalom_mapping = {
        "Nem nagyon végzek testmozgást": 10, 
        "Heti 1-2 alkalommal":40, 
        "Heti 3-4 alkalommal":70, 
        "Heti 4 alkalomnál többször":100
    }
        testmozgaspont_gyakorisag = testmozgas_alkalom_mapping.get(st.session_state['testmozgas_alkalom'], 1000)  

        testmozgas_ido_mapping = {
    "Kevesebb mint 30 percet":10, 
    "30-60 percet":35,
    "60-120 percet":60, 
    "120-180 percet":80, 
    "180 percnél többet":100
    }
        testmozgaspont_ido = testmozgas_ido_mapping.get(st.session_state['testmozgas_osszesen'], 1000)  

        testmozgas_nyujtas_mapping = {
        "előfordul":55,
        "rendszeresen":100,
        "elvétve/soha":10
    }
        testmozgaspont_nyujtas = testmozgas_nyujtas_mapping.get(st.session_state['testmozgas_nyujtas'], 1000)  
        
        testmozgas_kardio_mapping = {
        "előfordul":55,
        "rendszeresen":100,
        "elvétve/soha":10
    }
        testmozgaspont_kardio = testmozgas_kardio_mapping.get(st.session_state['testmozgas_kardio'], 1000)  
        
        testmozgas_erosites_mapping = {
        "előfordul":55,
        "rendszeresen":100,
        "elvétve/soha":10
    }
        testmozgaspont_erosites = testmozgas_erosites_mapping.get(st.session_state['testmozgas_erosites'], 1000)  
        
        testmozgas_valtozok = [
            testmozgaspont_gyakorisag,
            testmozgaspont_ido,
            testmozgaspont_erosites,
            testmozgaspont_kardio,
            testmozgaspont_nyujtas
        ]

        st.session_state['testmozgas_finalscore'] = atlag (testmozgas_valtozok)

    #Alvás----------------------------------------------------------------------------------------------------

        alvas_ido_mapping = {
            "Kevesebb mint 5 órát":10, 
            "5-6 órát":55, 
            "7 órát vagy többet":100
        }
        alvaspont_ido = alvas_ido_mapping.get(st.session_state['alvas_ido'], 1000)  

        alvas_felebredes_mapping = {
            "Igen":10, 
            "Nem":100, 
        }
        alvaspont_felebredes = alvas_felebredes_mapping.get(st.session_state['alvas_felebredes'], 1000)  

        alvas_kipihent_mapping = {
            "Igen":100, 
            "Nem":10, 
        }
        alvaspont_kipihent = alvas_kipihent_mapping.get(st.session_state['alvas_kipihent'], 1000)   

        alvas_altato_mapping = {
            "Igen":10, 
            "Nem":100, 
        }
        alvaspont_altato = alvas_altato_mapping.get(st.session_state['alvas_altato'], 1000)  

        alvas_valtozok = [
            alvaspont_ido,
            alvaspont_felebredes,
            alvaspont_kipihent,
            alvaspont_altato
        ]

        st.session_state['alvas_finalscore'] = atlag (alvas_valtozok)

    #Káros szenvedélyek----------------------------------------------------------------------------------------------------

        szenvedely_cigi_mapping = {
            "Nem dohányzom":100, 
            "Alkalmanként":70, 
            "Napi 1 dobozt vagy annál kevesebbet":40, 
            "Napi 1 doboznál többet":10
        }

        szenvedelypont_cigi = szenvedely_cigi_mapping.get(st.session_state['dohanyzas'], 1000)  

        szenvedely_alkohol_mapping = {
            "Soha":100, 
            "Alkalmanként":80, 
            "Havonta 1-2 alkalommal":60, 
            "Hetente 1-2 alkalommal":35, 
            "Naponta":10
        }

        szenvedelypont_alkohol = szenvedely_alkohol_mapping.get(st.session_state['alkohol'], 1000)

        szenvedely_egyeb_mapping = {
            "Van":10, 
            "Nincs":100, 
        }

        szenvedelypont_egyeb = szenvedely_egyeb_mapping.get(st.session_state['karos_szenvedely'], 1000)

        szenvedely_valtozok = [
            szenvedelypont_cigi,
            szenvedelypont_alkohol,
            szenvedelypont_egyeb
        ]

        st.session_state['karosszenvedely_finalscore'] = atlag (szenvedely_valtozok)

    #Érzelmi jóllét----------------------------------------------------------------------------------------------------

        erzelmi_stressz_mapping = {
            "Soha":100, 
            "Ritkán":70, 
            "Időnként":40, 
            "Gyakran":10
        }

        erzelmipont_stressz = erzelmi_stressz_mapping.get(st.session_state['stressz'], 1000)  

        erzelmi_jovokep_mapping = {
            "Inkább borúlátó":10, 
            "Inkább bizakodó":100
        }

        erzelmipont_jovokep = erzelmi_jovokep_mapping.get(st.session_state['jovokep'], 1000)  

        erzelmi_stressztechnika_mapping = {
            "Nem":10, 
            "Igen":100
        }

        erzelmipont_stressztechnika = erzelmi_stressztechnika_mapping.get(st.session_state['stressz_technika'], 1000) 

        erzelmi_valtozok = [
            erzelmipont_stressz,
            erzelmipont_jovokep,
            erzelmipont_stressztechnika
        ]

        st.session_state['erzelmi_egeszseg_finalscore'] = atlag (erzelmi_valtozok)

    #Szellemi jóllét----------------------------------------------------------------------------------------------------

        szellemi_egeszseg_mapping = {
            "Nagyon rossz": 10, 
            "Rossz": 35, 
            "Közepes": 60, 
            "Jó":80, 
            "Kiváló":100
        }

        szellemipont_egeszseg = szellemi_egeszseg_mapping.get(st.session_state['mentalis_egeszseg'], 1000)  

        szellemi_tanulas_mapping = {
            "Kevesebb mint heti 15 percet": 10, 
            "Heti 15-30 percet": 40, 
            "Heti 30-60 percet":70, 
            "Heti 60 percnél többet":100
        }

        szellemipont_tanulas = szellemi_tanulas_mapping.get(st.session_state['tanulas'], 1000)

        szellemi_valtozok = [
            szellemipont_egeszseg,
            szellemipont_tanulas
        ]   

        st.session_state['szellemi_egeszseg_finalscore'] = atlag (szellemi_valtozok)

    #Társasági kapcsolatok----------------------------------------------------------------------------------------------------

        tarsasagi_kapcsolatok_mapping = {
            "Naponta":100, 
            "Hetente": 70, 
            "Időnként":40, 
            "Ritkán":10
        }

        tarsasagipont_kapcsolatok = tarsasagi_kapcsolatok_mapping.get(st.session_state['tarsasagi'], 1000) 
            
        tarsasagi_minoseg_mapping = {
            "Rossz":10, 
            "Elfogadható":40, 
            "Jó":70, 
            "Kiváló":100
        }

        tarsasagipont_minoseg = tarsasagi_minoseg_mapping.get(st.session_state['kapcsolat_minoseg'], 1000) 

        tarsasagi_valtozok = [
            tarsasagipont_kapcsolatok,
            tarsasagipont_minoseg
        ]   

        st.session_state['tarsasagi_kapcsolatok_finalscore'] = atlag (tarsasagi_valtozok)
        
        st.session_state['kitoltes_ideje'] = datetime.datetime.now()

        
        # Connect to SQLite Cloud database
        cloud_conn = sqlitecloud.connect(
            "sqlitecloud://chabidxphz.g2.sqlite.cloud:8860/WellnessSurvey?apikey=7SEWz2HmF8ZXBeMqZtloHXzjs2CrsL2bStfRIm0xZFQ"
        )

        # Function to create a table in SQLite Cloud
        def create_survey_table(conn):
            create_table_query = """
            CREATE TABLE IF NOT EXISTS Survey (
                Felhasználónév TEXT PRIMARY KEY,
                Kitöltés_ideje DATE NOT NULL,
                Születési_dátum DATE NOT NULL,
                Neme TEXT,
                Munkakör TEXT,
                Egészség INTEGER,
                Táplálkozás INTEGER,
                Testmozgás INTEGER,
                Alvás INTEGER,
                Káros_szenvedély INTEGER,
                Érzelmi_egészség INTEGER,
                Szellemi_egészség INTEGER,
                Társas_kapcsolatok INTEGER
            );
            """
            conn.execute(create_table_query)
            conn.commit()

        # Create the table
        create_survey_table(cloud_conn)

        # Function to insert data into the table
        def insert_survey_data(conn, data):
            insert_query = """
            INSERT INTO Survey (
                Felhasználónév, Kitöltés_ideje, Születési_dátum, Neme, Munkakör,
                Egészség, Táplálkozás, Testmozgás, Alvás, Káros_szenvedély,
                Érzelmi_egészség, Szellemi_egészség, Társas_kapcsolatok
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """
            conn.execute(insert_query, data)
            conn.commit()

        # Example: Insert user-provided data into the table
        user_data = (
            st.session_state['felhasznalonev'],
            st.session_state['kitoltes_ideje'],
            st.session_state['szuletesi_datum'],
            st.session_state['neme'],
            st.session_state['munkakor'],
            st.session_state['egeszseg_finalscore'],
            st.session_state['taplalkozas_finalscore'],
            st.session_state['testmozgas_finalscore'],
            st.session_state['alvas_finalscore'],
            st.session_state['karosszenvedely_finalscore'],
            st.session_state['erzelmi_egeszseg_finalscore'],
            st.session_state['szellemi_egeszseg_finalscore'],
            st.session_state['tarsasagi_kapcsolatok_finalscore'],
        )

        try:
            insert_survey_data(cloud_conn, user_data)
            
        except Exception as e:
            st.error(f"Failure {e}")


        # conn = st.connection('sqlitecloud://chabidxphz.g2.sqlite.cloud:8860/WellnessSurvey?apikey=7SEWz2HmF8ZXBeMqZtloHXzjs2CrsL2bStfRIm0xZFQ', type='sql')
        # conn = sqlitecloud.connect("sqlitecloud://chabidxphz.g2.sqlite.cloud:8860/WellnessSurvey?apikey=7SEWz2HmF8ZXBeMqZtloHXzjs2CrsL2bStfRIm0xZFQ")

        # engine = db.create_engine('WellnessSurvey2.db')
        # conn = engine.connect()
        # metadata = db.MetaData()

        # Survey = db.Table('Survey', metadata,
        #             db.Column('Felhasználónév', db.String(),primary_key=True),      
        #             db.Column('Kitöltés_ideje', db.Date(),primary_key=True),
        #             db.Column('Születési_dátum', db.Date(), primary_key=True),
        #             db.Column('Neme', db.String(), primary_key=False),
        #             db.Column('Munkakör', db.String(), primary_key=False),
        #             db.Column('Egészség', db.Integer(), primary_key=False),
        #             db.Column('Táplálkozás', db.Integer(), primary_key=False),
        #             db.Column('Testmozgás', db.Integer(), primary_key=False),
        #             db.Column('Alvás', db.Integer(), primary_key=False),
        #             db.Column('Káros_szenvedély', db.Integer(), primary_key=False),
        #             db.Column('Érzelmi_egészség', db.Integer(), primary_key=False),
        #             db.Column('Szellemi_egészség', db.Integer(), primary_key=False),
        #             db.Column('Társas_kapcsolatok', db.Integer(), primary_key=False)
        #             )

        # metadata.create_all(engine) 

        # query = db.insert(Survey).values(
        #     Felhasználónév= st.session_state['felhasznalonev'],
        #     Kitöltés_ideje = st.session_state['kitoltes_ideje'], 
        #     Születési_dátum=st.session_state['szuletesi_datum'],
        #     Neme=st.session_state['neme'],
        #     Munkakör=st.session_state['munkakor'],
        #     Egészség=st.session_state['egeszseg_finalscore'],
        #     Táplálkozás=st.session_state['taplalkozas_finalscore'], 
        #     Testmozgás=st.session_state['testmozgas_finalscore'], 
        #     Alvás=st.session_state['alvas_finalscore'],
        #     Káros_szenvedély=st.session_state['karosszenvedely_finalscore'],
        #     Érzelmi_egészség=st.session_state['erzelmi_egeszseg_finalscore'],
        #     Szellemi_egészség=st.session_state['szellemi_egeszseg_finalscore'],
        #     Társas_kapcsolatok=st.session_state['tarsasagi_kapcsolatok_finalscore']
        #     )
        # Result = conn.execute(query)
       

        # existing_file = 'jolletfelmeres.xlsx'

        # # New data to append
        # b = [st.session_state['kitoltes_ideje'],
        #         st.session_state['szuletesi_datum'],
        #         st.session_state['neme'],
        #         st.session_state['munkakor'],
        #         st.session_state['egeszseg_finalscore'],
        #         st.session_state['taplalkozas_finalscore'], 
        #         st.session_state['testmozgas_finalscore'], 
        #         st.session_state['alvas_finalscore'],
        #         st.session_state['karosszenvedely_finalscore'],
        #         st.session_state['erzelmi_egeszseg_finalscore'],
        #         st.session_state['szellemi_egeszseg_finalscore'],
        #         st.session_state['tarsasagi_kapcsolatok_finalscore']]
        # db = pd.DataFrame(b)
        # db = db.T
        # # db.to_excel("jolletfelmeres.xlsx", index = False, header = False)
        
        # # Read existing data
        # df_existing = pd.read_excel(existing_file)

        # # Append new data
        # df_combined = pd.concat([df_existing, db], ignore_index=True)

        # # Save the combined data to Excel
        # df_combined.to_excel(existing_file, index=False)
        


        # Define the custom style to position the last entry at the bottom
        st.markdown("""
            <style>
            .bottom-text {
                position: fixed;
                bottom: 1;
                width: 50%;
                text-align: center;
                padding: 10px;
            }
        
            """, unsafe_allow_html=True)

        # Main content
        st.write()

        col1, col2, col3 = st.columns([1, 1, 1])
        col2.button("Kérem az eredményeket!*", on_click=next_step)
           

        # Place the last entry at the bottom
        st.markdown('<div class="bottom-text">*A gomb megnyomásával hozzájárul adatainak kezeléséhez</div>', unsafe_allow_html=True)


else:
    st.empty()
    with st.sidebar:
        
        add_radio = st.radio(
        "Kérem, válasszon!",
        ("HealthCompass", "MindFit")
        )
        st.empty()
    if add_radio == "HealthCompass":
        

        dfradar = pd.DataFrame(dict(
        r=[st.session_state['egeszseg_finalscore'],
            st.session_state['taplalkozas_finalscore'], 
            st.session_state['testmozgas_finalscore'], 
            st.session_state['alvas_finalscore'],
            st.session_state['karosszenvedely_finalscore'],
            st.session_state['erzelmi_egeszseg_finalscore'],
            st.session_state['szellemi_egeszseg_finalscore'],
            st.session_state['tarsasagi_kapcsolatok_finalscore']],
        theta=["Egészség", "Táplálkozás", "Testmozgás", "Alvás", "Káros szenvedélyek", "Érzelmi jóllét", "Szellemi jóllét", "Társasági kapcsolatok"]))
        fig = px.line_polar(dfradar, r='r', theta='theta', line_close=True, markers = True, range_r=(0,100))
        fig.update_polars(radialaxis_tickfont=dict(color='cornflowerblue', size=14))
        fig.update_polars(radialaxis=dict(linecolor='silver', linewidth=2))
        fig.update_polars(radialaxis=dict(tickcolor='silver', tickwidth=1))
        fig.update_layout(
            title={
                'text': 'HealthCompass',    # Customize this line with your desired title text
                'x': 0.5,                          # Center-align the title
                'xanchor': 'center',               # Ensure the title is centered
                'font': {
                    'size': 45,                    # Set the font size
                    'color': 'white'            # Set the font color
                }
            },
            autosize=False,
            width=600,
            height=600,
            margin=dict(t=100) 
        )
        st.plotly_chart(fig)

    if add_radio == "MindFit":
        st.empty()
        
        testiegeszseg=(st.session_state['egeszseg_finalscore']+
            st.session_state['taplalkozas_finalscore']+ 
            st.session_state['testmozgas_finalscore']+
            st.session_state['alvas_finalscore'])/4
        mentalisegeszseg=(st.session_state['karosszenvedely_finalscore']+
            st.session_state['erzelmi_egeszseg_finalscore']+
            st.session_state['szellemi_egeszseg_finalscore']+
            st.session_state['tarsasagi_kapcsolatok_finalscore'])/4

        fig = go.Figure(data=[go.Scatter(
        x=[testiegeszseg], y=[mentalisegeszseg],
        mode='markers',
        marker=dict(size=20, color='blue'),
        
        )])
        fig.update_xaxes(title_text='TESTI EGÉSZSÉG', range=[0, 100],showgrid=False)
        fig.update_yaxes(title_text='MENTÁLIS EGÉSZSÉG', range=[0, 100],showgrid=False)
        fig.update_layout(
        title_text="MindFit",
        title_x=0.4,
        title_font_size=45,                 
        title_font_color='white',
        autosize=False,
        width=600,
        height=600
        )

        img = Image.open("MindFit hatter ppt alap.png")

        fig.update_layout(
        images=[dict(
            source=img,
            xref="x", yref="y",
            x=0, y=100,
            sizing="stretch",
            sizex=100, sizey=100,
            visible = True,
            xanchor="left", yanchor="top",
            opacity=0.8,
            layer="below"
        )]
        )   

        
        st.plotly_chart(fig)