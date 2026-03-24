import streamlit as st 

st.title("Todo list app") 
st.write('create to-do list')

#Inicializar la lista de tareas 
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Agregar nueva tarea. 

new_task = st.text_input("Que tarea quieres agregar?", placeholder="ej:Comprar leche")

if st.button('Agregar tarea'):
    if new_task.strip():
       st.session_state.tasks.append({"text": new_task, "done": False})
       st.success(f"Tarea agregada: **{new_task}**")
    else:
       st.error("Por favor escribe una tarea")

st.subheader('📋 Tus tareas')
if not st.session_state.tasks:
    st.info('No tienes tareas aun tareas')
else:
        for i, task in enumerate(st.session_state.tasks):
            col1, col2 = st.columns([0.8,0.2])
        with col1:
            checked = st.checkbox(task["text"], value=task["done"], key=f"check_{i}")
            st.session_state.tasks[i]["done"] = checked
        with col2:
            if st.button("🗑️", key=f"delete_{i}"):
                del st.session_state.tasks[i]
                st.rerun()
total = len(st.session_state.tasks)
completadas = sum(1 for task in st.session_state.tasks if task["done"])

st.caption(f"Total: {total} | Completadas: {completadas} | Pendientes: {total - completadas}")
