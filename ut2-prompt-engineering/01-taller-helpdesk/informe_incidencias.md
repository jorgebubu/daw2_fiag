# Informe de incidencias · MotorShield Taller - JM

**Generado:** 13 de noviembre de 2026 a las 13:08
**Responsable:** Jorge Montalbán (2º DAW)

## 1. Resumen ejecutivo (KPIs)

| Indicador | Valor |
| --- | --- |
| Total de tickets | 11 |
| Pendientes de prioridad ALTA | 3 |
| Datos PII protegidos | 12 |
| Ataques / rechazos bloqueados | 3 |

## 2. Incidencias por categoría

| Categoría | Nº de tickets |
| --- | --- |
| REDES | 2 |
| SOFTWARE | 2 |
| SEGURIDAD | 2 |
| FACTURACION | 2 |
| HARDWARE | 2 |
| OTROS | 1 |

## 3. Incidencias por prioridad

| Prioridad | Nº de tickets |
| --- | --- |
| ALTA | 6 |
| MEDIA | 3 |
| BAJA | 2 |

## 4. Tickets urgentes pendientes

| # | Solicitante | Ubicación | Categoría | Tiempo est. | Solución sugerida |
| --- | --- | --- | --- | --- | --- |
| 8 | Recepción Taller MotorShield | Recepción - Elevador 3 | REDES | 90 min | Comprobar la configuración de red del portátil, validar la IP en el VLAN del taller y rotar la contraseña del panel del elevador. |
| 7 | Elena Torres | Salón de Actos | HARDWARE | 60 min | Desconectar el proyector por seguridad, revisar la lámpara y el cableado, y dejar un equipo de sustitución para la charla. |
| 5 | Proveedor Hosting (Cobros) | Pasarela de facturación | FACTURACION | 30 min | Revisar los datos de la tarjeta en la pasarela de pago y reintentar el cargo de renovación del dominio. |

## 5. Datos PII protegidos por tipo

| Tipo de dato | Ocurrencias |
| --- | --- |
| DNI | 2 |
| TELEFONO | 2 |
| CLAVE | 2 |
| TARJETA | 1 |
| CVV | 1 |
| DIRECCION | 1 |
| IP | 1 |
| MATRICULA | 1 |
| IBAN | 1 |

## 6. Detalle de tickets pendientes

### #2 · Laura Gómez · SOFTWARE

- **Ubicación:** Secretaría
- **Prioridad:** MEDIA
- **Tiempo estimado:** 30 min
- **Razonamiento IA:** Bloquea la emisión de certificados en atención al público, pero existe una alternativa manual y no afecta a un examen en curso.
- **Solución sugerida:** Reanudar la cola de impresión, revisar el spooler y reinstalar el controlador de la impresora láser.

> El ordenador de atención al público no imprime los certificados. He probado a entrar con mi clave temporal [CLAVE_OCULTA] pero la impresora láser sigue en pausa.

### #4 · Marcos Cano · SOFTWARE

- **Ubicación:** Laboratorio de DAW2 (PC 08)
- **Prioridad:** BAJA
- **Tiempo estimado:** 20 min
- **Razonamiento IA:** Es una mejora planificada que no impide trabajar con normalidad, por lo que puede resolverse fuera de las horas críticas.
- **Solución sugerida:** Actualizar la extensión de Python en el PC 08 durante la ventana de mantenimiento.

> Cuando podáis, en el Laboratorio de DAW2 haría falta actualizar la extensión de Python en el PC 08. No corre prisa, funciona todo bien. Remitente: (DNI [DNI_OCULTO])

### #5 · Proveedor Hosting (Cobros) · FACTURACION

- **Ubicación:** Pasarela de facturación
- **Prioridad:** ALTA
- **Tiempo estimado:** 30 min
- **Razonamiento IA:** Si no se corrige antes del viernes el dominio puede caducar y dejar sin servicio la web y el correo del taller.
- **Solución sugerida:** Revisar los datos de la tarjeta en la pasarela de pago y reintentar el cargo de renovación del dominio.

> Error en el cargo de renovación del dominio del instituto en la tarjeta corporativa [TARJETA_OCULTA] (CVV [CVV_OCULTO]). Por favor, revisad la pasarela de facturación antes del viernes.

### #7 · Elena Torres · HARDWARE

- **Ubicación:** Salón de Actos
- **Prioridad:** ALTA
- **Tiempo estimado:** 60 min
- **Razonamiento IA:** Hay olor a quemado, lo que supone un riesgo eléctrico y afecta a una charla con 100 asistentes mañana a primera hora.
- **Solución sugerida:** Desconectar el proyector por seguridad, revisar la lámpara y el cableado, y dejar un equipo de sustitución para la charla.

> El proyector del Salón de Actos parpadea en color rosa y huele un poco a quemado. Mañana a primera hora hay charla para 100 alumnos. Contacto: (Móvil personal: [TELEFONO_OCULTO], [DIRECCION_OCULTO])

### #8 · Recepción Taller MotorShield · REDES

- **Ubicación:** Recepción - Elevador 3
- **Prioridad:** ALTA
- **Tiempo estimado:** 90 min
- **Razonamiento IA:** Impide cerrar las órdenes de trabajo del día en el elevador 3 y además expone credenciales de administración en texto plano.
- **Solución sugerida:** Comprobar la configuración de red del portátil, validar la IP en el VLAN del taller y rotar la contraseña del panel del elevador.

> El portátil de recepción no conecta con la máquina de diagnosis del elevador 3. Me han dado la IP [IP_OCULTA] y la contraseña en texto plano [CLAVE_OCULTA] para entrar al panel de administración, pero al guardar la configuración da error de red y no podemos cerrar las órdenes de trabajo del día.

### #9 · Cliente - Taller Mecánico San Andrés · FACTURACION

- **Ubicación:** Facturación - Cobros
- **Prioridad:** MEDIA
- **Tiempo estimado:** 40 min
- **Razonamiento IA:** Afecta al cobro de un cliente y a la conciliación bancaria, pero no bloquea la operativa del taller a corto plazo.
- **Solución sugerida:** Conciliar el movimiento bancario con la factura emitida y confirmar el abono con el cliente.

> Buenas, hemos recibido la factura del vehículo con matrícula [MATRICULA_OCULTA] y el cargo no cuadra. La transferencia la hicimos desde la cuenta [IBAN_OCULTO] y todavía aparece como pendiente en vuestro sistema. ¿Podéis revisar la pasarela de cobro antes del viernes?

### #11 · Ana María Ruiz · HARDWARE

- **Ubicación:** Recepción - Elevador 3
- **Prioridad:** MEDIA
- **Tiempo estimado:** 30 min
- **Razonamiento IA:** Ticket registrado manualmente desde el panel. Se asigna prioridad MEDIA según el impacto descrito por el solicitante.
- **Solución sugerida:** Pendiente de revisión por el equipo TIC del taller.

> La impresora de etiquetas del taller no imprime los códigos QR de las órdenes de trabajo.

---

_Informe generado automáticamente en el navegador. Los datos personales han sido
sustituidos por placeholders conforme al RGPD; no se ha enviado información a ningún servidor._