import webbrowser
from datetime import datetime
def generar_HTML(repo):
    name = "Reporte"
    with open(name + ".html", "w") as f:
        f.write("<!DOCTYPE html>\n<html>\n<body>\n")
        f.write("\n<div><H1 style=\"align=center\">Reportes</H1></div>\n")

        f.write("<table><thead>")
        f.write("\n<tr><th>Date-Time</th>\n<th>Tipo</th>\n<th>Informacion</th>\n</tr></thead>")

        temp = repo.head
        f.write("<tbody>")
        while(temp != None):
            dt_string = temp.dt.strftime("%d/%m/%Y %H:%M:%S")
            f.write("<tr>")
            f.write("\n<td style=\"text-align: center; vertical-align: middle\">" + str(dt_string) + "</td><td>" + str(temp.type) + "</td><td>" + str(temp.desc) + "</td>")
            f.write("</tr>")
            temp = temp.next
        f.write("</tbody></table></div>")
        f.write("\n</body>\n</html>")
        webbrowser.open("Reporte.html")