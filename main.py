from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout



class KCalcApp(App):
    def build(self):
        box = BoxLayout(orientation="vertical")

        layout = GridLayout(cols=4)
        btns = [Button(text='7'), Button(text='8'), Button(text='9'), Button(text='CL'), Button(text='4'),Button(text='5'),Button(text='6'),Button(text='+'),Button(text='1'),
                Button(text='2'), Button(text='3'), Button(text='-'), Button(text='.'), Button(text='0'), Button(text='*'), Button(text='/')]

        for i in btns:
            layout.add_widget(i)

        btns[0].bind(on_press=self._7)
        btns[1].bind(on_press=self._8)
        btns[2].bind(on_press=self._9)
        btns[3].bind(on_press=self._cl)
        btns[4].bind(on_press=self._4)
        btns[5].bind(on_press=self._5)
        btns[6].bind(on_press=self._6)
        btns[7].bind(on_press=self._plus)
        btns[8].bind(on_press=self._1)
        btns[9].bind(on_press=self._2)
        btns[10].bind(on_press=self._3)
        btns[11].bind(on_press=self._pinus)
        btns[12].bind(on_press=self._dot)
        btns[13].bind(on_press=self._0)
        btns[14].bind(on_press=self._mult)
        btns[15].bind(on_press=self._delit)

        global ti
        ti = TextInput()
        box.add_widget(ti)
        box.add_widget(layout)
        btEquals = Button(text='=', size_hint = (1, .5))
        btEquals.bind(on_press=self._equals)
        box.add_widget(btEquals)

        return box

    def _7(self, instance):
        ti.text += '7'

    def _8(self, instance):
        ti.text += '8'

    def _9(self, instance):
        ti.text += '9'

    def _cl(self, instance):
        ti.text = ''

    def _4(self, instance):
        ti.text += '4'

    def _5(self, instance):
        ti.text += '5'

    def _6(self, instance):
        ti.text += '6'

    def _plus(self, instance):
        ti.text += '+'

    def _1(self, instance):
        ti.text += '1'

    def _2(self, instance):
        ti.text += '2'

    def _3(self, instance):
        ti.text += '3'

    def _pinus(self, instance):
        ti.text += '-'

    def _dot(self, instance):
        ti.text += '.'

    def _0(self, instance):
        ti.text += '0'

    def _mult(self, instance):
        ti.text += '*'

    def _delit(self, instance):
        ti.text += '/'

    def _equals(self, instance):
        ti.text = str(eval(ti.text))

if __name__ == '__main__':
    app = KCalcApp()
    app.run()