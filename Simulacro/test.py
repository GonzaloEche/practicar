import unittest;
import time

from serv_bueno import Servidor

class TestServidor(unittest.TestCase):

    def test_fecha(self):
        servidor = Servidor()
        fecha = time.strftime("%A %B %d %Y")
        parametro = "fecha"
        fecha2 = servidor.fecha(parametro)
        self.assertEqual(fecha2,fecha)

    def test_hora(self):
        servidor = Servidor()
        hora = time.strftime("%H:%M:%S")
        parametro = "hora"
        hora2 = servidor.hora(parametro)
        self.assertEqual(hora2,hora)

    def test_a_tomar_por_culo_el_strip(self):
        servidor = Servidor()
        parametro = "fecha "
        fecha = servidor.fecha(parametro)
        self.assertEqual(fecha,"Error en el formato")

    def test_a_tomar_por_culo_el_strip2(self):
        servidor = Servidor()
        parametro = " hora"
        hora = servidor.fecha(parametro)
        self.assertEqual(hora,"Error en el formato")

    def test_minusculas(self):
        servidor = Servidor()
        frase = "HORA"
        frase_minus = servidor.minusculas(frase)
        self.assertEqual(frase_minus,"hora")

    def test_puerto(self):
        servidor = Servidor()
        puerto = 16051
        puerto2 = servidor.obtener_puerto()
        self.assertEqual(puerto2,16051)



