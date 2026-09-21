import streamlit as st
import pandas as pd
import numpy as np

# Importación de librerías externas
import libreria_funciones_proyecto1 as lfunc
import librería_clases_proyecto1 as lclases

# Configuración de página
st.set_page_config(
    page_title="Academia de Analytics - Módulo 1",
    page_icon="🎓",
    layout="wide"
)

# =========================================================
# ESTILOS CSS PERSONALIZADOS (Paleta Academia de Estudios)
# =========================================================
st.markdown("""
    <style>
    /* Estilos generales */
    .main {
        background-color: #F8FAFC;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Barra lateral */
    [data-testid="stSidebar"] {
        background-color: #0F172A;
        color: #FFFFFF;
    }
    [data-testid="stSidebar"] * {
        color: #F8FAFC !important;
    }
    
    /* Encabezados */
    h1 {
        color: #1E3A8A !important;
        font-weight: 700;
    }
    h2, h3 {
        color: #2563EB !important;
        font-weight: 600;
    }
    
    /* Botones primarios */
    .stButton>button {
        background-color: #2563EB;
        color: white !important;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    /* Tarjetas personalizadas (Cards) */
    .academy-card {
        background-color: #FFFFFF;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #2563EB;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }
    
    .student-card {
        background-color: #EFF6FF;
        padding: 1.2rem;
        border-radius: 10px;
        border: 1px solid #BFDBFE;
    }

    /* Pestañas (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #E2E8F0;
        border-radius: 6px;
        padding: 8px 16px;
        color: #1E293B;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2563EB !important;
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

# Encabezado institucional en la barra lateral
st.sidebar.markdown("""
    <div style="text-align: center; padding: 10px 0;">
        <h2 style="color: #60A5FA !important; margin:0;">🎓 ACADEMIA</h2>
        <p style="font-size: 12px; color: #94A3B8 !important;">Python for Analytics</p>
    </div>
    <hr style="border-color: #334155;">
""", unsafe_allow_html=True)

opcion = st.sidebar.selectbox(
    "Seleccione un módulo/sección:",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# =========================================================
# 1. HOME
# =========================================================
if opcion == "Home":
    st.markdown("""
        <div class="academy-card">
            <h1>🎓 Sistema de Gestión y Prácticas Académicas</h1>
            <p style="font-size: 16px; color: #475569;">Especialización en Python for Analytics — Proyecto Integrador de Fundamentos</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
            <div class="student-card">
                <h3 style="margin-top:0;">👨‍🎓 Perfil del Estudiante</h3>
                <p><b>Nombre Completo:</b> Estudiante DMC</p>
                <p><b>Módulo:</b> Python Fundamentals</p>
                <p><b>Fecha:</b> 2026</p>
                <p><b>Estado:</b> <span style="color: #16A34A; font-weight: bold;">Activo</span></p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            ### 📘 Resumen de Contenidos del Módulo
            
            Esta aplicación interactiva sirve como entorno práctico e integrador para evaluar las competencias clave desarrolladas:

            * **Módulo 1:** Flujo de Caja Financiero *(Listas y Condicionales)*
            * **Módulo 2:** Registro de Inventario y Ventas *(Arrays NumPy & Pandas DataFrames)*
            * **Módulo 3:** Módulo de Cálculo Académico/Empresarial *(Integración de Funciones)*
            * **Módulo 4:** Sistema CRUD de Productos *(Programación Orientada a Objetos - POO)*
        """)

# =========================================================
# 2. EJERCICIO 1 - Flujo de Caja con Listas
# =========================================================
elif opcion == "Ejercicio 1":
    st.markdown("""
        <div class="academy-card">
            <h2>📊 Ejercicio 1: Registro de Flujo de Caja</h2>
            <p>Módulo interactivo para el control y balance de movimientos financieros mediante listas.</p>
        </div>
    """, unsafe_allow_html=True)

    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            concepto = st.text_input("Concepto del movimiento:")
        with col2:
            tipo = st.selectbox("Tipo de movimiento:", ["Ingreso", "Gasto"])
        with col3:
            valor = st.number_input("Valor ($):", min_value=0.0, step=10.0, format="%.2f")

        if st.button("➕ Registrar Movimiento"):
            if concepto.strip() != "":
                st.session_state.movimientos.append({
                    "Concepto": concepto,
                    "Tipo": tipo,
                    "Valor": valor
                })
                st.success("Movimiento añadido al registro.")
            else:
                st.warning("Ingrese un concepto válido.")

    if st.session_state.movimientos:
        st.markdown("---")
        df_movs = pd.DataFrame(st.session_state.movimientos)
        
        col_tabla, col_metrics = st.columns([2, 1])
        with col_tabla:
            st.subheader("Historial de Operaciones")
            st.dataframe(df_movs, use_container_width=True)

        with col_metrics:
            st.subheader("Balance")
            ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
            gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
            saldo = ingresos - gastos

            st.metric("Total Ingresos", f"${ingresos:,.2f}")
            st.metric("Total Gastos", f"${gastos:,.2f}")
            st.metric("Saldo Neto", f"${saldo:,.2f}")

            if saldo >= 0:
                st.success("Flujo de Caja: **A FAVOR**")
            else:
                st.error("Flujo de Caja: **EN CONTRA**")

# =========================================================
# 3. EJERCICIO 2 - Registro con NumPy y DataFrame
# =========================================================
elif opcion == "Ejercicio 2":
    st.markdown("""
        <div class="academy-card">
            <h2>📦 Ejercicio 2: Procesamiento de Inventario con NumPy</h2>
            <p>Captura de datos estructurados procesados vectorialmente en arreglos y convertidos a DataFrames.</p>
        </div>
    """, unsafe_allow_html=True)

    if "np_nombres" not in st.session_state:
        st.session_state.np_nombres = np.array([])
        st.session_state.np_categorias = np.array([])
        st.session_state.np_precios = np.array([])
        st.session_state.np_cantidades = np.array([])
        st.session_state.np_totales = np.array([])

    col1, col2 = st.columns(2)
    with col1:
        prod_nombre = st.text_input("Nombre del Artículo:")
        prod_categoria = st.selectbox("Categoría:", ["Material Académico", "Electrónica", "Servicios", "Otros"])
    with col2:
        prod_precio = st.number_input("Precio Unitario ($):", min_value=0.01, step=1.0, format="%.2f")
        prod_cantidad = st.number_input("Cantidad:", min_value=1, step=1)

    if st.button("💾 Guardar en Arreglo NumPy"):
        if prod_nombre.strip() != "":
            prod_total = prod_precio * prod_cantidad
            
            st.session_state.np_nombres = np.append(st.session_state.np_nombres, prod_nombre)
            st.session_state.np_categorias = np.append(st.session_state.np_categorias, prod_categoria)
            st.session_state.np_precios = np.append(st.session_state.np_precios, prod_precio)
            st.session_state.np_cantidades = np.append(st.session_state.np_cantidades, prod_cantidad)
            st.session_state.np_totales = np.append(st.session_state.np_totales, prod_total)
            
            st.success("Registro almacenado en matriz NumPy.")
        else:
            st.warning("Escriba el nombre del artículo.")

    if len(st.session_state.np_nombres) > 0:
        st.markdown("---")
        df_productos = pd.DataFrame({
            "Artículo": st.session_state.np_nombres,
            "Categoría": st.session_state.np_categorias,
            "Precio Unitario": st.session_state.np_precios,
            "Cantidad": st.session_state.np_cantidades,
            "Total Generado": st.session_state.np_totales
        })

        st.subheader("Registros Activos")
        st.dataframe(df_productos, use_container_width=True)
        st.metric("Total Acumulado", f"${st.session_state.np_totales.sum():,.2f}")

# =========================================================
# 4. EJERCICIO 3 - Librería de Funciones
# =========================================================
elif opcion == "Ejercicio 3":
    st.markdown("""
        <div class="academy-card">
            <h2>⚙️ Ejercicio 3: Calculadora de Indicadores</h2>
            <p>Ejecución de funciones externas especializadas importadas desde <code>libreria_funciones_proyecto1.py</code>.</p>
        </div>
    """, unsafe_allow_html=True)

    if "historico_func" not in st.session_state:
        st.session_state.historico_func = []

    st.subheader("Cálculo: Punto de Equilibrio Comercial")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        costos_fijos = st.number_input("Costos Fijos ($):", min_value=0.0, value=1500.0, step=100.0)
    with col2:
        precio_u = st.number_input("Precio Unitario ($):", min_value=0.1, value=50.0, step=1.0)
    with col3:
        costo_var_u = st.number_input("Costo Variable Unitario ($):", min_value=0.0, value=20.0, step=1.0)

    if st.button("🧮 Calcular e Registrar"):
        try:
            res = lfunc.calcular_punto_equilibrio(costos_fijos, precio_u, costo_var_u)
            
            st.markdown("#### Resultado del Análisis:")
            st.json(res)
            
            st.session_state.historico_func.append({
                "Costos Fijos": costos_fijos,
                "Precio Unitario": precio_u,
                "Costo Var. Unitario": costo_var_u,
                "Margen Contribución": res["margen_contribucion_unitario"],
                "Unidades Equilibrio": res["punto_equilibrio_unidades"],
                "Ventas Equilibrio ($)": res["punto_equilibrio_ventas"]
            })
            st.success("Resultado guardado en la base histórica.")
        except Exception as e:
            st.error(f"Error en la llamada a la función: {e}")

    if st.session_state.historico_func:
        st.markdown("---")
        st.subheader("Histórico de Evaluaciones")
        st.dataframe(pd.DataFrame(st.session_state.historico_func), use_container_width=True)

# =========================================================
# 5. EJERCICIO 4 - Librería de Clases y CRUD
# =========================================================
elif opcion == "Ejercicio 4":
    st.markdown("""
        <div class="academy-card">
            <h2>💻 Ejercicio 4: Gestión de Inventarios POO (CRUD)</h2>
            <p>Administración orientada a objetos con la clase <code>InventarioProducto</code> de <code>librería_clases_proyecto1.py</code>.</p>
        </div>
    """, unsafe_allow_html=True)

    if "inventario_crud" not in st.session_state:
        st.session_state.inventario_crud = {}

    tab_crear, tab_leer, tab_actualizar, tab_eliminar = st.tabs([
        "➕ Crear Registro", "📋 Listado General", "✏️ Modificar", "🗑️ Eliminar"
    ])

    # 1. CREAR
    with tab_crear:
        st.subheader("Nuevo Producto / Artículo")
        c_nombre = st.text_input("Código / Nombre Único:", key="c_nom")
        c_costo = st.number_input("Costo Unitario ($):", min_value=0.01, value=12.0, key="c_cost")
        c_precio = st.number_input("Precio Venta ($):", min_value=0.01, value=25.0, key="c_prec")
        c_stock = st.number_input("Stock Actual:", min_value=0, value=100, key="c_stk")
        c_minimo = st.number_input("Stock Mínimo Alerta:", min_value=0, value=15, key="c_min")

        if st.button("Guardar en Sistema"):
            if c_nombre and c_nombre not in st.session_state.inventario_crud:
                try:
                    obj = lclases.InventarioProducto(c_nombre, c_costo, c_precio, c_stock, c_minimo)
                    st.session_state.inventario_crud[c_nombre] = obj
                    st.success(f"Producto '{c_nombre}' creado con éxito.")
                except Exception as e:
                    st.error(f"Error al instanciar la clase: {e}")
            else:
                st.warning("Nombre ya existente o inválido.")

    # 2. LEER
    with tab_leer:
        st.subheader("Inventario Registrado")
        if st.session_state.inventario_crud:
            data = [obj.resumen() for obj in st.session_state.inventario_crud.values()]
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("Sin registros en el sistema.")

    # 3. ACTUALIZAR
    with tab_actualizar:
        st.subheader("Actualizar Parámetros")
        if st.session_state.inventario_crud:
            prod_sel = st.selectbox("Seleccione un registro:", list(st.session_state.inventario_crud.keys()))
            obj_act = st.session_state.inventario_crud[prod_sel]

            u_costo = st.number_input("Nuevo Costo ($):", value=float(obj_act.costo_unitario))
            u_precio = st.number_input("Nuevo Precio ($):", value=float(obj_act.precio_unitario))
            u_stock = st.number_input("Nuevo Stock:", value=int(obj_act.stock_actual))
            u_min = st.number_input("Nuevo Stock Mínimo:", value=int(obj_act.stock_minimo))

            if st.button("Actualizar"):
                try:
                    st.session_state.inventario_crud[prod_sel] = lclases.InventarioProducto(
                        prod_sel, u_costo, u_precio, u_stock, u_min
                    )
                    st.success(f"Registro '{prod_sel}' actualizado.")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.info("Inventario vacío.")

    # 4. ELIMINAR
    with tab_eliminar:
        st.subheader("Baja de Registros")
        if st.session_state.inventario_crud:
            prod_del = st.selectbox("Seleccione registro a dar de baja:", list(st.session_state.inventario_crud.keys()), key="del_sel")
            if st.button("Confirmar Eliminación", type="primary"):
                del st.session_state.inventario_crud[prod_del]
                st.success(f"Producto '{prod_del}' eliminado.")
                st.rerun()
        else:
            st.info("Sin registros para eliminar.")
