from graphviz import Digraph
import os
class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None
    
    def primer_elemento(self):
        if not self.esta_vacia():
            return self.elementos[0]
        return None
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def longitud(self):
        return len(self.elementos)
    
    def obtener_todos(self):
        return self.elementos.copy()
    
    def graficar_lista(self):
        # dot = Digraph("lista de pacientes", format='png')
        # dot.attr(rankdir='LB')

        # tabla_html = '''<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
        # <TR>
        #     <TD BGCOLOR="#4CAF50"><B>Nombre</B></TD>
        #     <TD BGCOLOR="#4CAF50"><B>Edad</B></TD>
        #     <TD BGCOLOR="#4CAF50"><B>Especialidad</B></TD>
        # </TR>'''
    
        # for paciente in self.elementos:
        #     tabla_html += f'''
        #     <TR>
        #         <TD>{paciente.nombre}</TD>
        #         <TD>{paciente.edad} años</TD>
        #         <TD>{paciente.especialidad}</TD>
        #     </TR>'''
            
        # tabla_html += '''
        #     </TABLE>>'''
        
        # dot.node('tabla', tabla_html, shape='none')
        # dot.render('tabla_pacientes', view=True)

        contenido = """
            graph G{
                node [shape=plaintext]; 
                tablero[label=<<TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">
                    <TR>
                        <TD BGCOLOR="#4CAF50"><B>Nombre</B></TD>
                        <TD BGCOLOR="#4CAF50"><B>Edad</B></TD>
                        <TD BGCOLOR="#4CAF50"><B>Especialidad</B></TD>
                    </TR>
                    """
        
        tabla_html = ""
        
        for paciente in self.elementos:
             tabla_html += f'''
             <TR>
                 <TD>{paciente.nombre}</TD>
                 <TD>{paciente.edad} años</TD>
                 <TD>{paciente.especialidad}</TD>
             </TR>
             '''

        contenido += tabla_html

        contenido += """
            </TABLE>>];
            }
            """
        file = open("Grafica.dot", "w", encoding="utf-8")
        file.write(contenido)
        file.close()
        os.system("dot -Tpng Grafica.dot -o Grafica.png")

    