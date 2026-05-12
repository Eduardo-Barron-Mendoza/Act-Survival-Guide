import random


PREGUNTAS = {
    "reglas": [
        {
            "pregunta": "¿Qué porcentaje mínimo de asistencia necesitas para tener derecho a evaluación parcial?",
            "tipo": "opcion",
            "opciones": ["70%", "75%", "80%", "90%"],
            "respuesta": "80%"
        },
        {
            "pregunta": "¿Cuántos minutos de tolerancia se permiten en los horarios de 7:00 a.m y 14:00 p.m?",
            "tipo": "opcion",
            "opciones": ["5 minutos", "10 minutos", "15 minutos", "20 minutos"],
            "respuesta": "10 minutos"
        },
        {
            "pregunta": "Si llegas después de los minutos de tolerancia, te cuentan la asistencia.",
            "tipo": "verdadero_falso",
            "respuesta": "Falso"
        },
        {
            "pregunta": "Las tareas pueden entregarse fuera de tiempo si tienes una justificación válida del tutor.",
            "tipo": "verdadero_falso",
            "respuesta": "Verdadero"
        },
        {
            "pregunta": "¿Cuántas incidencias de indisciplina te quitan el derecho a examen?",
            "tipo": "opcion",
            "opciones": ["1", "2", "3", "5"],
            "respuesta": "3"
        },
        {
            "pregunta": "¿Por qué medio debes justificar una falta?",
            "tipo": "opcion",
            "opciones": ["WhatsApp al maestro", "Correo institucional", "Mensaje de texto", "Llamada telefónica"],
            "respuesta": "Correo institucional"
        },
        {
            "pregunta": "¿Cuántas horas tienes para justificar una falta después de que ocurrió?",
            "tipo": "opcion",
            "opciones": ["12 horas", "24 horas", "48 horas", "72 horas"],
            "respuesta": "24 horas"
        },
        {
            "pregunta": "Está permitido comer en el salón si es algo pequeño como un snack.",
            "tipo": "verdadero_falso",
            "respuesta": "Falso"
        },
        {
            "pregunta": "El uso de audífonos está permitido si estás haciendo una actividad que lo requiere.",
            "tipo": "verdadero_falso",
            "respuesta": "Falso"
        },
        {
            "pregunta": "¿Qué documentos se aceptan para justificar una falta?",
            "tipo": "opcion",
            "opciones": [
                "Cualquier nota escrita a mano",
                "Receta médica o citatorio jurídico",
                "Captura de pantalla de una cita",
                "Correo de un familiar"
            ],
            "respuesta": "Receta médica o citatorio jurídico"
        },
        {
            "pregunta": "Si tienes un problema académico, debes ir directo a la dirección sin pasar con el maestro.",
            "tipo": "verdadero_falso",
            "respuesta": "Falso"
        },
        {
            "pregunta": "¿Qué porcentaje mínimo de trabajos en clase necesitas para tener derecho a evaluación?",
            "tipo": "opcion",
            "opciones": ["70%", "75%", "80%", "85%"],
            "respuesta": "80%"
        },
    ],
    "evaluacion": [
        {
            "pregunta": "¿Cuánto vale el Proyecto Integrador en el tercer parcial?",
            "tipo": "opcion",
            "opciones": ["10%", "20%", "30%", "50%"],
            "respuesta": "50%"
        },
        {
            "pregunta": "La Evidencia de conocimiento vale igual en el 1er y 2do parcial.",
            "tipo": "verdadero_falso",
            "respuesta": "Verdadero"
        },
        {
            "pregunta": "¿Cuánto vale la Evidencia de producto en los tres parciales?",
            "tipo": "opcion",
            "opciones": ["10%", "20%", "30%", "40%"],
            "respuesta": "30%"
        },
        {
            "pregunta": "El Proyecto Integrador vale más en el 1er parcial que en el 3er parcial.",
            "tipo": "verdadero_falso",
            "respuesta": "Falso"
        },
        {
            "pregunta": "¿Cuánto vale la Evidencia de desempeño en el primer parcial?",
            "tipo": "opcion",
            "opciones": ["10%", "20%", "30%", "40%"],
            "respuesta": "20%"
        },
        {
            "pregunta": "En el tercer parcial, la Evidencia de conocimiento vale lo mismo que en el primero.",
            "tipo": "verdadero_falso",
            "respuesta": "Falso"
        },
        {
            "pregunta": "¿Cuántos criterios de evaluación existen en la materia?",
            "tipo": "opcion",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "4"
        },
        {
            "pregunta": "La suma de todos los criterios en cualquier parcial da 100%.",
            "tipo": "verdadero_falso",
            "respuesta": "Verdadero"
        },
    ],
    "objetivos": [
        {
            "pregunta": "¿Cuál es el enfoque principal de la materia?",
            "tipo": "opcion",
            "opciones": [
                "Desarrollo de videojuegos",
                "Desarrollo de aplicaciones móviles",
                "Administración de bases de datos",
                "Diseño gráfico digital"
            ],
            "respuesta": "Desarrollo de aplicaciones móviles"
        },
        {
            "pregunta": "La materia incluye el uso de patrones de diseño y arquitecturas móviles.",
            "tipo": "verdadero_falso",
            "respuesta": "Verdadero"
        },
        {
            "pregunta": "¿Qué paradigma de programación se menciona en las competencias de la materia?",
            "tipo": "opcion",
            "opciones": [
                "Programación funcional",
                "Programación orientada a objetos",
                "Programación lógica",
                "Programación estructurada"
            ],
            "respuesta": "Programación orientada a objetos"
        },
        {
            "pregunta": "La materia solo cubre desarrollo para una sola plataforma móvil.",
            "tipo": "verdadero_falso",
            "respuesta": "Falso"
        },
        {
            "pregunta": "¿Qué tipo de soluciones tecnológicas se busca desarrollar en la materia?",
            "tipo": "opcion",
            "opciones": [
                "Solo aplicaciones de escritorio",
                "Soluciones multiplataforma web y móvil",
                "Únicamente videojuegos móviles",
                "Software para hardware industrial"
            ],
            "respuesta": "Soluciones multiplataforma web y móvil"
        },
        {
            "pregunta": "Los frameworks son parte de las herramientas que se estudian en la materia.",
            "tipo": "verdadero_falso",
            "respuesta": "Verdadero"
        },
    ],
    "fechas": [
        {
            "pregunta": "¿En qué fecha es el examen del primer parcial?",
            "tipo": "opcion",
            "opciones": ["02 de Junio 2026", "07 de Julio 2026", "11 de Agosto 2026", "17 de Agosto 2026"],
            "respuesta": "02 de Junio 2026"
        },
        {
            "pregunta": "El examen final es antes del tercer parcial.",
            "tipo": "verdadero_falso",
            "respuesta": "Falso"
        },
        {
            "pregunta": "¿Cuántos exámenes hay en total durante el semestre?",
            "tipo": "opcion",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "4"
        },
        {
            "pregunta": "¿En qué mes es el examen final?",
            "tipo": "opcion",
            "opciones": ["Junio", "Julio", "Agosto", "Septiembre"],
            "respuesta": "Agosto"
        },
        {
            "pregunta": "El segundo parcial se aplica en julio.",
            "tipo": "verdadero_falso",
            "respuesta": "Verdadero"
        },
        {
            "pregunta": "¿Cuántos días hay entre el tercer parcial y el examen final?",
            "tipo": "opcion",
            "opciones": ["3 días", "6 días", "10 días", "15 días"],
            "respuesta": "6 días"
        },
        {
            "pregunta": "El primer y segundo parcial son en meses diferentes.",
            "tipo": "verdadero_falso",
            "respuesta": "Verdadero"
        },
    ],
}

def get_preguntas(seccion, cantidad=2):
    banco = PREGUNTAS.get(seccion, [])
    return random.sample(banco, min(cantidad, len(banco)))