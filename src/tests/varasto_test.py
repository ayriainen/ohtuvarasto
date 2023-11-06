import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_saldo_isompi(self):
        #katsotaan voiko saldo olla isompi kuin tilavuus
        varasto = Varasto(10, 11)

        self.assertAlmostEqual(varasto.saldo, 10)
    
    def test_konstruktori_miinus_tilavuus(self):
        varasto = Varasto(-1)

        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_miinus_saldo(self):
        varasto = Varasto(10, -1)

        self.assertAlmostEqual(varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_yli(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus + 1)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
    
    def test_lisays_varasto_miinus(self):
        alku_saldo = self.varasto.saldo

        self.varasto.lisaa_varastoon(-3)

        self.assertAlmostEqual(self.varasto.saldo, alku_saldo)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_ottaminen_yli(self):
        self.varasto.lisaa_varastoon(1)

        otettu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(otettu_maara, 1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_miinus(self):
        alku_saldo = self.varasto.saldo

        otettu_maara = self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(otettu_maara, 0)

        self.assertAlmostEqual(self.varasto.saldo, alku_saldo)

    def test_tulostus(self):
        self.varasto.lisaa_varastoon(1)

        odotettu = "saldo = 1, vielä tilaa 9"

        self.assertEqual(str(self.varasto), odotettu)