import matplotlib.pyplot as plt
import numpy as np

# Datos proporcionados
umbrales = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4]
tpr = [1.0, 1.0, 1.0, 0.5, 0.5, 0.0]  # Tasa de Verdaderos Positivos
fpr = [0.0, 0.33, 0.67, 0.67, 1.0, 1.0]  # Tasa de Falsos Positivos

# Configuración de la gráfica
plt.figure(figsize=(10, 8))
plt.plot(fpr, tpr, 'b-', marker='o', linewidth=2, markersize=8, label='Curva ROC')

# Línea diagonal de referencia (clasificador aleatorio)
plt.plot([0, 1], [0, 1], 'r--', linewidth=1, label='Clasificador aleatorio (AUC = 0.5)')

# Personalización de la gráfica
plt.xlabel('Tasa de Falsos Positivos (FPR)', fontsize=12)
plt.ylabel('Tasa de Verdaderos Positivos (TPR)', fontsize=12)
plt.title('Curva ROC', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.xlim([-0.05, 1.05])
plt.ylim([-0.05, 1.05])

# Añadir etiquetas con los umbrales
for i, umbral in enumerate(umbrales):
    plt.annotate(f'{umbral}', (fpr[i], tpr[i]), 
                xytext=(5, 5), textcoords='offset points',
                fontsize=9, bbox=dict(boxstyle="round,pad=0.3", fc="yellow", alpha=0.7))

# Calcular AUC (Área bajo la curva) usando la regla del trapecio
auc = np.trapz(tpr, fpr)
plt.text(0.6, 0.2, f'AUC = {auc:.3f}', fontsize=12, 
         bbox=dict(boxstyle="round,pad=0.5", fc="lightblue", alpha=0.8))

plt.tight_layout()
plt.show()

# Mostrar tabla de datos
print("Tabla de datos:")
print("Umbral\tTPR\tFPR")
for i in range(len(umbrales)):
    print(f"{umbrales[i]}\t{tpr[i]}\t{fpr[i]}")