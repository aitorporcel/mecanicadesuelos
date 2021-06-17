import math
import matplotlib.pyplot as plt

def calculo_diametro_eficaz(Pm, PM, Dm, DM, Px):
	if Pm == PM:
 		return Dm
	return 10**(math.log10(Dm) + ((Px - Pm)/(PM - Pm)) * math.log10(DM/Dm))

def determinar_Ps(Px, suelo):
    tamices = {"0":76.2, "1": 19.05, "2": 4.75, "3": 2, "4": 0.425, "5": 0.075}
    Pm = 0
    PM = 0
    Dm = 0
    DM = 0
    if Px == 10 and min(suelo) >= 10:
    	#Devuelvo directamente los valores para que tome D10 = 0.075
    	return (10, 10, 0.075, 0.075)

    for n, i in enumerate(suelo):
        if i >= Px:
            PM = i
            DM = tamices[str(n)]
        if i <= Px and Pm == 0:
            Pm = i
            Dm = tamices[str(n)]
    return (Pm, PM, Dm, DM)


def calculo_diametros(suelo):

	diametros_eficaces = [10, 30, 60]
	diametros_resultados = {}
	for d in diametros_eficaces:
		Pm, PM, Dm, DM = determinar_Ps(d, suelo)
		diametros_resultados[str(d)] = calculo_diametro_eficaz(Pm, PM, Dm, DM, d)
	return diametros_resultados


def calculo_Cc_Cu(diametros_resultados):

	Cc = (diametros_resultados["30"]**2)/(diametros_resultados["60"] * diametros_resultados["10"])
	Cu = diametros_resultados["60"]/diametros_resultados["10"]
	return Cc, Cu

def calcular_porcentaje_gravas(suelo):

	X = (100 - suelo[2])/(100 - suelo[5]) * 100
	return X


def predomina_G_S(X):

	if X >= 50:
		return "G"
	else:
		return "S"


def calculo_IP(LL,LP):
	return LL - LP

def calculo_IPA(LL):
	return 0.73 * (LL - 30)

def calculo_IPU(LL):
	return 0.9 * (LL - 8)


def clasifica_grupo_1(suelo):

    #Calculo el porcentaje de gravas
	X = calcular_porcentaje_gravas(suelo)
	predomina = predomina_G_S(X)

	#Calculo los diametros eficaces
	diametros_resultados = calculo_diametros(suelo)

	#Calculo Cc y Cu
	Cc, Cu = calculo_Cc_Cu(diametros_resultados)

	if predomina == 'G':
		if Cc >= 1 and Cc <= 3 and Cu > 4:
			return "Grava bien graduada (GW)"
		else:
			return "Grava pobremente graduada (GP)"
	else:
		if Cc >= 1 and Cc <= 3 and Cu > 6:
			return "Arena bien graduada (SW)"
		else:
			return "Arena pobremente graduada (SP)"


def clasifica_grupo_2(suelo, LL, LP):

	#Calculo el porcentaje de gravas
	X = calcular_porcentaje_gravas(suelo)
	predomina = predomina_G_S(X)

	#Calculo los diametros eficaces
	diametros_resultados = calculo_diametros(suelo)

	#Calculo Cc y Cu
	Cc, Cu = calculo_Cc_Cu(diametros_resultados)

	#Calculo IPm e IPA:
	IPm = calculo_IP(LL, LP)
	IPa = calculo_IPA(LL)

	if predomina == 'G':

		if Cc >= 1 and Cc <= 3 and Cu > 4:
			if IPm >= 4 and IPm <= 7 and IPm >= IPa:
				return "Grava limo arcillosa bien graduada (GW-GC-GM)"
			if IPa <= IPm:
				return "Grava arcillosa bien graduada (GW-GC)"
			else:
				return "Grava limosa bien graduada (GW-GM)"
		else:
			if IPm >= 4 and IPm <= 7 and IPm >= IPa:
				return "Grava limo arcillosa pobremente graduada (GP-GC-GM)"
			if IPa <= IPm:
				return "Grava arcillosa pobremente graduada (GP-GC)"
			else:
				return "Grava limosa pobremente graduada (GP-GM)"
	else:
		if Cc >= 1 and Cc <= 3 and Cu > 6:
			if IPm >= 4 and IPm <= 7 and IPm >= IPa:
				return "Arena limo arcillosa bien graduada (SW-SC-SM)"
			if IPa <= IPm:
				return "Arena arcillosa bien graduada (SW-SC)"
			else:
				return "Arena limosa bien graduada (SW-SM)"
		else:
			if IPm >= 4 and IPm <= 7 and IPm >= IPa:
				return "Arena limo arcillosa pobremente graduada (SP-SC-SM)"
			if IPa <= IPm:
				return "Arena arcillosa pobremente graduada (SP-SC)"
			else:
				 return "Arena limosa pobremente graduada (SP-SM)"


