# curve_ROC
gráfica ROC en r



**Lista de datos de ejemplo:**

Verdadero positivo	Verdadero negativo	Probabilidad

1	0	0,9

1	0	0,8

1	0	0,7

0	1	0,6

0	1	0,5

0	1	0,4

Pasos para crear la curva ROC:

1.	Ordena los datos: Ordena los datos por probabilidad en orden descendente.

2.	Calcula la tasa de verdaderos positivos (TPR) y la tasa de falsos positivos (FPR):

•	TPR (sensibilidad): Número de verdaderos positivos / Número total de positivos
•	FPR (1 - especificidad): Número de falsos positivos / Número total de negativos

3.	Traza la curva ROC: Traza la TPR frente a la FPR para cada umbral de probabilidad.


**Ejemplo:**
Usando los datos de ejemplo:

Umbral	TPR	FPR

0,9	1,0	0,0

0,8	1,0	0,33

0,7	1,0	0,67

0,6	0,5	0,67

0,5	0,5	1,0

0,4	0,0	1,0


Trazando la TPR frente a la FPR


