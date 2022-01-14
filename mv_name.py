#FUNCTIONS:
def m_v_name(name):
    mass='0'
    v='0'
    if (name[-5]=='0'):
        v='0'
    elif (name[-5]=='4'):
        v='4'
    
    if (name[1:4]=='0p8'):
        mass='0.8'
    elif (name[1:4]=='0p9'):
        mass='0.9'
    elif (name[1:4]=='1p1'):
        mass='1.1'
    elif (name[1:4]=='1p5'):
        mass='1.5'
    elif (name[1:4]=='1p7'):
        mass='1.7'
    elif (name[1:5]=='1p25'):
        mass='1.25'
    elif (name[1:5]=='1p35'):
        mass='1.35'
    elif (name[1:4]=='001'):
        mass='1'
    elif (name[1:4]=='2p5'):
        mass='2.5'
    elif (name[1:4]=='002'):
        mass='2'
    elif (name[1:4]=='003'):
        mass='3'
    elif (name[1:4]=='004'):
        mass='4'
    elif (name[1:4]=='005'):
        mass='5'
    elif (name[1:4]=='007'):
        mass='7'
    elif (name[1:4]=='009'):
        mass='9'
    elif (name[1:4]=='012'):
        mass='12'
    elif (name[1:4]=='015'):
        mass='15'
    elif (name[1:4]=='020'):
        mass='20'
    elif (name[1:4]=='025'):
        mass='25'
    elif (name[1:4]=='032'):
        mass='32'
    elif (name[1:4]=='040'):
        mass='40'
    elif (name[1:4]=='060'):
        mass='60'
    elif (name[1:4]=='085'):
        mass='85'
    elif (name[1:4]=='120'):
        mass='120'
        
    return mass,v

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]