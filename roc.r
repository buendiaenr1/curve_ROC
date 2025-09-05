


install.packages("pROC")



library(pROC)
# Resultado real: 1 = enfermo, 0 = sano
enfermedad <- c(0, 0, 0, 0, 0, 1, 1, 1, 1, 1)

# Probabilidades predichas por el modelo (ej. resultado de una prueba)
# Valores entre 0 y 1: probabilidad de tener la enfermedad
probabilidades <- c(0.1, 0.2, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9)


# Crear la curva ROC
roc_obj <- roc(enfermedad, probabilidades)

# Graficarla
plot(roc_obj, 
     main = "Curva ROC - Diagnóstico de Enfermedad",
     col = "blue",
     lwd = 2)

# Añadir la línea de azar (modelo aleatorio)
lines(c(0,1), c(0,1), col = "red", lty = 2, lwd = 2)

# Calcular el AUC
auc_value <- auc(roc_obj)
print(paste("AUC:", round(auc_value, 2)))
#•	AUC = 1.0: Modelo perfecto
#•	AUC = 0.8–0.9: Muy bueno
#•	AUC = 0.5: Modelo inútil (azar)
#•	En este ejemplo, probablemente obtengas AUC = 0.9 o 1.0, lo que indica un buen modelo.
