

from expansiontermicamineral import ExpansionTermicaMineral


olivina=ExpansionTermicaMineral("olivino", 6.5,"V�TREO", True, "#9ab973", "(FeMg)2SiO4",
                                 "NO MET�LICO", 3.9, "Taller_1/olivine_angel_2017.csv")
grafito=ExpansionTermicaMineral("grafito", 1.5,"MET�LICO", False, "#5f6168", "C"
                                ,"HEXAGONAL", 2.2, "Taller_1/graphite_mceligot_2016.csv")

alpha_ol, error_ol, fig_ol=olivina.coeficiente()
alpha_gr, error_gr, fig_gr=grafito.coeficiente()

fig_ol.savefig("Taller_1/alpha_olvina.png")
fig_gr.savefig("Taller_1/alpha_grafito.png")