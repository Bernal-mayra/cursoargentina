print("PARTE 1: Resolucion del ejercicio de programación")
empleado = "Juan"
sueldo_efmamj = 300*6   #Enero a Junio
sueldo_jaso = 500*4     #Julio a Octubre
sueldo_nd = 700*2       #Noviembre y Diciembre
prom_s = (sueldo_efmamj + sueldo_jaso + sueldo_nd)/12 #resultado del Promedio
print("El promedio del sueldo del trabajador",empleado, "es de:",prom_s,"dólares.")
#estructura para saber que tipo de sueldo que cobra.
if prom_s >= 900:
    nivel = "se encuentra cobrando un sueldo mejor de lo normal."
elif prom_s < 900 and prom_s >= 300:
    nivel = "se encuentra cobrando un sueldo normal."
elif prom_s < 300:
    nivel = "se encuentra cobrando un sueldo bajo."
else:
    print("No es valido el resultado")
print("El empleado",empleado,nivel)