import time
import random
import matplotlib.pyplot as plt

# =====================================================================
# 1. INICIALIZACIÓN DE VARIABLES Y ESTRUCTURAS
# =====================================================================
cola_premium = []           # Cola de alta prioridad
cola_gratis = []            # Cola de baja prioridad
LIMITE_SATURACION = 6       # Capacidad máxima total entre ambas colas
TOTAL_PETICIONES = 15       # Número de solicitudes a simular

atendidas = 0
rechazadas = 0
tiempos_espera = []
historial_tiempos_resp = []

# =====================================================================
# 2. GENERACIÓN DE PETICIONES INICIALES
# =====================================================================
def generar_peticiones(cantidad):
    """Genera una lista de peticiones aleatorias (Premium o Gratis)."""
    peticiones = []
    for i in range(1, cantidad + 1):
        tipo = random.choice(["Premium", "Gratis"])
        peticiones.append({
            "id": i,
            "tipo": tipo,
            "tiempo_llegada": time.time()
        })
    return peticiones

# =====================================================================
# 3. MOTOR DE SIMULACIÓN (Bucle principal)
# =====================================================================
def ejecutar_simulacion():
    global atendidas, rechazadas
    
    peticiones_entrantes = generar_peticiones(TOTAL_PETICIONES)
    print("=== INICIANDO SIMULACIÓN DE COLAS Y BALANCEO DE CARGA ===")
    print(f"Límite máximo en colas: {LIMITE_SATURACION} peticiones.\n")

    while len(peticiones_entrantes) > 0 or len(cola_premium) > 0 or len(cola_gratis) > 0:
        
        # --- BLOQUE A: RECEPCIÓN Y BALANCEO (Llegan hasta 3 peticiones por ciclo) ---
        for _ in range(3):
            if len(peticiones_entrantes) > 0:
                nueva_peticion = peticiones_entrantes.pop(0)
                nueva_peticion["tiempo_llegada"] = time.time()
                
                total_en_colas = len(cola_premium) + len(cola_gratis)
                
                if total_en_colas >= LIMITE_SATURACION:
                    rechazadas += 1
                    print(f"[RECHAZADA] Petición #{nueva_peticion['id']} ({nueva_peticion['tipo']}) - Sistema saturado.")
                else:
                    if nueva_peticion["tipo"] == "Premium":
                        cola_premium.append(nueva_peticion)
                        print(f"[ENCOLADA]  Petición #{nueva_peticion['id']} -> Cola PREMIUM (En espera: {len(cola_premium)})")
                    else:
                        cola_gratis.append(nueva_peticion)
                        print(f"[ENCOLADA]  Petición #{nueva_peticion['id']} -> Cola GRATIS  (En espera: {len(cola_gratis)})")

        # --- BLOQUE B: PROCESAMIENTO SECUENCIAL POR PRIORIDAD ---
        peticion_actual = None
        
        if len(cola_premium) > 0:
            peticion_actual = cola_premium.pop(0)
        elif len(cola_gratis) > 0:
            peticion_actual = cola_gratis.pop(0)

        if peticion_actual is not None:
            tiempo_espera = time.time() - peticion_actual["tiempo_llegada"]
            tiempos_espera.append(tiempo_espera)
            
            latencia = round(random.uniform(0.3, 0.7), 2)
            print(f"   >>> Procesando Petición #{peticion_actual['id']} [{peticion_actual['tipo']}] (Latencia: {latencia}s)...")
            time.sleep(latencia)
            
            atendidas += 1
            tiempo_total_respuesta = tiempo_espera + latencia
            historial_tiempos_resp.append((peticion_actual["id"], peticion_actual["tipo"], tiempo_total_respuesta))

    # =====================================================================
    # 4. CÁLCULO DE MÉTRICAS FINALES Y REPORTE
    # =====================================================================
    tiempo_medio_espera = sum(tiempos_espera) / len(tiempos_espera) if tiempos_espera else 0
    tasa_atencion = (atendidas / TOTAL_PETICIONES) * 100

    print("\n" + "="*50)
    print("           REPORTE FINAL DE RENDIMIENTO")
    print("="*50)
    print(f"Total de peticiones generadas : {TOTAL_PETICIONES}")
    print(f"Peticiones atendidas con éxito: {atendidas}")
    print(f"Peticiones rechazadas         : {rechazadas}")
    print(f"Tasa de atención exitosa      : {tasa_atencion:.2f}%")
    print(f"Tiempo medio de espera        : {tiempo_medio_espera:.4f} segundos")
    print("="*50)

    generar_grafica(historial_tiempos_resp)

def generar_grafica(datos):
    """Genera un gráfico de barras con los tiempos de respuesta por petición."""
    if not datos:
        return
    
    ids = [f"#{d[0]}\n({d[1]})" for d in datos]
    tiempos = [d[2] for d in datos]
    colores = ["#FFD700" if d[1] == "Premium" else "#87CEEB" for d in datos]

    plt.figure(figsize=(10, 5))
    plt.bar(ids, tiempos, color=colores, edgecolor="black")
    plt.title("Tiempo Total de Respuesta por Petición (Dorado = Premium | Azul = Gratis)")
    plt.xlabel("ID de Petición y Tipo")
    plt.ylabel("Tiempo Total (Espera + Latencia en segundos)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    ejecutar_simulacion()