def clasifica_grupo_3(suelo, LL, LP):
	#Calculo el porcentaje de gravas
	X = calcular_porcentaje_gravas(suelo)
	predomina = predomina_G_S(X)

	#Calculo IPm e IPA:
	IPm = calculo_IP(LL, LP)
	IPa = calculo_IPA(LL)

	if predomina == 'G':
		if IPm >= 4 and IPm <= 7 and IPm >= IPa:
				return "Grava limo arcillosa (GC-GM)"
		if IPa <= IPm:
			return "Grava arcillosa (GC)"
		else:
			return "Grava limosa (GM)"
	else:
		if IPm >= 4 and IPm <= 7 and IPm >= IPa:
				return "Arena limo arcillosa (SC-SM)"
		if IPa <= IPm:
			return "Arena arcillosa (SC)"
		else:
			return "Arena limosa (SM)"

def clasifica_grupo_4(LL, LP):

	#Calculo IPm e IPA:
	IPm = calculo_IP(LL, LP)
	IPa = calculo_IPA(LL)

	if IPm >= 4 and IPm <= 7 and IPm >= IPa:
				return "CL - ML"

	if IPa <= IPm:
		if LL < 50:
			return "Arcilla de baja plasticidad o bajo límite líquido (CL)"
		else:
			return "Arcilla de alta plasticidad o alto límite líquido (CH)"
	else:
		if LL < 50:
			return "Limo de baja compresibilidad o bajo límite líquido (ML)"
		else:
			return "Limo de alta compresibilidad o alto límite líquido (MH)"


def control_logico(suelo, LL, LP):
	if suelo[0] >= suelo[1] >= suelo[2] >= suelo[3] >= suelo[4] >= suelo[5] and LL >= LP and suelo[0] <= 100:
		return "ok"
	else:
		return "revisar datos"


def clasificar_suelo(suelo, LL, LP):
	#Determino la fraccion fina
	FF = suelo[5]

	#Controlo que los datos sean coherentes
	if control_logico(suelo, LL, LP) == "revisar datos":
		return "revisar datos"

	if FF < 5:
		return clasifica_grupo_1(suelo)

	elif FF >= 5 and FF <= 12:
		return clasifica_grupo_2(suelo, LL, LP)

	elif FF > 12 and FF < 50:
		return clasifica_grupo_3(suelo, LL, LP)

	else:
		return clasifica_grupo_4(LL, LP)


def ploteo_curva(suelo):
	fig, ax = plt.subplots()
	tamices = [76.2, 19.05,  4.75, 2, 0.425,  0.075]

	ax.semilogx(tamices, suelo)
	ax.set_xlim(76.2, 0.075)
	ax.set_title('curva granulométrica')
	ax.grid(False)
	ax.set_xticks(tamices)
	ax.set_xticklabels(["3''", "3/4''",  "N°4", "N°10", "N°40",  "N°200"])
	return fig
