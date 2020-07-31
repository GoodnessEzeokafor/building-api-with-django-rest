from django.forms.widgets import Widget


class PlusMinusNumberInput(Widget):
    template_name = "widget/plusminusnumber.html"


    class Media:
        css = {
            "all":('css/plusminusnumber.js')
        }
        js = ('js/plusminusnumber.js',)