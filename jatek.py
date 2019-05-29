from jatek_fuggvenyek import *
import arcade
from spriteok.erme import Erme
from spriteok.kard import Kard
from spriteok.lada import Lada
from spriteok.ork import Ork
from spriteok.demon import Demon
from spriteok.jatekos import Jatekos
from spriteok.fal import Fal

KEP_SZELESSEG = 640
KEP_MAGASSAG = 480

MEZO_MERET = 32
BAL_HATAR = 48
JOBB_HATAR = 592
FELSO_HATAR = 432
ALSO_HATAR = 48


class LovagJatek(arcade.Window):

    def __init__(self):
        super().__init__(KEP_SZELESSEG, KEP_MAGASSAG, "Lovagjáték")

        self.jatekos_lista = None
        self.eletero_lista = None
        self.erme_jelzo_lista = None
        self.erme_lista = None
        self.kard_lista = None
        self.szorny_lista = None
        self.lada_lista = None
        self.fal_lista = None

        self.jatekos_sprite = None

        self.jatekos_1 = Jatekos(13, 9, 5)
        self.jatekos_2 = Jatekos(8, 7, 5)

    def on_key_press(self, megnyomott_gomb, modositok):
        self.mozgasd_a_jatekost(megnyomott_gomb)

        if self.jatekos_1.eletek == 0:
            self.kesz = True

        if self.kesz:
            self.close()

    def on_draw(self):

        arcade.start_render()
        self.jelenitsd_meg_a_hatteret()

        self.jatekos_lista.draw()
        self.erme_jelzo_lista.draw()
        self.jelenitsd_meg_az_aranymennyiseget()
        self.eletero_lista.draw()
        self.erme_lista.draw()
        self.kard_lista.draw()
        self.szorny_lista.draw()
        self.lada_lista.draw()
        self.fal_lista.draw()

    def inditas(self):
        self.grafika_init()

        self.eletek_kezdeti_kirajzolasa()

        self.kesz = False

        udvozlet()

        self.jatekos_1.aranyat_talal(5)

        arcade.run()

        viszlat(self.jatekos_1.tavolsag, self.jatekos_1.arany)
        kiir_fejlett(self.jatekos_1.targylista)

    def grafika_init(self):

        self.hatter_pozicio_x, self.hatter_pozicio_y = KEP_SZELESSEG / 2, KEP_MAGASSAG / 2
        self.hatter_kep = arcade.load_texture("img/palya.png")

        self.jatekos_sprite_init()

        self.eletero_lista = arcade.SpriteList()

        self.erme_jelzo_init()
        self.erme_sprite_init()
        self.kard_sprite_init()
        self.szorny_sprite_init()
        self.lada_sprite_init()
        self.fal_sprite_init()


    def jatekos_sprite_init(self):
        self.jatekos_lista = arcade.SpriteList()
        self.jatekos_lista.append(self.jatekos_1)
        self.jatekos_lista.append(self.jatekos_2)


    def erme_jelzo_init(self):
        self.erme_jelzo_sprite = arcade.Sprite("img/Coin1.png")
        self.erme_jelzo_sprite.center_x = MEZO_MERET / 2
        self.erme_jelzo_sprite.center_y = KEP_MAGASSAG - 1.5 * MEZO_MERET
        self.erme_jelzo_lista = arcade.SpriteList()
        self.erme_jelzo_lista.append(self.erme_jelzo_sprite)


    def erme_sprite_init(self):
        self.erme_lista = arcade.SpriteList()
        self.erme_lista.append(Erme(3, 5, 2))
        self.erme_lista.append(Erme(12, 7, 7))
        self.erme_lista.append(Erme(13, 2, 13))
        self.erme_lista.append(Erme(7, 8, 5))


    def kard_sprite_init(self):
        self.kard_lista = arcade.SpriteList()
        self.kard_lista.append(Kard(12, 5))
        self.kard_lista.append(Kard(3, 7))


    def szorny_sprite_init(self):
        self.szorny_lista = arcade.SpriteList()
        self.szorny_lista.append(Ork(2, 5))
        self.szorny_lista.append(Demon(7, 2))


    def lada_sprite_init(self):
        self.lada_lista = arcade.SpriteList()
        self.lada_lista.append(Lada(4, 5,['balta', 'kard'], True))
        self.lada_lista.append(Lada(11, 7, ['balta', 'páncél'], False))


    def fal_sprite_init(self):
        self.fal_lista = arcade.SpriteList()
        for i in range(4, 15):
            self.fal_lista.append(Fal(i, 11))
            self.fal_lista.append(Fal(i, 3))


    def koordinatak_szamolasa(self, x_mezo, y_mezo):
        x_pixelben = MEZO_MERET * x_mezo + MEZO_MERET / 2
        y_pixelben = MEZO_MERET * y_mezo + MEZO_MERET / 2
        return x_pixelben, y_pixelben

    def mozgasd_a_jatekost(self, megnyomott_gomb):

        if megnyomott_gomb == arcade.key.LEFT:

            if self.jatekos_1.center_x > BAL_HATAR:

                self.jatekos_1.balra_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.RIGHT:
            if self.jatekos_1.center_x < JOBB_HATAR:
                self.jatekos_1.jobbra_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.UP:
            if self.jatekos_1.center_y < FELSO_HATAR:
                self.jatekos_1.felfele_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.DOWN:
            if self.jatekos_1.center_y > ALSO_HATAR:
                self.jatekos_1.lefele_lep(self.fal_lista)

        if megnyomott_gomb == arcade.key.A:
            if self.jatekos_2.center_x > BAL_HATAR:
                self.jatekos_2.balra_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.D:
            if self.jatekos_2.center_x < JOBB_HATAR:
                self.jatekos_2.jobbra_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.W:
            if self.jatekos_2.center_y < FELSO_HATAR:
                self.jatekos_2.felfele_lep(self.fal_lista)

        elif megnyomott_gomb == arcade.key.S:
            if self.jatekos_2.center_y > ALSO_HATAR:
                self.jatekos_2.lefele_lep(self.fal_lista)

    def update(self, delta_time):

        for jatekos in self.jatekos_lista:
            erintett_ermek = arcade.check_for_collision_with_list(
                jatekos,
                self.erme_lista)

            for erme in erintett_ermek:
                erme.kill()
                Erme.szamlalo -= 1
                jatekos.aranyat_talal(erme.ertek)

            erintett_kardok = arcade.check_for_collision_with_list(
                jatekos,
                self.kard_lista
            )

            for kard in erintett_kardok:
                jatekos.targyat_talal("kard")
                kard.kill()

            erintett_ladak = arcade.check_for_collision_with_list(
                jatekos,
                self.lada_lista
            )

            for lada in erintett_ladak:
                lada.kifoszt(jatekos)

            jatekos.update()

        if Erme.szamlalo == 0:
            self.kesz = True

    def jelenitsd_meg_a_hatteret(self):
        arcade.draw_texture_rectangle(
            self.hatter_pozicio_x,
            self.hatter_pozicio_y,
            self.hatter_kep.width,
            self.hatter_kep.height,
            self.hatter_kep)

    def jelenitsd_meg_az_aranymennyiseget(self):
        arcade.draw_text(
            str(self.jatekos_1.arany),
            MEZO_MERET,
            KEP_MAGASSAG - 2 * MEZO_MERET,
            arcade.color.WHITE,
            30)

    def eletek_kezdeti_kirajzolasa(self):
        for i in range(self.jatekos_1.eletek):
            uj_elet_sprite = arcade.Sprite("img/heart.png")
            uj_elet_sprite.center_x = i * MEZO_MERET + MEZO_MERET / 2
            uj_elet_sprite.center_y = KEP_MAGASSAG - MEZO_MERET / 2
            self.eletero_lista.append(uj_elet_sprite)

    def uj_elet(self, jatekos):
        uj_elet_sprite = arcade.Sprite("img/heart.png")
        uj_elet_sprite.center_x = self.jatekos_1.eletek * MEZO_MERET + MEZO_MERET / 2
        uj_elet_sprite.center_y = KEP_MAGASSAG - MEZO_MERET / 2
        self.eletero_lista.append(uj_elet_sprite)
        jatekos.eletek += 1

    def veszits_eletet(self):
        utolso_elet = self.eletero_lista[self.eletek - 1]
        utolso_elet.kill()
        self.jatekos_1.eletek -= 1


if __name__ == "__main__":
    jatek = LovagJatek()
    jatek.inditas()
